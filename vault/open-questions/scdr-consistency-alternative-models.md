---
created_at: '2026-04-11T05:54:37Z'
source_papers:
- '[[openalex-2604.07325-conformal-prediction-with-time-series-data-via-sequential-co]]'
title: Extending SCDR model compatibility
---

**Background:** Sequential Conformalized Density Regions (SCDR) is a method for constructing prediction sets for time-series data by adjusting conditional highest predictive density regions. Broadening the class of density estimators beyond simple approximations is required for complex data.

**Question / Future Work:** Establishing theoretical consistency and validity for SCDR when paired with non-parametric or deep generative density estimators (e.g., normalizing flows) is essential to broaden the framework's applicability to non-linear and high-dimensional settings.

**Why It Matters:** Theoretical robustness of conformal methods is heavily dependent on the properties of the underlying density estimator; extending this to complex generative models is a key bottleneck.

**Evidence:** The first involves proving consistency results for other conditional distributions to broaden the range of models that can be used with SCDR.