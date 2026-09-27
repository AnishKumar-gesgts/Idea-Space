# Quantum Photonics and Information Science — STORM Idea Evaluation

**Date:** 27 September 2026

**Status:** Idea 1's [Phase 0 mechanism test and decision](experiments/calibration-sufficiency-phase0/RESULTS.md) are complete. The original ranking below is retained as a pre-test screen; Idea 1 is now **no go as a standalone project** on available evidence. Ideas 2–8 remain untested hypotheses.

**Novelty-first update:** The [Round 2 literature screen and revised project shortlist](Novelty-First%20Quantum%20Photonics%20Idea%20Search%20%E2%80%94%20Round%202.md) supersede the project-selection priorities below. This earlier scorecard remains as a record of what was proposed before stricter closest-work screening.

**Purpose:** Find a new software-first quantum photonics / quantum information science project after the [photonic decoder Phase 0 decisions](Photonic%20Decoder%20Evaluations.md#follow-up-decision-neither-advances-as-a-decoder-project). This is a separate search, not a renamed QEC decoder.

> **How to read the ranking:** These are provisional research priorities, **not probabilities of publication or promises of advantage**. The earlier hypergraph ranking was too confident before its physical and logical gates were tested. Every idea below has a first experiment capable of ending it. The research group of Professor Itay Hen is useful context for the student's QIS training; the ideas are intentionally not presented as his group's agenda or as endorsed by him.

## Method and scope

This adapts [Stanford STORM's perspective-guided question asking](https://aclanthology.org/2024.naacl-long.347/) to research selection. I used source-grounded questions from distinct analytical roles, followed the closest papers and contradictions, and synthesized a skeptical ranking. **No human experts were consulted**; the roles below are simulated analytical perspectives. This is a targeted, not exhaustive, literature screen current to the date above. Search absence does not prove novelty.

The [Ideation Space quality criteria](Photonic%20QEC%20Research%20Ideation%20%E2%80%94%20Model%20Handoff%20Protocol%20%28Unedited%29.md#4-required-quality-criteria-for-every-proposed-project) still control: a real question, a narrow novelty boundary, importance, a paper-depth result, software-only feasibility, scientifically necessary simulator coupling, and a clear science-fair narrative. A useful negative result is allowed. Device-rate claims need real parameter sources and explicit experimental assumptions; an idealized physical counterexample alone is insufficient.

**Shared target metric for networking ideas:** `delivered states per second above a prespecified fidelity or application threshold`, with uncertainties and rejected-attempt costs shown alongside conditional fidelity. Conditional fidelity alone can be raised by discarding almost everything.

| Analytical perspective | Question it forced | Selection consequence |
|---|---|---|
| Experimental single-photon-source physicist | Are brightness, purity, multipair rate, spectral diffusion, and their time correlations jointly plausible for the *same* source? | Reject parameter combinations assembled from incompatible papers. |
| Quantum-network architect | Does the proposed improvement survive link loss, heralding, synchronization, switch loss, memory time, and classical latency? | Count delivered usable pairs, not just local optical quality. |
| Quantum information theorist | Is the computed state or information quantity the one the protocol actually consumes? | Propagate conditional density matrices or justified channels; avoid arbitrary scalar fidelity proxies. |
| Photonic interferometry researcher | Which photon modes interfere, and what observable distinguishes the proposed mechanisms? | Require a concrete optical experiment and accessible measurement. |
| Detector and electronics researcher | Does a claimed record exist after finite efficiency, resolution, dead time, and binning? | Only observed clicks, tags, and heralds may guide a decision. |
| Statistical experimental designer | Is the effect identifiable at a finite calibration budget and robust to fitted-parameter uncertainty? | Use held-out counts, uncertainty coverage, and measurement cost. |
| Simulation-methods researcher | Are two tools genuinely doing different necessary work? | Build a local optical model plus task/protocol calculation; do not claim novelty from connecting APIs. |
| Skeptical reviewer | Which current paper is closest, and could the proposed finding be a special case? | Lower scores when a broad claim is already demonstrated. |
| Student project advisor | Can a decisive first test be done without proprietary data or hardware? | Put a falsifying Phase 0 before architecture expansion. |

## Literature anchors that change the ranking

1. [Ngan and Sun (2025)](https://journals.aps.org/pra/abstract/10.1103/bpsj-16wq) already compare photon-mediated entanglement schemes under optical dephasing and spectral diffusion, including rate–fidelity and filtering. “Optimize swapping under diffusion” alone is not new.
2. [Asynchronous multiphoton interference (2026)](https://www.nature.com/articles/s41534-026-01333-9) already studies timing, coincidence windows, jitter, and useful rate. “Choose a better window” alone is not new.
3. [Clayton et al. (2026 preprint)](https://arxiv.org/abs/2608.07163) already demonstrate trace-driven adaptive rate–fidelity link control under polarization drift. A generic adaptive link controller is weak as a lead.
4. [Rodari et al. (2025)](https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.6.020340), [van den Hoven et al. (2025 preprint)](https://arxiv.org/abs/2512.04903), and [Schadow et al. (2026 preprint)](https://arxiv.org/abs/2602.12269) already pursue multiphoton indistinguishability characterization and state certification. “HOM is insufficient” is established, not the proposed novelty.
5. [A 2026 three-photon experiment](https://www.nature.com/articles/s41377-026-02250-4) directly varies collective phase and observes behavior missed by pairwise overlaps. Merely simulating a triad phase is a reproduction.
6. [Bulmer et al. (2026)](https://doi.org/10.1117/1.AP.8.1.016010) develop fast lossy/partially distinguishable optical-circuit calculations. A general noisy photonic simulator or basic mode compression is crowded.
7. [Nanophotonic memory-network experiment](https://www.nature.com/articles/s41586-024-07252-z) measures frequency-conversion efficiency and converter noise in remote entanglement. These are consequential non-QEC parameters, but optimizing them generically is not new.
8. [Frequency-bin entanglement-based QKD (2025)](https://www.nature.com/articles/s41534-025-00991-5) demonstrates phase drift and real-time correction. Generic drift-aware frequency-bin control is occupied.
9. [Photon-number-resolution certification (2026 preprint)](https://arxiv.org/abs/2606.14365) and [multi-pair SPDC modeling](https://arxiv.org/abs/1410.3627) constrain claims about PNR detectors and multipair rejection.

## Disagreements retained in the synthesis

| Optimistic case | Skeptical response | Decision rule |
|---|---|---|
| A source-model pair can share average HOM and $g^{(2)}(0)$ yet deliver different swapping performance. | For a simple ideal two-photon model, the measured overlap may already determine the relevant output. Flexible hidden-mode models can manufacture differences. | Idea 1 advances only with **platform-consistent**, observation-matched models and a difference that survives finite-shot and rate accounting. |
| Source-history-aware pairing should exploit spectral diffusion. | The instantaneous frequency is usually hidden, and monitoring consumes time; a static or current-observation policy may suffice. | Idea 2 must use a documented observation process and beat both controls after switching/monitoring costs. |
| Better PNR detectors reject false heralds. | A lower pump setting may achieve the same useful-pair rate with cheaper threshold detectors. | Idea 4 compares at equal generated-photon, detector, and delivered-rate budgets. |
| A new simulator can make the study scalable. | Existing optical simulators and new algorithms already handle substantial loss/distinguishability complexity. | Build a simulator only when a new physical conclusion requires a capability or error certificate unavailable from existing methods. |

## Ranked portfolio

**Scores are judgmental 0–10 screening scores.** N = plausible *narrow* novelty (25%), I = scientific/practical importance (20%), F = executable Phase 0 without hardware (20%), C = strength of optical-to-QIS coupling (15%), D = publication depth if positive (10%), S = science-fair clarity (10%). Weighted totals are rounded to one decimal. A missing measured mechanism or failed Phase 0 overrides the numeric rank. “Conditional” means the first test may remove the idea entirely.

| Rank | Idea | N | I | F | C | D | S | Total | Current role |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | **Task-specific calibration sufficiency for entanglement swapping** | 7.5 | 9 | 8 | 9 | 8 | 9 | **8.3** | First Phase 0; possible standalone paper |
| 2 | **Source-memory-aware pairing in a small multiplexed link** | 7 | 8.5 | 7.5 | 9 | 8 | 8 | **7.9** | Second Phase 0; requires observed source state |
| 3 | **Heterogeneous-node conversion and filtering decision boundary** | 6.5 | 8.5 | 8 | 8.5 | 7.5 | 8 | **7.8** | Credible alternative if sourced converter curves exist |
| 4 | **Value of finite PNR resolution for useful swapped pairs** | 6 | 8 | 8.5 | 8.5 | 7 | 8.5 | **7.6** | Narrow device design study |
| 5 | **Protocol-specific multiphoton witness under imperfect readout** | 5.5 | 8 | 7.5 | 9 | 7.5 | 8 | **7.4** | Strong physics, close literature; needs a distinct decision |
| 6 | **Task-preserving reduced optical simulator with an error certificate** | 6 | 7.5 | 6 | 9 | 8.5 | 6.5 | **7.1** | Methods paper only if a new bound and speedup emerge |
| 7 | **Resource-normalized photonic distributed sensing boundary** | 5.5 | 8 | 6.5 | 8 | 7.5 | 7 | **6.9** | Higher theory burden; defer |
| 8 | **Generic adaptive rate–fidelity link controller** | 3 | 8 | 8 | 7 | 6 | 8 | **6.4** | Screened out as lead; use as baseline |

## 1. Task-specific calibration sufficiency for entanglement swapping

**Question.** For one specified pair-source or emitter platform and Bell-swap setup, are routine source measurements sufficient to choose between two source or filter settings according to **usable swapped entanglement per second**? If not, what *smallest feasible additional measurement* resolves the decision at a fixed calibration budget?

**Mechanism and closest work.** Two physical source models could agree on commonly reported mean efficiency, $g^{(2)}(0)$, and a chosen HOM measurement while differing in spectral-mode structure or temporal correlations. Their later conditional swapped-state density matrices might then differ. This is a **hypothesis**, not yet a proven available regime. Ngan and Sun already study the protocol noise and filtering tradeoff; Schadow, Rodari, and van den Hoven already study state certification/indistinguishability. The possible new result is **an operational sufficiency/decision boundary** for a named swapping task, including finite calibration counts. It is not the discovery that HOM alone is incomplete.

**Scientific interface.** A small exact wavepacket/Fock or Schmidt-mode calculation produces the observable calibration distributions and full Bell-herald-conditioned two-qubit states. A separate link/protocol model uses those states, source repetition rate, loss, and detector records to count states that meet a declared fidelity or entanglement threshold. The optical simulator and task model must agree on the same event definitions, with no hidden mode label available to the operator.

**Fair baselines.** (i) An operator choosing from published routine summaries; (ii) a full standard characterization or tomography when feasible; (iii) an oracle with exact source parameters only as an information ceiling. All policies receive the same calibration shots and pay for extra measurements. The alternative measurement could be a time-lagged HOM scan, an additional coincidence histogram, or a three-photon interference setting **only if it is physically available on the chosen platform**.

**Phase 0 before scaling.** Freeze one source family, one two-source swap circuit, one detector model, a calibration-shot budget, and a useful-state threshold. Fit two source instances to the *same simulated routine-observable confidence region* using parameter ranges from one coherent source/platform literature set. Independently compute their swapping outcomes. Check whether the decision difference survives finite-shot uncertainty and an experiment-feasible extra measurement. First verify ideal, no-interference, pure-loss, and zero-multipair limits.

**Kill gate.** Stop if routine measurements already identify the relevant state, the two matched physical models make the same optimal decision, differences disappear after rate/resource costs, or the extra measurement needs unavailable mode-resolved hardware. An adversarial pair of unconstrained states is a mathematical example, **not** a physical go.

**If positive, what changes?** A lab could know exactly when its usual calibration sheet suffices for choosing an operating point and when one more specific measurement is worth taking. A full study could vary source type, detector coarse graining, shot budget, model misspecification, and target fidelity; it could report decision-regret and coverage, not only raw state distance.

## 2. Source-memory-aware pairing in a small multiplexed link

**Question.** When several emitters or spectral channels drift over time, can **observable** source-history measurements guide which two photons to interfere so that the delivered high-fidelity entanglement rate improves after switch loss and latency?

**Mechanism and closest work.** [A 2026 emitter study](https://www.nature.com/articles/s41534-026-01221-2) measures two-photon interference versus pulse separation and fits a spectral-diffusion correlation time; [multiplexed network-node experiments](https://www.nature.com/articles/s41586-024-08537-z) show dynamic frequency differences. Adaptive link control under drift already exists in Clayton et al. The narrow proposal is **pair selection across a small source pool based on noisy, allowed source observations**, with its optical interference law evaluated before the network scheduler. This is distinct from controlling pump power or polarization on one link only if the pair-selection advantage survives realistic measurement and switch costs.

**Phase 0.** Use 2–4 emitters, one sourced spectral-diffusion timescale and linewidth family, a documented spectroscopic/HOM observation channel, and a simple one-hop entanglement protocol. Compare round-robin, best static pairing, current-observation greedy pairing, and a history-aware policy on identical traces. Lock fidelity threshold and account for lost attempts spent observing, optical-switch insertion loss, and control latency. Test held-out drift rates.

**Kill gate.** Stop if current-observation greedy selection captures all gain, source state is effectively unobservable at the required speed, or switching/monitoring costs erase the delivered-rate gain. The simulator's true instantaneous emitter frequency is an oracle, never a production policy input.

## 3. Heterogeneous-node conversion and filtering decision boundary

**Question.** For two incompatible photon-emitting nodes, which *measured* conversion-efficiency, added-noise, bandwidth, and filter settings make a converted optical link deliver more usable entanglement than the strongest feasible alternative connection?

**Mechanism and closest work.** Frequency conversion has enabled remote solid-state memory entanglement, and published experiments report large conversion-loss and noise terms. See the [nanophotonic-memory network](https://www.nature.com/articles/s41586-024-07252-z) and [heterogeneous high-rate protocol](https://arxiv.org/abs/2504.05567). The novelty could only be a **source-converter co-design boundary with uncertainty**, not “conversion helps networking” or a generic rate optimization.

**Phase 0.** Choose one published emitter pair and one measured conversion/noise curve. Propagate the conversion channel through a fixed heralded-entanglement circuit and fiber model; compare direct compatible-wavelength operation if physically possible, the paper's standard conversion point, and optimized filter/pump settings at identical generated-photon and detector resources. Check whether the preferred setting changes within published uncertainty. Include source bandwidth, false heralds, and delivered-state fidelity.

**Kill gate.** Stop if the answer is monotonic in one known efficiency/noise ratio, depends on combining incompatible devices, or needs unreported converter spectral data. Without an independent device data set this remains a model study, not a validated design rule.

## 4. Value of finite PNR resolution for useful swapped pairs

**Question.** For a fixed SPDC/SFWM entanglement-swap circuit, how much *actual detector resolution* is worth paying for to reject multipair false heralds at a fixed usable-pair rate?

**Mechanism and closest work.** Multipair modeling is long established, and a [2026 PNR certification proposal](https://arxiv.org/abs/2606.14365) makes clear that nominal output bins do not by themselves certify physical resolution. A useful result would map a *measured detector response matrix* to swapped-state quality and the smallest resolution that changes an operating decision; “PNR is better” is not novel.

**Phase 0.** Reproduce an SPDC two-pair limit, then compare threshold detection, 2-bin, and 3+-bin PNR using the same quantum efficiency and realistic saturation/confusion matrices. Compute full and false herald counts, conditional state, and useful states/s. Include the detector-channel or cryogenic cost if used for the ranking. Stop if resolution adds no benefit over pump-power adjustment and threshold detection at the same useful rate.

## 5. Protocol-specific multiphoton witness under imperfect readout

**Question.** Can a low-setting three-photon measurement certify that a *chosen* prepared state will succeed in a declared teleportation/entanglement task when HOM visibility and pairwise overlaps leave that task's result uncertain?

**Overlap.** Rodari, van den Hoven, Schadow, and the 2026 collective-phase experiment already establish most generic characterization and witness claims. The only plausible distinction is finite-shot **decision performance for one downstream protocol with specified loss, PNR confusion, and interferometer error**. Phase 0 must first reproduce a known three-photon result and show a decision failure of the strongest existing witness; otherwise use their method rather than launching this project.

## 6. Task-preserving reduced optical simulator with an error certificate

**Question.** Can a reduced spectral-mode or coarse-grained detector model compute a chosen protocol's herald rate and conditional output state materially faster while providing a bound tight enough to preserve its operating decision?

**Overlap.** Bulmer et al. and other recent algorithms already accelerate realistic photonic simulation. An API layer or a benchmark of existing packages is not research. The narrow possible contribution is a **provable or empirically validated task-error certificate** in a regime their methods do not already cover. Phase 0 should attempt an exact 3–4 photon reference, a stated reduction, and independent error/compute-cost curves. Stop if the bound is vacuous, speedup disappears at useful accuracy, or a current algorithm already does the same thing.

## 7. Resource-normalized photonic distributed sensing boundary

**Question.** When can delivered entangled photonic probes beat the strongest local/classical probe strategy after including source failures, heralding, link loss, detector time, and total generated photons?

**Overlap.** [Recent distributed-sensing theory](https://doi.org/10.1103/7n9w-9xd4) already studies quantum advantage in noisy networks, and [lossy multiphase estimation work](https://journals.aps.org/pra/abstract/10.1103/l44c-d76x) addresses robust photonic resources. A worthwhile new result would require a named physically producible probe and experiment-specific accounting. Phase 0 needs a correct classical/local Fisher-information baseline and a sourced optical source; otherwise defer.

## 8. Generic adaptive rate–fidelity link controller — screened out

The [2026 trace-driven controller](https://arxiv.org/abs/2608.07163) already jointly adapts source pump power and polarization compensation on a deployed-fiber trace. A fresh reinforcement-learning or Bayesian optimizer on generic links would add little. Keep its optimized static policy and published controller as baselines for Ideas 1–2 where applicable.

## Decision after STORM synthesis

**Historical pre-test recommendation:** Start with Idea 1's Phase 0 only. It tests whether a real measurement gap changes a meaningful end-to-end choice. Idea 2 is the best alternate if a professor or experimental group can share a documented observable source-history channel; without one, its apparent gain is at high risk of relying on simulator-only frequencies. Idea 3 is the best alternate when converter calibration data are available. Do not build a broad simulator, optimize a controller, or write a paper claim until one of these first gates passes.

**Positive threshold for expanding Idea 1:** two platform-consistent source models both fit routine observables within predeclared finite-shot uncertainty; they lead to different best operating choices or a consequential difference in useful delivered rate; one practical additional measurement resolves that difference on held-out simulations; the effect survives sourced parameter uncertainty and all attempts are counted. A mere difference in density-matrix entries, trace distance, or conditional fidelity is insufficient.

**Negative outcome worth retaining:** if a realistic model family shows that standard calibration *is* sufficient within a useful error bound, that can itself be a valuable, narrower result. Report the conditions and do not rescue the original hypothesis by inventing more extreme sources.

### Quantum information learning path built into the first project

| Stage | QIS concept to learn | Why the experiment needs it |
|---|---|---|
| Local two-source model | Density matrices, mixed states, partial trace, quantum operations | A heralded optical click generally leaves a *conditional state*, not just a success probability. |
| Bell swap | Bell measurements, entanglement swapping, Pauli frames | The circuit must produce the remote state whose quality the protocol consumes. |
| Decision metric | Entanglement fidelity or a declared witness, rate–fidelity tradeoff | The preferred source/filter setting is a task decision, not the largest HOM visibility. |
| Finite calibration | Identifiability, confidence regions, decision regret | A suggested extra measurement is useful only if it changes a decision with realistic numbers of counts. |

## Concrete next actions before implementation

1. Choose **one** actual source platform with published joint values for brightness, multipair probability, indistinguishability, timing, and detector response; ask the professor which platform or lab contact is most relevant only after presenting this bounded menu. Do not stitch an attractive parameter point from unrelated devices.
2. Make a one-page closest-work matrix for Idea 1: Ngan/Sun, asynchronous interference, Rodari, van den Hoven, Schadow, and any paper on the exact chosen source/swap circuit. Record what each paper measures, computes, and does not claim.
3. Freeze one swap primitive, allowed observations, shot budget, target threshold, output metric, parameter uncertainty, and kill criterion **before** optimizing extra measurements.
4. Run ideal/noise-limit checks and the smallest exact optical calculation. Connect its conditional state and herald probability to the protocol-level rate model; verify the latter with a second derivation or independent small simulator.
5. Only if the first gate passes, expand to multiple source conditions, held-out model families, uncertainty coverage, resource-cost robustness, and a direct comparison with the nearest published method. The simulator code becomes a reproducible artifact of the scientific result, not its novelty claim.

## 27 September 2026 — Idea 1 Phase 0 decision

The [exact two-mode test, code, checks, and limits](experiments/calibration-sufficiency-phase0/RESULTS.md) found a genuine *model* ambiguity: identical source pair-state fidelity and aggregate HOM visibility can accompany different optimal open-versus-filter swap choices at a declared 0.96 Bell-fidelity target. In the illustrative $c=0.92$ pair, the open analyzer gives swapped fidelity 1.000 for aligned spectral labels but 0.923 for reversed labels; a common-bin filter raises the latter to 0.993 while lowering its herald probability from 0.250 to 0.215 per double-pair attempt. An ordinary polarization-resolved HOM measurement exposes the distinction.

**Updated selection: no go for Idea 1 as a standalone project on present evidence.** The source pair, filter, target, and detector contrast are not calibrated to one actual device; absolute useful rate and multipair false heralds are unknown. More importantly, [Humble and Grice (2008)](https://www.ornl.gov/publication/effects-spectral-entanglement-polarization-entanglement-swapping-and-type-i-fusion) already analyze polarization-linked spectral structure in entanglement swapping across source configurations. The original 8.3 score is a preserved *pre-test judgment*, not a current endorsement. Reopen only with a measured source/detector package and a demonstrated decision gap beyond the lab's existing polarization-resolved characterization. Idea 2 is next for a Phase 0 **only if** an observable source-history channel is documented; otherwise Idea 3's converter-data gate is the more grounded next screen.
