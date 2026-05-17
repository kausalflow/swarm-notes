---
created_at: '2026-03-29T06:07:28Z'
generated_stub: true
modified_at: '2026-05-17T07:31:30Z'
processed_at: '2026-03-29T06:07:28Z'
slug: flow-grpo-post-training
source_papers:
- '[[openalex-2603.24936-tigflow-grpo-trajectory-forecasting-via-interaction-aware-fl]]'
- '[[openalex-2605.14696-eponav2-driving-world-model-with-comprehensive-future-reason]]'
title: Flow-GRPO Post-training
type: concept
---

# Flow-GRPO Post-training

> *Auto-generated stub. Edit this file to add more details.*

A post-training optimization technique that applies a Reward-Driven Optimization (GRPO) over the stochastic sampling process derived from a Continuous Normalizing Flow (CNF) to steer trajectory predictions towards desired behavioral outcomes.


## Why It Matters

This novel two-stage approach explicitly aligns flow-based generative modeling with behavioral objectives (social compliance, physical feasibility) using Reinforcement Learning (GRPO) applied to the flow's SDE formulation.

## Evidence

> we perform Flow-GRPO post-training,where deterministic flow rollout is reformulated as stochastic ODE-to-SDE sampling to enable trajectory exploration, and a composite reward combines view-aware social compliance with map-aware physical feasibility.

## Related Papers

- [[openalex-2603.24936-tigflow-grpo-trajectory-forecasting-via-interaction-aware-fl]]
- [[openalex-2605.14696-eponav2-driving-world-model-with-comprehensive-future-reason]]