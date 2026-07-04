---
# CSL-compatible fields
title: "LeNEPA: No-Augmentation Next-Latent Prediction for Time-Series Representation Learning"
author:
  - literal: "Alexander Chemeris"
  - literal: "Ming Jin"
  - literal: "Randall Balestriero"
issued:
  date-parts:
    - [2026, 7, 1]
url: "https://arxiv.org/abs/2607.00958"

# Custom fields
paper_id: "2607.00958"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "self-supervised-learning"
  - "representation-learning"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "lenepa"
  - "sigreg"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-04T07:35:45Z"
created_at: "2026-07-04T07:35:45Z"
---

# LeNEPA: No-Augmentation Next-Latent Prediction for Time-Series Representation Learning

**Authors**: Alexander Chemeris, Ming Jin, Randall Balestriero
**Date**: 2026-07-01
**Paper ID**: [openalex:2607.00958](https://arxiv.org/abs/2607.00958)

## Summary

LeNEPA addresses the over-reliance on domain-specific data augmentations in time-series self-supervised learning by introducing an augmentation-free predictive objective. By replacing traditional stability mechanisms like EMA or stop-gradients with SIGReg-based isotropy regularization, LeNEPA achieves robust representation learning that generalizes well across domains without tuning. Evaluation on PTB-XL and synthetic diagnostic datasets demonstrates faster convergence and competitive performance against established models like MOMENT.

## Key Contributions

- Introduced LeNEPA, an augmentation-free time-series SSL architecture using a causal backbone and SIGReg-based isotropy regularization.
- Demonstrated that LeNEPA maintains performance across domain shifts where standard JEPA recipes degrade when configurations are reused.
- Showed that LeNEPA reaches 80% performance significantly faster (2-5k updates) compared to standard JEPA (5-10k updates) in frozen-probe evaluation.

## Open Questions & Future Work

- [[universal-sigreg-hyperparameters-time-series]]

## Key Concepts

- [[lenepa]]: A self-supervised learning architecture for time series that uses a no-augmentation next-latent prediction objective stabilized by SIGReg-based isotropy regularization.
- [[sigreg]]: An isotropy regularization technique used to stabilize neural latent space training without requiring stop-gradients or exponential moving averages.

## Archivist Review

The paper introduces LeNEPA, a novel no-augmentation SSL framework for time series, and SIGReg, the associated isotropy regularization mechanism that enables this approach. I approved these as foundational concepts because they represent a departure from standard augmentation-heavy SSL recipes. I also approved an open question concerning the lack of universal regularization hyperparameters, as this is the primary bottleneck preventing the proposed no-augmentation approach from achieving true cross-domain portability. Datasets were rejected as either too routine or lack of broad community significance.

### Approved Concepts
- LeNEPA: It is the primary methodological contribution, proposing an augmentation-free, isotropic latent prediction objective for time-series SSL that replaces standard stabilization techniques like EMA/stop-gradients with SIGReg.
- SIGReg: This regularization method is the core stability mechanism enabling LeNEPA's no-augmentation objective, serving as a functional replacement for common but complex stabilization heuristics like EMA.

### Approved Open Questions
- Universal Hyperparameters for SIGReg: Understanding how to define stable, cross-domain defaults for regularization is the primary hurdle in realizing 'no-augmentation' SSL frameworks that are truly independent of domain-specific engineering.

### Rejected Candidates
- [dataset] PTB-XL (`PTB-XL`) - not_novel: Routine clinical dataset already widely used in time-series research.
- [dataset] Diag (`Diag`) - low_impact: Synthetic diagnostic corpus generated for this study and lacks broad adoption as a standard reference.

## Links

- [Abstract](https://arxiv.org/abs/2607.00958)
- [PDF](https://arxiv.org/pdf/2607.00958)

