---
created_at: '2026-09-26T09:37:35Z'
source_papers:
- '[[openalex-2609.27467-kairos-grounded-forecasting-of-presence-and-directional-flow]]'
title: Adaptive Change Detection in Dynamic Scene Graphs
---

**Background:** Long-term robot autonomy in human-populated environments requires anticipating pedestrian motion patterns through probabilistic and directional flow models grounded in hierarchical 3D scene graphs.

**Question / Future Work:** Explore the extension of change-detection and adaptation mechanisms within dynamic scene graph representations to handle permanent structural or flow environment modifications without relying solely on long-term cumulative counting filters.

**Why It Matters:** Crucial for deploying robots in non-stationary real-world environments where pedestrian patterns undergo abrupt or permanent shifts rather than purely periodic oscillations.

**Evidence:** First, the mixing-weight and presence predictors accumulate cumulative means, so every observation carries equal weight: a place whose flow changes permanently is corrected at a rate of one over its accumulated sample count, and no test separates such a change from sampling noise.