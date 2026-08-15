---
# CSL-compatible fields
title: "DLESyM-Ocean: A Deep Learning Probabilistic Global Model for Simulating Present-Day Upper Ocean and Sea Ice"
author:
  - literal: "Zachary I. Espinosa"
  - literal: "Nathaniel Cresswell‐Clay"
  - literal: "William Yik"
  - literal: "Cecilia M. Bitz"
  - literal: "Edward Blanchard‐Wrigglesworth"
  - literal: "Peter Harrington"
  - literal: "David Pruitt"
  - literal: "Michael S. Pritchard"
  - literal: "Dale R. Durran"
issued:
  date-parts:
    - [2026, 8, 12]
url: "https://arxiv.org/abs/2608.11545"

# Custom fields
paper_id: "2608.11545"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "patch-energy-score-loss"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-15T05:15:39Z"
created_at: "2026-08-15T05:15:39Z"
---

# DLESyM-Ocean: A Deep Learning Probabilistic Global Model for Simulating Present-Day Upper Ocean and Sea Ice

**Authors**: Zachary I. Espinosa, Nathaniel Cresswell‐Clay, William Yik, Cecilia M. Bitz, Edward Blanchard‐Wrigglesworth, Peter Harrington, David Pruitt, Michael S. Pritchard, Dale R. Durran
**Date**: 2026-08-12
**Paper ID**: [openalex:2608.11545](https://arxiv.org/abs/2608.11545)

## Summary

DLESyM-Ocean is a deep learning probabilistic global Earth system model designed to simulate present-day upper ocean and sea ice conditions under atmospheric forcing. Trained using a patch energy score loss instead of standard diffusion or CRPS objectives, it generates stable, well-calibrated, and multi-year autoregressive forecasts with minimal bias. Case studies demonstrate its ability to capture extreme events, marine heatwaves, and climate transitions while maintaining high computational efficiency for subseasonal to seasonal forecasting.

## Key Contributions

- DLESyM-Ocean simulates global present-day sea ice and upper ocean conditions stably over multi-year autoregressive runs when driven by atmospheric forcing.
- Optimized via a patch energy score loss rather than standard diffusion objectives or CRPS losses to yield well-calibrated and spatially coherent ensembles.
- Accurately captures complex ocean dynamics and variability across case studies including sea ice extremes, marine heatwaves, the 2023 El Niño transition, and global temperature spikes.

## Open Questions & Future Work

- [[fully-coupled-ai-earth-system-modeling]]

## Key Concepts

- [[patch-energy-score-loss]]: A training loss designed for probabilistic Earth system models to ensure spatial coherence and well-calibrated ensemble simulations.

## Archivist Review

Approved the central training loss concept and the core open question regarding fully coupled AI earth system modeling, ensuring high selectivity and strict compliance with review standards.

### Approved Concepts
- Patch Energy Score Loss: Serves as the core training objective enabling DLESyM-Ocean to produce well-calibrated and spatially coherent ensembles without standard diffusion or CRPS losses.

### Approved Open Questions
- Fully Coupled AI Earth System Modeling: Transitioning from forced ocean simulations to fully coupled interactive Earth system models is critical for operational subseasonal-to-seasonal forecasting and climate projections using artificial intelligence.

## Links

- [Abstract](https://arxiv.org/abs/2608.11545)
- [PDF](https://arxiv.org/pdf/2608.11545)

