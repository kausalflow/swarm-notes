---
# CSL-compatible fields
title: "PEtab SciML: an exchange format for specifying and training dynamic scientific machine learning models"
author:
  - literal: "Sebastian Persson"
  - literal: "Branwen Snelling"
  - literal: "Maren Philipps"
  - literal: "Daniel Weindl"
  - literal: "Marija Cvijović"
  - literal: "Jan Hasenauer"
  - literal: "Dilan Pathirana"
  - literal: "Fabian Fröhlich"
issued:
  date-parts:
    - [2026, 8, 20]
url: "https://arxiv.org/abs/2608.20184"

# Custom fields
paper_id: "2608.20184"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
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
processed_at: "2026-08-23T05:19:59Z"
created_at: "2026-08-23T05:19:59Z"
---

# PEtab SciML: an exchange format for specifying and training dynamic scientific machine learning models

**Authors**: Sebastian Persson, Branwen Snelling, Maren Philipps, Daniel Weindl, Marija Cvijović, Jan Hasenauer, Dilan Pathirana, Fabian Fröhlich
**Date**: 2026-08-20
**Paper ID**: [openalex:2608.20184](https://arxiv.org/abs/2608.20184)

## Summary

Dynamic scientific machine learning (SciML) models combine mechanistic ordinary differential equations (ODEs) with machine learning components to model complex biological and physical processes. To address reproducibility and interoperability challenges, the authors introduce PEtab SciML, an exchange format for specifying parameter estimation problems where mechanistic and ML parameters are jointly estimated from time series data. Supported by a reference Python package, JAX and Julia toolchains, and real data benchmarks, PEtab SciML facilitates standardized training and evaluation across scientific modeling frameworks.

## Key Contributions

- Introduces PEtab SciML, an interoperable data format for specifying parameter estimation problems in dynamic scientific machine learning models combining mechanistic ODEs and ML components.
- Supports diverse ML ODE hybridization patterns for joint estimation of mechanistic and ML parameters from time-series data.
- Provides reference implementations and downstream tooling via AMICI (Python/JAX) and PEtab.jl (Julia), alongside real data benchmarks.

## Archivist Review

No novel machine learning architectural or algorithmic concepts are introduced that require permanent vault notes; the paper presents a software exchange format and ecosystem tooling for scientific machine learning.

## Links

- [Abstract](https://arxiv.org/abs/2608.20184)
- [PDF](https://arxiv.org/pdf/2608.20184)

