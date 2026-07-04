---
created_at: '2026-07-04T07:36:03Z'
source_papers:
- '[[openalex-2607.01133-towards-metric-agnostic-trajectory-forecasting]]'
title: Temporal continuity in probabilistic forecasting
---

**Background:** Trajectory forecasting models often output discrete trajectory sets rather than explicit predictive distributions, which limits their utility for general downstream applications like planning.

**Question / Future Work:** Many state-of-the-art trajectory forecasting models either regress a fixed set of trajectories or parameterize independent per-timestep distributions, making it difficult to generate continuous, temporally consistent trajectories that remain optimal for metrics like minADE (minimum Average Displacement Error). Extending metric-specific policies to multi-agent forecasting and developing objectives that explicitly enforce temporal continuity of trajectories remains an open challenge.

**Why It Matters:** Addressing temporal continuity is critical for transitioning from purely evaluative forecasting metrics to downstream autonomous planning systems, where jittery or discontinuous trajectories are unsafe.

**Evidence:** A clear limitation of our minFDE and mAP policies is that they generally do not produce temporally continuous trajectories.