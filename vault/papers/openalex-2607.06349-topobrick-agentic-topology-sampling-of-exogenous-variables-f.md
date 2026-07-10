---
# CSL-compatible fields
title: "TopoBrick: Agentic Topology Sampling of Exogenous Variables for Zero-Shot Building IoT Forecasting"
author:
  - literal: "Xiachong Lin"
  - literal: "Du Yin"
  - literal: "Arian Prabowo"
  - literal: "Hao Xue"
  - literal: "Wen Hu"
  - literal: "Imran Razzak"
  - literal: "Matthew Amos"
  - literal: "Sam Behrens"
  - literal: "Flora D. Salim"
issued:
  date-parts:
    - [2026, 7, 7]
url: "https://arxiv.org/abs/2607.06349"

# Custom fields
paper_id: "2607.06349"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "agent"
  - "knowledge-graph"
  - "zero-shot-learning"
  - "iot"
architectures:
  []
datasets:
  []
concept_slugs:
  - "agentic-topology-sampler"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-10T08:15:05Z"
created_at: "2026-07-10T08:15:05Z"
---

# TopoBrick: Agentic Topology Sampling of Exogenous Variables for Zero-Shot Building IoT Forecasting

**Authors**: Xiachong Lin, Du Yin, Arian Prabowo, Hao Xue, Wen Hu, Imran Razzak, Matthew Amos, Sam Behrens, Flora D. Salim
**Date**: 2026-07-07
**Paper ID**: [openalex:2607.06349](https://arxiv.org/abs/2607.06349)

## Summary

TopoBrick is a training-free framework designed for zero-shot forecasting in building IoT environments by leveraging building-specific knowledge graphs. The system constructs a structural skeleton of the building and employs an agentic topology sampler to dynamically select relevant exogenous variables based on their deployment-time availability. By effectively separating past-observed states from future-known variables like weather and schedules, TopoBrick significantly improves accuracy in physically coupled sensing tasks compared to standard zero-shot baselines.

## Key Contributions

- Introduced TopoBrick, a training-free, zero-shot forecasting framework that utilizes building knowledge graphs for structural-aware inference.
- Proposed an agentic topology sampler that dynamically identifies relevant exogenous variables, outperforming traditional fixed-hop or ontology-only selection strategies.
- Demonstrated that TopoBrick achieves state-of-the-art zero-shot performance across three real-world building IoT datasets, while remaining competitive with fully-trained domain-specific models.

## Open Questions & Future Work

- [[generalizing-topology-reasoning-to-other-tasks]]

## Key Concepts

- [[agentic-topology-sampler]]: An agent-based framework that dynamically selects relevant exogenous variables from a knowledge graph to inform zero-shot time-series forecasting.

## Archivist Review

The TopoBrick framework introduces a distinct agentic approach to dynamic feature selection in IoT forecasting, which is conceptually significant and reusable. I have approved the 'Agentic Topology Sampler' as a core paradigm and identified the generalization of this topological reasoning to broader IoT tasks as a meaningful research direction. No datasets were approved as they were not specific or central enough to the paper's claimed novelty.

### Approved Concepts
- Agentic Topology Sampler: Provides a novel, training-free way to dynamically select relevant exogenous inputs based on structural topology rather than predefined static sets, serving as a transferable paradigm for IoT forecasting.

### Approved Open Questions
- Generalizing Topology-based Reasoning Tasks: Establishing a unified approach to building intelligence reduces the need for task-specific models and pipelines.

## Links

- [Abstract](https://arxiv.org/abs/2607.06349)
- [PDF](https://arxiv.org/pdf/2607.06349)

