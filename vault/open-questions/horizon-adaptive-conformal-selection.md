---
created_at: '2026-06-11T09:06:52Z'
source_papers:
- '[[openalex-2606.09473-report-the-floor-a-training-free-conformal-interval-is-a-man]]'
title: Horizon-adaptive conformal selection methods
---

**Background:** Conformal interval methods for time-series forecasting rely on residual pools to estimate uncertainty, but these intervals often fail to scale effectively as the forecast horizon increases.

**Question / Future Work:** Investigate horizon-adaptive selection mechanisms beyond simple persistence rules, such as online per-window selectors tracking interval scores or soft-blending techniques, to optimize sharpness and coverage for long-term forecasting.

**Why It Matters:** Bridges the performance gap between simple conformal floors and the theoretical oracle performance required for multi-step horizon accuracy.

**Evidence:** It does not reach the per-window oracle envelope (best-of-two), since it selects per horizon rather than per window. Closing that gap is future work...