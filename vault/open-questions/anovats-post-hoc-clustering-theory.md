---
created_at: '2026-10-04T10:48:47Z'
source_papers:
- '[[openalex-2511.08070-anovats-a-subsampling-based-test-to-detect-differences-among]]'
title: Theoretical Guarantees for Post-ANOVATS Clustering
---

**Background:** Subsampling-based ANOVA tests (ANOVATS) are used to detect differences among short time series across multiple groups without requiring spectral density estimation, but their post hoc clustering procedures currently rely on heuristics rather than fully integrated theoretical guarantees.

**Question / Future Work:** Investigate and establish rigorous statistical guarantees, consistency properties, and optimal significance level decay schedules for the ANOVATS post hoc grouping and hierarchical clustering procedures when applied to dependent short time series data.

**Why It Matters:** Crucial for providing theoretical validity and error control when grouping marine strata or other spatial regions after rejecting the global null hypothesis.

**Evidence:** Wang and Xu (2014) proposed a procedure for clustering data by repeatedly applying a test procedure and verified its consistency... In our setting, for \\varphi_n such that \\varphi_n \\to 0...