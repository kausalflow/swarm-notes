---
# CSL-compatible fields
title: "RMISC: A Large-scale Real-world Multivariate Corpus for Time Series Foundation Models"
author:
  - literal: "Qian Sun"
  - literal: "Yong-Ming Tian"
  - literal: "Jia-Wei Huang"
  - literal: "Cheng Feng"
  - literal: "Shao-Qun Zhang"
issued:
  date-parts:
    - [2026, 7, 7]
url: "https://arxiv.org/abs/2607.06504"

# Custom fields
paper_id: "2607.06504"
paper_source: "openalex"
domain: "time-series"
tags:
  - "language-model"
  - "time-series"
  - "dataset"
  - "benchmark"
  - "pre-training"
  - "zero-shot-learning"
architectures:
  []
datasets:
  - "rmisc-corpus"
concept_slugs:
  - "rmisc-corpus"
dataset_slugs:
  - "rmisc-corpus"
skill: "TimeSeriesSkill"
processed_at: "2026-07-10T08:14:58Z"
created_at: "2026-07-10T08:14:58Z"
---

# RMISC: A Large-scale Real-world Multivariate Corpus for Time Series Foundation Models

**Authors**: Qian Sun, Yong-Ming Tian, Jia-Wei Huang, Cheng Feng, Shao-Qun Zhang
**Date**: 2026-07-07
**Paper ID**: [openalex:2607.06504](https://arxiv.org/abs/2607.06504)

## Summary

This paper addresses the performance gap between synthetic-data-trained and real-world-data-trained time series foundation models (TSFMs). The authors introduce the RMISC corpus, a massive archive of 200 real-world, multivariate datasets containing 142 billion time points. Through systematic evaluation of four TSFMs, they show that real-world multivariate training data is critical for capturing complex temporal and cross-variable dynamics. The study concludes that incorporating RMISC consistently improves zero-shot generalization across diverse benchmarks.

## Key Contributions

- Introduces the RMISC corpus, containing 200 datasets and 142 billion time points for training multivariate time series foundation models.
- Evaluates the zero-shot generalization capabilities of four advanced TSFMs across different pre-training data regimes (univariate, synthetic, and real-world).
- Demonstrates that pre-training on real-world multivariate data significantly enhances zero-shot generalization performance for both univariate and multivariate TSFMs compared to synthetic-only regimes.

## Open Questions & Future Work

- [[optimal-tsfm-pretraining-data-composition]]

## Key Concepts

- [[rmisc-corpus]]: A large-scale, open-access multivariate time series archive comprising 200 datasets and 142 billion data points.

## Archivist Review

The RMISC corpus is approved as a central, high-impact resource for training and evaluating time series foundation models. The open question regarding pretraining data composition is approved as it addresses a fundamental trade-off between synthetic scalability and real-world fidelity that is critical for the next generation of time series research.

### Approved Concepts
- RMISC Corpus: Provides a large-scale, high-quality real-world benchmark for training multivariate time series foundation models.

### Approved Open Questions
- Optimal TSFM Pretraining Composition: Identifying the ideal balance of synthetic and real-world data is essential for the efficient scaling and performance optimization of foundation models, especially given data privacy and cross-domain imbalance constraints.

## Datasets

- [[rmisc-corpus]]

## Links

- [Abstract](https://arxiv.org/abs/2607.06504)
- [PDF](https://arxiv.org/pdf/2607.06504)

