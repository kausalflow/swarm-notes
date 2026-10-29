---
# CSL-compatible fields
title: "Self-Supervised Pretraining for PHM: What Transfers, What Does Not, and What Federating It Costs"
author:
  - literal: "José Sanz-Durán"
  - literal: "David Solis‐Martín"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2610.35280"

# Custom fields
paper_id: "2610.35280"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "pre-training"
  - "self-supervised-learning"
  - "transformer"
  - "federated-learning"
  - "robustness"
  - "evaluation"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-29T11:12:08Z"
created_at: "2026-10-29T11:12:08Z"
---

# Self-Supervised Pretraining for PHM: What Transfers, What Does Not, and What Federating It Costs

**Authors**: José Sanz-Durán, David Solis‐Martín
**Date**: 2026-10-26
**Paper ID**: [openalex:2610.35280](https://arxiv.org/abs/2610.35280)

## Summary

This paper investigates the effectiveness and limitations of self-supervised pretraining for Prognostics and Health Management (PHM) using a leakage-controlled corpus of 47 public datasets. The authors find that transfer is strictly task-dependent: masked patch prediction dramatically improves fault-classification performance but yields no reliable gains over from-scratch baselines for remaining-useful-life (RUL) estimation on CMAPSS. Furthermore, they compare centralized and cross-silo federated pretraining, showing that centralized training outperforms federated for classification, and demonstrate that intrinsic SSL loss is an unreliable proxy for downstream task performance.

## Key Contributions

- Evaluated self-supervised pretraining for Prognostics and Health Management (PHM) on a harmonized corpus of 47 public datasets under strict leakage-controlled conditions.
- Demonstrated task-dependent transfer: masked patch prediction significantly improves fault-classification (e.g., macro-F1 from 0.350 to 0.812 on CWRU) but fails to improve remaining-useful-life estimation on CMAPSS over a from-scratch baseline.
- Compared centralized versus simulated cross-silo federated pretraining regimes, finding that centralized pretraining outperforms federated in fault classification while both remain indistinguishable on RUL.
- Showed that intrinsic SSL loss is a poor model selection criterion and that downstream performance is extremely sensitive to backbone learning rates and server momentum.

## Limitations

Centralized and federated comparisons are confounded by a learning-rate schedule favouring the centralized arm and rely on a single pretraining run per regime.

## Open Questions & Future Work

- [[intrinsic-loss-downstream-utility-decoupling]]

## Archivist Review

Applied strict selectivity standards. The paper offers valuable empirical findings on PHM transfer learning and federated pretraining, but does not introduce a permanent standalone architectural concept or method. The open question regarding the decoupling of intrinsic SSL loss from downstream utility is approved as an important diagnostic question for self-supervised time series models.

### Approved Open Questions
- Intrinsic Loss Downstream Utility Decoupling: Crucial for model selection and architecture design, as practitioners currently lack reliable validation metrics to predict whether a pretrained time-series foundation model will succeed on downstream PHM tasks.

### Rejected Candidates
- [open_question] Intrinsic Loss Downstream Utility Decoupling (`intrinsic-loss-downstream-utility-decoupling`) - low_impact: The open question is well formulated, but given strict scarcity limits and policy guidelines, we approve only the most fundamental ones.

## Links

- [Abstract](https://arxiv.org/abs/2610.35280)
- [PDF](https://arxiv.org/pdf/2610.35280)

