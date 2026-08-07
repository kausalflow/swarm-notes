---
# CSL-compatible fields
title: "SocietyBench: Forecasting Counterfactual Social-World Evolution"
author:
  - literal: "Zhenran Wang"
  - literal: "Zhonghan Bian"
  - literal: "Jinsong Li"
  - literal: "Zhangyang Qi"
issued:
  date-parts:
    - [2026, 8, 4]
url: "https://arxiv.org/abs/2608.04009"

# Custom fields
paper_id: "2608.04009"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "benchmark"
  - "evaluation"
  - "forecasting"
  - "agent"
  - "multimodal"
architectures:
  []
datasets:
  - "societybench"
concept_slugs:
  - "societybench"
dataset_slugs:
  - "societybench"
skill: "TimeSeriesSkill"
processed_at: "2026-08-07T06:04:18Z"
created_at: "2026-08-07T06:04:18Z"
---

# SocietyBench: Forecasting Counterfactual Social-World Evolution

**Authors**: Zhenran Wang, Zhonghan Bian, Jinsong Li, Zhangyang Qi
**Date**: 2026-08-04
**Paper ID**: [openalex:2608.04009](https://arxiv.org/abs/2608.04009)

## Summary

The authors introduce SocietyBench, a benchmark designed to evaluate large language models and agents on forecasting counterfactual social-world evolution. To prevent memorization, the benchmark transforms real-world event timelines into counterfactual counterparts by stripping named entities and shifting dates. Evaluations across six frontier LLMs and multiple agent frameworks show that models struggle with this task, scoring low on orthogonal axes of probability calibration and temporal accuracy.

## Key Contributions

- Introduces SocietyBench, an end-to-end evaluation benchmark for counterfactual social-world evolution forecasting.
- Proposes a three-phase data anonymization and date-shifting procedure to strip surface labels from pre-training memory and test true reasoning.
- Evaluates six frontier LLMs, three agent frameworks, and two heuristics on 125 prediction points, revealing that the strongest model achieves only 75.0 out of 100.
- Decomposes evaluation into two orthogonal 100-point axes: probability calibration and temporal accuracy.

## Limitations

Evaluated on a limited set of five heterogeneous events and 125 prediction points across Chinese and English editions.

## Open Questions & Future Work

- [[stronger-anonymization-social-forecasting]]

## Key Concepts

- [[societybench]]: An end-to-end benchmark evaluating large language models on forecasting counterfactual social-world evolution through separated factual timelines and public-opinion layers.

## Archivist Review

Approved SocietyBench as a central concept and dataset, along with its core open question on counterfactual anonymization and scaling. Kept approvals scarce and strictly aligned with vault standards.

### Approved Concepts
- SocietyBench: It provides a novel counterfactual social-world evolution forecasting benchmark evaluating probability calibration and temporal accuracy.

### Approved Open Questions
- Stronger Anonymization and Broader Events: Enhances the robustness of counterfactual social-world evaluation, ensuring benchmarks remain resistant to memorization as foundation models scale.

## Datasets

- [[societybench]]

## Links

- [Abstract](https://arxiv.org/abs/2608.04009)
- [PDF](https://arxiv.org/pdf/2608.04009)

