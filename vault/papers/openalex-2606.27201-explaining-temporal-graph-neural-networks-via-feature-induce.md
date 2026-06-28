---
# CSL-compatible fields
title: "Explaining Temporal Graph Neural Networks via Feature-induced Information Flow"
author:
  - literal: "Ping Xiong"
  - literal: "Thomas Schnake"
  - literal: "Klaus-Robert Müller"
  - literal: "Shinichi Nakajima"
issued:
  date-parts:
    - [2026, 6, 25]
url: "https://arxiv.org/abs/2606.27201"

# Custom fields
paper_id: "2606.27201"
paper_source: "openalex"
domain: "nlp"
tags:
  - "graph-neural-network"
  - "explainability"
  - "information-extraction"
architectures:
  []
datasets:
  []
concept_slugs:
  - "feature-induced-information-flow"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-28T08:17:11Z"
created_at: "2026-06-28T08:17:11Z"
---

# Explaining Temporal Graph Neural Networks via Feature-induced Information Flow

**Authors**: Ping Xiong, Thomas Schnake, Klaus-Robert Müller, Shinichi Nakajima
**Date**: 2026-06-25
**Paper ID**: [openalex:2606.27201](https://arxiv.org/abs/2606.27201)

## Summary

This paper addresses the explainability challenges of Event-based Temporal Graph Neural Networks (ETGNNs) by introducing a novel attribution method focused on the complete information flow within the network. By extending the Normalized Relevance Measure (NRM) framework with a modular decomposition procedure, the approach accounts for event-induced variables that mediate node interactions, which are often overlooked by conventional methods. The method enables better quantification of event-based contributions and higher-order interaction analysis, resulting in more human-interpretable explanations compared to existing techniques. Experimental results confirm the effectiveness of this approach across various synthetic and real-world event-based graph scenarios.

## Key Contributions

- Introduces an attribution method that captures the complete information flow in Event-based Temporal Graph Neural Networks (ETGNNs).
- Extends the Normalized Relevance Measure (NRM) framework with a modular decomposition procedure to support complex, hierarchical neural architectures.
- Demonstrates superior explanation quality and performance against baseline attribution methods on synthetic and real-world political event network datasets.

## Open Questions & Future Work

- [[automated-relevance-structure-construction]]

## Key Concepts

- [[feature-induced-information-flow]]: An attribution framework for ETGNNs that tracks information propagation through both event embeddings and event-induced latent variables.

## Archivist Review

The paper proposes a novel attribution method for temporal graph neural networks by analyzing the full information flow including induced variables. I approved the core conceptual framework of feature-induced information flow and the identified bottleneck regarding automated relevance structure construction for complex neural models. No datasets were approved as they were synthetic or not central enough to the broader research field to warrant standalone vault status.

### Approved Concepts
- Feature-induced Information Flow: Addresses a critical gap in ETGNN explainability by accounting for event-induced pathways that mediate node interactions.

### Approved Open Questions
- Automated Relevance Structure Construction: As neural network architectures become increasingly complex and modular, the manual derivation of layer-wise relevance propagation rules for every component becomes a significant bottleneck for deploying robust explainability tools. Automating this process is essential for scaling XAI methods to deeper and more heterogeneous graph-based models.

## Links

- [Abstract](https://arxiv.org/abs/2606.27201)
- [PDF](https://arxiv.org/pdf/2606.27201)

