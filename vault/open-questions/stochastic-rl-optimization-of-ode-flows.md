---
created_at: '2026-03-29T06:07:28Z'
source_papers:
- '[[openalex-2603.24936-tigflow-grpo-trajectory-forecasting-via-interaction-aware-fl]]'
title: Stochastic RL Optimization of ODE Flows
---

**Background:** Continuous flow-based generative models inherently use deterministic rollout through an Ordinary Differential Equation (ODE) during inference and training.

**Question / Future Work:** Further investigation is needed to explore how to effectively integrate reinforcement learning, which typically requires stochastic policy exploration, with continuous flow-based generative models that inherently use deterministic ODE solvers, especially when optimizing for complex rewards over extended time horizons.

**Why It Matters:** The ODE-to-SDE reformulation allows for the application of RL techniques to continuous generative models, but the stability and optimal control of this stochastic sampling for long-horizon, multimodal motion prediction warrant further dedicated research.

**Evidence:** Standard CFM relies on deterministic rollout through an ordinary differential equation (ODE), which limits the trajectory exploration required by RL. To address this issue, we recast deterministic flow rollout during post-training as a stochastic differential equation (SDE) process, thereby injecting controlled stochasticity into generation.