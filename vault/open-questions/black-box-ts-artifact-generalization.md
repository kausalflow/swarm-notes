---
created_at: '2026-05-30T07:35:13Z'
source_papers:
- '[[openalex-2605.28355-detecting-diffusion-generated-time-series-under-generator-sh]]'
title: Black-box synthetic time series generalization
---

**Background:** Detection of synthetic time series is a critical capability in maintaining data integrity, yet the specific artifacts left by diffusion models remain largely opaque. Current black-box classifiers often demonstrate sensitivity to generator shift and sequence length, limiting their generalization capabilities.

**Question / Future Work:** It is essential to characterize the underlying features used by black-box detectors to improve robustness against unseen generators and varying sequence lengths, specifically investigating whether diffusion models leave universal fingerprints in the time series domain.

**Why It Matters:** Improving the transferability of detectors under generator shift is a primary bottleneck for deploying forensic tools for synthetic time series.