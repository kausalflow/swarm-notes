---
# CSL-compatible fields
title: "Evaluating Temporal Semantic Caching and Workflow Optimization in Agentic Plan-Execute Pipelines"
author:
  - literal: "Alimurtaza Mustafa Merchant"
  - literal: "Krish Veera"
  - literal: "Sajal Kumar Goyla"
  - literal: "Shambhawi Bhure"
  - literal: "Dhaval Patel"
  - literal: "Kaoutar El Maghraoui"
issued:
  date-parts:
    - [2026, 5, 20]
url: "https://arxiv.org/abs/2605.20630"

# Custom fields
paper_id: "2605.20630"
paper_source: "openalex"
domain: "nlp"
tags:
  - "agent"
  - "llm"
  - "tool-use"
  - "benchmark"
  - "language-model"
  - "latency-optimization"
architectures:
  []
datasets:
  - "AssetOpsBench"
concept_slugs:
  - "temporal-semantic-cache"
dataset_slugs:
  - "assetopsbench"
skill: "TimeSeriesSkill"
processed_at: "2026-05-23T07:26:28Z"
created_at: "2026-05-23T07:26:28Z"
---

# Evaluating Temporal Semantic Caching and Workflow Optimization in Agentic Plan-Execute Pipelines

**Authors**: Alimurtaza Mustafa Merchant, Krish Veera, Sajal Kumar Goyla, Shambhawi Bhure, Dhaval Patel, Kaoutar El Maghraoui
**Date**: 2026-05-20
**Paper ID**: [openalex:2605.20630](https://arxiv.org/abs/2605.20630)

## Summary

This paper addresses the high latency of agentic plan-execute pipelines in industrial asset operations by identifying the limitations of standard semantic caches. The authors introduce AssetOpsBench to evaluate these workflows and propose a temporal semantic cache that ensures output validity by accounting for time, asset, and sensor-specific parameters. Additionally, they implement MCP-based workflow optimizations, such as dependency-aware execution and tool-discovery caching, yielding significant reductions in end-to-end latency.

## Key Contributions

- Introduces AssetOpsBench (AOB), a dedicated benchmark for evaluating latency and correctness in industrial agentic plan-execute pipelines.
- Develops a temporal semantic cache that incorporates asset and sensor parameter validation, achieving a 30.6x speedup on cache hits.
- Implements MCP workflow optimizations, including disk-backed tool-discovery and dependency-aware parallel execution, resulting in a 1.67x pipeline speedup.

## Open Questions & Future Work

- [[parameter-aware-caching-industrial-agents]]

## Key Concepts

- [[temporal-semantic-cache]]: A specialized caching mechanism for agentic pipelines that incorporates time, asset, and sensor parameter validation to maintain correctness in latency-sensitive industrial workflows.

## Archivist Review

I approved the core temporal semantic caching concept and the associated parameter-awareness open question as they represent a fundamental shift in how agentic workflows manage stateful industrial context. The benchmark AssetOpsBench was approved as it provides a specific, named framework for evaluating these latency-sensitive industrial pipelines. Other implementation details like parallel execution and tool-discovery caching were deemed subcomponents of the broader agent pipeline optimization problem and rejected to prioritize the primary contributions.

### Approved Concepts
- Temporal Semantic Cache: It addresses the failure of traditional semantic caches to account for time-sensitive, parameter-rich industrial sensor data in agentic workflows.

### Approved Open Questions
- Parameter-Aware Caching for Agents: This is critical because it addresses a fundamental limitation of semantic caching in agentic systems, where result validity is state-dependent rather than just input-dependent. Solving this would move caching from a best-effort heuristic to a reliable component for safety-critical industrial applications.

## Datasets

- [[assetopsbench]]

## Links

- [Abstract](https://arxiv.org/abs/2605.20630)
- [PDF](https://arxiv.org/pdf/2605.20630)

