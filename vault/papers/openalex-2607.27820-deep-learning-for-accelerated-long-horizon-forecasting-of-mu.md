---
# CSL-compatible fields
title: "Deep Learning for Accelerated Long-Horizon Forecasting of Multicomponent Multiphase Microstructure Evolution in High-Entropy Alloys"
author:
  - literal: "Hamidreza Razavi"
  - literal: "Nele Moelans"
issued:
  date-parts:
    - [2026, 7, 30]
url: "https://arxiv.org/abs/2607.27820"

# Custom fields
paper_id: "2607.27820"
paper_source: "openalex"
domain: "materials-science"
tags:
  - "time-series"
  - "forecasting"
  - "long-context"
  - "graph-neural-network"
  - "convolutional-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-02T07:27:07Z"
created_at: "2026-08-02T07:27:07Z"
---

# Deep Learning for Accelerated Long-Horizon Forecasting of Multicomponent Multiphase Microstructure Evolution in High-Entropy Alloys

**Authors**: Hamidreza Razavi, Nele Moelans
**Date**: 2026-07-30
**Paper ID**: [openalex:2607.27820](https://arxiv.org/abs/2607.27820)

## Summary

This paper presents an AE-GCN-LSTM surrogate modeling framework designed to accelerate long-horizon forecasting of multicomponent and multiphase microstructure evolution in high-entropy alloys. By coupling a multi-head autoencoder with graph convolutional networks and LSTMs, the model captures spatial and temporal evolution from phase-field simulations. The framework successfully predicts up to 3,000,000 simulation timesteps across diverse unseen initial conditions, larger spatial domains, and alloy compositions, achieving computational speedups between 7,200x and 62,300x compared to traditional phase-field methods.

## Key Contributions

- Introduces an AE-GCN-LSTM surrogate framework combining a multi-head autoencoder, graph convolutional networks, and LSTMs for long-horizon microstructure evolution forecasting.
- Achieves long-horizon forecasting extending to 3,000,000 simulation timesteps for the multicomponent AlCrFeNi high-entropy alloy system with coexisting BCC and FCC phases.
- Demonstrates generalization to unseen conditions including larger spatial domains (256x256 and 512x512), varying precipitate counts/sizes, complex phase interactions, and unseen alloy compositions without retraining.
- Provides massive computational speedups ranging from approximately 7,200x to 62,300x relative to conventional phase-field simulations.

## Archivist Review

Evaluated the candidate open question against vault standards and rejected it as standard domain extension future work without a specific theoretical bottleneck. No concepts or datasets were submitted or approved.

### Rejected Candidates
- [open_question] Generalization to Other Material Systems (`generalize-surrogate-to-other-materials`) - low_impact: Standard domain extension future work that lacks a specific algorithmic or theoretical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2607.27820)
- [PDF](https://arxiv.org/pdf/2607.27820)

