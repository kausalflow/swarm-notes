---
# CSL-compatible fields
title: "Local Redundancy: An Information-Theoretic Measure of Plasticity from Synthetic Memorization"
author:
  - literal: "Jiaxuan Cheng"
issued:
  date-parts:
    - [2026, 7, 15]
url: "https://arxiv.org/abs/2607.13432"

# Custom fields
paper_id: "2607.13432"
paper_source: "openalex"
domain: "nlp"
tags:
  - "continual-learning"
  - "transfer-learning"
  - "information-theory"
  - "model-selection"
  - "pre-training"
  - "fine-tuning"
  - "time-series"
  - "image-classification"
architectures:
  []
datasets:
  []
concept_slugs:
  - "local-redundancy"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-18T06:52:36Z"
created_at: "2026-07-18T06:52:36Z"
---

# Local Redundancy: An Information-Theoretic Measure of Plasticity from Synthetic Memorization

**Authors**: Jiaxuan Cheng
**Date**: 2026-07-15
**Paper ID**: [openalex:2607.13432](https://arxiv.org/abs/2607.13432)

## Summary

The paper introduces local redundancy, a novel information-theoretic metric designed to quantify neural network plasticity, which is the capacity to adapt to new tasks. By leveraging universal compression theory, the author defines this measure based on the redundancy of local parameter neighborhoods. Since exact computation is intractable, the paper proposes using the expected squared gradient norm on synthetic memorization tasks as an efficient proxy. Empirical results confirm that this metric is a superior predictor of transfer and continual learning performance compared to traditional heuristics like weight norm or rank.

## Key Contributions

- Introduces local redundancy, a theoretically grounded plasticity measure derived from universal compression theory.
- Proves that the expected squared gradient norm on synthetic memorization tasks offers an efficiently computable lower bound for local redundancy.
- Demonstrates that local redundancy outperforms existing metrics (effective rank, dead neuron fraction) in predicting downstream performance on continual image classification and time series transfer tasks.
- Enables improved pretraining checkpoint selection in scenarios where standard validation loss plateaus.

## Open Questions & Future Work

- [[causal-mechanism-of-neural-plasticity]]

## Key Concepts

- [[local-redundancy]]: An information-theoretic measure of neural network plasticity defined as the worst-case redundancy of a local model family along gradient directions.

## Archivist Review

I approved 'Local Redundancy' as it provides a theoretically grounded, domain-agnostic metric for an important problem (plasticity) that is likely to recur. I rephrased the open question to focus on the broader causal mechanism of plasticity rather than focusing specifically on the paper's proposed measure, which makes it more robust for future research tracking. The scalability question was rejected as routine performance evaluation.

### Approved Concepts
- Local Redundancy: It serves as a new, theoretically grounded measure of neural network plasticity that correlates better with downstream task performance than existing heuristic metrics.

### Approved Open Questions
- Causal mechanisms of plasticity: Establishing causality is necessary to move beyond descriptive heuristics in the study of neural plasticity.

## Links

- [Abstract](https://arxiv.org/abs/2607.13432)
- [PDF](https://arxiv.org/pdf/2607.13432)

