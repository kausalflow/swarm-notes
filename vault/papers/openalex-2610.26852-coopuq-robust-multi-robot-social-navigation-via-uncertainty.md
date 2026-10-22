---
# CSL-compatible fields
title: "CoopUQ: Robust Multi-Robot Social Navigation via Uncertainty-Aware Cooperative Forecasting"
author:
  - literal: "Zehao Wang"
  - literal: "Jianpeng Yao"
  - literal: "Yuping Wang"
  - literal: "Yiping Li"
  - literal: "Jiaqi Li"
  - literal: "Zhixu Li"
  - literal: "Kanghoon Lee"
  - literal: "Jinfeng Wang"
  - literal: "Cong Liu"
  - literal: "Zhaowei Tan"
  - literal: "Jinkyoo Park"
  - literal: "Jiachen Li"
issued:
  date-parts:
    - [2026, 10, 19]
url: "https://arxiv.org/abs/2610.26852"

# Custom fields
paper_id: "2610.26852"
paper_source: "openalex"
domain: "robotics"
tags:
  - "reinforcement-learning"
  - "multi-agent"
  - "autonomous-agent"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-22T09:44:36Z"
created_at: "2026-10-22T09:44:36Z"
---

# CoopUQ: Robust Multi-Robot Social Navigation via Uncertainty-Aware Cooperative Forecasting

**Authors**: Zehao Wang, Jianpeng Yao, Yuping Wang, Yiping Li, Jiaqi Li, Zhixu Li, Kanghoon Lee, Jinfeng Wang, Cong Liu, Zhaowei Tan, Jinkyoo Park, Jiachen Li
**Date**: 2026-10-19
**Paper ID**: [openalex:2610.26852](https://arxiv.org/abs/2610.26852)

## Summary

Multi-robot navigation in human-shared environments often suffers under occlusions and out-of-distribution scenarios due to inaccurate individual risk assessments. To address this, the paper introduces CoopUQ, a multi-robot social navigation framework combining uncertainty-aware cooperative occupancy forecasting via spatiotemporal feature fusion with constrained multi-agent reinforcement learning. By leveraging forecast uncertainty to penalize risky navigation paths, CoopUQ enables policies to adapt their risk sensitivity under distribution shifts, outperforming baseline methods in both Unity3D simulations and real-world robot experiments.

## Key Contributions

- CoopUQ proposes an uncertainty-aware cooperative occupancy forecasting and robust decision-making framework for multi-robot social navigation under occlusions and OOD scenarios.
- Combines cross-robot spatiotemporal feature fusion for future occupancy grid map prediction with constrained multi-agent reinforcement learning that penalizes navigation through uncertain or occupied regions.
- Demonstrates improved prediction performance and safety across multiple Unity3D-based simulation environments with diverse pedestrian densities and rushing behaviors, as well as real-robot deployments.

## Archivist Review

Applied strict review criteria to reject the proposed open question, as it describes standard broad future work directions (heterogeneous robots, semantic occupancy, and broader environments) rather than a tightly scoped, technically concrete unresolved bottleneck. No concepts or datasets were proposed or approved.

### Rejected Candidates
- [open_question] Heterogeneous and Semantic Cooperative Navigation (`heterogeneous-semantic-cooperative-navigation`) - low_impact: Future work directions involving heterogeneous robots and richer semantic modalities are too broad and open-ended for our selective research vault.

## Links

- [Abstract](https://arxiv.org/abs/2610.26852)
- [PDF](https://arxiv.org/pdf/2610.26852)

