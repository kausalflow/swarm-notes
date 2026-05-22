---
created_at: '2026-05-22T08:16:30Z'
source_papers:
- '[[openalex-2605.20119-toto-20-time-series-forecasting-enters-the-scaling-era]]'
title: TSFM Long-Horizon Stability
---

**Background:** Classical forecasting models often exhibit superior extrapolation behavior on simple signals and more predictable performance on out-of-distribution samples compared to foundation models. Foundation models currently struggle to maintain coherence in long-horizon forecasts, specifically in tail behavior and regime shifts.

**Question / Future Work:** Research is needed to develop architectural modifications and scaling strategies that enable foundation models to match the structural coherence, reliability, and proper uncertainty growth of classical statistical methods on long-horizon forecasts.

**Why It Matters:** Bridging this gap is necessary for the adoption of TSFMs in mission-critical applications where long-horizon stability is essential.

**Evidence:** Closing the gap with classical baselines. Foundation models capture dynamics classical statistical methods largely cannot... But classical methods still have properties foundation models lack: clean extrapolation on simple signals, appropriate growth of prediction intervals with horizon...