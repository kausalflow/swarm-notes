---
# CSL-compatible fields
title: "When Tomorrow Becomes Today: Self-Evolving Policies for Agentic Time-Series Forecasting"
author:
  - literal: "Yifan Hu"
  - literal: "Xilin Dai"
  - literal: "Zhiyuan Qu"
  - literal: "Yiding Liu"
  - literal: "Zewei Dong"
  - literal: "Jiang-ming Yang"
  - literal: "Qiang Xu"
issued:
  date-parts:
    - [2026, 9, 21]
url: "https://arxiv.org/abs/2609.24862"

# Custom fields
paper_id: "2609.24862"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "agent"
  - "autonomous-agent"
  - "long-context"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "timevolve"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-24T09:37:42Z"
created_at: "2026-09-24T09:37:42Z"
---

# When Tomorrow Becomes Today: Self-Evolving Policies for Agentic Time-Series Forecasting

**Authors**: Yifan Hu, Xilin Dai, Zhiyuan Qu, Yiding Liu, Zewei Dong, Jiang-ming Yang, Qiang Xu
**Date**: 2026-09-21
**Paper ID**: [openalex:2609.24862](https://arxiv.org/abs/2609.24862)

## Summary

This paper introduces TimEvolve, a self-evolving time-series agent that leverages delayed feedback from realized outcomes during deployment to persistently update joint orchestration policies, including expert trust, path selection, and intervention strength. Operating on a frozen backbone via a predict, reveal, and update protocol, TimEvolve eliminates the need for extra manual annotations and surpasses fifteen baseline methods across multiple Time-MMD domains.

## Key Contributions

- Introduces TimEvolve, a self-evolving agentic time-series forecasting framework that uses a temporally ordered predict, reveal, and update protocol.
- Systematically converts realized future outcomes into persistent updates of expert trust, agent path selection, and intervention strength without requiring additional human annotations.
- Achieves the best average MSE and MAE ranks among fifteen comparison methods and secures the lowest errors across seven out of eight Time-MMD domains.

## Open Questions & Future Work

- [[end-to-end-agent-backbone-adaptation]]

## Key Concepts

- [[timevolve]]: A frozen-backbone time-series agent that systematically converts realized deployment outcomes into persistent updates of joint orchestration policies.

## Archivist Review

Approved the novel TimEvolve framework concept and the corresponding open question regarding backbone adaptation versus frozen orchestration policies. Rejected the dataset as a routine benchmark bucket.

### Approved Concepts
- TimEvolve: It serves as the core framework for self-evolving agentic time-series forecasting via a predict, reveal, and update protocol.

### Approved Open Questions
- End-to-End Agent Backbone Adaptation: Crucial for determining whether end-to-end gradient updates or active fine-tuning of the core foundation models and reasoners can further improve agentic time-series forecasting under distribution drift compared to restricting adaptation strictly to the orchestration layer.

### Rejected Candidates
- [dataset] Time-MMD (`time-mmd`) - low_impact: Routine or unnamed dataset bucket not meeting inclusion threshold.

## Links

- [Abstract](https://arxiv.org/abs/2609.24862)
- [PDF](https://arxiv.org/pdf/2609.24862)

