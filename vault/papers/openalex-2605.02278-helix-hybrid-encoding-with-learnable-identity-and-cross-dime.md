---
# CSL-compatible fields
title: "HELIX: Hybrid Encoding with Learnable Identity and Cross-dimensional Synthesis for Time Series Imputation"
author:
  - literal: "Fengming Zhang"
  - literal: "Wenjie Du"
  - literal: "Huan Zhang"
  - literal: "Ke Yu"
  - literal: "Shen Qu"
issued:
  date-parts:
    - [2026, 5, 4]
url: "https://arxiv.org/abs/2605.02278"

# Custom fields
paper_id: "2605.02278"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "attention-mechanism"
architectures:
  []
datasets:
  []
concept_slugs:
  - "learnable-feature-identity"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-07T07:37:06Z"
created_at: "2026-05-07T07:37:06Z"
---

# HELIX: Hybrid Encoding with Learnable Identity and Cross-dimensional Synthesis for Time Series Imputation

**Authors**: Fengming Zhang, Wenjie Du, Huan Zhang, Ke Yu, Shen Qu
**Date**: 2026-05-04
**Paper ID**: [openalex:2605.02278](https://arxiv.org/abs/2605.02278)

## Summary

HELIX is a novel time series imputation framework that addresses the inconsistency of attention-based models by introducing learnable feature identities as persistent semantic anchors. By combining these identities with a hybrid temporal-feature attention mechanism, the model learns arbitrary, end-to-end feature dependencies without relying on predefined topologies. Extensive evaluation across 16 baselines and 5 datasets confirms that HELIX achieves state-of-the-art performance by effectively translating learned cross-feature structures into improved imputation accuracy.

## Key Contributions

- Proposes HELIX, a hybrid encoding framework for time series imputation that integrates learnable feature identities with hybrid temporal-feature attention.
- Achieves state-of-the-art imputation performance, consistently outperforming 16 baselines across 5 diverse datasets and 21 experimental settings.
- Mechanistically demonstrates that the proposed architecture progressively aligns learned feature identities and dependencies with latent physical and semantic structures.

## Key Concepts

- [[learnable-feature-identity]]: A persistent embedding assigned to each time series feature that captures its intrinsic semantic properties and maintains representational consistency across layers.

## Archivist Review

I approved the 'Learnable Feature Identity' concept as it represents a distinct and reusable mechanism for maintaining representational consistency in multi-variate time series models. Other framework-level components were rejected as they are implementation-specific to this particular architecture. No open questions or datasets met the rigorous criteria for permanent inclusion.

### Approved Concepts
- Learnable Feature Identity: Provides a persistent representation anchor across network layers to maintain consistent feature relationships, addressing a limitation of standard attention.

### Rejected Candidates
- [concept] HELIX Framework (`helix-framework`) - subcomponent_of_broader_mechanism: The framework is a specific implementation of the learnable feature identity concept and is not independently reusable.

## Links

- [Abstract](https://arxiv.org/abs/2605.02278)
- [PDF](https://arxiv.org/pdf/2605.02278)

