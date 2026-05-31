---
created_at: '2026-05-31T08:10:28Z'
source_papers:
- '[[openalex-2605.29315-generalized-spectral-testing-with-sample-splitting]]'
title: Detecting joint conditional dependence
---

**Background:** Generalized spectral tests aggregate pairwise conditional moment restrictions to evaluate if a time series follows a specified model.

**Question / Future Work:** Current diagnostic statistics are largely limited to pairwise moment restrictions, which may miss higher-order or joint dependence structures in time series models. Future research is required to construct omnibus tests that detect these complex dependencies more effectively.

**Why It Matters:** This bottleneck limits the ability of diagnostic tests to identify complex nonlinear dependencies, which are common in real-world time series.

**Evidence:** Such alternatives involve higher-order or joint dependence on the past and are therefore not captured by a statistic built only from pairwise restrictions.