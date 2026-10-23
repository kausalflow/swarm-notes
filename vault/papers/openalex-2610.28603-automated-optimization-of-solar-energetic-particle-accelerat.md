---
# CSL-compatible fields
title: "Automated optimization of solar energetic particle acceleration and transport parameters against five-spacecraft observations of the 9 October 2021 event"
author:
  - literal: "Hiroyuki Tako Ishikawa"
  - literal: "Naho Fujita"
  - literal: "Yuta Kato"
  - literal: "Miki Kurihara"
  - literal: "Takashi Minoshima"
  - literal: "Daikou Shiota"
  - literal: "Kazumasa Iwai"
  - literal: "Marco Pinto"
  - literal: "António Pessanha Gomes"
  - literal: "Go Murakami"
  - literal: "K. Kusano"
  - literal: "Chihiro Mitsuda"
issued:
  date-parts:
    - [2026, 10, 20]
url: "https://arxiv.org/abs/2610.28603"

# Custom fields
paper_id: "2610.28603"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "seiten"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-23T09:41:07Z"
created_at: "2026-10-23T09:41:07Z"
---

# Automated optimization of solar energetic particle acceleration and transport parameters against five-spacecraft observations of the 9 October 2021 event

**Authors**: Hiroyuki Tako Ishikawa, Naho Fujita, Yuta Kato, Miki Kurihara, Takashi Minoshima, Daikou Shiota, Kazumasa Iwai, Marco Pinto, António Pessanha Gomes, Go Murakami, K. Kusano, Chihiro Mitsuda
**Date**: 2026-10-20
**Paper ID**: [openalex:2610.28603](https://arxiv.org/abs/2610.28603)

## Summary

The paper introduces the Fujitsu Solar Energetic particle Intelligent Tuning and Evaluation Network (SEITEN), an automated framework that couples MHD coronal mass ejection (CME) models with diffusive shock acceleration and focused transport models. By treating the parallel mean free paths and injection efficiencies along magnetic field lines as a 19-dimensional optimization problem solved via quasi-Monte Carlo sampling and a Tree-structured Parzen Estimator, SEITEN successfully reproduces proton flux profiles across five spacecraft for the 9 October 2021 solar energetic particle event. Multi-run analyses reveal that the relative dominance of transport parameters versus injection efficiencies depends heavily on MHD shock strength, indicating that joint MHD-SEP parameter estimation is essential for reliable space weather forecasting.

## Key Contributions

- Introduces SEITEN, an automated framework coupling MHD coronal mass ejection models with diffusive shock acceleration and focused transport models for solar energetic particle event simulation.
- Formulates particle parameter tuning as a 19-dimensional optimization problem solved via quasi-Monte Carlo sampling and Tree-structured Parzen Estimator.
- Demonstrates that the optimized model reproduces multi-spacecraft proton flux profiles for the 9 October 2021 event with a mean absolute error of approximately 0.45 in log10 flux.
- Shows through multi-run analysis that relative dominance of mean free paths versus injection efficiencies depends on MHD shock strength, underscoring the necessity of joint MHD-SEP parameter estimation.

## Limitations

Inferred parameter profiles are effective parameters conditional on the assumed transport geometry and MHD configurations.

## Open Questions & Future Work

- [[joint-mhd-sep-parameter-estimation]]

## Key Concepts

- [[seiten]]: The Fujitsu Solar Energetic particle Intelligent Tuning and Evaluation Network (SEITEN) is an automated framework that couples MHD CME propagation models with diffusive shock acceleration and focused transport models for parameter optimization.

## Archivist Review

Approved the core physics-based automated framework SEITEN and the open question on joint MHD-SEP parameter estimation, ensuring adherence to vault standards by filtering out non-reusable application-specific details.

### Approved Concepts
- SEITEN: Core framework introduced in the paper for automated optimization of solar energetic particle acceleration and transport parameters by coupling MHD and transport models.

### Approved Open Questions
- Joint MHD-SEP Parameter Estimation: Crucial for transitioning from event-specific physics-based hindcasting to generalized, operational real-time space weather forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2610.28603)
- [PDF](https://arxiv.org/pdf/2610.28603)

