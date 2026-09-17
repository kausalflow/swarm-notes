---
# CSL-compatible fields
title: "STHMoE: Hypergraph-Enhanced Heterogeneous Dependency Coordination for LLM-Based Urban Traffic Data Forecasting"
author:
  - literal: "Jiawen Chen"
  - literal: "Qi Shao"
  - literal: "Yongjian Chang"
  - literal: "Mingtong Zhou"
  - literal: "Duxin Chen"
  - literal: "Wenwu Yu"
issued:
  date-parts:
    - [2026, 9, 14]
url: "https://arxiv.org/abs/2609.15172"

# Custom fields
paper_id: "2609.15172"
paper_source: "openalex"
domain: "time-series"
tags:
  - "llm"
  - "language-model"
  - "time-series"
  - "forecasting"
  - "graph-neural-network"
  - "mixture-of-experts"
  - "moe"
  - "spatial-attention"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "sthmoe"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:44:32Z"
created_at: "2026-09-17T09:44:32Z"
---

# STHMoE: Hypergraph-Enhanced Heterogeneous Dependency Coordination for LLM-Based Urban Traffic Data Forecasting

**Authors**: Jiawen Chen, Qi Shao, Yongjian Chang, Mingtong Zhou, Duxin Chen, Wenwu Yu
**Date**: 2026-09-14
**Paper ID**: [openalex:2609.15172](https://arxiv.org/abs/2609.15172)

## Summary

Spatio-temporal urban traffic forecasting remains challenging due to complex heterogeneous, non-stationary, and structurally dynamic patterns that existing models struggle to coordinate. To solve this, the authors propose STHMoE, a Spatio-Temporal Hypergraph-Enhanced Mixture of Experts framework built upon a partially frozen large language model backbone. STHMoE decouples traffic dynamics into frequency, time, space, and higher-order spatial representations handled by prompt-guided heterogeneous experts, coordinated via an entropy-aware MoE router and adaptive hypergraph module. Experiments across multiple real-world traffic benchmarks demonstrate strong performance against existing spatio-temporal and LLM-based baselines.

## Key Contributions

- Introduces STHMoE, a spatio-temporal hypergraph-enhanced mixture of experts framework for urban traffic data forecasting.
- Decouples traffic dynamics into frequency-domain, time-domain, spatio-domain, and higher-order spatial representations modeled by prompt-guided heterogeneous experts on a frozen LLM backbone.
- Employs an adaptive hypergraph module and entropy-aware MoE router with coefficient-of-variation load balancing to jointly learn graph dependencies and higher-order group interactions without predefined topologies.

## Open Questions & Future Work

- [[efficient-routing-and-interpretable-expert-specialization]]

## Key Concepts

- [[sthmoe]]: A spatio-temporal hypergraph-enhanced mixture of experts framework for urban traffic forecasting using prompt-guided heterogeneous experts.

## Archivist Review

Approved the overarching STHMoE framework concept and an open question addressing efficient routing and expert specialization in spatio-temporal mixture-of-experts models. Rejected internal subcomponents and unnamed multi-benchmark evaluations to keep the vault concise and strictly adhere to the scarcity policy.

### Approved Concepts
- STHMoE: It is the core model architecture introduced in the paper for urban traffic forecasting.

### Approved Open Questions
- Efficient Routing and Interpretable Expert Specialization: Highlights concrete methodological directions for advancing mixture-of-experts and LLM-based spatio-temporal forecasting architectures beyond current limitations.

### Rejected Candidates
- [concept] Prompt-Guided Heterogeneous Experts (`prompt-guided-heterogeneous-experts`) - subcomponent_of_broader_mechanism: Subcomponent of the broader STHMoE framework mechanism and does not warrant a separate vault entry.

## Links

- [Abstract](https://arxiv.org/abs/2609.15172)
- [PDF](https://arxiv.org/pdf/2609.15172)

