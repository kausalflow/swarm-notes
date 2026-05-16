---
# CSL-compatible fields
title: "Toward AI-Driven Digital Twins for Metropolitan Floods: A Conditional Latent Dynamics Network Surrogate of the Shallow Water Equations"
author:
  - literal: "Phillip Si"
  - literal: "Yuan Qiu"
  - literal: "Omar Sallam"
  - literal: "Jeremy Feinstein"
  - literal: "Ziang He"
  - literal: "Eugene Yan"
  - literal: "Peng Chen"
issued:
  date-parts:
    - [2026, 5, 13]
url: "https://arxiv.org/abs/2605.13761"

# Custom fields
paper_id: "2605.13761"
paper_source: "openalex"
domain: "science"
tags:
  - "time-series"
  - "forecasting"
  - "neural-ordinary-differential-equations"
  - "physics-informed-machine-learning"
  - "simulation"
architectures:
  []
datasets:
  - "des-plaines-river-basin-dataset"
concept_slugs:
  - "conditional-latent-dynamics-network-cldnet"
dataset_slugs:
  - "des-plaines-river-basin-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-05-16T07:10:23Z"
created_at: "2026-05-16T07:10:23Z"
---

# Toward AI-Driven Digital Twins for Metropolitan Floods: A Conditional Latent Dynamics Network Surrogate of the Shallow Water Equations

**Authors**: Phillip Si, Yuan Qiu, Omar Sallam, Jeremy Feinstein, Ziang He, Eugene Yan, Peng Chen
**Date**: 2026-05-13
**Paper ID**: [openalex:2605.13761](https://arxiv.org/abs/2605.13761)

## Summary

The paper presents the Conditional Latent Dynamics Network (CLDNet), a neural surrogate model designed for rapid flood forecasting at metropolitan scales. By combining a latent neural ODE for temporal dynamics with a coordinate-based, terrain-conditioned decoder, CLDNet avoids the computational overhead of Cartesian grid-based hydrodynamic solvers. Experiments on the Des Plaines River basin demonstrate that the proposed model achieves a 115x speedup over numerical solvers while providing highly accurate water-surface elevation forecasts.

## Key Contributions

- Proposes CLDNet, a latent neural ODE surrogate that accelerates 2D shallow water equation simulations by ~115x compared to standard GPU solvers.
- Introduces coordinate-based decoding conditioned on static terrain, allowing memory-efficient simulations on irregular watershed geometries without grid interpolation.
- Achieves an 86% critical success index on inundation thresholds while halving the relative RMSE of unconditional baselines on metropolitan-scale flood forecasting tasks.

## Limitations

The method is evaluated specifically on shallow water equation surrogates; generalizability to more complex hydrodynamic phenomena (e.g., sediment transport) remains to be demonstrated.

## Open Questions & Future Work

- [[flood-twin-data-assimilation]]
- [[vector-discharge-accuracy]]

## Key Concepts

- [[conditional-latent-dynamics-network-cldnet]]: A low-dimensional latent neural ODE surrogate for shallow water equations that uses coordinate-based decoding conditioned on terrain data to handle irregular domains.

## Archivist Review

I have approved the core CLDNet architecture and two substantial open questions concerning data assimilation and discharge accuracy, as these represent significant challenges for the field of hydrodynamic surrogates. The Des Plaines dataset is approved as a key case study evaluation dataset. The review followed the policy of being highly selective with architectural novelties and substantial research bottlenecks.

### Approved Concepts
- Conditional Latent Dynamics Network (CLDNet): It is the core architectural innovation of the paper, enabling efficient metropolitan-scale hydrodynamic simulation by decoupling memory from grid resolution.

### Approved Open Questions
- Data assimilation for flood twins: This is critical for transitioning from offline hydrodynamic emulation to an operational, observation-coupled digital twin.
- Improving vector discharge prediction: Without accurate discharge predictions, flood models cannot fully inform structural risk assessments that depend on momentum and mass-flux conservation.

## Datasets

- [[des-plaines-river-basin-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2605.13761)
- [PDF](https://arxiv.org/pdf/2605.13761)

