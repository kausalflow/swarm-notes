---
# CSL-compatible fields
title: "Patched-DeltaNet: Token-Level Event-Driven Memory for Linear-Time Anomaly Detection"
author:
  - literal: "Tae-Gyun Lee"
  - literal: "Junyoung Park"
  - literal: "Kyu Won Han"
issued:
  date-parts:
    - [2026, 5, 27]
url: "https://arxiv.org/abs/2605.27992"

# Custom fields
paper_id: "2605.27992"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "efficient-transformer"
  - "benchmark"
architectures:
  []
datasets:
  - "smd"
concept_slugs:
  - "token-level-event-driven-memory"
dataset_slugs:
  - "smd"
skill: "TimeSeriesSkill"
processed_at: "2026-05-30T07:36:43Z"
created_at: "2026-05-30T07:36:43Z"
---

# Patched-DeltaNet: Token-Level Event-Driven Memory for Linear-Time Anomaly Detection

**Authors**: Tae-Gyun Lee, Junyoung Park, Kyu Won Han
**Date**: 2026-05-27
**Paper ID**: [openalex:2605.27992](https://arxiv.org/abs/2605.27992)

## Summary

Patched-DeltaNet is a resource-efficient time-series anomaly detection architecture that achieves linear O(L/P) time complexity by combining time-series patching with Gated Delta Networks. The model uses an event-driven memory mechanism to update its recurrent state only when significant physical changes, or 'deltas', are detected in local patches. Experimental results on the Server Machine Dataset (SMD) demonstrate that this approach effectively filters background noise and outperforms recent transformer-based architectures in both detection accuracy and computational efficiency.

## Key Contributions

- Patched-DeltaNet reduces computational complexity to O(L/P) by integrating time-series patching with Gated Delta Networks.
- Demonstrates the emergence of token-level event-driven memory that filters noise while preserving sensitivity to anomalous drifts.
- Achieves superior anomaly detection performance (0.957 ROC-AUC, 0.822 PA-F1) on the Server Machine Dataset benchmark compared to recent state-of-the-art baselines under equal compute budgets.

## Open Questions & Future Work

- [[gating-mechanism-optimization-linear-attention]]

## Key Concepts

- [[token-level-event-driven-memory]]: A mechanism where a model updates its recurrent memory state only upon detecting significant physical changes (deltas) within extracted local semantic patches.

## Archivist Review

The paper proposes a clever integration of patching and Gated Delta Networks to achieve linear-time complexity. I have approved the 'token-level event-driven memory' concept as it represents a novel, reusable paradigm for efficient time-series processing. The SMD dataset is approved as a standard benchmark for anomaly detection. Finally, the open question on gating mechanisms in linear attention captures a substantial unresolved bottleneck in the design of efficient state-space models.

### Approved Concepts
- Token-level event-driven memory: The concept provides a novel paradigm for state updates in time-series modeling, linking patching with event-triggered recurrence.

### Approved Open Questions
- Optimizing Gating in Linear Attention: Understanding the optimal design of gating mechanisms in linear state-space models is critical for balancing noise filtering and signal preservation, which directly impacts the reliability of anomaly detection in high-variance environments.

## Datasets

- [[smd]]

## Links

- [Abstract](https://arxiv.org/abs/2605.27992)
- [PDF](https://arxiv.org/pdf/2605.27992)

