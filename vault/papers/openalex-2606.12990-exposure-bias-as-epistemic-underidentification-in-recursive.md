---
# CSL-compatible fields
title: "Exposure Bias as Epistemic Underidentification in Recursive Forecasting"
author:
  - literal: "Riku Green"
  - literal: "Zahraa S. Abdallah"
  - literal: "Telmo M Silva Filho"
issued:
  date-parts:
    - [2026, 6, 11]
url: "https://arxiv.org/abs/2606.12990"

# Custom fields
paper_id: "2606.12990"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "autoregressive"
architectures:
  []
datasets:
  []
concept_slugs:
  - "epistemic-underidentification-in-recursive-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-14T08:38:07Z"
created_at: "2026-06-14T08:38:07Z"
---

# Exposure Bias as Epistemic Underidentification in Recursive Forecasting

**Authors**: Riku Green, Zahraa S. Abdallah, Telmo M Silva Filho
**Date**: 2026-06-11
**Paper ID**: [openalex:2606.12990](https://arxiv.org/abs/2606.12990)

## Summary

This paper challenges the traditional view of exposure bias as a simple distribution shift in recursive multi-step forecasting. The authors prove that, under partial observability or state truncation, the problem is fundamentally one of epistemic underidentification where the model lacks ground-truth targets for its own self-generated states. By formalizing induced states and provenance variables, they provide a novel error decomposition and show that improvements in closed-loop performance stem from managing the states visited during rollout. These findings reframe recursive forecasting errors as a challenge of reasoning under self-induced epistemic uncertainty.

## Key Contributions

- Formally proves that recursive multi-step forecasting suffers from epistemic underidentification due to state truncation or partial observability.
- Derives a decomposition of induced-state error into teacher-forcing/rollout mismatch, representation-class approximation, and provenance information gaps.
- Demonstrates that performance gains in closed-loop training result from both local adaptation and shifting the distribution of induced states visited during rollout.

## Open Questions & Future Work

- [[richer-provenance-representations-for-recursive-forecasting]]

## Key Concepts

- [[epistemic-underidentification-in-recursive-forecasting]]: The phenomenon where recursive autoregressive forecasting fails because self-generated states lack ground-truth labels and are not uniquely determined by observable history.

## Archivist Review

The approved concept provides a fundamental theoretical reframing of the well-known exposure bias problem as an epistemic issue, which is highly central to time-series forecasting. The approved open question addresses the practical limitation of current methods in handling this underidentification, defining a clear research trajectory for future work in state representation. No datasets were approved as none met the strict criteria for centrality and reusability.

### Approved Concepts
- Epistemic Underidentification in Recursive Forecasting: Reinterprets the long-standing 'exposure bias' problem in autoregressive forecasting as a structural epistemic failure rather than simple distribution shift.

### Approved Open Questions
- Richer Provenance Representations: This question identifies a critical bottleneck in leveraging provenance for improving recursive forecasting, moving beyond the current limitations of simplistic binary flags toward more robust, information-rich state representations.

## Links

- [Abstract](https://arxiv.org/abs/2606.12990)
- [PDF](https://arxiv.org/pdf/2606.12990)

