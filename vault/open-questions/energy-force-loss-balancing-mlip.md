---
created_at: '2026-05-22T08:17:54Z'
source_papers:
- '[[openalex-2605.19939-uncertainty-aware-machine-learning-interatomic-potentials-vi]]'
title: Energy-force loss balancing instability
---

**Background:** In the context of machine learning interatomic potentials (MLIPs), the performance and uncertainty quantification can be influenced by the balancing of different loss terms, such as energy and forces, which are often jointly optimized.

**Question / Future Work:** There is high observed variability in the energy prediction accuracy across different training seeds when fine-tuning pretrained models for specific benchmarks, which indicates that current strategies for balancing energy and force loss terms in the CRPS objective may not be optimal. Further research is required to stabilize this loss balancing to ensure consistent performance across energy and force predictions.

**Why It Matters:** Loss balancing is a fundamental issue in multitask training of MLIPs; failing to resolve it leads to inconsistent results and sensitivity to hyperparameter choices, hindering the robustness of learned models.

**Evidence:** higher seed-to-seed variance in P-Orb energy predictions on silica (sensitivity to loss balancing between energy and forces CRPS terms)