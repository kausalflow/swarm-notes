---
# CSL-compatible fields
title: "EvoTS: Evolutionary Transformer Search for Time Series Forecasting"
author:
  - literal: "Abdelrahman Elsaid"
  - literal: "Damir Pulatov"
issued:
  date-parts:
    - [2026, 7, 10]
url: "https://arxiv.org/abs/2607.00154"

# Custom fields
paper_id: "2607.00154"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "time-series"
  - "forecasting"
  - "neural-architecture-search"
  - "nas"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "evots-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-12T07:23:57Z"
created_at: "2026-07-12T07:23:57Z"
---

# EvoTS: Evolutionary Transformer Search for Time Series Forecasting

**Authors**: Abdelrahman Elsaid, Damir Pulatov
**Date**: 2026-07-10
**Paper ID**: [openalex:2607.00154](https://arxiv.org/abs/2607.00154)

## Summary

EvoTS addresses the limitations of fixed Transformer architectures in time-series forecasting by employing an evolutionary neural architecture search (NAS) framework to discover task-adaptive models. The system utilizes a modular genome representation and a structural repair mechanism to explore a diverse space of attention, feed-forward, and projection configurations. Evaluations on ETT family datasets across various horizons and forecasting settings show that evolved architectures consistently match or outperform standard Transformer baselines.

## Key Contributions

- Introduces EvoTS, an evolutionary neural architecture search (NAS) framework that automates the discovery of task-adaptive Transformer architectures.
- Implements a modular genome representation and structural repair mechanism to enable valid architecture search in multivariate time-series forecasting.
- Demonstrates competitive or superior MSE performance on ETT benchmark datasets across multiple forecasting horizons and settings compared to traditional fixed-architecture Transformers.

## Open Questions & Future Work

- [[multistage-retokenization-time-series]]

## Key Concepts

- [[evots-framework]]: An evolutionary neural architecture search (NAS) framework that evolves task-adaptive, modular Transformer architectures for multivariate time-series forecasting.

## Archivist Review

The EvoTS framework is approved for its distinct contribution in applying NAS to time-series Transformer architectures via a modular genome representation. I rejected the open question on multi-objective NAS optimization because multi-objective NAS is already a standard concept in architecture search research, rendering the application-specific proposal not novel enough for a standalone entry. The multi-stage retokenization question was retained as it highlights a specific structural bottleneck in current forecasting transformers.

### Approved Concepts
- EvoTS framework: It establishes a dedicated paradigm for optimizing Transformer architectures to time-series specific tasks using evolutionary strategies.

### Approved Open Questions
- Multi-stage architectural search expansion: It addresses the structural rigidity of current time-series Transformers which often fail to exploit hierarchical multiscale temporal structures.

### Rejected Candidates
- [open_question] Multi-objective architectural fitness optimization (`multi-objective-nas-forecasting`) - not_novel: Multi-objective NAS is a well-established field, and proposing its application as a future work item in a specific domain is not a novel open question.

## Links

- [Abstract](https://arxiv.org/abs/2607.00154)
- [PDF](https://arxiv.org/pdf/2607.00154)

