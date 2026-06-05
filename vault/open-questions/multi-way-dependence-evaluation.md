---
created_at: '2026-06-05T08:40:10Z'
source_papers:
- '[[openalex-2606.03656-beyond-point-estimates-reliable-evaluation-of-prediction-per]]'
title: Evaluation under multi-way dependence
---

**Background:** Performance evaluation methods often assume independence, yet many datasets exhibit complex, multi-way dependence structures that cannot be reduced to a single hierarchical or nested clustering scheme. Standard cluster-robust sandwich estimators require defining an independent 'cluster' unit and are not designed for crossed or multi-way correlations.

**Question / Future Work:** Future work must extend inferential frameworks for prediction performance metrics to accommodate non-nested, multi-way dependence structures where data are collected across multiple dimensions such as time, site, and geography. Addressing cross-cluster dependence that violates single-level independence assumptions is critical for reliable performance claims.

**Why It Matters:** As machine learning models are deployed in complex, multi-dimensional environments, ignoring non-nested dependencies results in biased variance estimates.