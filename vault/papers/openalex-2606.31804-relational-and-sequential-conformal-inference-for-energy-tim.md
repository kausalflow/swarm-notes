---
# CSL-compatible fields
title: "Relational and Sequential Conformal Inference for Energy Time Series over Graphs via Foundation Models"
author:
  - literal: "Keivan Faghih Niresi"
  - literal: "Alice Cicirello"
  - literal: "Olga Fink"
issued:
  date-parts:
    - [2026, 6, 30]
url: "https://arxiv.org/abs/2606.31804"

# Custom fields
paper_id: "2606.31804"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "graph-neural-network"
  - "conformal-prediction"
  - "in-context-learning"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "stoic-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-03T07:54:32Z"
created_at: "2026-07-03T07:54:32Z"
---

# Relational and Sequential Conformal Inference for Energy Time Series over Graphs via Foundation Models

**Authors**: Keivan Faghih Niresi, Alice Cicirello, Olga Fink
**Date**: 2026-06-30
**Paper ID**: [openalex:2606.31804](https://arxiv.org/abs/2606.31804)

## Summary

This paper presents STOIC, a novel framework for robust uncertainty quantification in energy grid time series that combines spatial-temporal graph neural networks (STGNNs) with tabular foundation models. While STGNNs excel at point forecasting, STOIC addresses the need for reliable uncertainty intervals by reformulating graph residuals into tabular representations for in-context learning. This approach enables zero-shot calibration that effectively accounts for both sequential and relational dependencies without requiring task-specific retraining. Experimental results across various electricity and district heating benchmarks demonstrate that STOIC provides more reliable coverage and sharper prediction intervals than existing conformal prediction baselines.

## Key Contributions

- Introduced STOIC, a framework that integrates STGNN point forecasting with tabular foundation models for robust zero-shot uncertainty calibration.
- Demonstrated that reformulating spatial-temporal residuals into tabular structures allows foundation models to capture complex cross-node and sequential dependencies for interval estimation.
- Achieved consistent performance improvements in uncertainty quantification across five energy system benchmarks, outperforming standard conformal prediction techniques.

## Open Questions & Future Work

- [[tabular-fm-consistency-guarantees-conformal-inference]]
- [[multi-horizon-spatial-temporal-uncertainty]]

## Key Concepts

- [[stoic-framework]]: A framework for calibrating uncertainty intervals in graph-structured time series by reformulating spatial-temporal residuals into tabular representations for in-context learning with foundation models.

## Archivist Review

I approved the STOIC framework as a novel and reusable methodology for uncertainty calibration in graph time series. I also approved two research questions that address key gaps in using foundation models for safety-critical conformal inference and the challenges of extending these methods to multi-horizon sequences. Standard datasets were rejected as they are common benchmarks.

### Approved Concepts
- STOIC framework: It introduces a novel methodology for decoupling point prediction from uncertainty calibration in graph time series by leveraging tabular foundation models via residual prompting, offering a model-agnostic improvement over traditional conformal prediction.

### Approved Open Questions
- Theoretical consistency of tabular FMs: Rigorous consistency guarantees are necessary for the widespread adoption of foundation models in safety-critical infrastructures where probabilistic coverage must be statistically sound.
- Multi-horizon uncertainty in graphs: Multi-horizon uncertainty quantification is a critical bottleneck for operational decisions in renewable-heavy energy grids, such as storage management and long-term generation scheduling.

### Rejected Candidates
- [dataset] ETTh1 (`ETTh1`) - not_novel: Routine benchmark dataset common in time-series forecasting.
- [dataset] Traffic (`Traffic`) - not_novel: Routine benchmark dataset common in time-series forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2606.31804)
- [PDF](https://arxiv.org/pdf/2606.31804)

