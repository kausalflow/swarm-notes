---
created_at: '2026-10-18T09:13:12Z'
source_papers:
- '[[openalex-2609.12496-tailweather-from-tail-to-extremes-a-global-climatological-da]]'
title: Reconciling Pointwise Accuracy and Extreme Detection
---

**Background:** Machine learning weather forecasting models are typically evaluated using average error metrics such as root-mean-square error, which reflect ordinary weather conditions rather than rare extremes.

**Question / Future Work:** Determine how to design training strategies and loss functions that simultaneously optimize for standard pointwise forecasting metrics (such as RMSE) and rare extreme-event detection skills, as current tail-aware post-processing corrections improve regular accuracy while degrading extreme-event detection.

**Why It Matters:** Resolving this trade-off is critical for developing trustworthy AI weather prediction systems that excel in both routine forecasting and disaster early warning.

**Evidence:** This experiment shows that improving pointwise accuracy does not necessarily improve event detection. It does not establish the mechanism behind that trade-off.