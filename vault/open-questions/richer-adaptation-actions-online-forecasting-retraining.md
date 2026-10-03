---
created_at: '2026-10-03T10:07:12Z'
source_papers:
- '[[openalex-2609.39789-pseudo-label-triggered-retraining-from-forecast-errors-for-o]]'
title: Richer Adaptation Actions for Retraining
---

**Background:** Real-world time series forecasting models operate under non-stationary conditions where performance degrades over time, requiring selective model retraining under computational constraints.

**Question / Future Work:** Investigate expanding online retraining trigger frameworks beyond binary decisions to support richer adaptation actions, such as partial fine-tuning, model recalibration, or cost-aware update selection under evolving data streams.

**Why It Matters:** Extending trigger policies to multi-action or continuous adaptation spaces is crucial for maximizing performance gains while minimizing computational overhead in online deployment.

**Evidence:** PILOT also supports only binary decisions, whereas richer actions such as recalibration, partial fine-tuning, or cost-aware update selection may further improve adaptation under evolving data streams.