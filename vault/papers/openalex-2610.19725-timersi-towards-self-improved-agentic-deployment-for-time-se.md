---
# CSL-compatible fields
title: "TIMERSI: Towards Self-Improved Agentic Deployment for Time-Series Foundation Models"
author:
  - literal: "Haoxin Liu"
  - literal: "Deqing Fu"
  - literal: "Lucheng Fu"
  - literal: "Yiqiao Jin"
  - literal: "Rushi Qiang"
  - literal: "Harshavardhan Kamarthi"
  - literal: "B. Aditya Prakash"
issued:
  date-parts:
    - [2026, 10, 14]
url: "https://arxiv.org/abs/2610.19725"

# Custom fields
paper_id: "2610.19725"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "agent"
  - "autonomous-agent"
  - "foundation-model"
  - "zero-shot-learning"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "timersi"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-17T08:54:33Z"
created_at: "2026-10-17T08:54:33Z"
---

# TIMERSI: Towards Self-Improved Agentic Deployment for Time-Series Foundation Models

**Authors**: Haoxin Liu, Deqing Fu, Lucheng Fu, Yiqiao Jin, Rushi Qiang, Harshavardhan Kamarthi, B. Aditya Prakash
**Date**: 2026-10-14
**Paper ID**: [openalex:2610.19725](https://arxiv.org/abs/2610.19725)

## Summary

Time-series foundation models often require heavy task-specific engineering for real-world deployment, which standard zero-shot inference or manual pipelines fail to handle robustly. To address this, the authors introduce TIMERSI, a self-improving agentic deployment framework built around frozen forecasting models that uses a coding agent to iteratively translate task descriptions and error feedback into executable pipeline improvements. During inference, an adaptive selector chooses the optimal pipeline based on historical performance under similar conditions, outperforming existing approaches across 198 tasks on TIME and FEVbench.

## Key Contributions

- Introduces TIMERSI, a self-improving agentic deployment framework for frozen time-series foundation models using coding agents and error-guided pipeline revision.
- Implements an adaptive selector during deployment to dynamically choose among generated pipelines using completed forecasts under similar conditions.
- Achieves state-of-the-art performance across six point and probabilistic forecasting metrics on 198 tasks across TIME and FEVbench.

## Open Questions & Future Work

- [[distribution-shift-generalization-tsfm-deployment]]

## Key Concepts

- [[timersi]]: A self-improving agentic deployment system around frozen time-series forecasting models that uses coding agents and adaptive selectors for task-specific pipelines.

## Archivist Review

Approved the core concept TIMERSI representing the self-improving agentic deployment framework and one open question on distribution shift generalization under deployment. Rejected the paper's specific evaluation datasets as they do not meet the high threshold for standalone canonical dataset notes.

### Approved Concepts
- TIMERSI: Central contribution as a self-improving agentic deployment system for time-series foundation models.

### Approved Open Questions
- Generalization under Distribution Shift: Addressing distribution shift is critical for ensuring that self-improving agentic deployment pipelines do not overfit to historical backtests and maintain robustness during actual real-world deployment.

### Rejected Candidates
- [dataset] TIME (`time`) - low_impact: Generic or unestablished dataset name lacking sufficient standalone benchmark documentation in the vault.
- [dataset] FEVbench (`fevbench`) - low_impact: Dataset is a paper-local collection or lacks a standalone canonical entry profile compared to established benchmarks.

## Links

- [Abstract](https://arxiv.org/abs/2610.19725)
- [PDF](https://arxiv.org/pdf/2610.19725)

