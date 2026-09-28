"""Exact two-source pump-correlation sensitivity screen.

Run from the repository root:
    python experiments/shared-pump-phase0/phase0.py

This is an analytic quadrature, not a calibrated device simulation.
"""

from __future__ import annotations

import math
import numpy as np
from numpy.polynomial.hermite import hermgauss
from numpy.polynomial.laguerre import laggauss


def single_source(
    mu: np.ndarray, herald_efficiency: float, detector: str = "threshold"
) -> tuple[np.ndarray, np.ndarray]:
    """Pr(accepted herald), Pr(exactly one pair and an accepted herald)."""
    if detector == "threshold":
        accepted = mu * herald_efficiency / (1.0 + mu * herald_efficiency)
    elif detector == "pnr_one":
        # For finite-efficiency PNR detection, n>1 photons can still yield
        # exactly one observed count when the others are lost.
        accepted = mu * herald_efficiency / (1.0 + mu * herald_efficiency) ** 2
    else:
        raise ValueError(detector)
    true = herald_efficiency * mu / (1.0 + mu) ** 2
    return accepted, true


def lognormal_power(cv: float, order: int = 96) -> tuple[np.ndarray, np.ndarray]:
    """Mean-one lognormal pump power and normalized quadrature weights."""
    if cv == 0:
        return np.array([1.0]), np.array([1.0])
    nodes, weights = hermgauss(order)
    sigma = math.sqrt(math.log1p(cv * cv))
    power = np.exp(math.sqrt(2.0) * sigma * nodes - 0.5 * sigma * sigma)
    return power, weights / math.sqrt(math.pi)


def thermal_power(order: int = 96) -> tuple[np.ndarray, np.ndarray]:
    """Mean-one exponential intensity, used only as an extreme-pump control."""
    return laggauss(order)


def evaluate(
    power: np.ndarray,
    weights: np.ndarray,
    pump_exponent: int,
    mean_pairs: float,
    herald_efficiency: float,
    detector: str = "threshold",
) -> dict[str, float]:
    # Match the mean pair number in both common-pump and independent controls.
    gain = power**pump_exponent
    gain /= np.dot(weights, gain)
    mu = mean_pairs * gain
    accepted, true = single_source(mu, herald_efficiency, detector)
    e_a, e_t = np.dot(weights, accepted), np.dot(weights, true)
    common_a, common_t = np.dot(weights, accepted**2), np.dot(weights, true**2)
    independent_a, independent_t = e_a**2, e_t**2
    common_false = 1.0 - common_t / common_a
    independent_false = 1.0 - independent_t / independent_a
    return {
        "cv_mu": math.sqrt(max(np.dot(weights, gain**2) - 1.0, 0.0)),
        "common_accept": common_a,
        "independent_accept": independent_a,
        "common_true": common_t,
        "independent_true": independent_t,
        "common_false": common_false,
        "independent_false": independent_false,
        "false_gap_pp": 100.0 * (common_false - independent_false),
        "accept_ratio": common_a / independent_a,
        "true_ratio": common_t / independent_t,
    }


def cv_for_gap(
    target_pp: float, pump_exponent: int, mean_pairs: float, detector: str
) -> float:
    """Sensitivity threshold, not a measured physical operating point."""
    low, high = 0.0, 0.8
    for _ in range(50):
        mid = (low + high) / 2.0
        power, weights = lognormal_power(mid)
        gap = evaluate(power, weights, pump_exponent, mean_pairs, 0.8, detector)[
            "false_gap_pp"
        ]
        if gap < target_pp:
            low = mid
        else:
            high = mid
    return high


def main() -> None:
    # Illustrative low-gain operating points. Neither is assigned to a device.
    mean_pairs = (0.01, 0.03, 0.1)
    herald_efficiency = 0.8
    cvs = (0, 0.005, 0.01, 0.05, 0.1, 0.2)
    print("Two sources; geometric pair counts conditional on pump; threshold heralds")
    print("P(n)=mu^n/(1+mu)^(n+1); eta_h=0.8; both heralds must click")
    print("False = P(at least one source emitted !=1 pair | both heralds clicked)")
    print("Independent control has identical single-source pump/pair statistics")
    print("CVs below are sensitivity settings, not measured source values.\n")
    print("exponent mean_mu pump_CV pair_CV false_ind false_common gap_pp accept_ratio true_ratio")
    for exponent in (1, 2):
        for mean_mu in mean_pairs:
            for cv in cvs:
                power, weights = lognormal_power(cv)
                result = evaluate(power, weights, exponent, mean_mu, herald_efficiency)
                print(
                    f"{exponent:8d} {mean_mu:7.3f} {cv:7.3f} "
                    f"{result['cv_mu']:7.3f} {result['independent_false']:9.6f} "
                    f"{result['common_false']:12.6f} {result['false_gap_pp']:7.4f} "
                    f"{result['accept_ratio']:12.6f} {result['true_ratio']:10.6f}"
                )
    print("\nExtreme thermal-like pump (not a coherent-laser noise setting):")
    power, weights = thermal_power()
    for exponent in (1, 2):
        for mean_mu in mean_pairs:
            result = evaluate(power, weights, exponent, mean_mu, herald_efficiency)
            print(
                f"exponent={exponent} mean_mu={mean_mu:.3f} "
                f"pair_CV={result['cv_mu']:.3f} gap_pp={result['false_gap_pp']:.4f} "
                f"accept_ratio={result['accept_ratio']:.4f} "
                f"true_ratio={result['true_ratio']:.4f}"
            )
    print("\nDetector control at mean_mu=0.03, SFWM exponent=2:")
    for cv in (0.01, 0.05, 0.1, 0.2):
        power, weights = lognormal_power(cv)
        for detector in ("threshold", "pnr_one"):
            result = evaluate(power, weights, 2, 0.03, herald_efficiency, detector)
            print(
                f"pump_CV={cv:.3f} detector={detector:9s} "
                f"false_ind={result['independent_false']:.6f} "
                f"false_common={result['common_false']:.6f} "
                f"gap_pp={result['false_gap_pp']:.4f} "
                f"accept_ratio={result['accept_ratio']:.6f}"
            )
    print("\nPump CV needed for a 1 percentage-point false-fraction gap, mean_mu=0.03:")
    for exponent in (1, 2):
        for detector in ("threshold", "pnr_one"):
            print(
                f"exponent={exponent} detector={detector:9s} "
                f"pump_CV={cv_for_gap(1.0, exponent, 0.03, detector):.4f}"
            )

    # Mathematical controls: zero pump noise makes models identical; all
    # accepted heralds are true one-pair events in the mu -> 0 limit.
    p0, w0 = lognormal_power(0)
    r0 = evaluate(p0, w0, 1, 0.03, herald_efficiency)
    assert abs(r0["false_gap_pp"]) < 1e-12
    assert abs(r0["accept_ratio"] - 1.0) < 1e-12
    p, w = lognormal_power(0.1)
    rlow = evaluate(p, w, 2, 1e-8, herald_efficiency)
    assert rlow["common_false"] < 1e-6
    assert rlow["independent_false"] < 1e-6
    assert abs(np.dot(w, p) - 1.0) < 1e-12
    # Independently sum the finite geometric distribution for one source.
    mu = 0.03
    n = np.arange(1, 50)
    probabilities = mu**n / (1 + mu) ** (n + 1)
    threshold_sum = np.sum(probabilities * (1 - (1 - herald_efficiency) ** n))
    pnr_sum = np.sum(probabilities * n * herald_efficiency * (1 - herald_efficiency) ** (n - 1))
    threshold_formula, _ = single_source(np.array([mu]), herald_efficiency)
    pnr_formula, _ = single_source(np.array([mu]), herald_efficiency, "pnr_one")
    assert abs(threshold_sum - threshold_formula[0]) < 1e-14
    assert abs(pnr_sum - pnr_formula[0]) < 1e-14
    # Perfect number resolution and efficiency reject every multi-pair event.
    ideal_p, ideal_w = lognormal_power(0.2)
    ideal = evaluate(ideal_p, ideal_w, 2, 0.03, 1.0, "pnr_one")
    assert abs(ideal["common_false"]) < 1e-12
    assert abs(ideal["independent_false"]) < 1e-12
    # The largest reported lognormal sensitivity point is quadrature-stable.
    p64, w64 = lognormal_power(0.2, 64)
    p128, w128 = lognormal_power(0.2, 128)
    gap64 = evaluate(p64, w64, 2, 0.03, herald_efficiency)["false_gap_pp"]
    gap128 = evaluate(p128, w128, 2, 0.03, herald_efficiency)["false_gap_pp"]
    assert abs(gap64 - gap128) < 1e-10
    print("\nLimit and normalization checks passed.")


if __name__ == "__main__":
    main()
