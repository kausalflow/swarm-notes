---
created_at: '2026-11-05T12:52:14Z'
source_papers:
- '[[openalex-2611.03244-forecasting-how-rlhf-responds-to-reward-model-edits-before-t]]'
title: Forecasting Incentive Evolution Along Path
---

**Background:** Reinforcement learning from human feedback (RLHF) policies are often optimized against learned reward models, but policies eventually diverge from true quality due to reward overoptimization and feature hacking. While practitioners edit reward models to fix these biases, evaluating whether an edit works currently requires expensive post-hoc reinforcement learning runs.

**Question / Future Work:** Determine whether future work can establish a reliable, pre-training method to forecast how reward model incentives (such as the covariance of features or reward differences) evolve along the path as policies drift and travel further in KL divergence.

**Why It Matters:** This is crucial because first-order pre-training forecasts fail or reverse over longer training horizons due to changing policy dynamics and shifting incentives along the optimization trajectory.

**Evidence:** How long this forecast holds depends on how far the policy travels, and thus on how the incentive changes along the path. We can measure this change at a checkpoint but cannot yet forecast it before RL.