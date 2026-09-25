---
# CSL-compatible fields
title: "Evaluating Accuracy and Probabilistic Reliability of Zero-Shot Time Series Foundation Models"
author:
  - literal: "Panagiotis Michael"
  - literal: "Moysis Symeonides"
  - literal: "Demetris Trihinas"
issued:
  date-parts:
    - [2026, 9, 22]
url: "https://arxiv.org/abs/2609.25788"

# Custom fields
paper_id: "2609.25788"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "foundation-model"
  - "zero-shot-learning"
  - "benchmark"
  - "evaluation"
  - "xlstm"
  - "transformer"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-25T09:53:56Z"
created_at: "2026-09-25T09:53:56Z"
---

# Evaluating Accuracy and Probabilistic Reliability of Zero-Shot Time Series Foundation Models

**Authors**: Panagiotis Michael, Moysis Symeonides, Demetris Trihinas
**Date**: 2026-09-22
**Paper ID**: [openalex:2609.25788](https://arxiv.org/abs/2609.25788)

## Summary

This paper presents a benchmark evaluation of six Time Series Foundation Models across energy, traffic, and financial datasets, analyzing the trade-offs between zero-shot point accuracy and probabilistic reliability. The study shows that while TSFMs outperform statistical baselines and supervised deep learning models, they face a fundamental trade-off where xLSTM architectures achieve superior calibration across horizons, whereas patch-based transformers experience calibration degradation at long horizons and standard transformers suffer from context saturation. These insights provide practical guidance for balancing generalization and uncertainty quantification in real-world deployments.

## Key Contributions

- Presents a comprehensive benchmark study evaluating six Time Series Foundation Models (TSFMs) against statistical baselines and supervised deep learning models across energy, traffic, and financial datasets.
- Reveals a fundamental trade-off between point forecasting accuracy and probabilistic reliability in zero-shot TSFMs.
- Demonstrates that xLSTM architectures provide robust probabilistic calibration across horizons, whereas patch-based transformers struggle with calibration at long horizons and standard transformer models exhibit context saturation points.

## Open Questions & Future Work

- [[tsfm-multivariate-robustness-drift]]

## Archivist Review

Rigorously evaluated the paper and found no novel, reusable concepts or specific theoretical open questions that surpass our strict threshold. The open question was rejected as standard future work for benchmark papers.

### Approved Open Questions
- Multivariate and Robustness Benchmarking for TSFMs: Evaluating robustness under real-world data imperfections and multivariate dependencies is critical for deploying foundation models safely in industrial pipelines.

### Rejected Candidates
- [open_question] Multivariate and Robustness Benchmarking for TSFMs (`tsfm-multivariate-robustness-drift`) - low_impact: The open question is essentially future work regarding multivariate extension and robustness testing, but it captures standard benchmark limitations rather than a specific unresolved methodological bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.25788)
- [PDF](https://arxiv.org/pdf/2609.25788)

