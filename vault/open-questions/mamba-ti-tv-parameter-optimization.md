---
created_at: '2026-04-19T06:23:54Z'
source_papers:
- '[[openalex-2604.15174-mambasl-exploring-single-layer-mamba-for-time-series-classif]]'
title: Optimizing SSM Time-Variance Parameterization
---

**Background:** State space models like Mamba are primarily developed for language and video, with limited investigation into their optimal configuration as a standalone backbone for time series classification.

**Question / Future Work:** The optimal configuration of time-variant versus time-invariant parameters in Mamba's selective state space models—specifically for the step size Δ, input-to-state projection B, and state-to-output projection C—appears to be dataset-dependent. Further research is required to determine if these parameters can be systematically tuned or automated to improve performance across diverse time series domains.

**Why It Matters:** This is a fundamental architectural question. Understanding the trade-off between time-invariance and time-variance in SSMs is crucial for adapting them to non-textual sequence data where temporal properties vary significantly by domain.