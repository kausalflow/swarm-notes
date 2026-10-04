---
# CSL-compatible fields
title: "LineupRL: Verifiable Reinforcement Learning for Time Series Captioning via Caption-to-Series Identification"
author:
  - literal: "Haochen Zhang"
  - literal: "Laura Yao"
  - literal: "Zachary Plotkin"
  - literal: "Gengwei Zhang"
  - literal: "Tianlong Chen"
issued:
  date-parts:
    - [2026, 10, 1]
url: "https://arxiv.org/abs/2610.01800"

# Custom fields
paper_id: "2610.01800"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "time-series"
  - "multimodal"
  - "vision-language-model"
  - "reinforcement-learning"
  - "fine-tuning"
  - "forecasting"
  - "benchmark"
  - "evaluation"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "lineuprl"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-04T10:48:24Z"
created_at: "2026-10-04T10:48:24Z"
---

# LineupRL: Verifiable Reinforcement Learning for Time Series Captioning via Caption-to-Series Identification

**Authors**: Haochen Zhang, Laura Yao, Zachary Plotkin, Gengwei Zhang, Tianlong Chen
**Date**: 2026-10-01
**Paper ID**: [openalex:2610.01800](https://arxiv.org/abs/2610.01800)

## Summary

Time series captioning struggles with supervised fine-tuning limits and poor transferability of reward functions designed for other domains. To resolve this, the authors propose LineupRL, a reinforcement learning with verifiable rewards pipeline that uses caption-to-series identification. A frozen large language model verifier assigns rewards by identifying the correct raw time series from distractors based solely on the generated caption. Experiments show that LineupRL outperforms existing supervised fine-tuning and RL baselines across captioning, forecasting, and reconstruction tasks, while allowing a small 3B VLM to surpass a much larger 72B VLM teacher.

## Key Contributions

- Proposes LineupRL, a reinforcement learning with verifiable rewards (RLVR) pipeline that leverages caption-to-series identification for time series captioning.
- Employs a frozen large language model verifier that reads generated captions and candidate raw time series to select the correct time series among distractors.
- Outperforms supervised fine-tuning and standard RL baselines across time series captioning, forecasting, and reconstruction benchmarks.
- Enables a 3B vision-language model trained with LineupRL to outperform a 72B VLM teacher model using only 1/24th of the parameters.

## Open Questions & Future Work

- [[longer-multivariate-time-series-captioning]]

## Key Concepts

- [[lineuprl]]: A reinforcement learning with verifiable rewards pipeline for time series captioning that uses caption-to-series identification as a reward.

## Archivist Review

Approved the core LineupRL concept as a novel verifiable reinforcement learning mechanism for time series captioning, along with the open question regarding its scaling to multivariate and long-horizon series.

### Approved Concepts
- LineupRL: It introduces a novel verifiable reinforcement learning pipeline for time series captioning using caption-to-series identification.

### Approved Open Questions
- Longer and Multivariate Time Series Captioning: Real-world time series data is frequently multivariate and spans long durations, making scalability to these settings a crucial milestone for time series representation learning and captioning.

## Links

- [Abstract](https://arxiv.org/abs/2610.01800)
- [PDF](https://arxiv.org/pdf/2610.01800)

