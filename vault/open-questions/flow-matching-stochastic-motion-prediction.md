---
created_at: '2026-05-07T07:38:25Z'
source_papers:
- '[[openalex-2605.02759-dynoslam-dynamic-slam-with-generative-graph-neural-networks]]'
title: Flow Matching for Stochastic Prediction
---

**Background:** Stochastic motion prediction models in robotics often rely on manual noise injection during Monte Carlo sampling to approximate the underlying distribution of agent trajectories.

**Question / Future Work:** The development of more theoretically sound generative models, specifically Flow Matching architectures, is needed to directly learn continuous probability density vector fields of pedestrian trajectories, potentially offering more precise multi-modal generation than surrogate stochastic sampling.

**Why It Matters:** This addresses the limitation of using heuristic-based sampling for uncertainty estimation in human motion prediction, which is critical for accurate safety-critical planning.

**Evidence:** While the Stochastic GAT successfully models interaction uncertainty via Monte Carlo sampling, it relies on manually injected perturbations. In future work, we plan to replace this surrogate stochasticity with a fully generative Flow Matching architecture.