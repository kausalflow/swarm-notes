---
# CSL-compatible fields
title: "TimeSRL: Generalizable Time-Series Behavioral Modeling via Semantic RL-Tuned LLMs -- A Case Study in Mental Health"
author:
  - literal: "Yuang Fan"
  - literal: "Lilin Xu"
  - literal: "Millie Wu"
  - literal: "Jingping Nie"
  - literal: "Qingyu Chen"
  - literal: "Yuzhe Yang"
  - literal: "Zhuo Zhang"
  - literal: "Xin Liu"
  - literal: "Subigya Nepal"
  - literal: "Xiaofan Jiang"
  - literal: "Xuhai \"Orson\" Xu"
issued:
  date-parts:
    - [2026, 5, 20]
url: "https://arxiv.org/abs/2605.21295"

# Custom fields
paper_id: "2605.21295"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "time-series"
  - "reinforcement-learning-from-human-feedback"
  - "alignment"
  - "few-shot-learning"
  - "multimodal"
  - "generalization"
architectures:
  []
datasets:
  []
concept_slugs:
  - "semantic-bottleneck-for-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-23T07:25:33Z"
created_at: "2026-05-23T07:25:33Z"
---

# TimeSRL: Generalizable Time-Series Behavioral Modeling via Semantic RL-Tuned LLMs -- A Case Study in Mental Health

**Authors**: Yuang Fan, Lilin Xu, Millie Wu, Jingping Nie, Qingyu Chen, Yuzhe Yang, Zhuo Zhang, Xin Liu, Subigya Nepal, Xiaofan Jiang, Xuhai "Orson" Xu
**Date**: 2026-05-20
**Paper ID**: [openalex:2605.21295](https://arxiv.org/abs/2605.21295)

## Summary

TimeSRL is a two-stage LLM-based framework designed to improve cross-dataset generalization in longitudinal behavioral modeling by routing raw sensor inputs through a semantic bottleneck. By abstracting time-series signals into natural language, the model shifts the reasoning burden from cohort-specific numerical artifacts to generalizable semantic concepts. The system is optimized end-to-end using Group Relative Policy Optimization (GRPO), which learns outcome-aligned abstractions without requiring expensive intermediate label annotations. Experimental results in mental health forecasting demonstrate significant performance gains and superior cross-cohort transfer capabilities compared to existing ML and LLM baselines.

## Key Contributions

- Introduces TimeSRL, a two-stage LLM framework that utilizes a semantic bottleneck to map raw longitudinal sensor signals to interpretable natural language before performing behavioral prediction.
- Employs GRPO with RLVR to enable end-to-end training of the semantic abstraction layer without the need for manual intermediate annotations.
- Achieves state-of-the-art cross-cohort generalization in mental health prediction (anxiety and depression) under a leave-one-dataset-out protocol, consistently outperforming standard ML and LLM baselines.

## Open Questions & Future Work

- [[faithfulness-of-semantic-summaries-in-behavioral-modeling]]

## Key Concepts

- [[semantic-bottleneck-for-forecasting]]: A forecasting framework that improves cross-dataset generalization by forcing LLMs to reason over intermediate natural language abstractions derived from raw time-series signals.

## Archivist Review

I approved the 'Semantic Bottleneck for Forecasting' as a core architectural concept because it reframes the distribution shift problem in time-series as a latent representation problem solvable via linguistic abstraction. I rejected the 'Flow GRPO' concept as it represents an application-specific optimization detail rather than a unique forecasting mechanism. The open question regarding the faithfulness of semantic abstractions addresses a critical, unresolved research bottleneck in deploying LLM-based time-series models for clinical use.

### Approved Concepts
- Semantic Bottleneck for Forecasting: It proposes a framework for cross-dataset generalization by forcing models to reason over human-interpretable linguistic abstractions rather than cohort-specific numerical sensor data.

### Approved Open Questions
- Faithfulness of semantic summaries: Determining whether latent behavioral representations are faithful to patient history is critical for ensuring the safety and interpretability of LLM-driven diagnostic systems.

### Rejected Candidates
- [concept] Flow GRPO Post-training (`flow-grpo-post-training`) - subcomponent_of_broader_mechanism: This is a specific implementation of an optimization technique (GRPO) rather than a fundamental forecasting concept; it is already well-represented by the broader concept of reinforcement learning for alignment.

## Links

- [Abstract](https://arxiv.org/abs/2605.21295)
- [PDF](https://arxiv.org/pdf/2605.21295)

