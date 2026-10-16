---
# CSL-compatible fields
title: "PING: physics informed graph neural network for advection-diffusion processes with applications to solar power forecasting"
author:
  - literal: "Jelena Simeunović"
  - literal: "Baptiste Schubnel"
  - literal: "Pierre-Jean Alet"
  - literal: "Pascal Frossard B"
  - literal: "Rafael E. Carrillo"
issued:
  date-parts:
    - [2026, 10, 13]
url: "https://arxiv.org/abs/2610.18280"

# Custom fields
paper_id: "2610.18280"
paper_source: "openalex"
domain: "time-series"
tags:
  - "graph-neural-network"
  - "forecasting"
  - "time-series"
  - "multimodal"
architectures:
  []
datasets:
  []
concept_slugs:
  - "physics-informed-graph-neural-network"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-16T09:23:54Z"
created_at: "2026-10-16T09:23:54Z"
---

# PING: physics informed graph neural network for advection-diffusion processes with applications to solar power forecasting

**Authors**: Jelena Simeunović, Baptiste Schubnel, Pierre-Jean Alet, Pascal Frossard B, Rafael E. Carrillo
**Date**: 2026-10-13
**Paper ID**: [openalex:2610.18280](https://arxiv.org/abs/2610.18280)

## Summary

The authors propose PING, a Physics-Informed Graph Neural Network for forecasting advection-diffusion processes on irregular spatial grids by framing particle dynamics as graph signals. The model integrates a discretized advection-diffusion equation as a soft loss constraint to guarantee physical consistency. Evaluated on sea surface temperature, cloud index, and solar power datasets, PING achieves state-of-the-art accuracy while successfully fusing satellite and ground station data for intra-day photovoltaic forecasting.

## Key Contributions

- Introduces a Physics-Informed Graph Neural Network (PING) that models advection-diffusion particle transport on irregular sensor networks using graph signal processing.
- Incorporates a discretized advection-diffusion equation as a soft constraint in the loss function to ensure physically consistent forecasting solutions.
- Demonstrates competitive performance against state-of-the-art models on synthetic, sea surface temperature, and cloud index transport datasets.
- Couples PING with PV power production forecasting models, successfully fusing ground sensor data and satellite imagery to improve intra-day solar power prediction.

## Open Questions & Future Work

- [[3d-multilayer-advection-diffusion-graph-networks]]

## Key Concepts

- [[physics-informed-graph-neural-network]]: A graph neural network incorporating discretized advection-diffusion equations as soft constraints in the loss function for physically consistent spatial-temporal forecasting.

## Archivist Review

Approved the core concept of physics-informed graph neural networks for transport phenomena and the open question regarding multi-layer 3D advection-diffusion modeling. No new datasets met the strict reuse bar.

### Approved Concepts
- Physics-Informed Graph Neural Network: Core architectural contribution combining graph neural networks with physical constraints for advection-diffusion processes on irregular grids.

### Approved Open Questions
- 3D Multi-Layer Advection-Diffusion Modeling: Real-world transport phenomena such as cloud dynamics and weather patterns possess significant vertical structure and multi-layer interactions that cannot be fully captured by 2D horizontal approximations.

## Links

- [Abstract](https://arxiv.org/abs/2610.18280)
- [PDF](https://arxiv.org/pdf/2610.18280)

