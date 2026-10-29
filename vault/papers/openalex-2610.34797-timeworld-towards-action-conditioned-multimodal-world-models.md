---
# CSL-compatible fields
title: "TimeWorld: Towards Action-Conditioned Multimodal World Models for Time Series Forecasting"
author:
  - literal: "Hang Ni"
  - literal: "Weijia Zhang"
  - literal: "Hao Liu"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2610.34797"

# Custom fields
paper_id: "2610.34797"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "forecasting"
  - "multimodal"
  - "language-model"
  - "pre-training"
architectures:
  []
datasets:
  []
concept_slugs:
  - "timeworld"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-29T11:10:07Z"
created_at: "2026-10-29T11:10:07Z"
---

# TimeWorld: Towards Action-Conditioned Multimodal World Models for Time Series Forecasting

**Authors**: Hang Ni, Weijia Zhang, Hao Liu
**Date**: 2026-10-26
**Paper ID**: [openalex:2610.34797](https://arxiv.org/abs/2610.34797)

## Summary

This paper introduces TimeWorld, an action-conditioned multimodal framework for time series forecasting that adapts pretrained time series foundation models (TSFMs) to model planned interventions and dynamic responses. To support this evaluation, the authors construct TSWM-Bench, a cross-domain benchmark covering seven datasets with textual interventions. By leveraging a Prototype-Guided Latent Modulation module and Action Contrastive Learning, TimeWorld effectively models how specific actions reshape future temporal dynamics without requiring dataset-specific training from scratch.

## Key Contributions

- Introduces TSWM-Bench, a cross-domain benchmark for multimodal time series world models spanning seven real-world datasets with grounded textual interventions.
- Demonstrates that simple text-prefix adaptations improve history-only time series foundation models (TSFMs), showing they encode implicit world knowledge.
- Proposes TimeWorld, a plug-in framework adapting pretrained TSFMs for action-conditioned forecasting via Prototype-Guided Latent Modulation (PLM) and Action Contrastive Learning (ACL).

## Limitations

Future work could explore scaling to broader action-outcome schemas and diverse non-textual modalities.

## Key Concepts

- [[timeworld]]: A plug-in framework that adapts pretrained time series foundation models through explicit action-response modeling.

## Archivist Review

Approved the overarching framework concept 'TimeWorld' as a reusable mechanism for action-conditioned forecasting with time series foundation models. Rejected the open question as it is relatively narrow and paper-local.

### Approved Concepts
- TimeWorld: Core novel framework introduced for action-conditioned multimodal time series forecasting using pretrained TSFMs.

### Rejected Candidates
- [open_question] Effective TSFM Action Fine-Tuning Strategies (`tsfm-action-finetuning-strategies`) - paper_local: Too paper-local and focused on specific fine-tuning mechanics of a single framework rather than a broad vault-worthy research bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.34797)
- [PDF](https://arxiv.org/pdf/2610.34797)

