---
created_at: '2026-07-19T07:24:49Z'
source_papers:
- '[[openalex-2607.14738-quantifying-the-complexity-of-trajectory-ensembles-with-clus]]'
title: Automated Resolution Selection CWMMSE
---

**Background:** The clustering-weighted multivariate multiscale sample entropy (CWMMSE) measure utilizes a user-defined clustering resolution to group trajectories, which influences the calculated population diversity and overall system complexity.

**Question / Future Work:** Developing a robust, data-driven method for selecting the clustering resolution in CWMMSE is necessary to remove subjectivity, as the current reliance on manual selection limits reproducibility and objective comparison across different scientific domains.

**Why It Matters:** The resolution is a primary free parameter that dictates the estimation of ensemble diversity; standardizing its selection is critical for the measure's scientific rigour.

**Evidence:** A data-driven rule for the resolution would remove the last free parameter.