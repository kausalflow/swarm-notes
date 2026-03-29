---
# CSL-compatible fields
title: "TIGFlow-GRPO: Trajectory Forecasting via Interaction-Aware Flow Matching and Reward-Driven Optimization"
author:
  - literal: "Xuepeng Jing"
  - literal: "Wenhuan Lu"
  - literal: "Hao Meng"
  - literal: "Zhizhi Yu"
  - literal: "Jianguo Wei"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.24936"

# Custom fields
paper_id: "2603.24936"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "llm"
  - "diffusion-model"
  - "multimodal"
  - "planning"
  - "agent"
  - "reinforcement-learning"
  - "attention-mechanism"
architectures:
  []
datasets:
  - "ETH/UCY"
  - "SDD"
concept_slugs:
  - "trajectory-interaction-graph-tig"
  - "flow-grpo-post-training"
dataset_slugs:
  - "ethucy"
  - "sdd"
skill: "TimeSeriesSkill"
processed_at: "2026-03-29T06:07:28Z"
created_at: "2026-03-29T06:07:28Z"
---

# TIGFlow-GRPO: Trajectory Forecasting via Interaction-Aware Flow Matching and Reward-Driven Optimization

**Authors**: Xuepeng Jing, Wenhuan Lu, Hao Meng, Zhizhi Yu, Jianguo Wei
**Date**: 2026-03-26
**Paper ID**: [openalex:2603.24936](https://arxiv.org/abs/2603.24936)

## Summary

TIGFlow-GRPO is a two-stage generative framework designed to improve human trajectory forecasting by integrating social and physical constraints into flow-based models. The first stage utilizes a Trajectory-Interaction-Graph (TIG) module to enhance the context encoding within a Conditional Flow Matching (CFM) predictor, capturing rich spatio-temporal interactions. The second stage introduces Flow-GRPO post-training, which converts the deterministic flow rollout into a stochastic SDE sampling process optimized by a composite reward that enforces view-aware social compliance and map-aware physical feasibility. Evaluations on ETH/UCY and SDD show that this approach achieves better accuracy and generates more behaviorally plausible, stable long-horizon trajectories.

## Key Contributions

- Proposed TIGFlow-GRPO, a two-stage framework connecting Conditional Flow Matching trajectory generation with behavior-aware alignment.
- Introduced the Trajectory-Interaction-Graph (TIG) module within the CFM framework to effectively model fine-grained agent-agent and agent-scene interactions.
- Developed Flow-GRPO post-training to refine predictions by reformulating deterministic flow rollout as stochastic SDE sampling guided by composite rewards for social compliance and physical feasibility.
- Demonstrated improvements in accuracy, long-horizon stability, and behavioral realism on ETH/UCY and SDD datasets.

## Limitations

The paper primarily focuses on connecting flow-based modeling with behavioral alignment, suggesting further exploration might be needed to fully analyze the impact of different reward components or the scalability to very large scenes.

## Open Questions & Future Work

- [[statistical-distribution-vs-behavioral-alignment]]
- [[stochastic-rl-optimization-of-ode-flows]]
- [[long-horizon-error-accumulation-mitigation]]

## Key Concepts

- [[trajectory-interaction-graph-tig]]: A graph-based module used within a Conditional Flow Matching framework to encode rich spatio-temporal interactions between agents and the scene for trajectory forecasting.
- [[flow-grpo-post-training]]: A post-training optimization technique that applies a Reward-Driven Optimization (GRPO) over the stochastic sampling process derived from a Continuous Normalizing Flow (CNF) to steer trajectory predictions towards desired behavioral outcomes.

## Archivist Review

Two core reusable concepts (TIG and Flow-GRPO Post-training) were approved as they represent novel methodological contributions to combining flow-based generation with RL alignment. Two established open questions concerning the distribution-vs-behavior gap and RL optimization over flow dynamics were also approved, alongside a strong candidate on long-horizon error accumulation. The final proposed open question was rejected as it was too vague and listed as generic future work. The datasets ETH/UCY and SDD were approved as they are standard benchmarks in trajectory forecasting.

### Approved Concepts
- Trajectory-Interaction-Graph (TIG): It explicitly models fine-grained agent-agent and agent-scene relations via a graph structure to enrich the conditional features for the flow-based model.
- Flow-GRPO Post-training: This novel two-stage approach explicitly aligns flow-based generative modeling with behavioral objectives (social compliance, physical feasibility) using Reinforcement Learning (GRPO) applied to the flow's SDE formulation.

### Approved Open Questions
- Bridging Distribution Fitting and Behavioral Alignment: Successfully bridging this gap is crucial for deploying trajectory forecasters in safety-critical applications like autonomous driving, where adherence to physical and social laws is paramount.
- Stochastic RL Optimization of ODE Flows: The ODE-to-SDE reformulation allows for the application of RL techniques to continuous generative models, but the stability and optimal control of this stochastic sampling for long-horizon, multimodal motion prediction warrant further dedicated research.
- Mitigating Long-Horizon Error Accumulation: Improving long-horizon stability is a primary bottleneck for autonomous system planning, as decision-making relies on accurate predictions far into the future.

### Rejected Candidates
- [open_question] Richer Visual and VLM Integration (`richer-visual-and-vlm-integration`) - generic: This is presented as boilerplate future work rather than a specific, established open technical bottleneck.

## Datasets

- [[ethucy]]
- [[sdd]]

## Links

- [Abstract](https://arxiv.org/abs/2603.24936)
- [PDF](https://arxiv.org/pdf/2603.24936)

