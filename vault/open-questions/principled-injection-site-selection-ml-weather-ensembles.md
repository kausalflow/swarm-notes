---
created_at: '2026-09-10T09:18:00Z'
source_papers:
- '[[openalex-2609.08412-stochastically-perturbed-weights-ensembles-from-deterministi]]'
title: Principled Injection Site Selection
---

**Background:** Deterministic machine learning weather models require costly sweeps or retraining to select weight perturbation injection sites for ensemble generation.

**Question / Future Work:** Remove the empirical search/sweep for the optimal weight perturbation injection site by substituting a principled criterion, such as Fisher information, and steering the noise generation toward physically consistent extremes or rare-event sampling.

**Why It Matters:** Eliminating the costly trial-and-error search phase across architectures is crucial for making post-hoc weight perturbation a truly portable, plug-and-play recipe for any arbitrary deterministic weather model.

**Evidence:** The most useful next step is to remove the sweep: the injection site could be chosen by a principled criterion (Fisher information) rather than searched, and the draw steered rather than randomised...