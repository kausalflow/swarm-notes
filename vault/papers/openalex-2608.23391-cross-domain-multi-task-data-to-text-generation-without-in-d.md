---
# CSL-compatible fields
title: "Cross-Domain, Multi-Task Data-to-Text Generation without In-Domain Training Data"
author:
  - literal: "Yifei Song"
  - literal: "Kun Efimov-Zhang"
  - literal: "Claire Gardent"
issued:
  date-parts:
    - [2026, 8, 24]
url: "https://arxiv.org/abs/2608.23391"

# Custom fields
paper_id: "2608.23391"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "fine-tuning"
  - "zero-shot-learning"
  - "knowledge-distillation"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  - "QUINTD-5"
concept_slugs:
  []
dataset_slugs:
  - "quintd-5"
skill: "TimeSeriesSkill"
processed_at: "2026-08-27T15:59:16Z"
created_at: "2026-08-27T15:59:16Z"
---

# Cross-Domain, Multi-Task Data-to-Text Generation without In-Domain Training Data

**Authors**: Yifei Song, Kun Efimov-Zhang, Claire Gardent
**Date**: 2026-08-24
**Paper ID**: [openalex:2608.23391](https://arxiv.org/abs/2608.23391)

## Summary

This paper investigates cross-domain data-to-text generation in settings lacking in-domain training text and references. The authors introduce data-driven knowledge distillation (DDKD) coupled with structure-preserving augmentation (via structural subsampling and perturbation). Experiments across five benchmarks and the newly introduced QUINTD-5 dataset demonstrate that smaller models trained with DDKD surpass standard fine-tuning and zero-shot LLM inference, frequently outperforming much larger fine-tuned models.

## Key Contributions

- Introduces data-driven knowledge distillation (DDKD) combined with structure-preserving augmentation for cross-domain data-to-text generation without in-domain training text.
- Constructs QUINTD-5, a fivefold extension of QUINTD-1, to evaluate cross-domain data scaling versus augmentation strategies.
- Demonstrates that 1.7B parameter models distilled via DDKD outperform larger fine-tuned models on two out of five benchmarks and match them on the rest.

## Limitations

Evaluated primarily at a constant model size of 1.7B parameters and across specific data-to-text structures.

## Archivist Review

The paper addresses cross-domain data-to-text generation in NLP rather than time series forecasting, which is the primary scope of this knowledge vault. Consequently, the proposed NLP concepts and open questions are rejected as out-of-domain, while the QUINTD-5 dataset is approved as a named benchmark dataset.

### Rejected Candidates
- [concept] Data-Driven Knowledge Distillation (`data-driven-knowledge-distillation`) - low_impact: This paper focuses primarily on natural language data-to-text generation rather than time series forecasting or core temporal/forecasting methodology.
- [open_question] Open-Source LLM-as-a-Judge Metrics (`open-source-llm-judge-metrics`) - low_impact: This open question is general to NLP evaluation and not specific to time series or the core forecasting vault scope.
- [open_question] Automated Structure-Preserving Augmentation (`automated-structure-preserving-augmentation`) - low_impact: This question pertains to general NLP structure-to-text generation rather than temporal dynamics or forecasting.

## Datasets

- [[quintd-5]]

## Links

- [Abstract](https://arxiv.org/abs/2608.23391)
- [PDF](https://arxiv.org/pdf/2608.23391)

