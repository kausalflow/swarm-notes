---
# CSL-compatible fields
title: "AstroSkyFlow: an astronomical sky image flow simulator for time domain survey validation and machine learning"
author:
  - literal: "Kexin Li"
  - literal: "Yicheng Rui"
  - literal: "Fabo Feng"
  - literal: "Shuyue Zheng"
  - literal: "Anton Pomazan"
  - literal: "Yiyang Guo"
  - literal: "Jie Zheng"
  - literal: "Lin-Qiao Jiang"
issued:
  date-parts:
    - [2026, 6, 1]
url: "https://arxiv.org/abs/2606.02140"

# Custom fields
paper_id: "2606.02140"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "dataset"
  - "evaluation"
  - "computer-vision"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-04T08:43:33Z"
created_at: "2026-06-04T08:43:33Z"
---

# AstroSkyFlow: an astronomical sky image flow simulator for time domain survey validation and machine learning

**Authors**: Kexin Li, Yicheng Rui, Fabo Feng, Shuyue Zheng, Anton Pomazan, Yiyang Guo, Jie Zheng, Lin-Qiao Jiang
**Date**: 2026-06-01
**Paper ID**: [openalex:2606.02140](https://arxiv.org/abs/2606.02140)

## Summary

AstroSkyFlow is a modular simulator designed to generate realistic, time-series astronomical sky images for validating survey pipelines and training machine learning models. By modeling the full observing stack, including celestial source variability, atmospheric effects, and sensor response, the tool produces multi-epoch data with high-fidelity noise and PSF properties. The authors demonstrate that the simulator outperforms existing tools like SkyMaker in accuracy and successfully recovers injected signals such as exoplanet transits and asteroid trails.

## Key Contributions

- Introduces AstroSkyFlow, a modular sky-image simulator for generating high-fidelity, time-dependent multi-epoch astronomical data.
- Demonstrates improved accuracy in replicating noise characteristics and PSF properties compared to existing tools like SkyMaker.
- Enables large-scale generation of labeled datasets for training machine learning pipelines and performing injection-recovery validation for time-domain surveys.

## Open Questions & Future Work

- [[astroskyflow-parallelization-throughput]]
- [[psf-model-realism-aberrations]]

## Archivist Review

I have approved the two open questions after minor rephrasing for clarity and encyclopedic tone. No new concepts or datasets were approved, as the proposed simulator is a specific tool rather than a generic concept or widely used dataset, and no specific datasets were put forward for approval. The review maintained strict adherence to the scarcity requirements.

### Approved Open Questions
- Simulator Parallelization and Throughput: As observational data rates in time-domain astronomy accelerate, current simulators—often operating at serial bottlenecks—become a significant limitation for real-time survey validation and automated pipeline development.
- Realistic PSF Aberration Modeling: Underestimation of optical broadening, defocus, and distortions in current simulators hampers the reliability of downstream tasks like source detection, deblending, and signal injection-recovery.

### Rejected Candidates
- [open_question] Parallelization for High Throughput (`astroskyflow-parallelization-throughput`) - other: Renamed to improve clarity and standardize terminology.

## Links

- [Abstract](https://arxiv.org/abs/2606.02140)
- [PDF](https://arxiv.org/pdf/2606.02140)

