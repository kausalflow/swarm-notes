---
created_at: '2026-10-23T09:40:11Z'
source_papers:
- '[[openalex-2610.28594-learning-the-4d-world-through-point-trajectory-forecasting]]'
title: Scaling Trajectory Supervision from Real Videos
---

**Background:** Real-world scene forecasting involves complex dynamics, where current models rely on structured training data and simulation corpora but face challenges with unannotated real-world videos and full-scene dynamics.

**Question / Future Work:** Deriving persistent point trajectory supervision directly from unannotated real-world multi-view videos at scale remains an open challenge, alongside extending current methods to denser, non-rigid content (such as independent cloth and hair motion) and relaxing the assumption of having known, calibrated camera intrinsics and poses during inference.

**Why It Matters:** Overcoming the dependency on simulation or synthetic datasets and pre-calibrated cameras is crucial for scaling world models and 4D trajectory forecasting to open-world, in-the-wild video data.

**Evidence:** Future work includes deriving trajectory supervision from real multi-view videos at scale, extending it to denser, non-rigid content, and relaxing the need for calibrated cameras.