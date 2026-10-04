---
# CSL-compatible fields
title: "Detect, Explain, Interpret: An End-to-End Benchmark for Time Series Anomaly Detection, Explainability and Interpretability"
author:
  - literal: "Roberto Stanzione"
  - literal: "Jules Barbe"
  - literal: "Magali Parrino"
  - literal: "Jérémie Fourmann"
  - literal: "Paul Boniol"
issued:
  date-parts:
    - [2026, 10, 1]
url: "https://arxiv.org/abs/2610.01168"

# Custom fields
paper_id: "2610.01168"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "benchmark"
  - "dataset"
  - "evaluation"
  - "interpretability"
  - "explainability"
  - "llm"
  - "multivariate"
architectures:
  []
datasets:
  - "shad"
concept_slugs:
  []
dataset_slugs:
  - "shad"
skill: "TimeSeriesSkill"
processed_at: "2026-10-04T10:48:41Z"
created_at: "2026-10-04T10:48:41Z"
---

# Detect, Explain, Interpret: An End-to-End Benchmark for Time Series Anomaly Detection, Explainability and Interpretability

**Authors**: Roberto Stanzione, Jules Barbe, Magali Parrino, Jérémie Fourmann, Paul Boniol
**Date**: 2026-10-01
**Paper ID**: [openalex:2610.01168](https://arxiv.org/abs/2610.01168)

## Summary

This paper introduces SHAD, a comprehensive and fully annotated benchmark of high-dimensional multivariate time series collected from real-world distributed cloud storage systems to address the lack of semantic annotations and explainability tools in existing time-series anomaly detection evaluations. The authors benchmark existing detection methods, spatial explainability attributions, and frozen large language models for anomaly interpretation. Results provide a robust foundation for multi-stage time series anomaly detection pipelines covering detection, explainability, and interpretability.

## Key Contributions

- Introduces SHAD, a fully annotated benchmark of 215 multivariate, high-dimensional time series from distributed cloud storage systems with rich contextual semantic annotations.
- Evaluates a wide range of baseline methods across all stages of a time series anomaly detection pipeline: detection, spatial explainability, and interpretability.
- Investigates the effectiveness of frozen Large Language Model baselines in localizing and interpreting anomalies using the proposed semantic annotations.

## Archivist Review

Approved the SHAD dataset as a valuable high-dimensional time series anomaly detection and interpretability benchmark, while rejecting the redundant concept candidate and the boilerplate open question.

### Rejected Candidates
- [concept] SHAD Benchmark (`shad-benchmark`) - duplicate_existing: The SHAD benchmark is already approved as a dataset note, and treating it as a standalone concept would be redundant.
- [open_question] Cross-Domain and Mixed-Failure Benchmarking (`cross-domain-and-mixed-failure-tsad-benchmarking`) - low_impact: This open question requests standard domain extensions and broader multi-platform evaluations, which is standard boilerplate future work.

## Datasets

- [[shad]]

## Links

- [Abstract](https://arxiv.org/abs/2610.01168)
- [PDF](https://arxiv.org/pdf/2610.01168)

