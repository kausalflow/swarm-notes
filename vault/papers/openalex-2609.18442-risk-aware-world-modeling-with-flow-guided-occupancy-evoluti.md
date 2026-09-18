---
# CSL-compatible fields
title: "Risk-Aware World Modeling with Flow-Guided Occupancy Evolution for Selective Trajectory Planning in Automated Driving"
author:
  - literal: "Rongxiang Zeng"
  - literal: "Linsen Cai"
  - literal: "Jiafu Zhang"
  - literal: "Yijie Zhong"
  - literal: "Yide Tao"
  - literal: "Shuai Wang"
  - literal: "Nan Zheng"
  - literal: "Hai L. Vu"
  - literal: "Alvaro Garcia Hernandez"
  - literal: "Yongqi Dong"
issued:
  date-parts:
    - [2026, 9, 16]
url: "https://arxiv.org/abs/2609.18442"

# Custom fields
paper_id: "2609.18442"
paper_source: "openalex"
domain: "robotics"
tags:
  - "autonomous-agent"
  - "planning"
  - "robustness"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-18T09:18:03Z"
created_at: "2026-09-18T09:18:03Z"
---

# Risk-Aware World Modeling with Flow-Guided Occupancy Evolution for Selective Trajectory Planning in Automated Driving

**Authors**: Rongxiang Zeng, Linsen Cai, Jiafu Zhang, Yijie Zhong, Yide Tao, Shuai Wang, Nan Zheng, Hai L. Vu, Alvaro Garcia Hernandez, Yongqi Dong
**Date**: 2026-09-16
**Paper ID**: [openalex:2609.18442](https://arxiv.org/abs/2609.18442)

## Summary

The paper introduces RiskWorld, a risk-aware world modeling framework that integrates spatial risk fields and flow-guided occupancy evolution for selective trajectory planning in automated driving. By reusing a single occupancy forecast across multiple candidate trajectories with a nonnegative collision-score correction, RiskWorld efficiently evaluates planning alternatives and triggers replacement only when predicted risks exceed safety bounds. Evaluated on the nuScenes open-loop planning benchmark, RiskWorld achieves superior safety with the lowest collision rate at a 3 s horizon while maintaining competitive trajectory accuracy and real-time execution speeds.

## Key Contributions

- Introduces RiskWorld, a risk-aware world modeling framework combining spatial risk fields, temporal actor context, and flow-guided occupancy evolution for selective trajectory planning.
- Employs forecast reuse across planning candidates with a nonnegative collision-score correction to evaluate trajectories efficiently.
- Achieves the lowest collision rate at a 3 s evaluation horizon and second-best average L2 error on the nuScenes open-loop planning benchmark at 11.5 FPS.

## Limitations

evaluated primarily on open-loop planning using camera features and dataset-provided map context.

## Archivist Review

Applied strict criteria: rejected the paper-local framework 'RiskWorld' and its corresponding open question because they are specific to autonomous driving motion planning rather than generally reusable time series or forecasting mechanisms.

### Rejected Candidates
- [concept] RiskWorld (`riskworld`) - paper_local: Paper-local architecture and framework name for a specific autonomous driving system.
- [open_question] Reactive Closed-Loop Planning and Uncertainty (`reactive-closed-loop-planning-and-uncertainty`) - paper_local: Paper-local future work direction on autonomous driving planning.

## Links

- [Abstract](https://arxiv.org/abs/2609.18442)
- [PDF](https://arxiv.org/pdf/2609.18442)

