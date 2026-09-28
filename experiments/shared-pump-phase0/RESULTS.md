# Shared-pump bursts — Phase 0 sensitivity result

**Date:** 27 September 2026  
**Decision:** **No go as a standalone project on present evidence.** Shared pump fluctuations can change a two-source herald distribution, but the incremental false-herald effect is small for modest fluctuation settings, a same-platform pump trace is unavailable in the screened literature, and a 22 September 2026 experiment directly establishes the central pump-to-photon-statistics mechanism. This is a reproducible *model sensitivity test*, not a measured device prediction or a proof that all architectures are insensitive.

## What was tested

Two low-gain pair sources share a pump realization. Conditional on that realization, their pair counts are independent and geometric with mean $\mu_t=\bar\mu P_t^k/\mathbb E[P^k]$, where $P_t$ is mean-one pump intensity, $k=1$ for SPDC-like scaling and $k=2$ for SFWM-like scaling. The target event is exactly one pair from each source. Each idler goes to a herald detector of efficiency $\eta_h=0.8$. A two-herald record is accepted. With threshold detectors, an event is called **false** if either source emitted more than one pair; there are no dark counts. Finite-efficiency number-resolving detectors accepting exactly one *observed* herald count provide a control. Signal propagation, interference, and delivered-state fidelity were not calculated; the outcome is source-number contamination before those stages.

The adversarial baseline draws *independent* pump fluctuations for each source from the **same marginal distribution**. Thus the mean pair rate, per-source pair statistics, and detector model are matched; only common versus independent source variation differs. A perfectly constant pump is another control. Pump variation is lognormal in the main sensitivity sweep, with pump coefficient of variation (CV) from 0 to 20%; these CV values are **assumptions, not measurements**. Mean pair number $\bar\mu$ takes 0.01, 0.03, and 0.10 as illustrative low-gain settings. The 0.03 order of magnitude also appears in a [2025 frequency-bin SFWM experiment](https://www.nature.com/articles/s41534-025-01087-w), but that paper does **not** supply the pump fluctuation distribution required to assign any row below to its device.

For a geometric pair distribution and threshold detector,

$$
A(\mu)=\Pr(\text{herald click}\mid\mu)=\frac{\eta_h\mu}{1+\eta_h\mu},\qquad
T(\mu)=\Pr(n=1,\text{herald click}\mid\mu)=\frac{\eta_h\mu}{(1+\mu)^2}.
$$

Then shared-pump accepted and true two-source probabilities are $\mathbb E[A^2]$ and $\mathbb E[T^2]$; the independent control gives $\mathbb E[A]^2$ and $\mathbb E[T]^2$. The false fraction is $1-T_2/A_2$. For a finite-efficiency number-resolving herald that accepts one *detected* photon, $A_{\rm PNR}(\mu)=\eta_h\mu/(1+\eta_h\mu)^2$, while $T$ is unchanged. This explicitly retains missed extra herald photons.

## Results

Selected $\bar\mu=0.03$ outcomes are below. “Gap” is shared minus independent false fraction, in **percentage points**. Rate ratios are common-pump divided by independent-pump probabilities, not rates per second.

| Scaling | Pump CV | Detector | Independent false | Shared false | Gap | Accepted-record ratio | True two-single-pair ratio |
|---|---:|---|---:|---:|---:|---:|---:|
| SPDC-like, $k=1$ | 1% | threshold | 6.8360% | 6.8366% | 0.0006 pp | 1.0001 | 1.0001 |
| SPDC-like, $k=1$ | 20% | threshold | 7.0784% | 7.3333% | 0.2549 pp | 1.0380 | 1.0352 |
| SFWM-like, $k=2$ | 1% | threshold | 6.8378% | 6.8403% | 0.0025 pp | 1.0004 | 1.0004 |
| SFWM-like, $k=2$ | 5% | threshold | 6.8967% | 6.9595% | 0.0628 pp | 1.0096 | 1.0089 |
| SFWM-like, $k=2$ | 10% | threshold | 7.0821% | 7.3408% | 0.2588 pp | 1.0386 | 1.0357 |
| SFWM-like, $k=2$ | 20% | threshold | 7.8453% | 8.9968% | 1.1515 pp | 1.1594 | 1.1449 |
| SFWM-like, $k=2$ | 20% | PNR one-count | 2.6462% | 3.0329% | 0.3868 pp | 1.1495 | 1.1449 |

As a **sensitivity marker**, a one-percentage-point false-fraction difference at $\bar\mu=0.03$ requires approximately 38.6% pump CV for SPDC-like scaling with threshold heralds, 18.8% for SFWM-like scaling with threshold heralds, and 30.2% for SFWM-like scaling with the finite-efficiency PNR control. One percentage point is an illustrative effect size, **not** a prespecified application fidelity threshold or a universal bound. A 20% SFWM-like example changes the false fraction substantially, but it also raises genuinely useful two-single-pair events by about 14.5%; an architecture-level decision needs a specified fidelity threshold, source rate, and losses.

An exponential/thermal-like pump yields far larger effects in the script. That is an **extreme control**, not a coherent-laser parameter point. [Song et al. (22 September 2026 preprint)](https://arxiv.org/abs/2609.26674) report a fluctuating filtered-ASE pump and directly measure its effect on SFWM photon statistics, including pump bunching and heralded $g^{(2)}$. Their continuous microring has a finite cavity response, so inserting its pump measurement into this pulse-by-pulse two-source model would be physically unjustified. Their result also strongly narrows novelty: the central nonlinear statistical-amplification mechanism has been demonstrated experimentally.

## Verification and limits

Run `python experiments/shared-pump-phase0/phase0.py` from the repository root; NumPy is the only dependency. The script evaluates exact one-source generating-function formulas with Gaussian quadrature rather than sampling rare fourfolds. It checks the no-fluctuation common/independent equality, the low-$\mu$ zero-false limit, pump normalization, and threshold/PNR formulas against direct finite sums of geometric pair probabilities. The complete 0.01/0.03/0.10 and SPDC/SFWM sensitivity grid is printed by the script.

The main missing measurement is **pulse-resolved pump power at the relevant source input, paired with the pair-generation response of that same multiplexed source**. The screened multiplexing papers report pair rates and multipair quality but not the required pulse-intensity distribution ([2013 two-source experiment](https://pmc.ncbi.nlm.nih.gov/articles/PMC3826656/); [2019 time-multiplexing experiment](https://pmc.ncbi.nlm.nih.gov/articles/PMC6777972/)). Published high-gain, low-repetition-rate SPDC pump noise cannot be imported into a low-gain heralded architecture. A variance/CV alone also cannot put a distribution-free bound on the high-intensity tail relevant to multipair bursts. Consequently, the sweep is **not a measured upper bound** on any existing device.

The simplified model omits pump spectral/phase effects, source interference, unequal source gain, dark counts, signal loss, and correlations from a shared nonlinear medium. These could matter in a chosen physical system. It also treats each source as geometric conditional on pump; a highly multimode source can approach different pair statistics. This scope is appropriate for the first kill gate, not an end-to-end protocol claim.

## Decision and reopen condition

**Stop here.** The mechanism is real, but it does not currently meet the Ideation Space publication gate: the closest new paper covers pump-statistics amplification, no same-platform low-gain noise distribution supports a consequential multi-source effect, and the modeled incremental false fraction is tiny at modest CV. Reopen only with a publicly measured or lab-supplied *same-platform* pulse histogram and gain curve indicating a consequential tail, plus a named multi-source protocol whose decision changes after true-rate, false-rate, detector, and loss accounting. Do not treat the large thermal-pump control as evidence for an ordinary shared coherent laser.
