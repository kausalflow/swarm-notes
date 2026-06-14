---
created_at: '2026-06-14T08:38:21Z'
source_papers:
- '[[openalex-2606.13513-cloudcons-a-comprehensive-end-to-end-benchmark-for-cloud-res]]'
title: Aligning Forecasting and Decision Utility
---

**Background:** The forecast-then-optimize paradigm for cloud resource consolidation relies on predicting future workload demands to inform VM migration and placement decisions. It remains unclear how to systematically bridge the gap between forecasting accuracy metrics and actual decision utility in this downstream context.

**Question / Future Work:** Future work is required to develop decision-centric evaluation metrics that better align with the objectives of cloud resource consolidation, rather than relying solely on traditional time series forecasting error metrics. This involves investigating how specific predictive failures, such as underestimation of peak loads in heterogeneous cloud environments, impact the reliability and efficiency of consolidation decisions, as existing error metrics do not capture these impacts.

**Why It Matters:** This is a fundamental challenge in applying machine learning to real-world infrastructure management, where optimizing for proxy objectives (like MAE) often leads to suboptimal system-level behavior (e.g., SLA violations).

**Evidence:** A critical question persists: do superior forecasting capabilities actually translate into better decision utility? Answering this is essential, as empirical evidence suggests that high forecasting accuracy does not guarantee optimal consolidation decisions due to the misalignment between prediction metrics and decision-making objectives.