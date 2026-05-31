---
# CSL-compatible fields
title: "Tiny but Trusted: Efficient Vision-Language Reasoning for Time-Series Anomaly Detection"
author:
  - literal: "Xiaona Zhou"
  - literal: "Muntasir Wahed"
  - literal: "Tianjiao Yu"
  - literal: "Constantin Brif"
  - literal: "Ismini Lourentzou"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.30344"

# Custom fields
paper_id: "2605.30344"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "multimodal"
  - "vision-language-model"
  - "anomaly-detection"
  - "time-series"
  - "parameter-efficient-fine-tuning"
  - "benchmark"
  - "reasoning"
architectures:
  []
datasets:
  - "visanombench"
concept_slugs:
  []
dataset_slugs:
  - "visanombench"
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:09:11Z"
created_at: "2026-05-31T08:09:11Z"
---

# Tiny but Trusted: Efficient Vision-Language Reasoning for Time-Series Anomaly Detection

**Authors**: Xiaona Zhou, Muntasir Wahed, Tianjiao Yu, Constantin Brif, Ismini Lourentzou
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.30344](https://arxiv.org/abs/2605.30344)

## Summary

The authors address the limitation of current vision-language models (VLMs) in performing interpretable anomaly detection on time-series data due to a lack of descriptive ground-truth annotations. They introduce VisAnomBench, a curated benchmark that provides high-quality natural-language explanations for anomalies, and leverage it to train VisAnomReasoner, a parameter-efficient VLM. The model demonstrates superior anomaly localization accuracy and strong generalization capabilities compared to existing baselines across multiple benchmarks.

## Key Contributions

- Introduces VisAnomBench, a curated benchmark for time-series anomaly detection that provides natural-language rationales for anomalous segments.
- Develops VisAnomReasoner, a parameter-efficient VLM that achieves state-of-the-art anomaly localization performance.
- Demonstrates significant performance gains, improving precision and F1 by over 20 percentage points on VisAnomBench, with strong cross-benchmark generalization on TSB-AD-U.

## Archivist Review

The paper introduces a dataset that specifically addresses the gap in natural language rationales for time-series anomaly detection, making it a valuable addition to the vault. VisAnomReasoner was rejected because it is a specific model implementation rather than a generalized architectural concept, in accordance with the requirement to be selective and avoid paper-local model names.

### Rejected Candidates
- [concept] VisAnomReasoner (`visanomreasoner`) - paper_local: VisAnomReasoner is a specific model instance rather than a foundational mechanism or architecture that would recur across future research.

## Datasets

- [[visanombench]]

## Links

- [Abstract](https://arxiv.org/abs/2605.30344)
- [PDF](https://arxiv.org/pdf/2605.30344)

