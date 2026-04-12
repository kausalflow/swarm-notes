---
created_at: '2026-04-12T06:18:40Z'
source_papers:
- '[[openalex-2604.07953-pruning-extensions-and-efficiency-trade-offs-for-sustainable]]'
title: Hardware-Aware Pruning for TSC
---

**Background:** Pruning is a technique used to reduce the computational and energy cost of models, but the choice of intermediate models and criteria used for importance ranking significantly influence the performance of the pruned output.

**Question / Future Work:** Explore alternative intermediate classifiers to derive feature importances for pruning time series classification models, and investigate if integrating hardware-aware information directly into the pruning criteria improves deployment efficiency.

**Why It Matters:** Standardizing the pruning methodology based on more robust importance metrics or hardware constraints is essential for maximizing the energy-efficiency gains of pruned TSC models.