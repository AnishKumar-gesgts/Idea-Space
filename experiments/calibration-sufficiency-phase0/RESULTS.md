# Idea 1 Phase 0 — calibration sufficiency for entanglement swapping

**Date:** 27 September 2026
**Decision:** **No go for a standalone project on the present evidence.** The narrow mechanism exists in an exact two-mode model, but the predeclared *physical* Phase 0 gate is unmet, and closely related source-configuration physics was published in 2008. Retain the calculation as a reproducible example, not a validated device or novelty claim.

## Question and frozen local test

Can two candidate source configurations have the same routine, frequency-blind calibration data yet require different choices between an open Bell-swap analyzer and a common-bin filter to maximize *accepted* heralds above a fixed Bell-fidelity threshold?

I used two polarization-entangled pair sources, each emitting **exactly one pair**, a balanced beam splitter for the middle photons, frequency-insensitive detection of either opposite-port H/V record, and a two-bin spectral space. The filter passes only bin 0 in both middle-photon arms. Both sources are described by

$$
|\Psi_s\rangle=\frac{|HH\rangle |u_{sH}\rangle+|VV\rangle |u_{sV}\rangle}{\sqrt{2}},\qquad
u_H=(1,0),\quad u_V=(c,\sqrt{1-c^2}).
$$

The second source is either **aligned**, assigning the same wavepackets to H and V, or **reversed**, swapping those assignments. A polarization rotation or different polarization-dependent source path can produce the latter *within this model*. Such spectral-polarization dependence is physically documented in type-II SPDC and integrated waveguide sources; the specific two-bin amplitudes and the aligned/reversed pair are **constructed examples, not measured devices**. [Poh et al. (2007)](https://doi.org/10.1103/PhysRevA.75.043816), [Vergyris et al. (2017)](https://www.nature.com/articles/s41534-016-0005-z).

The routine measurement bundle is both sources' pair polarization density matrices (equivalently Bell fidelity here), pair brightness, one-pair $g^{(2)}(0)=0$, unpolarized marginal spectra, and a single **aggregate** central-photon HOM visibility. These are *assumed* routine for this test; a lab that already measures H-H and V-V HOM has no ambiguity. The declared acceptance threshold is $F_{\mathrm{swap}}\geq0.96$; it is an illustrative target, not an application-derived requirement. The yield below is per attempt in which **both sources emitted one pair**, before source probability, channel loss, outer readout, and time costs. Identical pure detection loss multiplies both yields by $\eta^2$ without changing their ranking.

## Exact results

For $c=0.92$, the two configurations have *exactly* the same frequency-blind calibration statistics: pair Bell fidelity $0.9600$, aggregate HOM overlap $0.9232$, and unpolarized spectrum. The model predicts:

| Configuration | Extra H-H HOM | Open: herald / double-pair attempt | Open: conditional Bell fidelity | Common-bin filter: herald / double-pair attempt | Filtered fidelity | Best choice at $F\geq0.96$ |
|---|---:|---:|---:|---:|---:|---|
| Aligned | 1.0000 | 0.2500 | 1.0000 | 0.2116 | 1.0000 | Open |
| Reversed | 0.8464 | 0.2500 | 0.9232 | 0.2145 | 0.9931 | Filter |

The frequency-blind measurement bundle cannot discriminate these two configurations at *any* sample size in this model: its probability laws are identical. If the operator must guarantee the target without another measurement, filtering both configurations is the safe fixed choice. For equally likely cases, that yields 0.2131 accepted heralds per double-pair attempt, versus 0.2323 for a perfectly informed choice, about **9.0% relative**. The prior and target are illustrative, so this is **not** a measured gain.

A polarization-resolved H-H HOM measurement separates them. With an *assumed* common instrumental contrast ceiling of 0.90, 500 independent H-H trials yield an equal-prior minimum classification error of 0.00224 under a simple binomial coincidence model; 1,000 trials yield 0.0000287. This shows a plausible measurement channel in the toy model. Those contrast and shot counts are **not** a sourced apparatus calibration, and a full cost calculation would need measured collection/detection rates and the time over which a source setting stays stable. Neither the aggregate-HOM protocol nor this extra measurement uses hidden spectral labels during operation.

## Checks and analytic cross-check

The independent closed forms for the frequency-insensitive record are

$$
V_{\rm aggregate}=\frac{1+c^2}{2},\quad
F_{\rm open}^{\rm aligned}=1,\quad
F_{\rm open}^{\rm reversed}=\frac{1+c^2}{2},\quad
Y_{\rm open}=\frac14,
$$

$$
Y_{\rm filter}^{\rm aligned}=\frac{c^2}{4},\quad
Y_{\rm filter}^{\rm reversed}=\frac{1+c^4}{8},\quad
F_{\rm filter}^{\rm reversed}=\frac{(1+c^2)^2}{2(1+c^4)}.
$$

The implementation constructs the two-photon output amplitudes for each *observable* H/V click pattern, traces the unobserved frequency bins, and computes the remote density matrix. Assertions check the analytic formulas, normalization, positive semidefiniteness, ideal $c=1$, fully disjoint wavepackets (swapped $F=0.5$), and pure detector-loss scaling. A $c$ sweep at 0.88, 0.92, 0.95, 0.97, and 1.00 verifies that the choice flip is not isolated to one floating-point setting. For this threshold, reversed/open becomes admissible when $c\geq\sqrt{0.92}\approx0.9592$. The selected target therefore materially controls the outcome.

Reproduce with `python experiments/calibration-sufficiency-phase0/phase0.py` from the repository root. Dependencies: NumPy. The script prints the full sweep and finite-shot calculation.

## Why this does not pass the project's Phase 0 gate

1. **No sourced joint device point.** The source papers support polarization-linked spectral differences, but neither provides the exact pair of calibrated two-bin source settings, filter transmission, joint spectral amplitudes, and detector response used here. The chosen $c$, threshold, and 0.90 HOM contrast are illustrative. A mathematical counterexample is not evidence that two *actual* compatible source settings would occupy opposite sides of a useful decision boundary.
2. **The closest physics is established.** [Humble and Grice (2008)](https://www.ornl.gov/publication/effects-spectral-entanglement-polarization-entanglement-swapping-and-type-i-fusion) already calculate how spectral entanglement and polarization-correlated spectra change entanglement swapping with source configuration. [Poh et al. (2007)](https://doi.org/10.1103/PhysRevA.75.043816) show that spectral measurements can predict polarization behavior under filtering. This calculation does not establish a distinct publishable result beyond those papers.
3. **The extra measurement is straightforward.** H-H HOM directly distinguishes the examples. That could still be useful in a concrete lab workflow, but it weakens a claim of a surprising hidden calibration deficiency. Some real swapping testbeds explicitly use HOM and polarization calibration already; the asserted “routine” bundle is not universal. [QUANT-NET testbed description](https://quantnet.lbl.gov/research/quant-net-design-and-implementation).
4. **Absolute usable rate remains unknown.** Multipair emission, filtering of real continuous spectra, false heralds, detector confusion, channel loss, calibration downtime, and operating-point stability were not included. The exact-one-pair model sets $g^{(2)}(0)=0$ by construction and cannot predict a real source's $g^{(2)}$ or delivered states per second.

**Research decision:** Do not advance Idea 1 to a major standalone project or claim a lab advantage. It would become worth reopening only if one lab/source family provides measured joint spectra (including polarization-resolved amplitudes), filter curves, detector records, and an application-specified fidelity/rate target, and a predeclared comparison shows that the *measurements the lab already performs* leave a consequential choice unresolved. The result must survive finite calibration cost, multipair false heralds, and the strongest existing source-characterization baseline. Absent that package, move to the next independently falsifiable idea rather than enlarging this model.
