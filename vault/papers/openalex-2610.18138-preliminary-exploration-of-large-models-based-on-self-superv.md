---
# CSL-compatible fields
title: "Preliminary Exploration of Large Models Based on Self-Supervised Learning for Health Monitoring of Power Electronic Converters"
author:
  - literal: "Xinyuan Liao"
  - literal: "Xiangtian Deng"
  - literal: "Yang Liu"
  - literal: "Zhaobing Cai"
  - literal: "Haoran Wang"
  - literal: "Yi Zhang"
  - literal: "Yi Zhang"
issued:
  date-parts:
    - [2026, 10, 13]
url: "https://arxiv.org/abs/2610.18138"

# Custom fields
paper_id: "2610.18138"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "self-supervised-learning"
  - "pre-training"
  - "few-shot-learning"
  - "transformer"
  - "patchtst"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "pe-tsfm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-16T09:24:11Z"
created_at: "2026-10-16T09:24:11Z"
---

# Preliminary Exploration of Large Models Based on Self-Supervised Learning for Health Monitoring of Power Electronic Converters

**Authors**: Xinyuan Liao, Xiangtian Deng, Yang Liu, Zhaobing Cai, Haoran Wang, Yi Zhang, Yi Zhang
**Date**: 2026-10-13
**Paper ID**: [openalex:2610.18138](https://arxiv.org/abs/2610.18138)

## Summary

The authors introduce PE-TSFM, a time-series foundation model built on the PatchTST architecture and self-supervised learning, designed for power electronic converter health monitoring. Pre-trained on over 143 million timestamps of predominantly unlabeled operational data from a traction converter, PE-TSFM achieves an 87% accuracy on degradation classification tasks, substantially outperforming conventional baseline models. This work demonstrates the effectiveness of leveraging large-scale unlabeled operational data via foundation models for industrial health monitoring.

## Key Contributions

- Introduces PE-TSFM, a time-series foundation model tailored for power module health monitoring using the PatchTST architecture and self-supervised learning.
- Pre-trained on over 143 million timestamps, with over 98% unlabeled operational data collected from a real-world traction converter.
- Achieves 87% accuracy on degradation classification tasks, significantly outperforming five conventional time-series AI models (27% to 45% accuracy).
- Demonstrates strong few-shot learning capabilities and generalization across varying operating conditions for power electronics converters.

## Limitations

Future work could expand evaluation to broader converter topologies and operating environments beyond traction converters.

## Key Concepts

- [[pe-tsfm]]: A time-series foundation model tailored for power module health monitoring that combines PatchTST with self-supervised learning on large-scale unlabeled operational data.

## Archivist Review

Approved PE-TSFM as a domain-specific time-series foundation model for power electronics health monitoring, while rejecting existing architectures like PatchTST. No open questions or datasets met the strict novelty or scarcity thresholds.

### Approved Concepts
- PE-TSFM: It is the core time-series foundation model proposed for power electronic converter health monitoring using self-supervised learning on large-scale unlabeled operational data.

### Rejected Candidates
- [concept] PatchTST Architecture (`patchtst`) - duplicate_existing: PatchTST is an existing backbone architecture rather than a novel concept introduced by this paper.

## Links

- [Abstract](https://arxiv.org/abs/2610.18138)
- [PDF](https://arxiv.org/pdf/2610.18138)

