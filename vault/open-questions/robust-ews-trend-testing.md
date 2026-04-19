---
created_at: '2026-04-19T06:24:01Z'
source_papers:
- '[[openalex-2604.15230-on-the-robustness-of-mann-kendall-tests-used-to-forecast-cri]]'
title: Robust trend testing for EWS
---

**Background:** The rolling window method used to compute Early Warning Signals (EWS) for critical transitions introduces artificial autocorrelation in the resulting time series of indicator values. Standard Mann-Kendall trend tests assume a Gaussian distribution for their test statistics, which is invalid for these autocorrelated EWS time series.

**Question / Future Work:** It remains unresolved how to robustly detect trends in EWS indicator time series without resorting to computationally intensive resampling methods or suffering from significantly inflated Type I error rates. The authors suggest that weighted rolling windows, assigning more weight to points near the center of the window, might reduce the effective window size and associated autocorrelation, but this approach requires formal investigation to assess its efficacy and consequences in the context of EWS detection.

**Why It Matters:** This is critical because the current standard practice of using Mann-Kendall tests for EWS leads to a "cry wolf" effect, where false positives are routinely flagged due to the mismatch between the theoretical and empirical distributions of the test statistic. Finding a robust, computationally efficient alternative is essential for reliable early warning systems.