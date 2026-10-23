---
# CSL-compatible fields
title: "Turning TS2Vec into a Foundation Model for Time Series Classification"
author:
  - literal: "Vasilii Feofanov"
  - literal: "Zhenghan Tai"
  - literal: "Andrei Ermakov"
  - literal: "Irina Rish"
issued:
  date-parts:
    - [2026, 10, 20]
url: "https://arxiv.org/abs/2610.28602"

# Custom fields
paper_id: "2610.28602"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "pre-training"
  - "representation-learning"
  - "convolutional-neural-network"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "ts2vec-fm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-23T09:39:48Z"
created_at: "2026-10-23T09:39:48Z"
---

# Turning TS2Vec into a Foundation Model for Time Series Classification

**Authors**: Vasilii Feofanov, Zhenghan Tai, Andrei Ermakov, Irina Rish
**Date**: 2026-10-20
**Paper ID**: [openalex:2610.28602](https://arxiv.org/abs/2610.28602)

## Summary

This paper introduces TS2Vec-FM, adapting the classical per-dataset TS2Vec model into a general time series foundation model. By pre-training on a synthetic corpus using a dual-view input stem (raw amplitude and instance-normalized shape) and distilling specialist encoders into a single model, the 1.6M-parameter frozen dilated convolutional network reaches competitive performance on UCR-128 and UEA-27 benchmarks under linear probing. The findings challenge the necessity of attention mechanisms and patch tokenizers for building effective time series foundation models.

## Key Contributions

- Proposes TS2Vec-FM, turning the per-dataset TS2Vec model into a cross-dataset time series foundation model using synthetic corpus pre-training, raw-amplitude and instance-normalized shape stems, and specialist distillation.
- Achieves 83.3% accuracy on UCR-128 and 75.3% on UEA-27 under linear probing with a frozen 1.6M-parameter dilated convolutional network, coming within 0.3 pp of the state of the art.
- Demonstrates that competitive time series foundation models can be built without attention mechanisms, patch tokenizers, or intermediate-layer extraction by relying on an optimized convolutional encoder and two-layer MLP stems.

## Limitations

Evaluated primarily on classification benchmarks (UCR and UEA); downstream generalization to forecasting and other time series tasks remains to be explored.

## Open Questions & Future Work

- [[specialist-distillation-generalization]]

## Key Concepts

- [[ts2vec-fm]]: A time series foundation model adapting TS2Vec via synthetic corpus pre-training, dual-amplitude-shape stems, and distillation into a single frozen dilated convolutional encoder.

## Archivist Review

The concept TS2Vec-FM is approved because it introduces a distinctive convolutional foundation model architecture via synthetic corpus pre-training and distillation. The open question regarding specialist distillation generalization is also approved as it tackles an important cross-architecture question. The dataset was rejected in accordance with the scarcity policy for standard benchmark archives.

### Approved Concepts
- TS2Vec-FM: Presents a novel adaptation of the TS2Vec convolutional architecture into a cross-dataset time series foundation model using synthetic pre-training, dual-view stems, and view distillation.

### Approved Open Questions
- Generalization of Specialist Distillation: Determining whether specialist distillation is architecture-agnostic helps establish it as a universal pre-training paradigm for time series representation learning.

### Rejected Candidates
- [dataset] UCR-128 (`ucr-128`) - not_novel: Standard benchmark archive rather than a novel or uniquely critical standalone dataset contribution.

## Links

- [Abstract](https://arxiv.org/abs/2610.28602)
- [PDF](https://arxiv.org/pdf/2610.28602)

