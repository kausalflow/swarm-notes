---
# CSL-compatible fields
title: "Low-Rank Clebsch--Gordan Coupling for Equivariant Spherical Forecasting"
author:
  - literal: "Yaojun Li"
  - literal: "Zhixuan Zhao"
  - literal: "Dongzhe Zheng"
  - literal: "Christine Allen-Blanchette"
issued:
  date-parts:
    - [2026, 11, 2]
url: "https://arxiv.org/abs/2611.03411"

# Custom fields
paper_id: "2611.03411"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "time-series"
  - "forecasting"
  - "efficient-transformer"
architectures:
  []
datasets:
  []
concept_slugs:
  - "lcg-sfno"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-04T12:40:46Z"
created_at: "2026-11-04T12:40:46Z"
---

# Low-Rank Clebsch--Gordan Coupling for Equivariant Spherical Forecasting

**Authors**: Yaojun Li, Zhixuan Zhao, Dongzhe Zheng, Christine Allen-Blanchette
**Date**: 2026-11-02
**Paper ID**: [openalex:2611.03411](https://arxiv.org/abs/2611.03411)

## Summary

This paper introduces LCG-SFNO, a spherical forecasting model that integrates low-rank Clebsch-Gordan (CG) tensor products, coefficient-space residual propagation, and exactly projected quadratic nonlinearities to preserve exact SO(3) equivariance without prohibitive computational overhead. To achieve forecasting-scale efficiency, the authors develop SSHCG, a sparse GPU implementation with a factorized alternative that restricts CG coupling overhead to roughly 10 percent of a training step. Evaluated on spherical shallow-water dynamics and ERA5-based WeatherBench, LCG-SFNO reduces rotational error by three to five orders of magnitude compared to traditional SFNO while improving forecast skill and matching or exceeding performance benchmarks.

## Key Contributions

- Introduces LCG-SFNO, combining low-rank Clebsch-Gordan interactions, coefficient-space residual propagation, and projected quadratic nonlinearity for SO(3)-equivariant global forecasting.
- Develops SSHCG, a sparse GPU implementation and factorized alternative enabling practical Clebsch-Gordan coupling at forecasting scale.
- Reduces rotational error to numerical precision (over 3-5 orders of magnitude below SFNO) on spherical shallow-water dynamics and ERA5-based WeatherBench, while improving forecast skill.
- Demonstrates that SSHCG keeps Clebsch-Gordan coupling to about 10% of a training step at operational bandwidth.

## Key Concepts

- [[lcg-sfno]]: A spherical Fourier neural operator leveraging low-rank Clebsch-Gordan coupling for exactly equivariant global forecasting.

## Archivist Review

Approved LCG-SFNO as a novel and reusable equivariant spherical forecasting architecture combining low-rank Clebsch-Gordan interactions. The open question regarding operator transfer across architectures was rejected for being a routine architectural generalization study.

### Approved Concepts
- LCG-SFNO: Introduces a novel low-rank Clebsch-Gordan coupling framework for equivariant spherical forecasting that achieves exact SO(3) equivariance while remaining practical at large operational bandwidths.

### Rejected Candidates
- [open_question] Equivariant Operator Transfer across Architectures (`equivariant-operator-transfer-architecture`) - low_impact: Standard architectural integration and modularity inquiry that lacks a specific algorithmic bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2611.03411)
- [PDF](https://arxiv.org/pdf/2611.03411)

