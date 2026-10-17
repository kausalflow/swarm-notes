---
created_at: '2026-10-17T08:56:01Z'
source_papers:
- '[[openalex-2610.20369-real-refine-neural-operators-via-aligning-dynamical-flow]]'
title: Physics-Guided Reward Formulation for PDEs
---

**Background:** Neural ordinary differential equations and flow matching models for partial differential equations face error accumulation during autoregressive multi-step rollouts.

**Question / Future Work:** Investigate how physics-specific reward functions (such as vorticity, divergence, or kinetic energy constraints) can be optimized alongside or instead of standard error metrics in trajectory-level reinforcement learning to improve long-term physical consistency and prevent metric misalignment.

**Why It Matters:** Understanding how to correctly formulate proxy rewards for dynamical systems is crucial for aligning generative video/fluid models with real-world physical laws without destabilizing training.

**Evidence:** FE optimization does not consistently minimize FE, indicating that physics-specific rewards need not improve their corresponding metrics.