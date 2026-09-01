---
# CSL-compatible fields
title: "Weak-Form Learning for Mean-Field Partial Differential Equations: An Application to Insect Movement"
author:
  - literal: "Seth Minor"
  - literal: "Bret D. Elderd"
  - literal: "Benjamin L. Allen"
  - literal: "David M. Bortz"
  - literal: "Vanja Dukić"
issued:
  date-parts:
    - [2026, 8, 31]
url: "https://arxiv.org/abs/2510.07786"

# Custom fields
paper_id: "2510.07786"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-01T09:41:19Z"
created_at: "2026-09-01T09:41:19Z"
---

# Weak-Form Learning for Mean-Field Partial Differential Equations: An Application to Insect Movement

**Authors**: Seth Minor, Bret D. Elderd, Benjamin L. Allen, David M. Bortz, Vanja Dukić
**Date**: 2026-08-31
**Paper ID**: [openalex:2510.07786](https://arxiv.org/abs/2510.07786)

## Summary

This paper extends weak-form equation learning techniques, specifically adapting the WSINDy algorithm coupled with kernel density estimation, to learn effective mean-field partial differential equation models for insect population movement from sparse experimental data. By modeling lepidopteran larval trajectories as overdamped stochastic processes, the approach characterizes dominant dispersal mechanisms, external potentials, and diffusion rates for fall armyworms under simulated agricultural conditions. The findings reveal that dispersal dynamics are primarily diffusive, with nonnegligible contributions from nonuniform resource distributions.

## Key Contributions

- Extends weak-form equation learning techniques to model lepidopteran larval population movement directly from sparse experimental data.
- Couples the WSINDy algorithm with kernel density estimation to learn nonlinear Fokker-Planck models from McKean-Vlasov stochastic differential equations.
- Demonstrates quantitative characterization of dispersal dynamics and effective diffusion rates of fall armyworms (Spodoptera frugiperda) under simulated agricultural conditions.

## Limitations

Limited to learning mean-field governing equations from sparse experimental data under specific simulated agricultural conditions.

## Archivist Review

The candidate concept WSINDy is a pre-existing method rather than a novel conceptual contribution introduced by this paper, and the open question is standard boilerplate calling for more data. Both are rejected under our stringent review policy.

### Rejected Candidates
- [concept] Weak-form Sparse Identification of Nonlinear Dynamics (WSINDy) (`weak-form-sparse-identification-of-nonlinear-dynamics-wsindy`) - not_novel: WSINDy is an established method from prior literature rather than a new core methodological contribution of this paper.
- [open_question] Expanding Data for Insect Dispersal Models (`improving-insect-dispersal-models-with-expanded-data`) - low_impact: Boilerplate future work suggesting more data and better precision rather than a specific algorithmic or theoretical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2510.07786)
- [PDF](https://arxiv.org/pdf/2510.07786)

