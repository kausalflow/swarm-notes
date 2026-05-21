---
created_at: '2026-05-21T08:36:39Z'
source_papers:
- '[[openalex-2605.17792-hydroagent-closing-the-gap-between-frontier-llms-and-human-e]]'
title: Multi-modal Critics for Calibration
---

**Background:** Many scientific domains rely on complex, non-differentiable numerical simulators where traditional gradient-based optimization is impossible and calibration is performed through iterative parameter refinement.

**Question / Future Work:** There is a need to determine whether vision-language verifiers, which can interpret visual diagnostic plots, can provide more robust reward signals than traditional scalar metrics like NSE in scientific calibration tasks.

**Why It Matters:** Replacing narrow, scalar rewards with richer, multi-modal feedback could solve persistent bottlenecks in physical simulator calibration where single-metric optimization often leads to suboptimal results.

**Evidence:** The strict pair-to-pair scalar comparator can be replaced with a vision-language verifier that reads a rendered hydrograph plot—simulated, observed, and residual—directly.