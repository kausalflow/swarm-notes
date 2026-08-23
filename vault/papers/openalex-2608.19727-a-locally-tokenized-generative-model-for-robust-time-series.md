---
# CSL-compatible fields
title: "A Locally Tokenized Generative Model for Robust Time-Series Watermarking"
author:
  - literal: "Dongbin Kim"
  - literal: "Geonwoo Shin"
  - literal: "Yujin Choi"
  - literal: "Soyeon Park"
  - literal: "Jaewook Lee"
issued:
  date-parts:
    - [2026, 8, 20]
url: "https://arxiv.org/abs/2608.19727"

# Custom fields
paper_id: "2608.19727"
paper_source: "openalex"
domain: "time-series"
tags:
  - "generative-adversarial-network"
  - "time-series"
  - "robustness"
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
processed_at: "2026-08-23T05:19:14Z"
created_at: "2026-08-23T05:19:14Z"
---

# A Locally Tokenized Generative Model for Robust Time-Series Watermarking

**Authors**: Dongbin Kim, Geonwoo Shin, Yujin Choi, Soyeon Park, Jaewook Lee
**Date**: 2026-08-20
**Paper ID**: [openalex:2608.19727](https://arxiv.org/abs/2608.19727)

## Summary

Watermarking multivariate time series faces reliability failures due to bidirectional drift in globally coupled re-encoding detectors under post-editing attacks. To address this, the authors propose L-VQVAE, a generative model that restricts each discrete token to a bounded temporal neighborhood, alongside LVQMark, a watermarking method combining logit-bias injection and robust re-encoding. Experiments across financial, energy, and neuroimaging benchmarks show that the approach preserves generation quality while stabilizing false-positive behavior and detection power against post-editing attacks.

## Key Contributions

- Identifies bidirectional drift of the null distribution in globally coupled re-encoding detectors under post-editing attacks for time-series watermarking.
- Proposes L-VQVAE, a locally tokenized generative model producing discrete tokens from bounded temporal windows.
- Introduces LVQMark, combining logit-bias injection with robust re-encoding for reliable attack-time detection.
- Demonstrates stable detection power and false-positive control across finance, energy, and neuroimaging benchmarks.

## Archivist Review

The paper addresses time-series watermarking via local tokenization and robust re-encoding. The proposed concepts (L-VQVAE and LVQMark) are specific watermarking mechanisms rather than broad time-series forecasting primitives, and the open question is boilerplate future work calling for broader dataset evaluation. Therefore, all candidates have been rejected to maintain strict vault standards.

### Rejected Candidates
- [concept] L-VQVAE (`l-vqvae`) - paper_local: Paper-internal architecture component for watermarking time series rather than a broadly reusable time-series forecasting or modeling primitive.
- [concept] LVQMark (`lvqmark`) - paper_local: Specific paper-local watermarking method rather than a general-purpose time-series forecasting concept.
- [open_question] Broad Domain and Horizon Evaluation (`extending-evaluation-domains-horizons`) - low_impact: Boilerplate future work suggesting evaluation on more domains and longer horizons.

## Links

- [Abstract](https://arxiv.org/abs/2608.19727)
- [PDF](https://arxiv.org/pdf/2608.19727)

