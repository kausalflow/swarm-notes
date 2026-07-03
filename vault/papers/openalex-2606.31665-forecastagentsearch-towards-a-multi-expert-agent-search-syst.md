---
# CSL-compatible fields
title: "ForecastAgentSearch: Towards a Multi-Expert Agent Search System for Geopolitical Event Forecasting"
author:
  - literal: "Miaomiao Cai"
  - literal: "He Chang"
  - literal: "Yunshan Ma"
  - literal: "See-Kiong Ng"
issued:
  date-parts:
    - [2026, 6, 30]
url: "https://arxiv.org/abs/2606.31665"

# Custom fields
paper_id: "2606.31665"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "agent"
  - "autonomous-agent"
  - "planning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "forecastagentsearch-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-03T07:55:22Z"
created_at: "2026-07-03T07:55:22Z"
---

# ForecastAgentSearch: Towards a Multi-Expert Agent Search System for Geopolitical Event Forecasting

**Authors**: Miaomiao Cai, He Chang, Yunshan Ma, See-Kiong Ng
**Date**: 2026-06-30
**Paper ID**: [openalex:2606.31665](https://arxiv.org/abs/2606.31665)

## Summary

ForecastAgentSearch is a novel framework for geopolitical event forecasting that leverages a multi-expert agent system to handle complex, uncertain scenarios. The system retrieves and ranks specialized agents based on task context and complementarity, coordinating their expertise to produce forecasts accompanied by explanations and uncertainty assessments. This approach addresses the limitations of monolithic models by enabling targeted, multi-perspective reasoning for high-stakes forecasting queries.

## Key Contributions

- Introduces ForecastAgentSearch, a framework that models geopolitical forecasting as a multi-expert agent search and coordination problem.
- Proposes a systemic approach to agent selection based on regional knowledge, domain expertise, and complementarity to improve forecasting reliability.
- Identifies critical design challenges in agent profiling, retrieval, ranking, and coordination for specialized forecasting systems.

## Open Questions & Future Work

- [[multi-agent-coordination-and-synthesis]]

## Key Concepts

- [[forecastagentsearch-framework]]: A framework that treats event forecasting as a multi-expert agent search and coordination problem.

## Archivist Review

I approved the ForecastAgentSearch framework for its potential in adapting agent search and coordination architectures to complex forecasting domains. I also approved the open question regarding multi-expert coordination, as it identifies a central bottleneck in synthesizing diverse, often conflicting expert agent perspectives for high-stakes forecasting. All other candidates were rejected to maintain focus on high-impact mechanisms and universal research challenges.

### Approved Concepts
- ForecastAgentSearch: It is the core framework introduced in the paper, defining a novel paradigm for combining expert-level AI agents for complex forecasting.

### Approved Open Questions
- Coordinating Multi-Expert Forecasts: Without effective coordination, the potential benefits of utilizing specialized agents are undermined, which is a critical bottleneck for high-stakes forecasting.

### Rejected Candidates
- [open_question] Coordinating Multi-Expert Forecasts (`multi-agent-coordination-and-synthesis`) - other: The open question was approved and therefore not rejected.

## Links

- [Abstract](https://arxiv.org/abs/2606.31665)
- [PDF](https://arxiv.org/pdf/2606.31665)

