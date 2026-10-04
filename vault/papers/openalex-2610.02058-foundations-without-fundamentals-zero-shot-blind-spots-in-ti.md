---
# CSL-compatible fields
title: "Foundations without Fundamentals: Zero-Shot Blind Spots in Time Series FMs"
author:
  - literal: "Nafiseh Ghoroghchian"
  - literal: "Haipeng Zhang"
  - literal: "Shuyi Han"
  - literal: "Alex Labach"
  - literal: "George Stein"
issued:
  date-parts:
    - [2026, 10, 1]
url: "https://arxiv.org/abs/2610.02058"

# Custom fields
paper_id: "2610.02058"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "evaluation"
  - "zero-shot-learning"
  - "multimodal"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-04T10:48:18Z"
created_at: "2026-10-04T10:48:18Z"
---

# Foundations without Fundamentals: Zero-Shot Blind Spots in Time Series FMs

**Authors**: Nafiseh Ghoroghchian, Haipeng Zhang, Shuyi Han, Alex Labach, George Stein
**Date**: 2026-10-01
**Paper ID**: [openalex:2610.02058](https://arxiv.org/abs/2610.02058)

## Summary

This paper evaluates the zero-shot capabilities of prominent Time Series Foundation Models (TSFMs) using SimpleTimeBench, a diagnostic suite of basic temporal primitives and exogenous covariates. The findings reveal that models like Chronos-2, Moirai, and Toto often fail on trivial patterns, and that fine-tuning only shifts failures rather than improving generalizable reasoning. These blind spots also manifest in real-world sensor forecasting, highlighting a fundamental limitation in current TSFM architectures and inductive biases.

## Key Contributions

- Introduces SimpleTimeBench, a diagnostic unit test suite for evaluating time series foundation models on fundamental primitives like monotonic trends, periodic signals, and leading indicators.
- Demonstrates that prominent multivariate time series foundation models (Chronos-2, Moirai, Toto) frequently produce suboptimal zero-shot forecasts on these trivial patterns.
- Shows that fine-tuning specific models improves performance on targeted tasks while degrading other fundamental patterns, highlighting a lack of robust inductive biases.
- Reveals that these zero-shot blind spots persist in real-world sensor forecasting where models underutilize leading indicators.

## Limitations

The study primarily highlights zero-shot and fine-tuning limitations on fundamental patterns without proposing a comprehensive architectural fix.

## Open Questions & Future Work

- [[tsfm-covariate-underutilization-inductive-biases]]

## Archivist Review

Strictly evaluated the candidate concept and open question against vault policies. The concept SimpleTimeBench is a benchmark suite and therefore does not qualify as a standalone methodological concept note. The open question regarding TSFM covariate underutilization and inductive biases is retained as it addresses a substantive architectural and training bottleneck.

### Approved Open Questions
- Inductive Biases for Leading Indicators: Understanding whether covariate underutilization stems from architectural bottlenecks or training limitations is critical for building general-purpose multivariate forecasting models that can reliably incorporate exogenous signals in high-stakes domains.

### Rejected Candidates
- [concept] SimpleTimeBench (`simpletimebench`) - not_reusable: SimpleTimeBench is a benchmark suite rather than a reusable algorithmic concept or architectural mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2610.02058)
- [PDF](https://arxiv.org/pdf/2610.02058)

