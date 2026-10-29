---
# CSL-compatible fields
title: "Guarded Agent-in-the-Loop Residual Adaptation for Evolving Wind Power Regimes"
author:
  - literal: "Yuhang Dong"
  - literal: "Min Xia"
  - literal: "Jinghong Li"
  - literal: "Yue Dai"
  - literal: "Xinyue Wang"
  - literal: "Shi Liang"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2610.34968"

# Custom fields
paper_id: "2610.34968"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "agent"
  - "adaptation"
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
processed_at: "2026-10-29T11:11:11Z"
created_at: "2026-10-29T11:11:11Z"
---

# Guarded Agent-in-the-Loop Residual Adaptation for Evolving Wind Power Regimes

**Authors**: Yuhang Dong, Min Xia, Jinghong Li, Yue Dai, Xinyue Wang, Shi Liang
**Date**: 2026-10-26
**Paper ID**: [openalex:2610.34968](https://arxiv.org/abs/2610.34968)

## Summary

Wind power forecasting models often suffer from performance degradation under shifting meteorological regimes like cold waves and typhoons. This paper introduces a guarded agent-in-the-loop residual adaptation framework that leaves the underlying temporal backbone unchanged while routing corrections through scene-conditioned residual experts selected by an agent layer. Evaluated across nine time-series backbones and five lead times, the proposed approach consistently reduces MAE and RMSE across all 45 backbone-horizon combinations.

## Key Contributions

- Proposes a guarded agent-in-the-loop residual adaptation framework for wind power forecasting that keeps temporal backbones frozen while adapting scene-conditioned residual experts.
- Implements an agent layer that interprets external scene information, identifies meteorological regimes, selects residual experts, and applies corrections conditionally based on recent observed errors.
- Achieves lower MAE and RMSE across all 45 backbone-horizon combinations (lead times 4, 8, 12, 24, 48 across nine backbones), with average MAE reductions between 11.21% and 20.26%.

## Limitations

Long-term unattended deployment was not evaluated.

## Archivist Review

The paper presents a guarded agent-in-the-loop residual adaptation framework for wind power forecasting. No novel concepts or datasets met the strict reusability threshold for permanent vault notes, and the single open question was rejected as being paper-local to wind power deployment limits rather than a foundational algorithmic bottleneck.

### Rejected Candidates
- [open_question] Long-Term Unattended Wind Adaptation (`long-term-unattended-wind-adaptation`) - paper_local: Paper-local evaluation limitation concerning wind power deployment rather than a foundational algorithmic open question.

## Links

- [Abstract](https://arxiv.org/abs/2610.34968)
- [PDF](https://arxiv.org/pdf/2610.34968)

