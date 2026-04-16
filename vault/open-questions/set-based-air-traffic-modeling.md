---
created_at: '2026-04-16T06:28:42Z'
source_papers:
- '[[openalex-2604.11198-towards-situation-aware-state-modeling-for-air-traffic-flow]]'
title: Set-based Air Traffic Representation Learning
---

**Background:** Air traffic flow prediction currently relies on macroscopic models that aggregate aircraft trajectories into time-series sequences.

**Question / Future Work:** The transition from macroscopic time-series modeling to microscopic state-based set modeling requires resolving how to best encode, represent, and scale situational aircraft sets, particularly regarding long-range dependencies and physical constraints.

**Why It Matters:** This addresses the fundamental architectural limitation of current forecasting systems, providing a path toward higher predictive fidelity in multi-agent control settings.

**Evidence:** To address this dynamic set problem, Deep Sets and Set Transformer provide principled permutation-invariant modeling tools, yet their potential in real-world scenarios remains largely underexplored.