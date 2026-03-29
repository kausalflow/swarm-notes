---
created_at: '2026-03-29T06:07:19Z'
source_papers:
- '[[openalex-2603.25378-prism-dynamic-primitive-based-forecasting-for-large-scale-gp]]'
title: Characterize Primitive-Spectral Synergy
---

**Background:** Effective workload forecasting in large-scale GPU clusters requires modeling highly volatile, multi-periodic, and heterogeneous signals.

**Question / Future Work:** The synergistic effect between the Primitive Dictionary Decomposition module and the Adaptive Spectral Refinement module needs further characterization to fully understand how their combination contributes to performance beyond the sum of their individual parts. While the paper shows removing both causes a disproportionately large drop, the precise nature of this synergy requires deeper architectural investigation.

**Why It Matters:** Understanding the synergistic interaction between component-based decomposition (primitives) and frequency-domain refinement (spectral) is key to designing future compositional forecasting models for complex systems.

**Evidence:** Critically, removing both (w/o-prim-spec) results in a disproportionately severe performance drop of 15.27% (MSE). This degradation, which far exceeds the sum of their individual impacts, suggests a powerful synergistic effect between the primitive and spectral, indicating that their combination is crucial for the model’s high accuracy.