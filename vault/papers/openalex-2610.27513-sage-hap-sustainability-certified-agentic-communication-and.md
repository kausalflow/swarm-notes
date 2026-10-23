---
# CSL-compatible fields
title: "SAGE-HAP: Sustainability-Certified Agentic Communication and Computing at a Solar-Powered High-Altitude Platform"
author:
  - literal: "Haoxiang Luo"
  - literal: "Bang Huang"
  - literal: "Mohamed-Slim Alouini"
issued:
  date-parts:
    - [2026, 10, 20]
url: "https://arxiv.org/abs/2610.27513"

# Custom fields
paper_id: "2610.27513"
paper_source: "openalex"
domain: "reinforcement-learning"
tags:
  - "agent"
  - "autonomous-agent"
  - "reinforcement-learning"
  - "robustness"
  - "optimization"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-23T09:41:25Z"
created_at: "2026-10-23T09:41:25Z"
---

# SAGE-HAP: Sustainability-Certified Agentic Communication and Computing at a Solar-Powered High-Altitude Platform

**Authors**: Haoxiang Luo, Bang Huang, Mohamed-Slim Alouini
**Date**: 2026-10-20
**Paper ID**: [openalex:2610.27513](https://arxiv.org/abs/2610.27513)

## Summary

The paper introduces SAGE, a Sustainability-certified Agentic Ground-service Engine designed to manage communication and computing on solar-powered High-Altitude Platforms under uncertain solar supply and coupled resource demands. SAGE translates operator intent into candidates via an agent, which are then strictly verified using deterministic convex refinement and an action shield powered by calibrated solar lower bounds. Theoretical analysis establishes convexity, reserve safety, and online utility bounds, while simulation results confirm significant gains in energy efficiency, task completion, and constraint satisfaction over baseline Lyapunov controls.

## Key Contributions

- Proposes SAGE (Sustainability-certified Agentic Ground-service Engine), an agentic framework for solar-powered High-Altitude Platforms combining LLM candidate generation with deterministic convex refinement and action shields.
- Establishes theoretical guarantees including fixed-candidate convexity, reserve safety under calibrated solar coverage and bounded actuation error, and online utility bounds.
- Demonstrates through simulations 2.38 percentage points higher completion and 5.27% greater useful-workload energy efficiency over energy-harvesting Lyapunov control at nominal load, with reserve violations dropping from 47/50 to 1/50 under stressed conditions.

## Archivist Review

Applied strict relevance filtering per the time series and forecasting skill context. The proposed candidate open question pertains specifically to high-altitude platform (HAP) energy-constrained agentic control rather than core time-series forecasting methodology, temporal modeling, or distribution shift mechanisms, and was therefore rejected. No concepts or datasets met the strict novelty and reusability criteria for the vault.

### Rejected Candidates
- [open_question] Certified Agentic Control under Extreme Disturbances (`certified-agentic-control-under-extreme-compounding-disturbances`) - low_impact: This question addresses specialized high-altitude platform agent control systems rather than general time-series forecasting, temporal modeling, or forecasting methodology.

## Links

- [Abstract](https://arxiv.org/abs/2610.27513)
- [PDF](https://arxiv.org/pdf/2610.27513)

