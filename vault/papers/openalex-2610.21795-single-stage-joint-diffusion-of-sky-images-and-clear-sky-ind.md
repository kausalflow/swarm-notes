---
# CSL-compatible fields
title: "Single-stage joint diffusion of sky images and clear-sky index for ultra-short-term irradiance forecasting: what the frame-to-irradiance stage discards"
author:
  - literal: "Kanawut Suwandee"
  - literal: "Suwichaya Suwanwimolkul"
issued:
  date-parts:
    - [2026, 10, 15]
url: "https://arxiv.org/abs/2610.21795"

# Custom fields
paper_id: "2610.21795"
paper_source: "openalex"
domain: "time-series"
tags:
  - "diffusion-model"
  - "time-series"
  - "forecasting"
  - "multimodal"
architectures:
  []
datasets:
  []
concept_slugs:
  - "single-stage-joint-diffusion-for-irradiance-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-18T09:13:42Z"
created_at: "2026-10-18T09:13:42Z"
---

# Single-stage joint diffusion of sky images and clear-sky index for ultra-short-term irradiance forecasting: what the frame-to-irradiance stage discards

**Authors**: Kanawut Suwandee, Suwichaya Suwanwimolkul
**Date**: 2026-10-15
**Paper ID**: [openalex:2610.21795](https://arxiv.org/abs/2610.21795)

## Summary

Traditional sky-image irradiance forecasting relies on a decoupled two-stage pipeline consisting of future video prediction followed by a separate regression mapping to irradiance. This paper introduces a single-stage alternative that jointly co-denoises future sky images and clear-sky indices in a single diffusion process equipped with an irradiance head reading a denoised preview. Evaluated on 2023 SIRTA data, the proposed framework achieves a pooled RMSE of 104.1 W m^-2 and a CRPS skill score of +0.34 against smart persistence, outperforming twelve baseline configurations while recovering approximately 46 W m^-2 of information lost by traditional cascade architectures.

## Key Contributions

- Proposes a single-stage joint diffusion model that co-denoises future sky images and clear-sky indices for ultra-short-term solar irradiance forecasting.
- Achieves a pooled RMSE of 104.1 W m^-2 and a CRPS skill score of +0.34 against smart persistence on 2023 SIRTA data, outperforming twelve baseline configurations.
- Demonstrates that joint training recovers roughly 46 W m^-2 of error that traditional two-stage decoupled cascades discard.

## Open Questions & Future Work

- [[calibrating-diffusion-prediction-intervals]]

## Key Concepts

- [[single-stage-joint-diffusion-for-irradiance-forecasting]]: A single-stage framework that co-denoises future sky images and clear-sky indices in one diffusion process for irradiance forecasting.

## Archivist Review

Applied strict filtering to preserve only the overarching single-stage joint diffusion concept and the precise diffusion uncertainty calibration open question while rejecting routine datasets.

### Approved Concepts
- Single-Stage Joint Diffusion for Irradiance Forecasting: Replaces the traditional decoupled two-stage video prediction and regression cascade with a unified single-stage joint diffusion process.

### Approved Open Questions
- Calibrating Diffusion Prediction Intervals: Reliable probabilistic uncertainty quantification and well-calibrated prediction intervals are critical for power grid operators scheduling reserves against severe ramp events.

## Links

- [Abstract](https://arxiv.org/abs/2610.21795)
- [PDF](https://arxiv.org/pdf/2610.21795)

