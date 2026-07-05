---
# CSL-compatible fields
title: "Zeus: Towards Tuning-Free Foundation Model for Time Series Analysis"
author:
  - literal: "Yisong Fu"
  - literal: "Zezhi Shao"
  - literal: "C Shijia Yu"
  - literal: "Yujie Li"
  - literal: "Yongjun Xu"
  - literal: "Xueqi Cheng"
  - literal: "Fang Wang"
issued:
  date-parts:
    - [2026, 7, 2]
url: "https://arxiv.org/abs/2607.01918"

# Custom fields
paper_id: "2607.01918"
paper_source: "openalex"
domain: "time-series"
tags:
  - "llm"
  - "language-model"
  - "transformer"
  - "attention-mechanism"
  - "long-context"
  - "zero-shot-learning"
  - "time-series"
  - "forecasting"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "multi-objective-temporal-masking-motm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-05T07:51:57Z"
created_at: "2026-07-05T07:51:57Z"
---

# Zeus: Towards Tuning-Free Foundation Model for Time Series Analysis

**Authors**: Yisong Fu, Zezhi Shao, C Shijia Yu, Yujie Li, Yongjun Xu, Xueqi Cheng, Fang Wang
**Date**: 2026-07-02
**Paper ID**: [openalex:2607.01918](https://arxiv.org/abs/2607.01918)

## Summary

Zeus is a unified time series foundation model designed for tuning-free performance across a wide range of analysis tasks. The model utilizes a U-shaped multi-scale Transformer architecture to effectively bridge the gap between point-level granularity and long-sequence scalability. Furthermore, it employs a Multi-Objective Temporal Masking strategy to accommodate varying task-specific inductive biases without requiring fine-tuning. Evaluation across five representative tasks demonstrates its effectiveness as a general-purpose time series foundation model.

## Key Contributions

- Introduces Zeus, a unified tuning-free time series foundation model that achieves high performance across diverse analysis tasks without task-specific fine-tuning.
- Proposes a U-shaped multi-scale Transformer architecture with point-wise tokenization to balance fine-grained fidelity and long-sequence scalability.
- Develops Multi-Objective Temporal Masking (MOTM) to reconcile heterogeneous tasks such as extrapolation, interpolation, and global abstraction within a single framework.

## Open Questions & Future Work

- [[point-level-fidelity-vs-scalability]]
- [[divergent-inductive-biases-tsfms]]

## Key Concepts

- [[multi-objective-temporal-masking-motm]]: A unified training strategy enabling a single foundation model to handle heterogeneous time series tasks through varied temporal masking patterns.

## Archivist Review

The paper introduces a unified approach to time series foundation models. I approved the MOTM concept as a distinct, reusable methodology for multi-task training, and the two open questions as they capture fundamental, well-defined bottlenecks in architectural design and task generalization that are central to the field's current progression.

### Approved Concepts
- Multi-Objective Temporal Masking (MOTM): Provides a unified mechanism to handle diverse time series tasks (extrapolation, interpolation, abstraction) within a single model without fine-tuning.

### Approved Open Questions
- Granularity vs. Scalability Dilemma: This is a fundamental architectural bottleneck that limits the universal applicability of time series foundation models to reconstruction-oriented tasks while maintaining long-range modeling capabilities.
- Reconciling Divergent Inductive Biases: This challenge addresses the core of what makes a model a 'foundation' model; without solving the reconciliation of these biases, models remain specialized or require costly adaptation.

## Links

- [Abstract](https://arxiv.org/abs/2607.01918)
- [PDF](https://arxiv.org/pdf/2607.01918)

