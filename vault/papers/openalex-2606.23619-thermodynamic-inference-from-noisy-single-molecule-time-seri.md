---
# CSL-compatible fields
title: "Thermodynamic inference from noisy single-molecule time series"
author:
  - literal: "Todd R. Gingrich"
  - literal: "Oleg A. Igoshin"
  - literal: "Anatoly B. Kolomeisky"
  - literal: "Dmitrii E. Makarov"
issued:
  date-parts:
    - [2026, 6, 22]
url: "https://arxiv.org/abs/2606.23619"

# Custom fields
paper_id: "2606.23619"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  - "non-markovian-entropy-production-estimator"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-25T08:16:40Z"
created_at: "2026-06-25T08:16:40Z"
---

# Thermodynamic inference from noisy single-molecule time series

**Authors**: Todd R. Gingrich, Oleg A. Igoshin, Anatoly B. Kolomeisky, Dmitrii E. Makarov
**Date**: 2026-06-22
**Paper ID**: [openalex:2606.23619](https://arxiv.org/abs/2606.23619)

## Summary

This paper investigates the thermodynamic consequences of noisy measurement limits in single-molecule trajectories. It proves that estimating entropy production from noisy experimental data consistently results in lower bounds, regardless of whether the true state is inferred beforehand or the observed signal is used as a direct proxy. The authors demonstrate that observational noise turns Markovian microscopic processes into non-Markovian dynamics, requiring specialized estimators. Furthermore, the study highlights a complex relationship between spatial and temporal resolution, showing that higher temporal sampling can sometimes worsen estimate reliability in noisy conditions.

## Key Contributions

- Formulated a framework proving that standard inference strategies on noise-degraded trajectories provide lower bounds on the true entropy production.
- Demonstrated that detection noise induces non-Markovian dynamics, necessitating the use of non-Markovian entropy production estimators for improved accuracy.
- Identified a paradoxical trade-off where increasing temporal resolution in the presence of noise can degrade the quality of entropy production estimates.

## Open Questions & Future Work

- [[robust-model-selection-for-thermodynamic-inference]]

## Key Concepts

- [[non-markovian-entropy-production-estimator]]: A statistical method designed to estimate entropy production accurately from non-Markovian dynamics induced by detection noise.

## Archivist Review

I have approved the non-Markovian entropy production estimator as a conceptually rigorous method for handling noise-induced dynamics in stochastic time series, along with a corresponding open question on the model selection bottleneck in this domain. These selections focus on the fundamental physical-statistical trade-offs inherent in noisy trajectory analysis, which aligns with the vault's interest in robust scientific inference and time series dynamics.

### Approved Concepts
- Non-Markovian entropy production estimator: Proposes a novel estimator framework specifically for entropy production in trajectories degraded by non-Markovian observational noise, challenging standard Markovian assumptions in single-molecule inference.

### Approved Open Questions
- Robust Model Selection for Thermodynamic Inference: This is a fundamental bottleneck in the field of stochastic thermodynamics. If inference results depend strongly on the chosen model, the resulting thermodynamic conclusions may not be objectively grounded in the data. Developing model-robust inference is essential for the reliability of applying stochastic thermodynamics to complex biological systems.

## Links

- [Abstract](https://arxiv.org/abs/2606.23619)
- [PDF](https://arxiv.org/pdf/2606.23619)

