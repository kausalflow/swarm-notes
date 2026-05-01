---
created_at: '2026-05-01T07:22:23Z'
source_papers:
- '[[openalex-2604.25559-representing-the-surface-ocean-in-ecmwfs-data-driven-forecas]]'
title: Predicting Trend-Dominated Ocean Variables
---

**Background:** Machine learning weather models often struggle to represent variables that evolve on significantly different temporal and spatial scales or that are dominated by persistent, long-term trends. Standard practices, such as predicting absolute values, can lead to biases in variables like sea surface height that contain global mean trends.

**Question / Future Work:** Investigate methods to improve the representation of trend-dominated and slowly varying oceanic variables, specifically by evaluating the benefits of training models to predict anomalies rather than absolute values.

**Why It Matters:** This is a crucial technical challenge for integrating long-term climate-relevant variables into short-term, data-driven forecasting systems, as it directly impacts prediction accuracy for essential ocean metrics.

**Evidence:** A plausible explanation is that SSH contains a persistent, nearly monotonic climate-change signal over the training period, namely global mean sea-level rise. As a result, the model may tend to predict a more climatological state that reflects the average conditions seen during training. In future versions of the system, this issue could likely be mitigated by training the model to predict detrended SSH anomalies rather than absolute values.