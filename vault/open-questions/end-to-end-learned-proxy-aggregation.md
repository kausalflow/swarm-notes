---
created_at: '2026-05-21T08:32:50Z'
source_papers:
- '[[openalex-2605.18607-forecasting-downstream-performance-of-llms-with-proxy-metric]]'
title: End-to-End Learned Proxy Aggregation
---

**Background:** Performance forecasting for large language models (LLMs) currently relies on either expensive direct downstream evaluation or task-agnostic metrics like cross-entropy loss, which often fail to accurately predict capabilities on specific reasoning tasks. Proxy metrics derived from token-level predictive distributions over expert reasoning trajectories offer a more informative and efficient alternative for forecasting performance.

**Question / Future Work:** The current reliance on fixed libraries of proxy metrics selected post hoc leaves open the question of whether an end-to-end learned aggregation function or custom metrics designed for specific downstream failure modes could outperform current approaches and bridge the gap to the oracle upper bounds. Determining if such learned approaches can consistently improve over current manually-constructed proxy libraries across diverse model architectures and task domains remains a significant research opportunity.

**Why It Matters:** The reported oracle gap suggests significant potential for improving forecasting accuracy; transitioning from manual, heuristic-based proxy selection to learned, adaptive methods is a standard and necessary evolution in improving predictive modeling robustness.

**Evidence:** Finally, we have treated the eighty proxy metrics as a fixed library and selected among them post hoc. Learning the aggregation function end-to-end, or designing metrics that target specific failure modes of downstream evaluation, could close the remaining gap between the oracle upper bound and the cross-validated performance we report.