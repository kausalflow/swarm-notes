---
# CSL-compatible fields
title: "ForcingDAS: Unified and Robust Data Assimilation via Diffusion Forcing"
author:
  - literal: "Yixuan Jia"
  - literal: "Siyi Chen"
  - literal: "Yida Pan"
  - literal: "Xiao Li"
  - literal: "Lianghe Shi"
  - literal: "Chanyong Jung"
  - literal: "Haijie Yuan"
  - literal: "Ismail Alkhouri"
  - literal: "Yue Wu"
  - literal: "Saiprasad Ravishankar"
  - literal: "Jeffrey A. Fessler"
  - literal: "Qing Qu"
issued:
  date-parts:
    - [2026, 5, 14]
url: "https://arxiv.org/abs/2605.14285"

# Custom fields
paper_id: "2605.14285"
paper_source: "openalex"
domain: "time-series"
tags:
  - "diffusion-model"
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "forcingdas"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-17T07:32:15Z"
created_at: "2026-05-17T07:32:15Z"
---

# ForcingDAS: Unified and Robust Data Assimilation via Diffusion Forcing

**Authors**: Yixuan Jia, Siyi Chen, Yida Pan, Xiao Li, Lianghe Shi, Chanyong Jung, Haijie Yuan, Ismail Alkhouri, Yue Wu, Saiprasad Ravishankar, Jeffrey A. Fessler, Qing Qu
**Date**: 2026-05-14
**Paper ID**: [openalex:2605.14285](https://arxiv.org/abs/2605.14285)

## Summary

ForcingDAS is a robust data assimilation framework that addresses the error accumulation issues in traditional frame-to-frame transition models by learning a joint-trajectory prior using diffusion forcing. By assigning independent noise levels to each frame, the framework avoids committing to a single regime, allowing the same model to perform filtering, fixed-lag smoothing, and batch reanalysis through inference schedule adjustments alone. Evaluation across fluid dynamics and global atmospheric benchmarks shows that ForcingDAS achieves competitive or superior performance compared to regime-specialized classical and learned baselines.

## Key Contributions

- Introduces ForcingDAS, a unified data assimilation framework that replaces frame-to-frame transitions with a learned joint-trajectory prior.
- Enables a flexible inference schedule that spans the full filtering to smoothing spectrum without model retraining.
- Demonstrates robust performance against state-of-the-art classical and learned baselines across nowcasting and reanalysis tasks, with significant improvements on atmospheric benchmarks.

## Open Questions & Future Work

- [[unified-da-frameworks-non-markovian-systems]]

## Key Concepts

- [[forcingdas]]: A unified data assimilation framework built on diffusion forcing that learns joint-trajectory priors to replace frame-to-frame transition models.

## Archivist Review

ForcingDAS represents a significant advancement in data assimilation by replacing iterative frame-to-frame transition models with a unified joint-trajectory prior using diffusion. The framework's ability to span filtering and smoothing regimes through inference schedule adjustments alone is a highly reusable methodology. The open question reflects a fundamental bottleneck in the field regarding the fragmentation of DA pipelines.

### Approved Concepts
- ForcingDAS: It is the core proposed framework that unifies filtering and smoothing via diffusion forcing.

### Approved Open Questions
- Unified Data Assimilation Frameworks: This is critical because operational systems currently rely on separate, specialized models for real-time forecasting and retrospective reanalysis, which is computationally redundant and fails to leverage the full latent structure of the dynamical system.

## Links

- [Abstract](https://arxiv.org/abs/2605.14285)
- [PDF](https://arxiv.org/pdf/2605.14285)

