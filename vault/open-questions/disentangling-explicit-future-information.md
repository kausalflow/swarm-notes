---
created_at: '2026-09-25T09:54:56Z'
source_papers:
- '[[openalex-2609.25969-predict-before-you-step-auditable-occupancy-forecasting-for]]'
title: Disentangling Explicit Future Information
---

**Background:** Dynamic obstacle avoidance policies for legged robots under sparse guidance rely on future state predictions, but separating the contribution of explicit future occupancy information from model capacity and auxiliary supervision remains an unresolved challenge.

**Question / Future Work:** Investigate methods to disentangle the benefits of explicit future occupancy predictions from model capacity, auxiliary supervision, and representation learning within end-to-end predictive navigation policies.

**Why It Matters:** Crucial for understanding whether predictive representations genuinely improve decision-making or merely act as regularizers or capacity expansions.

**Evidence:** the rollout ablation removes network, supervision, tokens and risk vector together (0.30 M of 0.94 M parameters), so separating explicit future information from supervision and capacity remains open