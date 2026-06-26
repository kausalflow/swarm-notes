---
created_at: '2026-06-26T08:25:22Z'
source_papers:
- '[[openalex-2606.24604-uncertainty-aware-longitudinal-forecasting-of-alzheimers-dis]]'
title: Modeling Diagnostic Reversals
---

**Background:** Current clinical trajectory models often employ hard-coded monotonicity constraints to ensure ordinal consistency, which may inadvertently filter out rare but documented clinical events.

**Question / Future Work:** Explore methods to incorporate the possibility of diagnostic reversals into probabilistic frameworks without relying on rigid hard-coded impossibility masks, potentially by learning reversal probabilities from empirical data.

**Why It Matters:** Strict monotonicity constraints may limit the clinical realism of forecasting models in cases where genuine diagnostic reversals occur.

**Evidence:** 100% of generated diagnosis trajectories are non decreasing, a direct consequence of the structural impossibility mask... Although there are outlier cases reported in ADNI where reversal does occur, we do not consider that modeling under our study.