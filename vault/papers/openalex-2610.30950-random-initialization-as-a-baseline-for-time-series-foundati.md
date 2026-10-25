---
# CSL-compatible fields
title: "Random Initialization as a Baseline for Time Series Foundation Models"
author:
  - literal: "Pinar Sungu Isiacik"
  - literal: "Georgiana Ifrim"
issued:
  date-parts:
    - [2026, 10, 22]
url: "https://arxiv.org/abs/2610.30950"

# Custom fields
paper_id: "2610.30950"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "pre-training"
  - "benchmark"
  - "evaluation"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "random-initialization-baseline-for-time-series-foundation-models"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-25T09:29:17Z"
created_at: "2026-10-25T09:29:17Z"
---

# Random Initialization as a Baseline for Time Series Foundation Models

**Authors**: Pinar Sungu Isiacik, Georgiana Ifrim
**Date**: 2026-10-22
**Paper ID**: [openalex:2610.30950](https://arxiv.org/abs/2610.30950)

## Summary

This paper investigates the true contribution of self-supervised pretraining in time series foundation models (TSFMs) by comparing pretrained instances with architecture-matched randomly initialized counterparts on the UEA multivariate time series classification archive. The authors find that pretraining yields only modest mean accuracy improvements (an average of 2.58 percentage points) when using frozen representations, with most models showing no statistically significant gains after correction. Furthermore, traditional non-pretrained approaches like ROCKET, Hydra, and Quant remain highly competitive, suggesting that future evaluations must rigorously separate architectural effects from pretrained weight efficacy.

## Key Contributions

- Compares seven publicly released instances from four TSFM families against architecture-matched randomly initialized counterparts across the UEA MTSC archive.
- Shows that self-supervised pretraining yields modest mean accuracy gains ranging from 1.43 to 5.19 percentage points, with an overall average improvement of 2.58 points.
- Demonstrates that classical non-pretrained baselines like ROCKET, Hydra, and Quant remain highly competitive without requiring large-scale pretraining.
- Advocates for rigorous evaluation standards in time series classification that explicitly isolate pretrained weight contributions from underlying architectural priors.

## Limitations

Focused primarily on multivariate time series classification tasks using frozen representations evaluated via linear and kernel classifiers.

## Open Questions & Future Work

- [[scaling-laws-and-capacity-in-tsfms]]

## Key Concepts

- [[random-initialization-baseline-for-time-series-foundation-models]]: Evaluating time series foundation models against architecture-matched randomly initialized counterparts to isolate the contribution of pretrained weights.

## Archivist Review

Approved the core methodology concept of architecture-matched random initialization baselines for time series foundation models, along with the open question regarding scaling laws and capacity. The UEA archive dataset was rejected as it is already standard and widely established.

### Approved Concepts
- Random Initialization Baseline for Time Series Foundation Models: Highlights that randomly initialized neural architectures can serve as strong baselines for time series foundation models, challenging the perceived necessity of self-supervised pretraining for downstream classification.

### Approved Open Questions
- Scaling Laws and Capacity in Time Series Foundation Models: Determining whether pretraining benefits scale predictably with model size and architecture is critical for resource allocation and architectural design in time series representation learning.

### Rejected Candidates
- [dataset] UEA MTSC Archive (`uea-mtsc-archive`) - not_reusable: Standard public benchmark archive, insufficiently novel or distinct to warrant a standalone architectural note.

## Links

- [Abstract](https://arxiv.org/abs/2610.30950)
- [PDF](https://arxiv.org/pdf/2610.30950)

