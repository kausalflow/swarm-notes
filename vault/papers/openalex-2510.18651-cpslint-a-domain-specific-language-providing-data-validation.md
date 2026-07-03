---
# CSL-compatible fields
title: "CPSLint: A Domain-Specific Language Providing Data Validation and Sanitisation for Industrial Cyber-Physical Systems"
author:
  - literal: "Uraz Odyurt"
  - literal: "Ömer Sayilir"
  - literal: "Mariëlle Stoelinga"
  - literal: "Vadim Zaytsev"
issued:
  date-parts:
    - [2026, 6, 30]
url: "https://arxiv.org/abs/2510.18651"

# Custom fields
paper_id: "2510.18651"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "anomaly-detection"
  - "information-extraction"
architectures:
  []
datasets:
  []
concept_slugs:
  - "cpslint"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-03T07:55:34Z"
created_at: "2026-07-03T07:55:34Z"
---

# CPSLint: A Domain-Specific Language Providing Data Validation and Sanitisation for Industrial Cyber-Physical Systems

**Authors**: Uraz Odyurt, Ömer Sayilir, Mariëlle Stoelinga, Vadim Zaytsev
**Date**: 2026-06-30
**Paper ID**: [openalex:2510.18651](https://arxiv.org/abs/2510.18651)

## Summary

Industrial cyber-physical systems often yield noisy, semi-structured time-series data that complicate downstream machine learning tasks like fault detection. This paper presents CPSLint, a domain-specific language (DSL) that allows domain experts to specify and automate data validation and sanitisation procedures. The framework efficiently identifies and corrects common corruption patterns, ensuring data consistency while minimizing manual preprocessing overhead. Evaluation results confirm the practicality and efficiency of CPSLint in handling industrial sensor datasets with manageable computational costs.

## Key Contributions

- Introduces CPSLint, a DSL designed to automate data validation and sanitisation workflows for industrial time-series data.
- Demonstrates that CPSLint significantly reduces the manual effort required for data preparation by non-programming domain experts.
- Provides performance analysis of the sanitisation process, tracking memory and CPU usage across representative industrial datasets.

## Open Questions & Future Work

- [[detecting-unreliable-temporal-corruption]]

## Key Concepts

- [[cpslint]]: A domain-specific language for automated data validation and sanitisation in industrial cyber-physical systems.

## Archivist Review

I have approved the CPSLint DSL as it introduces a reusable paradigm for automating the pre-processing of industrial time-series data, which is a frequent bottleneck. I also approved the open question regarding the disambiguation of sensor-induced data corruption from genuine physical anomalies, as this remains a core challenge in reliable machine learning for time-series. All other candidates were rejected as they were either too narrow, local to the specific implementation, or did not meet the archival standard of novelty and reusability.

### Approved Concepts
- CPSLint: It provides a reusable DSL-based approach to the widespread problem of automating data sanitisation for industrial time-series, which is a major bottleneck for reliable fault detection.

### Approved Open Questions
- Handling Unreliable Temporal Data Corruptions: Distinguishing between noise and genuine physical anomalies is a fundamental prerequisite for robust temporal forecasting and fault detection.

## Links

- [Abstract](https://arxiv.org/abs/2510.18651)
- [PDF](https://arxiv.org/pdf/2510.18651)

