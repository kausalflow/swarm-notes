---
# CSL-compatible fields
title: "Evaluating Forecasting Techniques for Hardware Errors on a Large-scale HPC System"
author:
  - literal: "Kaiyuan Liao"
  - literal: "Xiwei Xuan"
  - literal: "Tanwi Mallick"
  - literal: "Kevin Brown"
  - literal: "Christopher D. Carothers"
  - literal: "Kwan‐Liu Ma"
issued:
  date-parts:
    - [2026, 8, 3]
url: "https://arxiv.org/abs/2608.01648"

# Custom fields
paper_id: "2608.01648"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "transformer"
  - "lstm"
  - "benchmark"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-06T07:31:41Z"
created_at: "2026-08-06T07:31:41Z"
---

# Evaluating Forecasting Techniques for Hardware Errors on a Large-scale HPC System

**Authors**: Kaiyuan Liao, Xiwei Xuan, Tanwi Mallick, Kevin Brown, Christopher D. Carothers, Kwan‐Liu Ma
**Date**: 2026-08-03
**Paper ID**: [openalex:2608.01648](https://arxiv.org/abs/2608.01648)

## Summary

This paper investigates the boundaries of applying time-series forecasting to hardware error dynamics in high-performance computing (HPC) systems using seven years of production logs from the Theta supercomputer. The authors evaluate classical statistical and deep learning models, revealing that predictive efficacy relies heavily on the temporal structure of the error series. While structurally stable and regularly occurring errors can be effectively captured by LSTM and Transformer architectures, sparse and burst-dominated errors remain challenging to predict.

## Key Contributions

- Evaluated classical statistical and deep learning forecasting models on a seven-year production log dataset from the Theta supercomputer.
- Demonstrated that forecasting efficacy is strongly dependent on the temporal structure, with regular errors modeled well by LSTM and Transformer models.
- Established empirical boundaries showing that sparse and burst-dominated HPC hardware errors remain difficult to predict accurately with standard time-series techniques.

## Limitations

Focuses on empirical evaluation of existing methods without introducing a deployment-ready failure prediction framework.

## Open Questions & Future Work

- [[hpc-error-forecasting-evaluation-criteria]]

## Archivist Review

The paper provides a comprehensive empirical evaluation of time-series forecasting techniques applied to long-term HPC hardware logs. Since no novel modeling concept or reusable mechanism is introduced, no concepts are approved. The open question regarding standardized evaluation criteria for HPC error forecasting is retained as it highlights a persistent gap in proactive maintenance benchmarks.

### Approved Open Questions
- Standardized Evaluation Criteria for HPC Error Forecasting: Establishing rigorous and standardized performance benchmarks is critical to determine whether forecasting models provide practical utility for real-world HPC fault avoidance and proactive scheduling.

### Rejected Candidates
- [open_question] Standardized Evaluation Criteria for HPC Error Forecasting (`hpc-error-forecasting-evaluation-criteria`) - low_impact: The paper evaluates existing time series methods on HPC hardware error logs without introducing a novel core architecture or architectural concept.

## Links

- [Abstract](https://arxiv.org/abs/2608.01648)
- [PDF](https://arxiv.org/pdf/2608.01648)

