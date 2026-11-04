---
# CSL-compatible fields
title: "Hinted Scaling Laws"
author:
  - literal: "Suze van Adrichem"
  - literal: "Luke Bailey"
  - literal: "Rohith Kuditipudi"
  - literal: "Christine Ye"
  - literal: "Neil Band"
  - literal: "Ahmed Ahmed"
  - literal: "John C. Duchi"
  - literal: "Percy Liang"
  - literal: "Tatsunori Hashimoto"
issued:
  date-parts:
    - [2026, 11, 1]
url: "https://arxiv.org/abs/2611.02270"

# Custom fields
paper_id: "2611.02270"
paper_source: "openalex"
domain: "nlp"
tags:
  - "scaling-law"
  - "evaluation"
  - "benchmark"
  - "llm"
architectures:
  []
datasets:
  []
concept_slugs:
  - "hinted-scaling-laws"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-04T12:41:13Z"
created_at: "2026-11-04T12:41:13Z"
---

# Hinted Scaling Laws

**Authors**: Suze van Adrichem, Luke Bailey, Rohith Kuditipudi, Christine Ye, Neil Band, Ahmed Ahmed, John C. Duchi, Percy Liang, Tatsunori Hashimoto
**Date**: 2026-11-01
**Paper ID**: [openalex:2611.02270](https://arxiv.org/abs/2611.02270)

## Summary

Scaling law extrapolation often fails on complex downstream evaluations because small, cheaper models score near zero. To address this, the paper introduces hinted scaling laws, which use privileged information to create a continuum of easier benchmark versions where small models score above zero. This technique enables smooth extrapolation below the noise threshold, drastically reducing median forecasting error on challenging tasks like GSM8K, AIME, and HLE.

## Key Contributions

- Introduces hinted scaling laws, which leverage privileged information to transform benchmarks into an easier continuum so small models avoid floor effects.
- Demonstrates that hinted scaling laws accurately forecast GSM8K performance of a $10^{23}$ FLOP model (within 3 percentage points) when fit on models using at most $10^{20}$ FLOPs, outperforming standard scaling laws.
- Reduces the median forecasting error across GSM8K, AIME, and HLE from 21 percentage points down to 4.3 percentage points on pretraining ladders and post-trained model families.
- Shows that hinting widens accuracy gaps while preserving model rankings, reducing the required test samples for evaluation.

## Open Questions & Future Work

- [[alternative-teacher-instantiations-logit-mixing]]

## Key Concepts

- [[hinted-scaling-laws]]: A framework for extrapolating downstream model performance trends by using privileged information to transform hard benchmarks into a continuum of easier versions where weaker models score above zero.

## Archivist Review

Approved the core concept of hinted scaling laws and its explicit open question concerning teacher instantiations and logit mixing across diverse post-trained models. All review policies were carefully followed.

### Approved Concepts
- Hinted Scaling Laws: Directly addresses the fundamental limitation of zero-score floor effects in downstream scaling law extrapolation by leveraging privileged information to create a continuum of task difficulties.

### Approved Open Questions
- Alternative Teacher Instantiations and Vocabulary-Bridging Logit Mixing: This is crucial because extending hinted scaling laws and logit mixing to post-trained models without tokenizer constraints is necessary for making the method broadly applicable across proprietary or diverse open-source ecosystems.

### Rejected Candidates
- [open_question] Alternative Teacher Instantiations and Vocabulary-Bridging Logit Mixing (`alternative-teacher-instantiations-logit-mixing`) - duplicate_existing: Already approved.

## Links

- [Abstract](https://arxiv.org/abs/2611.02270)
- [PDF](https://arxiv.org/pdf/2611.02270)

