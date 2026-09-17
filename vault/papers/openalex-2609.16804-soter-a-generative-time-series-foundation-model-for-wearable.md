---
# CSL-compatible fields
title: "SOTER: A Generative Time-Series Foundation Model for Wearable Human Physiological Signals"
author:
  - literal: "Fangke Chen"
  - literal: "Sirry Chen"
  - literal: "Wei Chen"
  - literal: "Zhongyu Wei"
issued:
  date-parts:
    - [2026, 9, 15]
url: "https://arxiv.org/abs/2609.16804"

# Custom fields
paper_id: "2609.16804"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "forecasting"
  - "pre-training"
  - "zero-shot-learning"
  - "mixture-of-experts"
  - "moe"
  - "multimodal"
  - "robustness"
  - "evaluation"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:43:14Z"
created_at: "2026-09-17T09:43:14Z"
---

# SOTER: A Generative Time-Series Foundation Model for Wearable Human Physiological Signals

**Authors**: Fangke Chen, Sirry Chen, Wei Chen, Zhongyu Wei
**Date**: 2026-09-15
**Paper ID**: [openalex:2609.16804](https://arxiv.org/abs/2609.16804)

## Summary

SOTER is a generative time-series foundation model designed specifically for wearable human physiological signals by unifying spatial feature modeling, power spectral density-guided mixture-of-experts routing, and continuous-time neural controlled differential equation decoding. Pre-trained on 226 billion time points, SOTER demonstrates robust performance across out-of-distribution zero-shot forecasting, frozen-encoder linear-probe classification, and high-missingness continuous-time imputation.

## Key Contributions

- SOTER introduces a generative time-series foundation model pre-trained on 226 billion time points that unifies cross-channel coupling, spectrum-guided expert specialization, and continuous-time latent evolution.
- It combines a spatial feature-aware backbone, a power spectral density (PSD)-guided mixture-of-experts layer using non-learned routing, and a neural controlled differential equation decoder for arbitrary timestamp imputation and prediction.
- SOTER achieves state-of-the-art zero-shot forecasting, superior frozen-encoder classification performance, and robust continuous-time imputation across wearable benchmarks even under 75% missingness and heavy acquisition noise.

## Archivist Review

Applied strict evaluation standards to ensure only highly reusable concepts and substantial, non-boilerplate open questions enter the vault. The proposed open question was rejected as boilerplate future work.

### Rejected Candidates
- [open_question] Broad Physiological Foundation Models (`physiological-foundation-model-scaling`) - weak_evidence: Boilerplate future work proposing larger pre-training corpora, broader modalities, and future clinical evaluations without a specific unresolved technical mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2609.16804)
- [PDF](https://arxiv.org/pdf/2609.16804)

