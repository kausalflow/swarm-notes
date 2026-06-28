---
# CSL-compatible fields
title: "Simulation-based inference for rapid Bayesian parameter estimation in epidemiological models: a comparison with MCMC"
author:
  - literal: "Alina Bazarova"
  - literal: "Johann F. Jadebeck"
  - literal: "Henrik Zunker"
  - literal: "Carolina J. Klett-Tammen"
  - literal: "Torben Heinsohn"
  - literal: "Wolfgang Wiechert"
  - literal: "Katharina Noeh"
  - literal: "Stefan Kesselheim"
issued:
  date-parts:
    - [2026, 6, 25]
url: "https://arxiv.org/abs/2606.27286"

# Custom fields
paper_id: "2606.27286"
paper_source: "openalex"
domain: "biology"
tags:
  - "reinforcement-learning"
  - "bayesian-inference"
architectures:
  []
datasets:
  []
concept_slugs:
  - "sbi-for-epidemiological-modeling"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-28T08:17:23Z"
created_at: "2026-06-28T08:17:23Z"
---

# Simulation-based inference for rapid Bayesian parameter estimation in epidemiological models: a comparison with MCMC

**Authors**: Alina Bazarova, Johann F. Jadebeck, Henrik Zunker, Carolina J. Klett-Tammen, Torben Heinsohn, Wolfgang Wiechert, Katharina Noeh, Stefan Kesselheim
**Date**: 2026-06-25
**Paper ID**: [openalex:2606.27286](https://arxiv.org/abs/2606.27286)

## Summary

This paper evaluates Simulation-Based Inference (SBI) using neural posterior estimation as a high-performance alternative to Markov Chain Monte Carlo (MCMC) for the Bayesian calibration of mechanistic epidemiological models. By leveraging GPU acceleration, SBI significantly reduces the computational overhead required for model parameter estimation in high-dimensional or long-horizon scenarios, such as modeling COVID-19 ICU occupancy. The experimental results demonstrate that SBI provides comparable posterior distribution accuracy and predictive power to MCMC while achieving substantial speedups, facilitating rapid real-time outbreak analysis.

## Key Contributions

- Investigates Simulation-Based Inference (SBI) using neural posterior estimation as an efficient, scalable alternative to MCMC for calibrating mechanistic SECIR epidemiological models.
- Demonstrates that SBI achieves comparable posterior accuracy and predictive performance to MCMC while reducing runtime from 1000s to ~65s (31-day window) and 19,000s to 157s (201-day window).
- Validates the approach using COVID-19 ICU occupancy data from Germany, showing robustness across multiple epidemic phases and complex scenarios involving multiple change points.

## Open Questions & Future Work

- [[sbi-generalization-and-operational-deployment]]

## Key Concepts

- [[sbi-for-epidemiological-modeling]]: The use of neural posterior estimation for the Bayesian calibration of mechanistic epidemiological models to significantly reduce computational runtime.

## Archivist Review

The paper presents a clear methodological shift toward simulation-based inference (SBI) for accelerating parameter estimation in mechanistic epidemiological models. I approved the concept as it offers a reusable, scalable alternative to MCMC for compartmental forecasting. The open question is also approved as it captures the necessary research trajectory for transitioning these models into robust, real-time public health tools.

### Approved Concepts
- Simulation-Based Inference (SBI) for Epidemiological Modeling: Demonstrates a concrete, scalable alternative to traditional MCMC for calibrating mechanistic compartmental models, essential for time-critical forecasting scenarios.

### Approved Open Questions
- Generalization and operational deployment of SBI: This question addresses the critical need to validate the robustness and operational utility of machine learning-based inference in public health, moving beyond retrospective analyses to active, sequential forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2606.27286)
- [PDF](https://arxiv.org/pdf/2606.27286)

