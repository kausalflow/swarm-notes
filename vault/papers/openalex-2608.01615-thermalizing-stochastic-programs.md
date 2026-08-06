---
# CSL-compatible fields
title: "Thermalizing Stochastic Programs"
author:
  - literal: "Mirko Amico"
  - literal: "Andraž Jelinčič"
  - literal: "Colin Oscar Nancarrow"
  - literal: "Leo Tyrpak"
  - literal: "David Roberts"
  - literal: "Seth Morton"
  - literal: "Dalton Sakthivadivel"
  - literal: "Ashwin Gopal"
  - literal: "Guillaume Verdon"
issued:
  date-parts:
    - [2026, 8, 3]
url: "https://arxiv.org/abs/2608.01615"

# Custom fields
paper_id: "2608.01615"
paper_source: "openalex"
domain: "time-series"
tags:
  - "reinforcement-learning"
  - "probabilistic-model"
  - "energy-based-model"
  - "time-series"
  - "simulation"
  - "stochastic-sampling"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-06T07:32:22Z"
created_at: "2026-08-06T07:32:22Z"
---

# Thermalizing Stochastic Programs

**Authors**: Mirko Amico, Andraž Jelinčič, Colin Oscar Nancarrow, Leo Tyrpak, David Roberts, Seth Morton, Dalton Sakthivadivel, Ashwin Gopal, Guillaume Verdon
**Date**: 2026-08-03
**Paper ID**: [openalex:2608.01615](https://arxiv.org/abs/2608.01615)

## Summary

This paper introduces a framework to map general stochastic programs, represented as Directed Factor Graphs or Parametrized Stochastic Circuits, onto thermodynamic hardware designed for energy-efficient stochastic sampling. The method compiles individual factors into native Energy-Based Models, analyzes error accumulation, and introduces training refinements like context matching and trajectory-level REINFORCE to minimize compilation residual error. Implemented in the thermalizers framework, the approach is successfully demonstrated on financial time series simulation, ecological modeling, Gibbs sampling, and sequential Bayesian design loops.

## Key Contributions

- Introduced a method to approximately compile Directed Factor Graphs (DFGs) of stochastic channels and Parametrized Stochastic Circuits (PSCs) into Energy-Based Models native to thermodynamic hardware.
- Analyzed error accumulation across compiled DFGs from per-factor compilation errors and introduced context matching and trajectory-level REINFORCE post-training refinements.
- Developed the thermalizers framework integrating torx and thrml libraries to map stochastic programs to energy-efficient thermodynamic sampling hardware.
- Demonstrated the framework on financial market simulation, ecological probabilistic modeling, Gibbs sampling, and sequential Bayesian design.

## Links

- [Abstract](https://arxiv.org/abs/2608.01615)
- [PDF](https://arxiv.org/pdf/2608.01615)

