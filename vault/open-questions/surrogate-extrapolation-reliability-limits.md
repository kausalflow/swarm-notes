---
created_at: '2026-04-24T07:00:21Z'
source_papers:
- '[[openalex-2604.19442-state-forecasting-in-an-estimation-framework-with-surrogate]]'
title: Surrogate Extrapolation Reliability Limits
---

**Background:** Data-driven surrogate models used to extrapolate measurements in estimation frameworks often suffer from inaccuracies during long-term prediction.

**Question / Future Work:** Research is needed to develop strategies for maintaining the long-term reliability of surrogate-based forecasting, including methods for handling potential biases like 'double dipping' during iterative model refinement and retraining with incoming sparse data.

**Why It Matters:** This is a fundamental bottleneck for deploying hybrid state estimation frameworks in real-world systems where model drift and prediction error accumulation are unavoidable.

**Evidence:** Future work will focus on formal theoretical guarantees, handling multiple measurements, and addressing potential biases like ”double dipping” when retraining surrogate models.