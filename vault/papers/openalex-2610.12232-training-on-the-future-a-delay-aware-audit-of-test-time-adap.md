---
# CSL-compatible fields
title: "Training on the Future: A Delay-Aware Audit of Test-Time Adaptation for Time-Series Forecasting"
author:
  - literal: "Mohamed Readh FENTAZI"
  - literal: "Mazene Ameur"
  - literal: "Adlen Ksentini"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.12232"

# Custom fields
paper_id: "2610.12232"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-10T10:52:09Z"
created_at: "2026-10-10T10:52:09Z"
---

# Training on the Future: A Delay-Aware Audit of Test-Time Adaptation for Time-Series Forecasting

**Authors**: Mohamed Readh FENTAZI, Mazene Ameur, Adlen Ksentini
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.12232](https://arxiv.org/abs/2610.12232)

## Summary

This paper audits test-time adaptation (TTA) methods for time-series forecasting under realistic causal label delays where ground-truth labels arrive at step s+d with d >= H. By building a leakage-free harness and evaluating four recent TTA methods alongside closed-form baselines across five benchmarks, the authors reveal that leaky next-step updates severely inflate reported gains, and that simple closed-form correctors frequently outperform costly gradient-based adapters.

## Key Contributions

- Demonstrated that leaky next-step updates in test-time adaptation for time-series forecasting inflate apparent gains by up to 110%.
- Built a leakage-free evaluation harness enforcing causal delayed labels (delay d >= H) for TTA methods across ETTm1, ETTh2, Weather, Electricity, and Traffic benchmarks.
- Showed that closed-form references such as RLS filter banks and ELF-style linear correctors often outperform or match expensive published TTA adapters at a fraction of the computational cost.

## Limitations

Longer label delays make every adapter significantly harmful on drift-heavy datasets like ETTh2.

## Open Questions & Future Work

- [[tata-time-series-delayed-feedback]]

## Archivist Review

The paper provides a rigorous audit of test-time adaptation under realistic label delays, highlighting how leaky evaluations inflate reported gains. We approved the open question on delay-aware test-time adaptation as it exposes critical evaluation vulnerabilities in streaming forecasting, but rejected all concept candidates because they represent paper-specific evaluation harnesses and standard closed-form baselines rather than novel standalone architectures.

### Approved Open Questions
- Delay-Aware Test-Time Adaptation: Important for bridging classical adaptive signal processing with modern deep learning foundations for reliable streaming predictions under delayed feedback.

### Rejected Candidates
- [open_question] Delay-Aware Test-Time Adaptation (`tata-time-series-delayed-feedback`) - other: The open question was retained, but no concepts met the strict novelty and long-term standalone reusability criteria.

## Links

- [Abstract](https://arxiv.org/abs/2610.12232)
- [PDF](https://arxiv.org/pdf/2610.12232)

