---
# CSL-compatible fields
title: "Least Absolute Deviations Estimation for Sinusoidal Models"
author:
  - literal: "Zehaan Naik"
  - literal: "Debasis Kundu"
issued:
  date-parts:
    - [2026, 6, 11]
url: "https://arxiv.org/abs/2606.13242"

# Custom fields
paper_id: "2606.13242"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-14T08:39:03Z"
created_at: "2026-06-14T08:39:03Z"
---

# Least Absolute Deviations Estimation for Sinusoidal Models

**Authors**: Zehaan Naik, Debasis Kundu
**Date**: 2026-06-11
**Paper ID**: [openalex:2606.13242](https://arxiv.org/abs/2606.13242)

## Summary

This paper presents a robust parameter estimation framework for sinusoidal regression models based on the Least Absolute Deviations (LAD) criterion, addressing the sensitivity of classical least-squares methods to outliers and heavy-tailed noise. The authors develop a modular coordinate descent algorithm that utilizes weighted median computations for amplitude updates and periodogram-inspired refinement for frequencies, offering significant computational speedups. Theoretical results establish the consistency and asymptotic normality of these estimators. Experimental evaluations confirm that the LAD-based approach provides an interpretable and reliable alternative for signal modeling in the presence of non-Gaussian noise.

## Key Contributions

- Formulates robust parameter estimation for sinusoidal regression models using the Least Absolute Deviations (LAD) objective.
- Introduces a modular coordinate descent algorithm that optimizes amplitude parameters via weighted median computations and frequency parameters via grid search with local refinement.
- Provides theoretical proofs for strong consistency and asymptotic normality of the LAD estimator under mild regularity conditions.
- Demonstrates superior robustness to heavy-tailed noise compared to traditional least-squares methods on synthetic and real-world datasets like Mauna Loa CO2 and UK drivers' deaths.

## Open Questions & Future Work

- [[regularization-for-lad-sinusoidal-models]]

## Archivist Review

I approved the open question regarding regularization for LAD sinusoidal models, as it addresses a fundamental limitation in parameter estimation stability for robust signal modeling. I rejected the proposed coordinate descent algorithm as a concept because it is a specific implementation detail for sinusoidal regression rather than a broad, reusable ML architecture. I also rejected the Mauna Loa dataset as it is a standard scientific dataset and does not warrant a unique vault entry.

### Approved Open Questions
- Regularization for LAD sinusoidal models: Regularization is critical for handling overparameterized models, a significant bottleneck identified by the authors when applying the proposed method to real-world datasets with limited samples.

### Rejected Candidates
- [concept] LAD coordinate descent for sinusoidal models (`lad-coordinate-descent-for-sinusoidal-models`) - paper_local: This is a specific algorithmic optimization strategy for a classical regression model rather than a general-purpose ML framework or architecture.
- [dataset] Mauna Loa atmospheric CO2 data (`mauna-loa-atmospheric-co2-data`) - low_impact: This is a generic scientific dataset commonly used for benchmarking and does not require a standalone vault entry.

## Links

- [Abstract](https://arxiv.org/abs/2606.13242)
- [PDF](https://arxiv.org/pdf/2606.13242)

