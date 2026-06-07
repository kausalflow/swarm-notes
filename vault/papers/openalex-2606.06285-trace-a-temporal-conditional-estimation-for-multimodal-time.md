---
# CSL-compatible fields
title: "TRACE: A Temporal Conditional Estimation for Multimodal Time Series Foundation Models"
author:
  - literal: "Ziwen Kan"
  - literal: "Yishuo Chen"
  - literal: "Kecheng Li"
  - literal: "Andrew Wen"
  - literal: "Xiaomeng Wang"
  - literal: "Liwei Wang"
  - literal: "Jihao Duan"
  - literal: "Song Wang"
  - literal: "Hongfang Liu"
  - literal: "Tianlong Chen"
issued:
  date-parts:
    - [2026, 6, 4]
url: "https://arxiv.org/abs/2606.06285"

# Custom fields
paper_id: "2606.06285"
paper_source: "openalex"
domain: "nlp"
tags:
  - "multimodal"
  - "time-series"
  - "language-model"
  - "embedding"
  - "benchmark"
architectures:
  []
datasets:
  - "mimic-iv"
  - "cmu-mosei"
concept_slugs:
  - "temporal-conditional-estimation-trace"
dataset_slugs:
  - "mimic-iv"
  - "cmu-mosei"
skill: "TimeSeriesSkill"
processed_at: "2026-06-07T08:18:45Z"
created_at: "2026-06-07T08:18:45Z"
---

# TRACE: A Temporal Conditional Estimation for Multimodal Time Series Foundation Models

**Authors**: Ziwen Kan, Yishuo Chen, Kecheng Li, Andrew Wen, Xiaomeng Wang, Liwei Wang, Jihao Duan, Song Wang, Hongfang Liu, Tianlong Chen
**Date**: 2026-06-04
**Paper ID**: [openalex:2606.06285](https://arxiv.org/abs/2606.06285)

## Summary

TRACE is a conditional estimation paradigm designed to address challenges of temporal misalignment and partial modality missingness in multimodal time series foundation models. By systematically inferring incomplete target modalities from available auxiliary inputs, the model handles irregular sampling without relying on naive imputation strategies. Empirical evaluations on clinical and affective computing benchmarks demonstrate that TRACE yields more robust cross-modal representations and superior performance across diverse downstream prediction tasks.

## Key Contributions

- Introduced TRACE, a conditional estimation framework to address temporal misalignment and modality missingness in time series foundation models.
- Outperformed prior multimodal fusion methods on downstream tasks under severe missing-modality and irregular sampling conditions.
- Demonstrated improved robustness and cross-modal representation quality on healthcare (MIMIC-IV) and affective computing (CMU-MOSI/MOSEI) benchmarks.

## Open Questions & Future Work

- [[generative-modeling-absent-modalities]]

## Key Concepts

- [[temporal-conditional-estimation-trace]]: A paradigm for conditionally inferring incomplete target modalities from auxiliary modalities in multimodal time series foundation models.

## Archivist Review

I approved the TRACE concept as it introduces a reusable conditional estimation paradigm for multimodal time series. I limited the datasets to MIMIC-IV and CMU-MOSEI as they are widely recognized benchmarks. The open question regarding generative modeling of missing modalities captures a significant research bottleneck, while I rejected the foundation model specialization gap question as it reflects a performance-based comparison rather than a core structural challenge.

### Approved Concepts
- Temporal Conditional Estimation (TRACE): It provides a systematic approach for cross-modal inference that explicitly addresses irregular sampling and missing modalities in time series FMs.

### Approved Open Questions
- Generative Modeling of Absent Modalities: Addressing complete modality absence is a critical challenge for real-world multimodal time series foundation models, as it represents a more complex scenario than partial missingness.

### Rejected Candidates
- [open_question] Bridging Foundation Models and Specialization (`foundation-model-domain-specialization-gap`) - low_impact: This question is framed as a performance comparison with a specific architecture rather than a fundamental scientific bottleneck.
- [dataset] CMU-MOSI (`cmu-mosi`) - duplicate_existing: Dataset redundant with CMU-MOSEI in the context of affective computing benchmarks.

## Datasets

- [[mimic-iv]]
- [[cmu-mosei]]

## Links

- [Abstract](https://arxiv.org/abs/2606.06285)
- [PDF](https://arxiv.org/pdf/2606.06285)

