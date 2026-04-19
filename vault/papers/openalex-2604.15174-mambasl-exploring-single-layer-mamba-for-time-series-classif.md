---
# CSL-compatible fields
title: "MambaSL: Exploring Single-Layer Mamba for Time Series Classification"
author:
  - literal: "Yoo-Min Jung"
  - literal: "Leekyung Kim"
issued:
  date-parts:
    - [2026, 4, 16]
url: "https://arxiv.org/abs/2604.15174"

# Custom fields
paper_id: "2604.15174"
paper_source: "openalex"
domain: "time-series"
tags:
  - "mamba"
  - "state-space-model"
  - "ssm"
  - "time-series"
  - "text-classification"
  - "benchmark"
  - "evaluation"
architectures:
  - "mamba"
datasets:
  - "uea-dataset-archive"
concept_slugs:
  - "mambasl"
dataset_slugs:
  - "uea-dataset-archive"
skill: "TimeSeriesSkill"
processed_at: "2026-04-19T06:23:54Z"
created_at: "2026-04-19T06:23:54Z"
---

# MambaSL: Exploring Single-Layer Mamba for Time Series Classification

**Authors**: Yoo-Min Jung, Leekyung Kim
**Date**: 2026-04-16
**Paper ID**: [openalex:2604.15174](https://arxiv.org/abs/2604.15174)

## Summary

MambaSL explores the efficacy of single-layer selective state space models (SSMs) for time series classification (TSC). By redesigning the selective SSM and projection layers based on specific TSC hypotheses, the authors create an efficient and high-performing model. Furthermore, the paper addresses widespread benchmarking limitations by conducting a comprehensive re-evaluation of 20 strong baselines across the complete 30-dataset UEA archive under a rigorous, reproducible protocol. Results indicate that the proposed single-layer Mamba architecture achieves state-of-the-art results, demonstrating its potential as a robust backbone for classification tasks.

## Key Contributions

- Proposes MambaSL, a streamlined, single-layer Mamba architecture specifically redesigned for time series classification.
- Establishes a unified benchmarking protocol for all 30 datasets in the UEA archive to address reproducibility and coverage issues in current TSC research.
- Achieves state-of-the-art performance on the full UEA benchmark suite while providing open-source checkpoints for all 20 re-evaluated baselines.

## Open Questions & Future Work

- [[mamba-ti-tv-parameter-optimization]]

## Key Concepts

- [[mambasl]]: A single-layer state space model architecture optimized for time series classification through redesigned selective SSM and projection layers.

## Archivist Review

I approved the MambaSL architecture concept and the open question regarding time-variant vs. time-invariant parameterization, as these represent substantive architectural contributions and research bottlenecks in the application of state space models to time series. I also approved the UEA dataset archive as it serves as the central evaluation ground for the paper. No other candidates were proposed.

### Approved Concepts
- MambaSL: Introduces a specific single-layer architectural adaptation of Mamba optimized for time series classification.

### Approved Open Questions
- Optimizing SSM Time-Variance Parameterization: This is a fundamental architectural question. Understanding the trade-off between time-invariance and time-variance in SSMs is crucial for adapting them to non-textual sequence data where temporal properties vary significantly by domain.

## Datasets

- [[uea-dataset-archive]]

## Links

- [Abstract](https://arxiv.org/abs/2604.15174)
- [PDF](https://arxiv.org/pdf/2604.15174)

