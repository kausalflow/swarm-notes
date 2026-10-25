---
created_at: '2026-10-25T09:29:27Z'
source_papers:
- '[[openalex-2610.30965-energy-and-latency-first-how-deployment-constraints-reverse]]'
title: Deployment-Constrained Time-Series Benchmarking
---

**Background:** Time-series models are typically evaluated and ranked solely based on accuracy benchmarks without accounting for real-world deployment constraints such as latency deadlines and energy consumption.

**Question / Future Work:** Future research needs to establish generalized, cross-domain benchmarking methodologies and theoretical frameworks that integrate explicit hardware deployment constraints—specifically tail latency feasibility and duty-cycled inference energy—into the standard model selection process for time-series classification.

**Why It Matters:** Crucial for bridging the gap between theoretical machine learning research and resource-constrained edge/IoT deployments, where accuracy-only benchmarks frequently select models that fail to meet runtime or energy requirements.

**Evidence:** In this paper, we study a real setting where these constraints are explicit and measurable... Neither appears in the objective these models are selected on.