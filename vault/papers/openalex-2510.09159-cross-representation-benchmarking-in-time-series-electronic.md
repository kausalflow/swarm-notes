---
# CSL-compatible fields
title: "Cross-Representation Benchmarking in Time-Series Electronic Health Records for Clinical Outcome Prediction"
author:
  - literal: "Tianyi Chen"
  - literal: "Min Zhu"
  - literal: "Zhiyao Luo"
  - literal: "Tingting Zhu"
issued:
  date-parts:
    - [2026, 4, 21]
url: "https://arxiv.org/abs/2510.09159"

# Custom fields
paper_id: "2510.09159"
paper_source: "openalex"
domain: "medicine"
tags:
  - "llm"
  - "transformer"
  - "lstm"
  - "language-model"
  - "time-series"
  - "few-shot-learning"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  - "mimic-iv"
  - "ehrshot"
concept_slugs:
  - "cross-representation-ehr-benchmarking"
dataset_slugs:
  - "mimic-iv"
  - "ehrshot"
skill: "TimeSeriesSkill"
processed_at: "2026-04-24T06:59:34Z"
created_at: "2026-04-24T06:59:34Z"
---

# Cross-Representation Benchmarking in Time-Series Electronic Health Records for Clinical Outcome Prediction

**Authors**: Tianyi Chen, Min Zhu, Zhiyao Luo, Tingting Zhu
**Date**: 2026-04-21
**Paper ID**: [openalex:2510.09159](https://arxiv.org/abs/2510.09159)

## Summary

This paper introduces a comprehensive benchmark for evaluating electronic health record (EHR) representation methods across diverse clinical tasks and data modalities. By standardizing evaluation for multivariate time-series, event streams, and textual formats, the authors compare a wide range of architectures including Transformers and LLMs. Their findings suggest that event-based representations are generally superior and highlight the critical role of clinical context-specific feature selection in achieving optimal predictive performance.

## Key Contributions

- Presents the first systematic, unified benchmark standardizing EHR data curation and evaluation across time-series, event stream, and textual representation paradigms.
- Reveals that event stream models consistently outperform others, with CLMBR demonstrating superior sample efficiency in few-shot settings.
- Demonstrates that optimal feature selection strategies depend on the clinical setting, with ICU tasks favoring pruned features and longitudinal tasks requiring retention of sparse information.

## Open Questions & Future Work

- [[broadening-ehr-representation-benchmarks]]

## Key Concepts

- [[cross-representation-ehr-benchmarking]]: A unified, reproducible evaluation pipeline that standardizes data curation and model assessment across clinical representation paradigms like multivariate time-series and event streams.

## Archivist Review

I approved the benchmark framework concept because it addresses a fundamental methodological challenge in clinical ML—the lack of standardized evaluation across competing data representation strategies. The EHRSHOT and MIMIC-IV datasets were approved as they are the primary benchmarks used in this work. I also approved the open question regarding the expansion of such benchmarks, as it correctly identifies the need for broader clinical domain coverage and output calibration as the next step for this field.

### Approved Concepts
- Cross-Representation EHR Benchmarking: Establishes a standardized framework for evaluating diverse patient data representations, which is a key bottleneck in clinical ML research.

### Approved Open Questions
- Expanding EHR representation benchmarks: Evaluating clinical models across a wider variety of settings and tasks is critical for determining the true general-purpose utility of different EHR representation methods and for identifying environment-specific performance bottlenecks.

## Datasets

- [[mimic-iv]]
- [[ehrshot]]

## Links

- [Abstract](https://arxiv.org/abs/2510.09159)
- [PDF](https://arxiv.org/pdf/2510.09159)

