---
created_at: '2026-03-29T06:07:13Z'
source_papers:
- '[[openalex-2603.25217-modeling-and-forecasting-tail-risk-spillovers-a-component-ba]]'
title: Alternative influential asset selection
---

**Background:** Value at Risk (VaR) models, such as CAViaR, traditionally estimate the maximum expected loss for a single asset based on its own past returns and observed variables.

**Question / Future Work:** Investigating whether the recursive partial correlation algorithm used to select influential assets for the spillover component can be further refined or generalized to select sources of risk that operate through different dynamic mechanisms, potentially beyond partial correlation alone.

**Why It Matters:** The current selection method relies solely on recursive partial correlation; exploring alternative, theoretically justified selection criteria could improve the identification of true risk contagion channels.

**Evidence:** The set of influential assets is identified using the recursive algorithm proposed by Gallo et al. (2025), which selects the variables exhibiting the highest partial correlation with the asset of interest.