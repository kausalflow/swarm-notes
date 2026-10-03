---
# CSL-compatible fields
title: "FlapKAD: A Simulation Dataset of Coupled Wing Kinematics and Aerodynamic Dynamics for Flapping-Wing Aerial Vehicles"
author:
  - literal: "Haichuan Li"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2609.38719"

# Custom fields
paper_id: "2609.38719"
paper_source: "openalex"
domain: "robotics"
tags:
  - "dataset"
  - "benchmark"
  - "time-series"
  - "forecasting"
  - "robotics"
architectures:
  []
datasets:
  - "FlapKAD"
concept_slugs:
  []
dataset_slugs:
  - "flapkad"
skill: "TimeSeriesSkill"
processed_at: "2026-10-03T10:09:12Z"
created_at: "2026-10-03T10:09:12Z"
---

# FlapKAD: A Simulation Dataset of Coupled Wing Kinematics and Aerodynamic Dynamics for Flapping-Wing Aerial Vehicles

**Authors**: Haichuan Li
**Date**: 2026-09-30
**Paper ID**: [openalex:2609.38719](https://arxiv.org/abs/2609.38719)

## Summary

The paper introduces FlapKAD, a large-scale simulation dataset comprising 2,000 flight episodes and over 720,000 synchronously recorded time steps that temporally align bilateral wing kinematics, aerodynamic responses, and flight states for flapping-wing aerial vehicles. Based on this dataset, the author establishes a bidirectional sequence-prediction benchmark with forward and inverse tasks to evaluate time-series architectures. Experiments across eight representative models demonstrate horizon-dependent behaviors and highlight difficulties in twist-angle reconstruction compared to flap-angle prediction.

## Key Contributions

- Introduces FlapKAD, an episode-structured simulation dataset containing 2,000 rigid-wing flight episodes and 720,152 synchronously recorded time steps of wing kinematics, aerodynamics, and flight states.
- Constructs a unified bidirectional sequence-prediction benchmark covering forward (kinematics-to-aerodynamics) and inverse (aerodynamics-to-kinematics) tasks across multiple horizons.
- Evaluates eight representative time-series architectures, revealing higher reconstruction errors for twist angle than flap angle and showing no consistent performance advantage from increased architectural complexity.

## Archivist Review

In accordance with the review policy and dataset scarcity limits, we approved the FlapKAD dataset as a standalone benchmark resource for flapping-wing aerial vehicles and rejected the concept candidate since the dataset itself is already captured under datasets. No open questions met the bar for long-term vault retention.

### Rejected Candidates
- [concept] FlapKAD (`flapkad`) - not_reusable: FlapKAD is primarily a named simulation dataset and benchmark rather than a reusable conceptual methodology, so it belongs in the dataset category.

## Datasets

- [[flapkad]]

## Links

- [Abstract](https://arxiv.org/abs/2609.38719)
- [PDF](https://arxiv.org/pdf/2609.38719)

