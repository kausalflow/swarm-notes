---
# CSL-compatible fields
title: "Adaptive Group-Based Counterfactual Explanations for Time-Series Rehabilitation Data"
author:
  - literal: "Emmanuel C. Chukwu"
  - literal: "Rianne M. Schouten"
  - literal: "Monique Tabak"
  - literal: "Mykola Pechenizkiy"
issued:
  date-parts:
    - [2026, 7, 2]
url: "https://arxiv.org/abs/2607.01838"

# Custom fields
paper_id: "2607.01838"
paper_source: "openalex"
domain: "nlp"
tags:
  - "interpretability"
  - "time-series"
  - "explainability"
architectures:
  []
datasets:
  - "kne-e-pad-dataset"
concept_slugs:
  - "learnable-gate-lg-methods"
dataset_slugs:
  - "kne-e-pad-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-07-05T07:52:09Z"
created_at: "2026-07-05T07:52:09Z"
---

# Adaptive Group-Based Counterfactual Explanations for Time-Series Rehabilitation Data

**Authors**: Emmanuel C. Chukwu, Rianne M. Schouten, Monique Tabak, Mykola Pechenizkiy
**Date**: 2026-07-02
**Paper ID**: [openalex:2607.01838](https://arxiv.org/abs/2607.01838)

## Summary

This paper addresses the interpretability challenge of counterfactual explanations (CEs) in high-dimensional time-series data by proposing a two-stage, group-based generation framework. Unlike standard channel-level methods that produce biomechanically incoherent explanations, the proposed approach leverages semantic feature groups, such as muscle segments in IMU-based rehabilitation data. By introducing Learnable Gate (LG) methods to enforce group-level sparsity, the framework provides more concise and clinically relevant corrective guidance while maintaining counterfactual validity and generation efficiency.

## Key Contributions

- Introduces a two-stage framework for generating semantic group-based counterfactuals in multivariate time-series data.
- Proposes Learnable Gate (LG) methods that outperform channel-level baselines in group-level sparsity while maintaining temporal smoothness and counterfactual validity.
- Demonstrates superior clinical alignment for corrective motion guidance compared to traditional channel-level methods on the KneE-PAD dataset.

## Open Questions & Future Work

- [[automated-group-discovery-for-counterfactuals]]

## Key Concepts

- [[learnable-gate-lg-methods]]: A technique using trainable per-group relevance gates jointly optimized with perturbation masks to enforce group-level sparsity in counterfactual generation.

## Archivist Review

I approved the Learnable Gate method as it represents a core, reusable mechanism for group-based sparsity in time-series interpretability. I also approved the open question regarding automated group discovery, as it addresses a fundamental limitation in transitioning these models from manual to automated, scalable applications. The KneE-PAD dataset was approved as a specific clinical benchmark. The Shapley-Adaptive ranking was rejected as it is a baseline component superseded by the Learnable Gate architecture.

### Approved Concepts
- Learnable Gate (LG) Methods: Introduces a flexible architectural approach to enforce group-level sparsity in interpretability tasks, moving beyond channel-level analysis.

### Approved Open Questions
- Automated Group Discovery Strategies: Automating group discovery is essential for transitioning explainable AI frameworks from hand-crafted, study-specific domains to robust, automated tools suitable for varied sensor configurations and clinical settings.

### Rejected Candidates
- [concept] Shapley-Adaptive (SA) group ranking (`shapley-adaptive-sa-group-ranking`) - subcomponent_of_broader_mechanism: This method serves as a baseline comparison and is less central to the primary contribution (the Learnable Gate method) of the paper.

## Datasets

- [[kne-e-pad-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2607.01838)
- [PDF](https://arxiv.org/pdf/2607.01838)

