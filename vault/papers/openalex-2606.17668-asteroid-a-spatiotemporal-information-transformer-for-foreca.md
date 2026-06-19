---
# CSL-compatible fields
title: "ASTEROID: A Spatiotemporal Information Transformer for Forecasting Multi-Step Time Series of Molecular Dynamics"
author:
  - literal: "Kexin Wu"
  - literal: "Luonan Chen"
  - literal: "Renxiao Wang"
issued:
  date-parts:
    - [2026, 6, 16]
url: "https://arxiv.org/abs/2606.17668"

# Custom fields
paper_id: "2606.17668"
paper_source: "openalex"
domain: "biology"
tags:
  - "transformer"
  - "self-attention"
  - "time-series"
  - "forecasting"
  - "llm"
architectures:
  []
datasets:
  []
concept_slugs:
  - "spatiotemporal-information-sti-transformation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-19T09:24:13Z"
created_at: "2026-06-19T09:24:13Z"
---

# ASTEROID: A Spatiotemporal Information Transformer for Forecasting Multi-Step Time Series of Molecular Dynamics

**Authors**: Kexin Wu, Luonan Chen, Renxiao Wang
**Date**: 2026-06-16
**Paper ID**: [openalex:2606.17668](https://arxiv.org/abs/2606.17668)

## Summary

ASTEROID is a data-driven framework designed to accelerate molecular dynamics (MD) simulations by predicting multi-step atomic coordinates directly, bypassing traditional iterative integration. The model reconfigures MD trajectories as high-dimensional spatiotemporal sequences and integrates a Spatiotemporal Information (STI) Transformation equation into a Transformer architecture. By utilizing a local-global self-attention mechanism and an encoder-decoder structure, ASTEROID effectively captures multiscale dependencies, achieving superior forecasting accuracy and lower computational costs on quantum-mechanics derived benchmarks.

## Key Contributions

- Introduces ASTEROID, a Transformer-based framework that predicts multi-step atomic coordinates directly to accelerate molecular dynamics (MD) simulations.
- Implements a local-global self-attention mechanism to capture multi-scale spatial interactions and an encoder-decoder architecture for temporal forecasting.
- Demonstrates significant accuracy improvements and computational cost reduction over conventional iterative integration methods across quantum-mechanics derived molecular datasets.

## Key Concepts

- [[spatiotemporal-information-sti-transformation]]: A transformation integrated into a Transformer to model complex dynamics as spatiotemporal sequences.

## Archivist Review

The ASTEROID framework is primarily a model-specific architecture for molecular dynamics; however, the Spatiotemporal Information (STI) Transformation is a sufficiently defined mathematical paradigm for representing spatiotemporal dynamics that warrants a permanent vault note for its potential in future sequence modeling research. Other candidates were rejected for being model-specific or redundant within the existing vault architecture.

### Approved Concepts
- Spatiotemporal Information (STI) Transformation: Core mathematical innovation for mapping molecular dynamics trajectories into a neural-friendly spatiotemporal representation.

### Rejected Candidates
- [concept] ASTEROID Framework (`asteroid-framework`) - paper_local: ASTEROID is the specific name of the model proposed in the paper, which functions as an overarching framework rather than a general, reusable concept.
- [concept] Local-Global Self-Attention (`local-global-self-attention`) - not_novel: This is a common architectural pattern already covered by broader concepts like attention and multi-scale modeling.

## Links

- [Abstract](https://arxiv.org/abs/2606.17668)
- [PDF](https://arxiv.org/pdf/2606.17668)

