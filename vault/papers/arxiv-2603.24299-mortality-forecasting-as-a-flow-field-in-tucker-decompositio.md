---
# CSL-compatible fields
title: "Mortality Forecasting as a Flow Field in Tucker Decomposition Space"
author:
  - literal: "Samuel J. Clark"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.24299"

# Custom fields
paper_id: "2603.24299"
paper_source: "arxiv"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "tensor-decomposition"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  - "Human Mortality Database"
skill: "TimeSeriesSkill"
processed_at: "2026-03-26T07:11:08Z"
created_at: "2026-03-26T07:11:08Z"
---

# Mortality Forecasting as a Flow Field in Tucker Decomposition Space

**Authors**: Samuel J. Clark
**Date**: 2026-03-25
**Paper ID**: [arxiv:2603.24299](https://arxiv.org/abs/2603.24299)

## Summary

This paper proposes a novel method for mortality forecasting that reframes the problem as integrating a flow field through the latent score space derived from a Tucker tensor decomposition of multi-population mortality data. By reducing the dimensionality of the mortality structure, the authors find that the transition primarily follows a one-dimensional flow characterized by a scalar speed function advancing the level. The system incorporates an era-weighted speed function for contemporary adaptation and uses calibrated convergence rates to guide country-specific trajectories toward a canonical structure. Evaluation via 50-year, leave-country-out cross-validation shows the approach competes effectively with established methods like Lee-Carter and Hyndman-Ullah.

## Key Contributions

- Reframing mortality forecasting as integrating a flow field through the low-dimensional score space of a Tucker tensor decomposition of multi-population mortality data.
- Demonstrating that PCA reduction of the effective core matrices reveals the mortality transition is fundamentally a one-dimensional flow governed by a scalar speed function.
- Introducing an era-weighted speed function to adapt to contemporary dynamics and calibrated convergence rates to control relaxation toward a canonical mortality structure.
- Achieving competitive or superior performance against Lee-Carter and Hyndman-Ullah benchmarks over a 50-year forecast horizon in leave-country-out cross-validation.

## Limitations

The reliance on the structure captured by the Tucker decomposition might limit the ability to model entirely novel, abrupt shifts in mortality dynamics that fall outside the learned low-dimensional space.

## Open Questions & Future Work

- [[mortality-trajectory-very-low-levels]]
- [[hybrid-short-long-horizon-forecasting]]
- [[generalizability-beyond-european-hmd]]
- [[data-scarcity-super-low-mortality]]
- [[adaptive-era-weighting-kernels]]
- [[conditioning-on-covariates]]
- [[fully-bayesian-uncertainty-quantification]]
- [[era-weighting-extensions]]
- [[hybrid-short-horizon-system]]
- [[modelife-table-byproduct-use]]

## Key Concepts

- [Tucker Decomposition for Mortality Forecasting](../concepts/tucker-decomposition-mortality-forecasting.md): A method reframing mortality forecasting as integrating a flow field within the low-dimensional score space derived from a Tucker tensor decomposition of multi-population mortality data.

## Datasets

- [Human Mortality Database](../datasets/human-mortality-database.md)

## Limitations

The reliance on the structure captured by the Tucker decomposition might limit the ability to model entirely novel, abrupt shifts in mortality dynamics that fall outside the learned low-dimensional space.

## Links

- [ArXiv Abstract](https://arxiv.org/abs/2603.24299)
- [PDF](https://arxiv.org/pdf/2603.24299)

