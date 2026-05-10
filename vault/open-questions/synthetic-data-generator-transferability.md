---
created_at: '2026-05-10T07:20:46Z'
source_papers:
- '[[openalex-2605.06032-does-synthetic-data-help-empirical-evidence-from-deep-learni]]'
title: Generator Selection and Matching
---

**Background:** Synthetic data generators for time series forecasting are categorized into different temporal archetypes, yet no consensus exists on which generator types best transfer to diverse real-world forecasting domains.

**Question / Future Work:** Current synthetic data generators are often optimized for specific temporal archetypes, but it is unclear how to perform optimal generator selection or composition to match the latent statistical properties of a target real-world dataset. The lack of a principled framework for matching synthetic data distributions to target domain characteristics often leads to suboptimal or harmful performance when augmenting sparse datasets.

**Why It Matters:** Without a formal approach to matching generator characteristics to target data, practitioners must rely on trial-and-error, which is costly and often leads to performance degradation.

**Evidence:** The NR, LM, and VE bundles consistently degrade performance more than ST across all tested datasets. We believe this is a distribution mismatch problem rather than an implementation defect.