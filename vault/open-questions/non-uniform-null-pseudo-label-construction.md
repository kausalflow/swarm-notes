---
created_at: '2026-06-21T08:54:08Z'
source_papers:
- '[[openalex-2606.19737-calibration-without-labels-in-multiple-testing]]'
title: Non-uniform null pseudo-label construction
---

**Background:** Multiple hypothesis testing calibration often relies on the assumption that the null distribution of test statistics is uniform, facilitating the use of ordered p-value spacings for pseudo-label construction.

**Question / Future Work:** Developing robust pseudo-label construction methods that remain valid when the null distribution is non-uniform, such as for z-scores or high-dimensional test statistics, is a critical open challenge for extending empirical Bayes calibration frameworks.

**Why It Matters:** The current pseudo-labeling framework is restricted to p-values; extending it to other common test statistics would significantly broaden the applicability of post-hoc calibration in statistical modeling and empirical Bayes methods.

**Evidence:** We pose it as an open question for how to construct similar pseudo-labels when the class-conditional null density is not uniform, for example with z-scores or high-dimensional test statistics.