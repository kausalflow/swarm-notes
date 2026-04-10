---
# CSL-compatible fields
title: "Joint Bayesian inference of Earth's magnetic field and core surface flow on millennial timescales"
author:
  - literal: "Andreas Nilsson"
  - literal: "Neil Suttie"
  - literal: "Marie Troyano"
  - literal: "Nicolas Gillet"
  - literal: "Julien Aubert"
  - literal: "Anders Irbäck"
issued:
  date-parts:
    - [2026, 4, 7]
url: "https://arxiv.org/abs/2601.10344"

# Custom fields
paper_id: "2601.10344"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "forecasting"
  - "bayesian-inference"
architectures:
  []
datasets:
  []
concept_slugs:
  - "efficient-discrete-marginalisation-of-age-uncertainties"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-10T06:27:01Z"
created_at: "2026-04-10T06:27:01Z"
---

# Joint Bayesian inference of Earth's magnetic field and core surface flow on millennial timescales

**Authors**: Andreas Nilsson, Neil Suttie, Marie Troyano, Nicolas Gillet, Julien Aubert, Anders Irbäck
**Date**: 2026-04-07
**Paper ID**: [openalex:2601.10344](https://arxiv.org/abs/2601.10344)

## Summary

This paper introduces a Bayesian framework for jointly modeling Earth's geomagnetic field and core surface flow using sparse, uncertain archaeo- and palaeomagnetic data. The approach integrates a stochastic geodynamo prior with an efficient discrete marginalisation technique to handle chronological uncertainties, circumventing typical convergence issues in high-dimensional Hamiltonian Monte Carlo inversions. Validation on synthetic geodynamo data confirms the framework's ability to reconstruct millennial-scale dynamical features such as westward drift and eccentric gyres, offering a robust foundation for future geophysical reconstructions.

## Key Contributions

- Developed a Bayesian framework for the joint inference of Earth's core surface flow and magnetic field over millennial timescales.
- Introduced efficient discrete marginalisation of age uncertainties, enabling stable HMC inversions for noisy archaeo/palaeomagnetic data.
- Demonstrated the capability to recover large-scale core dynamics, such as planetary-scale eccentric gyres and westward drift, using synthetic geodynamo data.

## Open Questions & Future Work

- [[ensemble-geodynamo-prior-validation]]

## Key Concepts

- [[efficient-discrete-marginalisation-of-age-uncertainties]]: A technique for integrating chronological uncertainty into Bayesian models by marginalizing over temporal indices instead of co-estimating them.

## Archivist Review

This paper presents a robust Bayesian framework for geophysical time-series reconstruction. I have approved the discrete marginalisation technique as it provides a generalized approach to handling irregular temporal uncertainty in MCMC, and the open question regarding ensemble validation as it is a critical concern for reliability in inverse modeling. No further concepts or datasets met the rigorous threshold for inclusion.

### Approved Concepts
- Efficient discrete marginalisation of age uncertainties: Addresses the fundamental challenge of high-dimensional MCMC convergence when dealing with imprecise chronological data in geophysical inversions.

### Approved Open Questions
- Ensemble validation of core models: The dependency on kinematic priors is a fundamental challenge in geomagnetic data assimilation and similar inverse problems. Without systematic ensemble validation, it is difficult to quantify the reliability and physical validity of reconstructed dynamics.

## Links

- [Abstract](https://arxiv.org/abs/2601.10344)
- [PDF](https://arxiv.org/pdf/2601.10344)

