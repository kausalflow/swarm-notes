---
created_at: '2026-05-21T08:27:04Z'
source_papers:
- '[[openalex-2503.20148-addressing-challenges-in-time-series-forecasting-a-comprehen]]'
title: Automated Hyperparameter Optimization TS
---

**Background:** Modern machine learning models for time series forecasting are highly sensitive to hyperparameter configurations and feature engineering choices, which often necessitate extensive, case-specific tuning to achieve optimal performance across diverse datasets.

**Question / Future Work:** There is an urgent need to develop automated, robust, and generalizable hyperparameter optimization frameworks for time series forecasting models. Current approaches rely heavily on domain expertise and trial-and-error, which inhibits the scalability and reliable application of these models in automated management systems. Future research should prioritize systematic methods that can adaptively tune parameters—such as window sizes, network architectures, and regularization settings—without requiring manual intervention for every new dataset.

**Why It Matters:** This is a critical bottleneck preventing the widespread, reliable adoption of advanced ML forecasting models, as performance variability makes it difficult to trust automated deployments in real-world scenarios.

**Evidence:** We determine the hyper-parameters for the algorithms based on our experience and repeated implementations of the algorithms... This outcome does not imply that other algorithms are unsuitable; rather, it indicates that they require further attention to hyper-parameters and feature engineering to perform effectively.