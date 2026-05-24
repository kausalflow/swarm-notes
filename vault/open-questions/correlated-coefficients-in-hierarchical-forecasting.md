---
created_at: '2026-05-24T07:46:47Z'
source_papers:
- '[[openalex-2605.22676-comparison-of-probabilistic-nowcasts-and-forecasts-of-sars-c]]'
title: Correlated coefficients in HMLR
---

**Background:** Hierarchical multinomial logistic regression models often assume independence of regression coefficients across locations to simplify data sharing, which may restrict their ability to model complex dependencies in infectious disease surveillance.

**Question / Future Work:** Future work should explore incorporating correlations between regression coefficients—specifically across different locations and predictors like intercepts and time trends—to assess if this improves predictive flexibility and performance in data-sparse settings.

**Why It Matters:** This addresses a significant constraint in current hierarchical forecasting frameworks used for disease surveillance and has the potential to enhance performance where data is sparse.

**Evidence:** For the purposes of this paper, we assume the independence of regression coefficients across locations and predictors... Allowing for correlated regression coefficients across locations and predictors is a possible direction for future work.