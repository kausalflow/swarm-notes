---
# CSL-compatible fields
title: "From Surface Forecasting to Observability Forecasting: A Latent World Model for Cloud-Aware EO Monitoring"
author:
  - literal: "Mohanad Albughdadi"
issued:
  date-parts:
    - [2026, 7, 15]
url: "https://arxiv.org/abs/2607.13651"

# Custom fields
paper_id: "2607.13651"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "time-series"
  - "multimodal"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  - "EarthNet2021"
concept_slugs:
  - "observability-forecasting"
dataset_slugs:
  - "earthnet2021"
skill: "TimeSeriesSkill"
processed_at: "2026-07-18T06:52:13Z"
created_at: "2026-07-18T06:52:13Z"
---

# From Surface Forecasting to Observability Forecasting: A Latent World Model for Cloud-Aware EO Monitoring

**Authors**: Mohanad Albughdadi
**Date**: 2026-07-15
**Paper ID**: [openalex:2607.13651](https://arxiv.org/abs/2607.13651)

## Summary

This paper addresses the operational challenge of cloud-obscured Earth Observation imagery by framing it as an observability forecasting task. By adapting a joint-embedding world model (LeWorldModel) to process multispectral imagery and meteorological covariates, the system predicts the usability of future satellite acquisitions. Experimental results on the EarthNet2021 benchmark demonstrate that the model significantly outperforms traditional persistence and statistical baselines in predicting precise usable-view horizons and clear/cloud regression.

## Key Contributions

- Introduces the observability forecasting problem to quantify Earth Observation image usability under cloud cover.
- Adapts a LeWorldModel joint-embedding predictive architecture to integrate multispectral imagery and meteorological covariates for temporal observability modeling.
- Demonstrates significant performance gains over persistence and LightGBM baselines on the EarthNet2021 benchmark, particularly for exact recovery timing prediction.

## Open Questions & Future Work

- [[ood-robustness-observability-forecasting]]

## Key Concepts

- [[observability-forecasting]]: A predictive task focusing on determining whether the surface is visible in future Earth Observation acquisitions rather than predicting surface values directly.

## Archivist Review

I have approved 'Observability Forecasting' as a novel task formulation for Earth Observation and 'EarthNet2021' as the canonical benchmark dataset for this domain. The open question on OOD robustness is approved as it addresses a fundamental bottleneck in latent world model generalization for environmental monitoring. Other candidates were rejected to maintain the high-quality, selective standard of the vault.

### Approved Concepts
- Observability Forecasting: Shifts the focus from surface state prediction to the binary usability of Earth Observation imagery, which is a critical operational bottleneck.

### Approved Open Questions
- OOD robustness for EO observability: Robustness to distribution shift is critical for the practical, reliable deployment of Earth Observation observability models in real-world, global monitoring systems.

## Datasets

- [[earthnet2021]]

## Links

- [Abstract](https://arxiv.org/abs/2607.13651)
- [PDF](https://arxiv.org/pdf/2607.13651)

