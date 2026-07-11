---
# CSL-compatible fields
title: "Rethinking Multimodal Time-Series Forecasting Evaluation"
author:
  - literal: "Haoxin Liu"
  - literal: "Yichen Zhou"
  - literal: "Rajat Sen"
  - literal: "B. Aditya Prakash"
  - literal: "Abhimanyu Das"
issued:
  date-parts:
    - [2026, 7, 8]
url: "https://arxiv.org/abs/2607.06973"

# Custom fields
paper_id: "2607.06973"
paper_source: "openalex"
domain: "time-series"
tags:
  - "multimodal"
  - "benchmark"
  - "time-series"
  - "forecasting"
  - "dataset"
architectures:
  []
datasets:
  - "timesx"
concept_slugs:
  - "timesx"
dataset_slugs:
  - "timesx"
skill: "TimeSeriesSkill"
processed_at: "2026-07-11T07:04:44Z"
created_at: "2026-07-11T07:04:44Z"
---

# Rethinking Multimodal Time-Series Forecasting Evaluation

**Authors**: Haoxin Liu, Yichen Zhou, Rajat Sen, B. Aditya Prakash, Abhimanyu Das
**Date**: 2026-07-08
**Paper ID**: [openalex:2607.06973](https://arxiv.org/abs/2607.06973)

## Summary

This paper introduces TimesX, a comprehensive multimodal time series forecasting benchmark designed to overcome the limitations of existing datasets, such as small scale and data leakage. By utilizing an automated data generation pipeline, the authors provide a diverse collection of real-world time series paired with rich textual contexts. Empirical evaluation reveals that many current zero-shot multimodal forecasting models struggle with the complexity of TimesX, whereas ensemble methods that effectively utilize accompanying text show superior performance.

## Key Contributions

- Introduced TimesX, a large-scale, context-enriched, multimodal time series forecasting benchmark featuring diverse real-world domains and rich textual information.
- Identified and addressed critical limitations in current benchmarks, specifically small scale, synthetic bias, limited context, and data leakage.
- Demonstrated that simple ensemble methods leveraging textual context often outperform complex state-of-the-art models when evaluated on the robust TimesX benchmark.

## Open Questions & Future Work

- [[multimodal-context-integration-challenges]]

## Key Concepts

- [[timesx]]: A large-scale, context-enriched, multimodal time-series forecasting benchmark designed to mitigate data leakage and evaluate real-world generalization.

## Archivist Review

I have approved the TimesX benchmark as a core evaluation resource for the field and the identified challenge of multimodal context integration. The review prioritizes these items as they represent a significant shift in how multimodal forecasting evaluation is conducted, moving away from small, leaked datasets toward more robust, context-rich testing. Other candidates were rejected to maintain the required scarcity of the knowledge vault.

### Approved Concepts
- TimesX: TimesX addresses systemic issues in current multimodal time series benchmarks, including data leakage and poor generalizability, by providing a large-scale, diverse, and robust platform for evaluation.

### Approved Open Questions
- Multimodal Context Integration Challenges: The authors demonstrate that current models often struggle to leverage text effectively on robust benchmarks, identifying the integration of multi-domain context as a primary bottleneck for achieving generalization.

### Rejected Candidates
- [concept] TimesX (`timesx-concept`) - duplicate_existing: This is a duplicate of the TimesX concept entry.

## Datasets

- [[timesx]]

## Links

- [Abstract](https://arxiv.org/abs/2607.06973)
- [PDF](https://arxiv.org/pdf/2607.06973)

