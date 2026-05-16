---
# CSL-compatible fields
title: "MILM: Large Language Models for Multimodal Irregular Time Series with Informative Sampling"
author:
  - literal: "Hsing-Huan Chung"
  - literal: "Shijun Li"
  - literal: "Yoav Wald"
  - literal: "Xing Han"
  - literal: "Suchi Saria"
  - literal: "Joydeep Ghosh"
issued:
  date-parts:
    - [2026, 5, 13]
url: "https://arxiv.org/abs/2605.13711"

# Custom fields
paper_id: "2605.13711"
paper_source: "openalex"
domain: "nlp,medicine"
tags:
  - "llm"
  - "multimodal"
  - "time-series"
  - "fine-tuning"
  - "language-model"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "xml-serialization-of-time-series-events"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-16T07:09:21Z"
created_at: "2026-05-16T07:09:21Z"
---

# MILM: Large Language Models for Multimodal Irregular Time Series with Informative Sampling

**Authors**: Hsing-Huan Chung, Shijun Li, Yoav Wald, Xing Han, Suchi Saria, Joydeep Ghosh
**Date**: 2026-05-13
**Paper ID**: [openalex:2605.13711](https://arxiv.org/abs/2605.13711)

## Summary

MILM is an LLM-based approach to modeling multimodal, irregularly sampled time series, such as EHRs containing both numerical measurements and clinical text. By serializing data as XML triplets, it treats time-series classification as a sequence modeling task while explicitly capturing the informative nature of sampling timestamps. Through a two-stage training strategy—first focusing on sampling patterns and then full observations—the model achieves superior performance in clinical classification tasks, particularly when handling partially missing data.

## Key Contributions

- Introduces MILM, a framework that serializes multimodal, irregular time-series (MITS) as XML-formatted triplets to leverage LLMs for heterogeneous data.
- Proposes a two-stage training strategy (MILM-2S) that pre-trains on sampling patterns before fine-tuning on full observational data, significantly improving predictive performance.
- Demonstrates that MILM-2S outperforms standard baselines and direct fine-tuning, especially in scenarios with value-pending observations and informative sampling patterns.

## Open Questions & Future Work

- [[robustness-under-sampling-distribution-shift]]

## Key Concepts

- [[xml-serialization-of-time-series-events]]: A framework for linearizing irregular, multimodal time series data into time-ordered XML-formatted triplets for direct LLM consumption.

## Archivist Review

The paper's primary contribution is the XML serialization strategy for treating irregular time-series as sequences, which is a reusable and distinct mechanism for LLM-based time series modeling. The open question on sampling distribution shift is approved as it addresses a core limitation of informative-missingness models in real-world clinical deployment, while the request to extend modalities is rejected as generic boilerplate future work.

### Approved Concepts
- XML serialization of time-series events: Provides a structured, prompt-compatible mechanism to serialize asynchronous, multimodal temporal data for LLMs, effectively bypassing tokenization limitations for irregular structures.

### Approved Open Questions
- Robustness under sampling distribution shift: Sampling shift is a fundamental bottleneck for deploying predictive healthcare models, as 'informative missingness' models are highly sensitive to the underlying data-collection mechanism.

### Rejected Candidates
- [open_question] Extending Modalities in MITS (`multimodal-extension-challenges`) - low_impact: Generic future work concerning adding more modalities is a common boilerplate limitation and lacks a specific methodological framing.

## Links

- [Abstract](https://arxiv.org/abs/2605.13711)
- [PDF](https://arxiv.org/pdf/2605.13711)

