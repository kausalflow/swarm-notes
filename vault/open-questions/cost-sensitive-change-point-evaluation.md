---
created_at: '2026-10-09T11:36:18Z'
source_papers:
- '[[openalex-2610.09023-evaluating-change-point-detection-methods-for-software-perfo]]'
title: Cost-Sensitive Change Point Evaluation
---

**Background:** Change point detection methods are widely used for software performance regression analysis, but existing evaluations rely heavily on standard metrics without considering asymmetric costs of false positives and false negatives.

**Question / Future Work:** Future work should explore cost-sensitive formulations and alternative evaluation metrics for change point detection methods that reflect practical operational priorities, such as the differing costs of missing a true performance regression versus investigating a false alarm.

**Why It Matters:** Evaluating change point detection under symmetric scores does not align with industrial realities where missing regressions and false positives have vastly different economic impacts.

**Evidence:** However, in the context of performance regression detection, the relative cost of these errors may differ depending on operational constraints... Exploring alternative evaluation metrics or cost-sensitive formulations that better reflect practical priorities represents an important direction for future research.