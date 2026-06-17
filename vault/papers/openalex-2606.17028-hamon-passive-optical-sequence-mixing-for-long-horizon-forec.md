---
# CSL-compatible fields
title: "HAMON: Passive Optical Sequence Mixing for Long-Horizon Forecasting"
author:
  - literal: "Alper Yıldırım"
issued:
  date-parts:
    - [2026, 6, 15]
url: "https://arxiv.org/abs/2606.17028"

# Custom fields
paper_id: "2606.17028"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "long-context"
architectures:
  []
datasets:
  []
concept_slugs:
  - "passive-optical-sequence-mixing"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-17T09:25:44Z"
created_at: "2026-06-17T09:25:44Z"
---

# HAMON: Passive Optical Sequence Mixing for Long-Horizon Forecasting

**Authors**: Alper Yıldırım
**Date**: 2026-06-15
**Paper ID**: [openalex:2606.17028](https://arxiv.org/abs/2606.17028)

## Summary

This paper investigates whether time-series forecasting, which often relies on simple linear or frequency-domain operations, can be offloaded from digital circuits to passive optical hardware. The authors introduce HAMON, a diffractive optical forecasting core that encodes input historical sequences onto an aperture and uses cascaded phase masks to generate forecasts via light diffraction. Experimental results show that this passive, zero-compute-inference approach is highly competitive with state-of-the-art digital models on several ETT benchmarks, challenging the necessity of digital sequence-mixing layers for specific time-series tasks.

## Key Contributions

- Introduces HAMON, a diffractive optical forecasting architecture that replaces digital sequence mixing with passive physical light propagation.
- Demonstrates that passive optical propagation can perform high-fidelity long-horizon forecasting, achieving up to 14% MSE improvement over strong digital baselines on ETTm2.
- Establishes a rigorous methodology for evaluating physically encoded sequence models using TorchOptics cross-simulations and phase-encoding ablations.

## Open Questions & Future Work

- [[experimental-hardware-validation-of-diffractive-forecasting]]

## Key Concepts

- [[passive-optical-sequence-mixing]]: A forecasting paradigm that performs temporal sequence mixing via passive diffractive optics instead of digital compute layers.

## Archivist Review

I approved 'Passive Optical Sequence Mixing' as it provides a novel, hardware-centric paradigm for forecasting that is distinct from existing digital attention or linear mechanisms. I also approved the open question regarding the physical realization of this architecture, as this gap represents the primary bottleneck for the technology's practical adoption. Standard benchmarks like ETT and Traffic were rejected as they are routine and not unique to this specific contribution.

### Approved Concepts
- Passive Optical Sequence Mixing: It shifts the paradigm of time-series forecasting from digital matrix operations to passive physical light propagation, offering a path toward zero-compute inference.

### Approved Open Questions
- Hardware validation of optical forecasting: Validating the physical realization is essential to proving the viability of passive optics as a substitute for digital sequence mixing layers in time-series forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2606.17028)
- [PDF](https://arxiv.org/pdf/2606.17028)

