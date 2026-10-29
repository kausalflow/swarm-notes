---
# CSL-compatible fields
title: "GNN-VIEW: Visual Inspection and Explanation of Graph-based Earth-System Models"
author:
  - literal: "Alessandro Lucatelli"
  - literal: "Ferdinand Unterhuber"
  - literal: "Katharina Krenzer"
  - literal: "Mennatallah El‐Assady"
  - literal: "Benedikt Soja"
  - literal: "Christina Humer"
  - literal: "Joel Oskarsson"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2610.35693"

# Custom fields
paper_id: "2610.35693"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "graph-neural-network"
  - "gnn"
  - "explainability"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-29T11:11:22Z"
created_at: "2026-10-29T11:11:22Z"
---

# GNN-VIEW: Visual Inspection and Explanation of Graph-based Earth-System Models

**Authors**: Alessandro Lucatelli, Ferdinand Unterhuber, Katharina Krenzer, Mennatallah El‐Assady, Benedikt Soja, Christina Humer, Joel Oskarsson
**Date**: 2026-10-26
**Paper ID**: [openalex:2610.35693](https://arxiv.org/abs/2610.35693)

## Summary

Graph-based machine learning models are widely used in Earth-system forecasting, but understanding their connectivity and post-training predictions remains difficult. This paper introduces GNN-VIEW, an interactive browser-based visualization tool designed to inspect and debug graph information pathways prior to training. Additionally, it leverages attribution-based explainability to help developers analyze how trained models generate forecasts and diagnose failures, such as during extreme weather events.

## Key Contributions

- Introduces GNN-VIEW, an interactive browser-based visualization and explanation tool for graph-based Earth-system models.
- Exposes graph information pathways to allow developers to debug and inspect graph connectivity prior to training.
- Integrates attribution-based explainability to reveal input feature usage and debug failure modes in trained weather and ocean forecasting models.

## Archivist Review

The paper introduces GNN-VIEW, an interactive visualization and explanation tool for graph-based Earth-system models. Neither the visualization software framework nor the candidate open questions meet the stringent reusability, standalone importance, and methodological depth requirements for permanent vault notes.

### Rejected Candidates
- [open_question] Structure-Aware Explainers for GNNs (`structure-aware-gnn-explainers`) - low_impact: This open question is a fairly broad future work suggestion about combining GNN explanations with graph structures rather than a sharp, technically bounded methodological bottleneck.
- [open_question] Explainability of Forecast Rollouts and Ensembles (`explainability-forecast-rollouts-ensembles`) - low_impact: This is standard boilerplate future work suggesting the extension of attribution methods to rollout ensembles, lacking a specific methodological formulation.

## Links

- [Abstract](https://arxiv.org/abs/2610.35693)
- [PDF](https://arxiv.org/pdf/2610.35693)

