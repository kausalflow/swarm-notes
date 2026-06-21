---
# CSL-compatible fields
title: "TelcoAgent: A Scalable 5G Multi-KPM Forecasting With 3GPP-Grounded Explainability"
author:
  - literal: "Geon Kim"
  - literal: "Dara Ron"
  - literal: "Sukhdeep Singh"
  - literal: "Suyog Moogi"
  - literal: "Pranshav Gajjar"
  - literal: "V V N K Someswara Rao Koduri"
  - literal: "Een Kee Hong"
  - literal: "Vijay K. Shah"
issued:
  date-parts:
    - [2026, 6, 18]
url: "https://arxiv.org/abs/2606.19821"

# Custom fields
paper_id: "2606.19821"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "time-series"
  - "forecasting"
  - "agent"
  - "knowledge-graph"
  - "zero-shot-learning"
  - "explainability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "telcoagent-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-21T08:53:36Z"
created_at: "2026-06-21T08:53:36Z"
---

# TelcoAgent: A Scalable 5G Multi-KPM Forecasting With 3GPP-Grounded Explainability

**Authors**: Geon Kim, Dara Ron, Sukhdeep Singh, Suyog Moogi, Pranshav Gajjar, V V N K Someswara Rao Koduri, Een Kee Hong, Vijay K. Shah
**Date**: 2026-06-18
**Paper ID**: [openalex:2606.19821](https://arxiv.org/abs/2606.19821)

## Summary

TelcoAgent is a foundation model-based framework designed for scalable, zero-shot forecasting of Key Performance Measurements (KPMs) in 5G telecommunication networks. It utilizes a three-agent pipeline to build a 3GPP-grounded knowledge graph, facilitating explainable diagnostics alongside time-series predictions. Evaluated on a city-scale, real-world 5G dataset, the framework achieves high predictive accuracy across multiple KPMs while providing actionable insights for network management without the need for site-specific retraining.

## Key Contributions

- Introduces TelcoAgent, a foundation model framework enabling zero-shot, multi-KPM forecasting without site-specific model training.
- Develops an automated three-agent pipeline that extracts and structures network domain knowledge directly from 3GPP technical specifications.
- Provides a reasoning and explanation module that generates actionable, domain-grounded diagnostic insights for 5G network degradations.
- Demonstrates scalability and accuracy across 200 city-scale 5G cells using 3 months of operational KPM data.

## Open Questions & Future Work

- [[spatiotemporal-context-integration]]

## Key Concepts

- [[telcoagent-framework]]: A foundation model-based framework for scalable, zero-shot, and explainable 5G Key Performance Measurement (KPM) forecasting across diverse network cells.

## Archivist Review

I approved the TelcoAgent framework as a novel pattern for domain-grounded forecasting and the open question regarding spatiotemporal context as a critical architectural bottleneck for telecommunications forecasting. I rejected the proposal to expand knowledge graphs as it constitutes routine future work rather than an unresolved research challenge.

### Approved Concepts
- TelcoAgent Framework: It introduces a unified foundation model approach to 5G network KPM forecasting, shifting from site-specific training to zero-shot, multi-KPM prediction grounded in 3GPP standards.

### Approved Open Questions
- Integrating Spatiotemporal Network Context: Integrating neighboring cell context is essential for achieving truly proactive and adaptive network management in dense 5G deployments where performance issues are spatially correlated.

### Rejected Candidates
- [open_question] Expanding 3GPP Knowledge Graphs (`expanding-3gpp-knowledge-graphs`) - low_impact: This is boilerplate future work regarding data/knowledge base expansion rather than an architectural or scientific bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2606.19821)
- [PDF](https://arxiv.org/pdf/2606.19821)

