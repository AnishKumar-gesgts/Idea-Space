"""Exact two-frequency-bin, single-pair entanglement-swap calculation.

All rates are conditional on both sources emitting one pair. This is a
mechanism check, not a device-calibrated SPDC simulation.
"""

from math import exp, lgamma, log, sqrt

import numpy as np


def source_spectra(overlap: float, reversed_labels: bool = False) -> np.ndarray:
    h = np.array([1.0, 0.0])
    v = np.array([overlap, sqrt(1 - overlap**2)])
    return np.array([v, h]) if reversed_labels else np.array([h, v])


def calibration(a: np.ndarray, b: np.ndarray) -> dict:
    # A source is (|HH> |u_H> + |VV> |u_V>)/sqrt(2).
    marginal_a = sum(np.outer(u, u.conj()) for u in a) / 2
    marginal_b = sum(np.outer(u, u.conj()) for u in b) / 2
    return {
        "pair_bell_fidelity_a": float((1 + np.vdot(a[0], a[1]).real) / 2),
        "pair_bell_fidelity_b": float((1 + np.vdot(b[0], b[1]).real) / 2),
        "aggregate_hom": float(np.trace(marginal_a @ marginal_b).real),
        "hh_hom": float(abs(np.vdot(a[0], b[0])) ** 2),
        "vv_hom": float(abs(np.vdot(a[1], b[1])) ** 2),
        "marginal_spectrum_a": np.diag(marginal_a).real.tolist(),
        "marginal_spectrum_b": np.diag(marginal_b).real.tolist(),
    }


def swap(a: np.ndarray, b: np.ndarray, filtered: bool = False, detector_eta: float = 1.0) -> dict:
    """Two opposite-port, orthogonal-polarization click records at a 50:50 BS.

    A frequency-blind detector traces over the two output frequencies. The
    filter projects both interfering inputs onto frequency bin 0 before BS.
    """
    assert a.shape == b.shape and a.shape[0] == 2
    assert 0 <= detector_eta <= 1
    if filtered:
        a, b = a.copy(), b.copy()
        a[:, 1:] = 0
        b[:, 1:] = 0
    # Remote polarization order HH, HV, VH, VV; output dH,eV frequency f,g.
    nfreq = a.shape[1]
    amplitudes = np.zeros((4, nfreq, nfreq), dtype=complex)
    for f in range(nfreq):
        for g in range(nfreq):
            amplitudes[1, f, g] += a[0, f] * b[1, g] / 4
            amplitudes[2, f, g] -= a[1, g] * b[0, f] / 4
    x = amplitudes.reshape(4, -1)
    rho = detector_eta**2 * (x @ x.conj().T)
    p_record = float(np.trace(rho).real)
    singlet = np.array([0, 1, -1, 0]) / sqrt(2)
    fidelity = float(np.vdot(singlet, rho @ singlet).real / p_record) if p_record else float("nan")
    eig = np.linalg.eigvalsh(rho / p_record) if p_record else np.array([0.0])
    return {
        "herald_per_double_pair": 2 * p_record,
        "conditional_bell_fidelity": fidelity,
        "min_density_eigenvalue": float(eig.min()),
        "rho": rho,
    }


def binomial_error(n: int, visibility_floor: float, overlap: float) -> float:
    """Equal-prior ML error distinguishing two H-H HOM coincidence laws."""
    p_match = (1 - visibility_floor) / 2
    p_reverse = (1 - visibility_floor * overlap**2) / 2
    error = 0.0
    for k in range(n + 1):
        log_choose = lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1)
        pm = exp(log_choose + k * log(p_match) + (n - k) * log(1 - p_match))
        pr = exp(log_choose + k * log(p_reverse) + (n - k) * log(1 - p_reverse))
        error += min(pm, pr) / 2
    return error


def main() -> None:
    threshold = 0.96
    for overlap in [1.0, 0.97, 0.95, 0.92, 0.88, 0.0]:
        a = source_spectra(overlap)
        print(f"\noverlap={overlap:.2f}, pair_fidelity={(1 + overlap)/2:.4f}")
        for label, b in [
            ("aligned", source_spectra(overlap)),
            ("reversed", source_spectra(overlap, True)),
        ]:
            cal = calibration(a, b)
            settings = {name: swap(a, b, filt) for name, filt in [("open", False), ("filter", True)]}
            best = max(
                ((v["herald_per_double_pair"], name) for name, v in settings.items()
                 if v["conditional_bell_fidelity"] >= threshold),
                default=(0.0, "none"),
            )[1]
            print(
                label,
                "aggregate_HOM", round(cal["aggregate_hom"], 6),
                "HH_HOM", round(cal["hh_hom"], 6),
                "choice", best,
                "open", tuple(round(settings["open"][k], 6) for k in
                              ["herald_per_double_pair", "conditional_bell_fidelity"]),
                "filter", tuple(round(settings["filter"][k], 6) for k in
                                ["herald_per_double_pair", "conditional_bell_fidelity"]),
            )
            assert abs(sum(cal["marginal_spectrum_a"]) - 1) < 1e-12
            assert abs(sum(cal["marginal_spectrum_b"]) - 1) < 1e-12
            assert all(v["min_density_eigenvalue"] > -1e-12 for v in settings.values())
            assert all(0 <= v["herald_per_double_pair"] <= 0.25 + 1e-12 for v in settings.values())
        assert abs(calibration(a, source_spectra(overlap))["aggregate_hom"] -
                   calibration(a, source_spectra(overlap, True))["aggregate_hom"]) < 1e-12
        aligned = swap(a, source_spectra(overlap))
        reversed_open = swap(a, source_spectra(overlap, True))
        reversed_filter = swap(a, source_spectra(overlap, True), True)
        assert abs(aligned["conditional_bell_fidelity"] - 1) < 1e-12
        assert abs(reversed_open["conditional_bell_fidelity"] - (1 + overlap**2) / 2) < 1e-12
        assert abs(reversed_filter["herald_per_double_pair"] - (1 + overlap**4) / 8) < 1e-12
    # Independent limiting checks: mutually orthogonal input wavepackets and pure loss.
    disjoint_a = np.array([[1, 0, 0, 0], [1, 0, 0, 0]], dtype=float)
    disjoint_b = np.array([[0, 0, 1, 0], [0, 0, 1, 0]], dtype=float)
    assert abs(calibration(disjoint_a, disjoint_b)["aggregate_hom"]) < 1e-12
    assert abs(swap(disjoint_a, disjoint_b)["conditional_bell_fidelity"] - 0.5) < 1e-12
    base = swap(source_spectra(0.92), source_spectra(0.92, True))
    lossy = swap(source_spectra(0.92), source_spectra(0.92, True), detector_eta=0.8)
    assert abs(lossy["herald_per_double_pair"] - 0.64 * base["herald_per_double_pair"]) < 1e-12
    assert abs(lossy["conditional_bell_fidelity"] - base["conditional_bell_fidelity"]) < 1e-12
    for n in [100, 250, 500, 1000, 2000]:
        print("H-H classification", n, binomial_error(n, 0.90, 0.92))


if __name__ == "__main__":
    main()
