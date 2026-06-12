---
# CSL-compatible fields
title: "Toward Proactive RF Charging Scheduling: Generative AI for Decision Support"
author:
  - literal: "Amirhossein Azarbahram"
  - literal: "Osmel M. Rosabal"
  - literal: "David E. Ruíz‐Guirola"
  - literal: "Melike Erol‐Kantarci"
  - literal: "Kaibin Huang"
  - literal: "Onel L. A. Lopez"
issued:
  date-parts:
    - [2026, 6, 9]
url: "https://arxiv.org/abs/2606.10600"

# Custom fields
paper_id: "2606.10600"
paper_source: "openalex"
domain: "reinforcement-learning"
tags:
  - "generative-model"
  - "reinforcement-learning"
  - "uncertainty-aware"
  - "resource-allocation"
  - "decision-support"
architectures:
  []
datasets:
  []
concept_slugs:
  - "generative-uncertainty-aware-decision-support"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-12T08:55:12Z"
created_at: "2026-06-12T08:55:12Z"
---

# Toward Proactive RF Charging Scheduling: Generative AI for Decision Support

**Authors**: Amirhossein Azarbahram, Osmel M. Rosabal, David E. Ruíz‐Guirola, Melike Erol‐Kantarci, Kaibin Huang, Onel L. A. Lopez
**Date**: 2026-06-09
**Paper ID**: [openalex:2606.10600](https://arxiv.org/abs/2606.10600)

## Summary

This paper addresses the resource allocation challenge in large-scale radio frequency wireless power transfer (RF-WPT) systems. By integrating generative AI as an uncertainty-aware support layer, the authors enable schedulers to better account for incomplete information and stochastic charging conditions. A warehouse-style case study demonstrates that leveraging the sampling capabilities of generative models improves the robustness of charging decisions compared to deterministic forecasting.

## Key Contributions

- Introduced a GenAI-based support layer for RF wireless power transfer scheduling that provides uncertainty-aware scenario inputs for decision-making.
- Demonstrated through a warehouse-style case study that sampling-based generative uncertainty quantification outperforms deterministic and heuristic baselines in risk-sensitive charging environments.
- Identified key open challenges and architectural directions for integrating generative models into industrial resource scheduling systems.

## Open Questions & Future Work

- [[scenario-processing-efficiency-for-scheduling]]

## Key Concepts

- [[generative-uncertainty-aware-decision-support]]: A framework where generative models serve as an uncertainty-capturing support layer providing scenario-based inputs for downstream resource allocation agents.

## Archivist Review

I approved the overarching mechanism of 'generative uncertainty-aware decision support' because it is a reusable paradigm for bridging generative models with downstream schedulers. I rejected the more domain-specific concepts and questions, focusing instead on the high-level bottleneck of scenario processing efficiency for scheduling, which is a fundamental research problem in time-series decision support. I maintained a strict adherence to the limit of two concepts and two questions.

### Approved Concepts
- Generative Uncertainty-Aware Decision Support: The conceptual decoupling of GenAI as an uncertainty-capturing 'scenario generator' from the decision-making scheduler provides a modular architecture for resource allocation tasks.

### Approved Open Questions
- Scenario Processing Efficiency for Scheduling: The 'curse of dimensionality' in scenario space is a primary bottleneck for deploying generative-AI-assisted scheduling in real-time environments.

### Rejected Candidates
- [concept] Generative AI Decision Support for RF-WPT (`generative-ai-decision-support-for-rf-wpt`) - not_reusable: The concept is overly specific to RF-WPT; I have generalized it to be more reusable.
- [open_question] Cross-Layer Physical Integration (`cross-layer-integration-rf-wpt`) - not_novel: This is essentially a call for general physics-informed control integration, which is a broad theme in the vault, and it is too specific to RF-WPT.

## Links

- [Abstract](https://arxiv.org/abs/2606.10600)
- [PDF](https://arxiv.org/pdf/2606.10600)

