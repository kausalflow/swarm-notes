---
# CSL-compatible fields
title: "Guided Diffusion Sampling for Precipitation Forecast Interventions"
author:
  - literal: "Ayumu Ueyama"
  - literal: "Kazuhiko Kawamoto"
  - literal: "Hiroshi Kera"
issued:
  date-parts:
    - [2026, 5, 14]
url: "https://arxiv.org/abs/2605.14317"

# Custom fields
paper_id: "2605.14317"
paper_source: "openalex"
domain: "time-series,"
tags:
  - "diffusion-model"
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "robustness"
architectures:
  []
datasets:
  - "WeatherBench2"
concept_slugs:
  - "guided-diffusion-sampling-for-weather-intervention"
dataset_slugs:
  - "weatherbench2"
skill: "TimeSeriesSkill"
processed_at: "2026-05-17T07:30:39Z"
created_at: "2026-05-17T07:30:39Z"
---

# Guided Diffusion Sampling for Precipitation Forecast Interventions

**Authors**: Ayumu Ueyama, Kazuhiko Kawamoto, Hiroshi Kera
**Date**: 2026-05-14
**Paper ID**: [openalex:2605.14317](https://arxiv.org/abs/2605.14317)

## Summary

This paper introduces a gradient-based guidance framework for precipitation-reduction interventions within diffusion-based weather forecasting models. Unlike standard adversarial attacks that exploit model artifacts, this method steers the diffusion sampling trajectory to ensure that interventions remain consistent with the underlying atmospheric distribution. Extensive evaluation on WeatherBench2 shows that the proposed approach effectively reduces predicted extreme precipitation while demonstrating greater physical plausibility across vertical profiles and cross-model transferability tests.

## Key Contributions

- Introduced a gradient-based guidance framework for precipitation reduction that avoids the physical inconsistencies of traditional adversarial perturbations.
- Proposed a novel intervention method that steers the diffusion sampling trajectory in atmospheric forecasting models while maintaining latent distribution consistency.
- Demonstrated on WeatherBench2 that the proposed interventions achieve effective precipitation reduction with superior physical plausibility compared to standard adversarial approaches.

## Open Questions & Future Work

- [[nwp-validation-of-weather-interventions]]

## Key Concepts

- [[guided-diffusion-sampling-for-weather-intervention]]: A method to steer diffusion-based weather forecasts toward reduced precipitation by applying gradient-based guidance to the sampling trajectory while preserving physical consistency.

## Archivist Review

The paper presents a novel approach for controlling weather model outputs by guiding diffusion sampling, which is a reusable methodology in the growing field of generative forecasting. WeatherBench2 is approved as it is the canonical benchmark for these types of large-scale atmospheric models. One open question regarding NWP validation is approved as it represents a significant, non-boilerplate bottleneck for transitioning data-driven weather intervention research into physical science applications.

### Approved Concepts
- Guided Diffusion Sampling for Weather Intervention: It provides a new framework for physically-constrained weather control interventions via diffusion model trajectory guidance.

### Approved Open Questions
- NWP Validation of Interventions: Validating interventions against NWP models is critical for establishing the real-world operational feasibility of data-driven weather modification strategies.

## Datasets

- [[weatherbench2]]

## Links

- [Abstract](https://arxiv.org/abs/2605.14317)
- [PDF](https://arxiv.org/pdf/2605.14317)

