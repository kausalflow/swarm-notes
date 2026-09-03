---
# CSL-compatible fields
title: "Uncertainty-Aware Trajectory Forecasting from Imperfect Tracking"
author:
  - literal: "Stephane Da Silva Martins"
  - literal: "Victor Petrovic"
  - literal: "Emanuel Aldea"
  - literal: "Sylvie Le Hégarat-Mascle"
issued:
  date-parts:
    - [2026, 8, 31]
url: "https://arxiv.org/abs/2608.30899"

# Custom fields
paper_id: "2608.30899"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "forecasting"
  - "robustness"
  - "uncertainty-quantification"
  - "knowledge-distillation"
  - "multimodal"
architectures:
  []
datasets:
  []
concept_slugs:
  - "uncertainty-aware-trajectory-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-03T09:17:13Z"
created_at: "2026-09-03T09:17:13Z"
---

# Uncertainty-Aware Trajectory Forecasting from Imperfect Tracking

**Authors**: Stephane Da Silva Martins, Victor Petrovic, Emanuel Aldea, Sylvie Le Hégarat-Mascle
**Date**: 2026-08-31
**Paper ID**: [openalex:2608.30899](https://arxiv.org/abs/2608.30899)

## Summary

This paper addresses the degradation of trajectory forecasting models when deployed with imperfect multi-object tracker outputs rather than clean annotations. The authors propose a plug-in uncertainty-aware formulation that represents observed states as Gaussian distributions combining localization uncertainty and association ambiguity using the law of total variance. To handle structured observation noise during training, they combine Ornstein-Uhlenbeck perturbations with knowledge distillation from a clean-trajectory teacher. Experiments across multiple benchmarks confirm enhanced displacement accuracy and probabilistic forecast reliability.

## Key Contributions

- Proposes an uncertainty-aware trajectory forecasting formulation that models observed states as Gaussian distributions combining detection localization uncertainty and association ambiguity via the law of total variance.
- Adapts existing backbones with minimal architectural changes to ingest Gaussian observations and output probabilistic Gaussian forecasts.
- Combines temporally correlated Ornstein-Uhlenbeck perturbations with response-based knowledge distillation from a clean-data teacher to ensure robustness against structured observation noise.
- Demonstrates improved displacement accuracy and reliability-sharpness trade-offs on Oxford Town Centre, VIRAT, and ETH/UCY using real tracker outputs and pseudo-detection protocols.

## Key Concepts

- [[uncertainty-aware-trajectory-forecasting]]: A trajectory forecasting framework that propagates tracking-derived reliability cues via Gaussian representations combined through the law of total variance.

## Archivist Review

Approved the core overarching concept of uncertainty-aware trajectory forecasting via the law of total variance as a reusable plug-in mechanism for handling tracking noise. Standard evaluation datasets were correctly rejected per vault policies.

### Approved Concepts
- Uncertainty-Aware Trajectory Forecasting: Provides a principled plug-in formulation using the law of total variance to combine localization uncertainty and association ambiguity from imperfect multi-object trackers.

### Rejected Candidates
- [dataset] Oxford Town Centre (`oxford-town-centre`) - not_novel: Standard evaluation dataset rather than a novel contribution.
- [dataset] VIRAT (`virat-dataset`) - not_novel: Standard evaluation dataset rather than a novel contribution.
- [dataset] ETH/UCY (`eth-ucy-dataset`) - not_novel: Standard evaluation dataset rather than a novel contribution.

## Links

- [Abstract](https://arxiv.org/abs/2608.30899)
- [PDF](https://arxiv.org/pdf/2608.30899)

