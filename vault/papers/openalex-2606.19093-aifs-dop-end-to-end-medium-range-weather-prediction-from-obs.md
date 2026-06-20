---
# CSL-compatible fields
title: "AIFS-DOP: End-to-End Medium-Range Weather Prediction from Observations Alone with Machine Learning"
author:
  - literal: "Ewan Pinnington"
  - literal: "Peter Lean"
  - literal: "Mihai Alexe"
  - literal: "Eulalie Boucher"
  - literal: "Simon Lang"
  - literal: "Patrick Laloyaux"
  - literal: "Gert Mertes"
  - literal: "Tomáš Kráľ"
  - literal: "Patricia de Rosnay"
  - literal: "Matthew Chantry"
  - literal: "Anthony Mcnally"
issued:
  date-parts:
    - [2026, 6, 17]
url: "https://arxiv.org/abs/2606.19093"

# Custom fields
paper_id: "2606.19093"
paper_source: "openalex"
domain: "nlp"
tags:
  - "language-model"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "aifs-dop"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-20T08:18:46Z"
created_at: "2026-06-20T08:18:46Z"
---

# AIFS-DOP: End-to-End Medium-Range Weather Prediction from Observations Alone with Machine Learning

**Authors**: Ewan Pinnington, Peter Lean, Mihai Alexe, Eulalie Boucher, Simon Lang, Patrick Laloyaux, Gert Mertes, Tomáš Kráľ, Patricia de Rosnay, Matthew Chantry, Anthony Mcnally
**Date**: 2026-06-17
**Paper ID**: [openalex:2606.19093](https://arxiv.org/abs/2606.19093)

## Summary

The authors introduce AIFS-DOP, a novel machine learning framework for medium-range weather prediction that is trained entirely on raw gridded observations. By bypassing the common reliance on NWP reanalysis or synthetic model data, the system directly maps historical observational sequences to future states. Evaluation against ECMWF's IFS on 2021/2022 data confirms that the model is competitively accurate for major upper-air and surface metrics.

## Key Contributions

- Introduces AIFS-DOP, a medium-range weather forecasting system trained exclusively on 40 years of harmonized gridded observation data.
- Demonstrates that observation-only data-driven models can achieve performance competitive with the ECMWF Integrated Forecasting System (IFS) for key upper-air and surface scores.
- Eliminates reliance on traditional Numerical Weather Prediction (NWP) reanalysis or model data in the training pipeline of high-performance weather forecasters.

## Open Questions & Future Work

- [[probabilistic-training-dop-smoothing]]

## Key Concepts

- [[aifs-dop]]: An end-to-end machine learning model for medium-range weather prediction trained solely on gridded observations without NWP reanalysis.

## Archivist Review

I approved the AIFS-DOP framework as it introduces a fundamental shift in training paradigms for weather forecasting by eliminating reliance on NWP reanalysis, which is highly reusable for physical modeling. I also approved the open question regarding probabilistic training for DOP because it identifies a critical bottleneck in observation-driven models: the tendency toward over-smoothing. I rejected the dynamic graph candidate as it was too closely tied to specific potential ecosystem integrations and lacks a clear, universal research agenda.

### Approved Concepts
- Artificial Intelligence Forecasting System for Direct Observation Prediction (AIFS-DOP): AIFS-DOP demonstrates the viability of training medium-range weather forecasting models directly from raw observations, bypassing reliance on synthetic reanalysis data, a major shift in geophysical ML.

### Approved Open Questions
- Probabilistic Training for DOP Smoothing: Mitigating the smoothing effect is a primary bottleneck in transitioning observation-driven AI models into high-reliability operational weather forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2606.19093)
- [PDF](https://arxiv.org/pdf/2606.19093)

