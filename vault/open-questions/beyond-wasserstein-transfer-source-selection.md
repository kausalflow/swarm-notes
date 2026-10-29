---
created_at: '2026-10-29T11:11:27Z'
source_papers:
- '[[openalex-2610.35314-beyond-wasserstein-proximity-finding-better-transfer-sources]]'
title: Beyond Wasserstein Transfer Source Selection
---

**Background:** Source selection in transfer learning typically favors domains with high marginal proximity, yet marginal distance metrics may fail to capture underlying predictive relationships or the benefits of broader source variation.

**Question / Future Work:** Investigate and design prospective source-selection and screening methods that account for broader source variation and conditional predictive relationships beyond marginal Wasserstein proximity, evaluating their generalizability across diverse asset cohorts, regimes, and computational budgets.

**Why It Matters:** Understanding how to select transfer sources beyond simple marginal distance is crucial for optimizing pretraining initialization and avoiding negative transfer in time series and neural forecasting.

**Evidence:** Prospective studies should rotate regimes, hold out asset cohorts, match training budgets, and vary adaptation length. Task-aware distances, additional horizons, and tuned GARCH benchmarks would broaden the comparison.