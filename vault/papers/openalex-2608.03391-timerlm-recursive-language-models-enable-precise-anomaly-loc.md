---
# CSL-compatible fields
title: "TimeRLM: Recursive Language Models Enable Precise Anomaly Localization in Long-Context Time-Series"
author:
  - literal: "Nicolas Zumarraga"
  - literal: "Lorenzo Steno"
  - literal: "Ning Wang"
  - literal: "Max Rosenblattl"
  - literal: "Thomas Kaar"
  - literal: "Maxwell A. Xu"
  - literal: "Kevin O'Sullivan"
  - literal: "Markus Kreft"
  - literal: "Elgar Fleisch"
  - literal: "Paul Schmiedmayer"
  - literal: "Patrick Langer"
  - literal: "Robert Jakob"
issued:
  date-parts:
    - [2026, 8, 4]
url: "https://arxiv.org/abs/2608.03391"

# Custom fields
paper_id: "2608.03391"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series-analysis"
  - "long-context"
  - "language-model"
  - "reinforcement-learning"
  - "anomaly-detection"
  - "benchmark"
architectures:
  []
datasets:
  - "anomalyxl"
concept_slugs:
  - "timerlm"
dataset_slugs:
  - "anomalyxl"
skill: "TimeSeriesSkill"
processed_at: "2026-08-07T06:04:08Z"
created_at: "2026-08-07T06:04:08Z"
---

# TimeRLM: Recursive Language Models Enable Precise Anomaly Localization in Long-Context Time-Series

**Authors**: Nicolas Zumarraga, Lorenzo Steno, Ning Wang, Max Rosenblattl, Thomas Kaar, Maxwell A. Xu, Kevin O'Sullivan, Markus Kreft, Elgar Fleisch, Paul Schmiedmayer, Patrick Langer, Robert Jakob
**Date**: 2026-08-04
**Paper ID**: [openalex:2608.03391](https://arxiv.org/abs/2608.03391)

## Summary

TimeRLM is a recursive language model framework designed for precise anomaly localization in long-context time series by keeping the context external and querying it via code and vision. To evaluate this, the authors introduce AnomalyXL, a synthetic benchmark with programmatically injected anomalies across multiple task categories. Experiments show that TimeRLM significantly outperforms single-pass time-series language models and baselines on localization tasks, and reinforcement learning post-training further boosts performance while reducing required agent interaction turns.

## Key Contributions

- Introduces TimeRLM, a recursive language model formulation that sequentially manipulates long-context time-series using code and vision capabilities.
- Proposes AnomalyXL, a synthetic long-context benchmark with programmatically injected anomalies spanning multiple task categories (AnomalyXL-MCQ and AnomalyXL-Localize).
- Demonstrates that TimeRLM achieves 0.682 IoU on localization and 0.745 on classify-with-evidence, substantially outpassing single-pass TSLM baselines (0.329 and 0.072).
- Shows that reinforcement learning post-training improves performance while reducing agent interaction turns by approximately two-thirds.

## Limitations

Evaluated primarily on synthetic training data before generalization to real-world datasets (ECG, sleep, software observability).

## Open Questions & Future Work

- [[real-world-long-context-anomaly-localization]]

## Key Concepts

- [[timerlm]]: A recursive language model formulation for time-series that sequentially manipulates signals using code and vision capabilities.

## Archivist Review

Approved the core TimeRLM framework concept, the AnomalyXL benchmark dataset, and an important open question on real-world long-context anomaly localization. All decisions adhere strictly to the vault's standards for scarcity, novelty, and reusability.

### Approved Concepts
- TimeRLM: Central framework proposed in the paper for recursive long-context time-series anomaly localization via code and vision.

### Approved Open Questions
- Real-World Long-Context Anomaly Localization: Essential for bridging the gap between synthetic evaluations and practical deployment in complex real-world operations.

### Rejected Candidates
- [concept] AnomalyXL (`anomalyxl`) - duplicate_existing: Redundant with the approved dataset entry; concepts should represent algorithmic mechanisms or frameworks.

## Datasets

- [[anomalyxl]]

## Links

- [Abstract](https://arxiv.org/abs/2608.03391)
- [PDF](https://arxiv.org/pdf/2608.03391)

