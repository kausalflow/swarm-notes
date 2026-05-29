---
# CSL-compatible fields
title: "LATTE: Forecasting Peer Anchored Preference Trajectories for Personalized LLM Generation"
author:
  - literal: "Jinze Li"
  - literal: "Xiaoyan Yang"
  - literal: "Shuo Yang"
  - literal: "Jinfeng Xu"
  - literal: "Yue Shen"
  - literal: "Jian Wang"
  - literal: "Jinjie Gu"
  - literal: "Edith Cheuk-Han Ngai"
issued:
  date-parts:
    - [2026, 5, 26]
url: "https://arxiv.org/abs/2605.26612"

# Custom fields
paper_id: "2605.26612"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "personalization"
  - "prompt-tuning"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "latte-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-29T08:38:22Z"
created_at: "2026-05-29T08:38:22Z"
---

# LATTE: Forecasting Peer Anchored Preference Trajectories for Personalized LLM Generation

**Authors**: Jinze Li, Xiaoyan Yang, Shuo Yang, Jinfeng Xu, Yue Shen, Jian Wang, Jinjie Gu, Edith Cheuk-Han Ngai
**Date**: 2026-05-26
**Paper ID**: [openalex:2605.26612](https://arxiv.org/abs/2605.26612)

## Summary

LATTE addresses the limitations of aggregate static user profiles in personalized LLM generation by modeling preference evolution as a dynamic trajectory. The method achieves this by calculating a relative preference state that subtracts time-masked peer baselines for shared item contexts, which is then forecasted and injected into a frozen LLM via an anchored soft token. This approach effectively disentangles stable user identity from recent behavior drift and noise, outperforming conventional memory-based and prompt-based baselines.

## Key Contributions

- Introduced LATTE, a framework for personalizing frozen LLMs by forecasting peer-anchored relative preference trajectories instead of aggregate static profiles.
- Developed a State to Token Bridge that injects forecasted preference states into frozen LLMs using single anchored soft tokens.
- Demonstrated that LATTE outperforms existing retrieval, static latent profile, and soft prompt compression methods, achieving 0.259 ROUGE-L on Amazon Reviews 2023.

## Open Questions & Future Work

- [[temporal-drift-latent-forecasting-challenges]]

## Key Concepts

- [[latte-framework]]: A personalization framework that models user preferences as a forecasted trajectory relative to peer behavior under shared item contexts.

## Archivist Review

I approved the LATTE framework as it introduces a reusable mechanism for peer-anchored state trajectory modeling. I also approved the open question regarding temporal drift as it identifies a substantive limitation in how current latent forecasting methods balance historical stability against recent signal noise. Other candidates were either subcomponents or general enough to be considered standard practice.

### Approved Concepts
- LAtent Trajectory Tracking and Extrapolation (LATTE): It provides a structured approach for disentangling stable user identity from recent preference drift by forecasting peer-anchored relative preference trajectories, which is a transferable technique for personalization.

### Approved Open Questions
- Temporal Drift in Latent Forecasting: This addresses a core bottleneck in personalized generation; shifting from static aggregation to dynamic forecasting is essential, yet it introduces significant challenges in robustness, noise management, and benchmarking.

## Links

- [Abstract](https://arxiv.org/abs/2605.26612)
- [PDF](https://arxiv.org/pdf/2605.26612)

