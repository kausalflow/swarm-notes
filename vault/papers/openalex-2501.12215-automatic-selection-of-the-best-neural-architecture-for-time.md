---
# CSL-compatible fields
title: "Automatic selection of the best neural architecture for time series forecasting"
author:
  - literal: "Qianying Cao"
  - literal: "Shanqing Liu"
  - literal: "Alan John Varghese"
  - literal: "Jérôme Darbon"
  - literal: "Michael S. Triantafyllou"
  - literal: "George Em Karniadakis"
issued:
  date-parts:
    - [2026, 6, 2]
url: "https://arxiv.org/abs/2501.12215"

# Custom fields
paper_id: "2501.12215"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "neural-architecture-search"
  - "transformer"
  - "attention-mechanism"
  - "lstm"
  - "gru"
  - "ssm"
architectures:
  []
datasets:
  []
concept_slugs:
  - "multi-objective-neural-architecture-search-for-time-series"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-05T08:37:41Z"
created_at: "2026-06-05T08:37:41Z"
---

# Automatic selection of the best neural architecture for time series forecasting

**Authors**: Qianying Cao, Shanqing Liu, Alan John Varghese, Jérôme Darbon, Michael S. Triantafyllou, George Em Karniadakis
**Date**: 2026-06-02
**Paper ID**: [openalex:2501.12215](https://arxiv.org/abs/2501.12215)

## Summary

The authors present an automated framework for designing hybrid time series forecasting architectures by combining LSTM, GRU, attention, and SSM modules. Through multi-objective optimization, the system identifies Pareto-optimal designs that effectively balance accuracy, computational complexity, and inference speed. Additionally, two sampling-based iterative exploration procedures are introduced, which reduce the total computational cost of model discovery by nearly eightfold. Results across four benchmarks suggest that optimal forecasting architectures are highly task-dependent, favoring hybrid compositions for balanced performance profiles.

## Key Contributions

- Introduces an automated framework that constructs hybrid neural architectures from LSTM, GRU, attention, and SSM blocks for time series forecasting.
- Employs a multi-objective optimization strategy to identify Pareto-optimal architectures tailored to specific user-defined accuracy-complexity constraints.
- Develops two sampling-based iterative procedures for Pareto-front exploration, yielding nearly an 8x reduction in total training cost compared to exhaustive search.
- Demonstrates that hybrid compositions outperform single architectures when balancing accuracy and computational complexity across diverse time series benchmarks.

## Key Concepts

- [[multi-objective-neural-architecture-search-for-time-series]]: A framework that systematically designs hybrid time series architectures using multi-objective optimization to balance accuracy, complexity, and computational cost.

## Archivist Review

I approved the overarching concept of multi-objective neural architecture search for time series, as it represents a significant, reusable methodological shift towards objective-driven model design. I rejected the duplicate concept proposal as it was redundant. No datasets or open questions met the high bar for permanent tracking.

### Approved Concepts
- Multi-objective neural architecture search for time series: It shifts the paradigm of time series forecasting from static architecture selection to objective-driven, automated composition of heterogeneous modules.

### Rejected Candidates
- [concept] Multi-objective optimization for Pareto-optimal architectures (`multi-objective-optimization-for-pareto-optimal-architectures`) - duplicate_existing: This is effectively the same as the overarching multi-objective NAS concept identified.

## Links

- [Abstract](https://arxiv.org/abs/2501.12215)
- [PDF](https://arxiv.org/pdf/2501.12215)

