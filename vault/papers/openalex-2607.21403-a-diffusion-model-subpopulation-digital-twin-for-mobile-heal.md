---
# CSL-compatible fields
title: "A Diffusion-Model Subpopulation Digital Twin for Mobile Health Deployment: A Case Study on the HeartSteps Intervention"
author:
  - literal: "Ziping Xu"
  - literal: "Yuyi Chang"
  - literal: "Chun‐Lin Ni"
  - literal: "Nithin Sugavanam"
  - literal: "Asim H. Gazi"
  - literal: "Pedja Klasnja"
  - literal: "Emre Ertin"
  - literal: "Susan A. Murphy"
issued:
  date-parts:
    - [2026, 7, 23]
url: "https://arxiv.org/abs/2607.21403"

# Custom fields
paper_id: "2607.21403"
paper_source: "openalex"
domain: "time-series"
tags:
  - "diffusion-model"
  - "time-series"
  - "reinforcement-learning"
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
processed_at: "2026-07-26T07:30:41Z"
created_at: "2026-07-26T07:30:41Z"
---

# A Diffusion-Model Subpopulation Digital Twin for Mobile Health Deployment: A Case Study on the HeartSteps Intervention

**Authors**: Ziping Xu, Yuyi Chang, Chun‐Lin Ni, Nithin Sugavanam, Asim H. Gazi, Pedja Klasnja, Emre Ertin, Susan A. Murphy
**Date**: 2026-07-23
**Paper ID**: [openalex:2607.21403](https://arxiv.org/abs/2607.21403)

## Summary

This paper introduces JITAI-Twins, a conditional time-series diffusion model designed to create realistic digital twins of target subpopulations for pre-evaluating mobile health just-in-time adaptive interventions (JITAIs). The method incorporates a temporally consistent structure and a three-step updating procedure: observational pre-training, deployment fine-tuning, and expert-guided calibration. Validated across the HeartSteps intervention series, the proposed digital twin accurately reproduces complex temporal and between-participant dynamics to facilitate safer online algorithm design.

## Key Contributions

- Proposes JITAI-Twins, a conditional time-series diffusion model framework for generating temporally consistent digital twins of target subpopulations to vet just-in-time adaptive intervention algorithms prior to deployment.
- Implements a three-stage updating pipeline comprising large-scale observational pre-training, fine-tuning on prior related interventions, and inference-time calibration via domain-scientist expertise.
- Validates the digital twin across sequential HeartSteps physical-activity intervention deployments (v2 through v4), demonstrating superior reproduction of temporal and between-participant structures over simpler simulators.

## Archivist Review

The paper introduces JITAI-Twins for mobile health simulation using diffusion models. No concepts or datasets qualified as sufficiently general or canonical under our strict vault guidelines, and the single open question was paper-local.

### Rejected Candidates
- [open_question] Action-Dependent Calibration Targets (`action-dependent-calibration-targets`) - paper_local: The open question concerns specific paper-local calibration tilts and extensions rather than a broad, reusable time-series research bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2607.21403)
- [PDF](https://arxiv.org/pdf/2607.21403)

