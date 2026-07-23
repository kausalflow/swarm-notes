---
# CSL-compatible fields
title: "On the Predictive Skill of Artificial Intelligence-based Weather Models for Extreme Events using Uncertainty Quantification"
author:
  - literal: "Rodrigo Andrade Botelho de Almeida"
  - literal: "Noelia Otero"
  - literal: "Miguel‐Ángel Fernández‐Torres"
  - literal: "Jackie Ma"
issued:
  date-parts:
    - [2026, 7, 20]
url: "https://arxiv.org/abs/2511.17176"

# Custom fields
paper_id: "2511.17176"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-23T07:27:15Z"
created_at: "2026-07-23T07:27:15Z"
---

# On the Predictive Skill of Artificial Intelligence-based Weather Models for Extreme Events using Uncertainty Quantification

**Authors**: Rodrigo Andrade Botelho de Almeida, Noelia Otero, Miguel‐Ángel Fernández‐Torres, Jackie Ma
**Date**: 2026-07-20
**Paper ID**: [openalex:2511.17176](https://arxiv.org/abs/2511.17176)

## Summary

This study evaluates the predictive skill of state-of-the-art deterministic AI-based weather models (such as FuXi, GraphCast, and SFNO) for extreme events by applying four initial-condition perturbation strategies to generate 50-member ensembles. The findings indicate that simple perturbations (Gaussian, Perlin noise) yield comparable probabilistic skill to complex flow-based methods, while model choice remains the dominant factor determining ensemble performance. Although these perturbed deterministic frameworks narrow the performance gap, native probabilistic models and numerical weather prediction ensembles continue to exhibit superior reliability, particularly for temperature extremes over precipitation.

## Key Contributions

- Investigated how state-of-the-art deterministic AI weather models respond to initial-condition perturbations (Gaussian, Perlin noise, HCBV, and HENS) for forecasting extreme events like the August 2022 Pakistan floods and China heatwave.
- Demonstrated that simpler perturbation strategies (Gaussian and Perlin noise) perform comparably to complex flow-based approaches (HCBV and HENS), showing that model choice is the dominant factor for ensemble performance rather than the perturbation method.
- Evaluated ensemble skill against ERA5 and compared with IFS ENS and AIFS ENS, finding that while perturbed deterministic models narrow the performance gap, native probabilistic models retain superior probabilistic skill across variables.
- Showed that AI weather models capture temperature extremes more effectively than precipitation extremes, highlighting key limitations in extreme weather forecasting.

## Limitations

Deterministic AI models perturbed via initial conditions still lag behind native probabilistic models and numerical weather prediction ensembles in probabilistic skill, particularly for complex variables like precipitation.

## Archivist Review

This paper investigates the application of various initial-condition perturbation strategies to deterministic AI-based weather models for extreme event forecasting. No novel, reusable algorithmic concepts, datasets, or specific open questions were identified that meet the high novelty and reusability standards required for permanent vault inclusion.

## Links

- [Abstract](https://arxiv.org/abs/2511.17176)
- [PDF](https://arxiv.org/pdf/2511.17176)

