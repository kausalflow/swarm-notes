---
# CSL-compatible fields
title: "Multi-Task Learning for Sparsely-Labeled Time Series: A Case Study on Cold-Hardiness Modeling"
author:
  - literal: "Aseem Saxena"
  - literal: "Paola Pesantez-Cabrera"
  - literal: "Jonathan Magby"
  - literal: "Markus Keller"
  - literal: "Alan Fern"
issued:
  date-parts:
    - [2026, 9, 8]
url: "https://arxiv.org/abs/2609.09062"

# Custom fields
paper_id: "2609.09062"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "recurrent-neural-network"
  - "rnn"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-10T09:16:10Z"
created_at: "2026-09-10T09:16:10Z"
---

# Multi-Task Learning for Sparsely-Labeled Time Series: A Case Study on Cold-Hardiness Modeling

**Authors**: Aseem Saxena, Paola Pesantez-Cabrera, Jonathan Magby, Markus Keller, Alan Fern
**Date**: 2026-09-08
**Paper ID**: [openalex:2609.09062](https://arxiv.org/abs/2609.09062)

## Summary

This paper investigates multi-task learning (MTL) and transfer learning using recurrent neural networks to model temporal processes from temporally sparse labels, focusing on the agricultural applications of grape cold-hardiness and budbreak prediction. The authors evaluate various MTL architectures across different plant cultivars and show that shared multi-task models consistently outperform single-task baselines and state-of-the-art scientific models. Furthermore, they demonstrate that a unified model can jointly learn both cold-hardiness and budbreak prediction to achieve enhanced accuracy.

## Key Contributions

- Investigated multi-task learning (MTL) and transfer learning approaches for sparsely-labeled time series modeling, specifically targeting agricultural cold-hardiness and budbreak prediction across multiple plant cultivars.
- Demonstrated that specific MTL recurrent neural network architectures consistently outperform single-task learning and state-of-the-art scientific models.
- Showed that a single MTL model can simultaneously learn related agricultural tasks (cold hardiness and budbreak) to achieve improved predictive accuracy.

## Limitations

Future work could explore expanding the MTL framework to a broader set of agricultural variables and evaluating on additional perennial crop datasets.

## Open Questions & Future Work

- [[robust-task-embedding-transfer-learning]]

## Archivist Review

Applied strict selectivity per instructions. No new standalone concepts were warranted since multi-task learning for recurrent neural networks represents standard architectural exploration. Retained one open question addressing negative transfer in task embedding optimization.

### Approved Open Questions
- Robust Task Embedding Transfer Learning: Understanding why target embedding optimization fails during transfer learning is crucial for enabling zero-shot or few-shot adaptation in sparse multi-task time series applications.

### Rejected Candidates
- [open_question] Interpretable Deep Learning for Mechanistic Science (`interpretable-deep-learning-mechanistic-science`) - low_impact: Too broad and philosophical rather than a specific algorithmic or methodological bottleneck for time series modeling.

## Links

- [Abstract](https://arxiv.org/abs/2609.09062)
- [PDF](https://arxiv.org/pdf/2609.09062)

