---
# CSL-compatible fields
title: "Time Series Causal Discovery via Context-Conditioned and Causality-Augmented Pretraining"
author:
  - literal: "Biao Ouyang"
  - literal: "Tengxue Zhang"
  - literal: "Zhihao Zhuang"
  - literal: "Yang Shu"
  - literal: "Chenjuan Guo"
  - literal: "Bin Yang"
issued:
  date-parts:
    - [2026, 5, 26]
url: "https://arxiv.org/abs/2605.26759"

# Custom fields
paper_id: "2605.26759"
paper_source: "openalex"
domain: "time-series"
tags:
  - "causal-discovery"
  - "pre-training"
  - "time-series"
  - "attention-mechanism"
  - "generalization"
architectures:
  []
datasets:
  []
concept_slugs:
  - "ptcd-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-29T08:37:47Z"
created_at: "2026-05-29T08:37:47Z"
---

# Time Series Causal Discovery via Context-Conditioned and Causality-Augmented Pretraining

**Authors**: Biao Ouyang, Tengxue Zhang, Zhihao Zhuang, Yang Shu, Chenjuan Guo, Bin Yang
**Date**: 2026-05-26
**Paper ID**: [openalex:2605.26759](https://arxiv.org/abs/2605.26759)

## Summary

The paper proposes PTCD, a pretraining framework designed to improve the cross-task generalization of time series causal discovery. PTCD leverages a dual-scale iterative attention mechanism and context-level routing to model heterogeneous causal dependencies across diverse distributions. By utilizing synthetic pretraining with intervention-based learning and causal mixup, the framework demonstrates robust causal discovery and root cause identification capabilities on out-of-distribution real-world benchmarks.

## Key Contributions

- Introduces PTCD, a pretraining framework for time series causal discovery that enhances cross-task generalization via context-conditioned modeling and causal augmentation.
- Implements a dual-scale iterative attention mechanism to capture both window-level and context-level causal dependencies.
- Demonstrates superior performance in causal discovery and root cause identification on out-of-distribution (OOD) real-world datasets compared to existing optimization-based methods.

## Open Questions & Future Work

- [[non-additive-causal-mechanisms]]

## Key Concepts

- [[ptcd-framework]]: A pretraining framework for time series causal discovery that improves cross-task generalization via context-conditioned modeling and causal augmentation.

## Archivist Review

I approved the PTCD framework as a significant shift towards pretraining-based causal discovery in time series, which is a reusable and distinct methodological contribution. The open question on non-additive causal mechanisms was approved because it addresses a fundamental limitation in structural causal models for time series that persists across the field. All other candidate suggestions were rejected as they were either too narrow or lacked the necessary novelty for a long-term knowledge vault.

### Approved Concepts
- PTCD Framework: The paper introduces PTCD as a foundational pretraining approach to enable zero-shot or better-generalized causal discovery across heterogeneous time series datasets, overcoming the limitations of dataset-specific optimization.

### Approved Open Questions
- Non-additive causal mechanisms: The current reliance on ANM limits the applicability of time-series causal discovery to systems where non-additive noise is prevalent. Developing non-additive models is a key bottleneck for advancing robust and generalizable causal discovery in complex, noisy real-world environments.

## Links

- [Abstract](https://arxiv.org/abs/2605.26759)
- [PDF](https://arxiv.org/pdf/2605.26759)

