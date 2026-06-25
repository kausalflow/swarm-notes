---
# CSL-compatible fields
title: "Topological Out-of-Domain Generalization in Dynamical Systems Reconstruction"
author:
  - literal: "Georg Trede"
  - literal: "Charlotte Ricarda Doll"
  - literal: "Elias Weber"
  - literal: "Daniel Durstewitz"
issued:
  date-parts:
    - [2026, 6, 22]
url: "https://arxiv.org/abs/2606.22969"

# Custom fields
paper_id: "2606.22969"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "zero-shot-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "feature-splitting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-25T08:19:52Z"
created_at: "2026-06-25T08:19:52Z"
---

# Topological Out-of-Domain Generalization in Dynamical Systems Reconstruction

**Authors**: Georg Trede, Charlotte Ricarda Doll, Elias Weber, Daniel Durstewitz
**Date**: 2026-06-22
**Paper ID**: [openalex:2606.22969](https://arxiv.org/abs/2606.22969)

## Summary

This paper addresses the failure of current neural models to perform out-of-domain forecasting in dynamical systems, specifically when crossing tipping points or parameter boundaries. By identifying a mismatch between traditional model architectures and the underlying physics of dynamical systems, the authors pinpoint three critical structural shortcomings. They propose a modified architecture incorporating 'feature splitting' and provide a formal, closed-form bound on the reliable extrapolation range, enabling zero-shot forecasting into unseen regimes.

## Key Contributions

- Identifies three core structural shortcomings in current dynamical systems reconstruction (DSR) models that hinder out-of-domain (OOD) generalization.
- Introduces a feature splitting mechanism that enables zero-shot prediction of dynamical regimes outside the training distribution, including across tipping points.
- Derives a novel, closed-form theoretical bound on the reliable extrapolation range for neural dynamical systems.

## Open Questions & Future Work

- [[nonlinear-scaling-in-discrete-time-dsr]]

## Key Concepts

- [[feature-splitting]]: A structural modification to neural dynamical system reconstruction models that explicitly separates system features to improve out-of-domain generalization.

## Archivist Review

I have approved 'Feature Splitting' as a reusable architectural pattern for dynamical systems reconstruction and 'Nonlinear Scaling in DSR' as a fundamental theoretical open question. The selection follows the review policy to favor overarching mechanisms and substantial research bottlenecks over paper-specific implementation details or boilerplate future work. No datasets were approved as none provided met the stringent criteria for standalone long-lived vault entries.

### Approved Concepts
- Feature Splitting: It addresses the core structural mismatch identified by the authors that prevents zero-shot extrapolation in dynamical system reconstruction.

### Approved Open Questions
- Nonlinear scaling in DSR: This identifies a fundamental mathematical limit of current state-of-the-art DSR models for long-term forecasting and provides a clear theoretical barrier for future model architectures.

## Links

- [Abstract](https://arxiv.org/abs/2606.22969)
- [PDF](https://arxiv.org/pdf/2606.22969)

