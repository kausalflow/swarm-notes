---
# CSL-compatible fields
title: "Traceable Multi-Agent System for Knowledge-Based Forecasting"
author:
  - literal: "Junhyuk Kang"
  - literal: "Sangjun Han"
  - literal: "Hyeokjun Choe"
  - literal: "Soonyoung Lee"
issued:
  date-parts:
    - [2026, 8, 4]
url: "https://arxiv.org/abs/2608.03339"

# Custom fields
paper_id: "2608.03339"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "multi-agent"
  - "agent"
  - "autonomous-agent"
  - "rag"
  - "knowledge-graph"
  - "interpretability"
  - "explainability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "tracemas"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-07T06:04:23Z"
created_at: "2026-08-07T06:04:23Z"
---

# Traceable Multi-Agent System for Knowledge-Based Forecasting

**Authors**: Junhyuk Kang, Sangjun Han, Hyeokjun Choe, Soonyoung Lee
**Date**: 2026-08-04
**Paper ID**: [openalex:2608.03339](https://arxiv.org/abs/2608.03339)

## Summary

Enterprise forecasting relies increasingly on autonomous agents, making it difficult to inspect the evidence and revisions behind forecast changes. To address this, the authors present TraceMAS, an interactive multi-agent system organized around two causal-loop representations: an Ideal CLD for extracting causal factors from domain documents, and a Data-Grounded CLD for linking those factors to internal variables and external data. Demonstrated on crude oil price forecasting, TraceMAS allows practitioners to explore causal maps, review feature-data mappings, and trace model revisions from textual evidence to final market scenarios.

## Key Contributions

- Proposes TraceMAS, an interactive multi-agent system for traceable knowledge-based enterprise forecasting.
- Introduces dual causal-loop representations (Ideal CLD and Data-Grounded CLD) to link domain document factors to internal variables and external data.
- Demonstrates the system on crude oil price forecasting, enabling practitioners to inspect agent-level revisions, causal maps, and feature-data mappings.

## Limitations

Demonstrated primarily as a system demo on a single specific domain (crude oil price forecasting) without large-scale quantitative benchmark evaluations across diverse time-series datasets.

## Open Questions & Future Work

- [[evaluating-agent-derived-causal-diagrams]]

## Key Concepts

- [[tracemas]]: An interactive multi-agent system for traceable knowledge-based forecasting using dual causal loop diagrams.

## Archivist Review

Approved the core multi-agent traceable forecasting system concept (TraceMAS) and its corresponding open question regarding the evaluation of agent-derived causal diagrams. No standard benchmark datasets were introduced, so none were approved.

### Approved Concepts
- TraceMAS: TraceMAS introduces a novel interactive multi-agent system architecture organized around dual causal loop diagrams (Ideal CLD and Data-Grounded CLD) to make forecasting pipelines fully traceable.

### Approved Open Questions
- Evaluating Agent-Derived Causal Diagrams: Evaluating intermediate causal graphs and representations is critical to ensuring that agent-driven forecasting modifications are methodologically sound and reliable for enterprise decision-making.

## Links

- [Abstract](https://arxiv.org/abs/2608.03339)
- [PDF](https://arxiv.org/pdf/2608.03339)

