---
# CSL-compatible fields
title: "FreqCondNorm: Towards Cross-domain Predictive Maintenance through a Frequency-Conditioned Transformer Foundation Model"
author:
  - literal: "Zaynab Raounak"
  - literal: "Camille LHermine"
  - literal: "Zhiguo Zeng"
issued:
  date-parts:
    - [2026, 9, 17]
url: "https://arxiv.org/abs/2609.20535"

# Custom fields
paper_id: "2609.20535"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "time-series"
  - "pre-training"
  - "contrastive-learning"
  - "zero-shot-learning"
  - "benchmark"
  - "evaluation"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "freqcondnorm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-20T09:30:48Z"
created_at: "2026-09-20T09:30:48Z"
---

# FreqCondNorm: Towards Cross-domain Predictive Maintenance through a Frequency-Conditioned Transformer Foundation Model

**Authors**: Zaynab Raounak, Camille LHermine, Zhiguo Zeng
**Date**: 2026-09-17
**Paper ID**: [openalex:2609.20535](https://arxiv.org/abs/2609.20535)

## Summary

This paper introduces FreqCondNorm, a Transformer-based foundation model designed to overcome poor transferability in deep learning predictive maintenance across varying operating conditions and sampling frequencies. By incorporating a FiLM-style frequency-conditioned normalization layer, the model effectively unifies heterogeneous time-series signals spanning 1 Hz to ~100 kHz. Pretrained via masked auto-encoding and contrastive learning on multiple public datasets, FreqCondNorm achieves high accuracy on fault diagnosis and zero-shot transfer, though it highlights an objective mismatch for remaining useful life prediction.

## Key Contributions

- Proposes FreqCondNorm, a Transformer-based architecture featuring a FiLM-style frequency-conditioned normalization layer for cross-domain predictive maintenance across signals spanning five orders of magnitude in sampling frequency.
- Pretrains on five public predictive maintenance datasets using masked auto-encoding and contrastive learning with balanced domain sampling.
- Achieves 99.2% accuracy on CWRU and 82.1% zero-shot accuracy on MFPT, demonstrating robust transfer learning across sampling frequencies.

## Limitations

The approach does not improve remaining useful life (RUL) prediction, indicating a task-specific objective mismatch during pretraining.

## Open Questions & Future Work

- [[improving-rul-regression-pretraining]]

## Key Concepts

- [[freqcondnorm]]: A Transformer-based architecture using a frequency-conditioned normalization layer to unify heterogeneous time-series across different sampling frequencies.

## Archivist Review

Approved FreqCondNorm as a distinct frequency-conditioned normalization method for heterogeneous time-series. Retained the open question on improving RUL regression pretraining due to its clarity on the task mismatch limitation. Rejected the metadata extension open question and aggregate dataset list.

### Approved Concepts
- FreqCondNorm: It introduces a FiLM-style frequency-conditioned normalization layer to handle multi-frequency time-series signals spanning five orders of magnitude.

### Approved Open Questions
- Improving RUL Regression Pretraining: Addressing the pretraining-task mismatch for prognostic regression is essential to bridging the performance gap between fault diagnosis and remaining useful life prediction foundation models.

### Rejected Candidates
- [open_question] Extending Conditioning Vector with Metadata (`extending-conditioning-vector-metadata`) - low_impact: Minor incremental exploration of metadata conditioning rather than a foundational unresolved bottleneck.
- [dataset] Predictive Maintenance Datasets (`cwru-mfpt-uoc18-pronostia-cmapss`) - not_reusable: Listing multiple aggregate benchmark datasets is not appropriate for vault entry.

## Links

- [Abstract](https://arxiv.org/abs/2609.20535)
- [PDF](https://arxiv.org/pdf/2609.20535)

