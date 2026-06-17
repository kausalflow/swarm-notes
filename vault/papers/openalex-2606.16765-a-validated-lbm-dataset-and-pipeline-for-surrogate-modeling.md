---
# CSL-compatible fields
title: "A Validated LBM Dataset and Pipeline for Surrogate Modeling of Turbulent 3D Obstructed Channel Flows"
author:
  - literal: "Lukas Schröder"
  - literal: "Shubham Kavane"
  - literal: "Harald Köstler"
issued:
  date-parts:
    - [2026, 6, 15]
url: "https://arxiv.org/abs/2606.16765"

# Custom fields
paper_id: "2606.16765"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "dataset"
  - "benchmark"
  - "fourier-neural-operator"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-17T09:27:08Z"
created_at: "2026-06-17T09:27:08Z"
---

# A Validated LBM Dataset and Pipeline for Surrogate Modeling of Turbulent 3D Obstructed Channel Flows

**Authors**: Lukas Schröder, Shubham Kavane, Harald Köstler
**Date**: 2026-06-15
**Paper ID**: [openalex:2606.16765](https://arxiv.org/abs/2606.16765)

## Summary

This paper introduces a validated, reproducible pipeline for generating high-fidelity 3D turbulent channel flow data using a cumulant lattice Boltzmann solver. The framework is verified against experimental benchmarks, providing a standardized platform for assessing the performance of neural surrogate models in fluid dynamics. The authors propose specific evaluation tasks including forecasting and super-resolution, with an emphasis on the correct representation of turbulent energy cascades.

## Key Contributions

- Introduces a reproducible lattice Boltzmann method (LBM) pipeline for generating high-fidelity 3D turbulent channel flow datasets at Re=1,000-10,000.
- Provides rigorous verification of generated data against experimental physical metrics including Strouhal numbers, drag coefficients, and turbulent fluctuations at 1024x512x512 resolution.
- Establishes a standardized framework for benchmarking neural operators on turbulent flow tasks such as forecasting, super-resolution, and error correction.

## Links

- [Abstract](https://arxiv.org/abs/2606.16765)
- [PDF](https://arxiv.org/pdf/2606.16765)

