---
# CSL-compatible fields
title: "Bayesian reversal of the liquid level trajectory in a draining tank for pollution forensics"
author:
  - literal: "Kyla Jones"
  - literal: "Gbenga Fabusola"
  - literal: "Alexander W. Dowling"
  - literal: "Cory M. Simon"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.29193"

# Custom fields
paper_id: "2605.29193"
paper_source: "openalex"
domain: "physics"
tags:
  - "time-series"
  - "forecasting"
  - "uncertainty-quantification"
  - "bayesian-inference"
architectures:
  []
datasets:
  []
concept_slugs:
  - "inverse-cvae-for-retrodiction"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:11:17Z"
created_at: "2026-05-31T08:11:17Z"
---

# Bayesian reversal of the liquid level trajectory in a draining tank for pollution forensics

**Authors**: Kyla Jones, Gbenga Fabusola, Alexander W. Dowling, Cory M. Simon
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.29193](https://arxiv.org/abs/2605.29193)

## Summary

This paper introduces a Bayesian inverse framework for estimating the initial volume of hazardous liquids lost during a tank breach. By combining a physics-based model derived from Torricelli's law with an empirical discrepancy function, the approach accounts for model uncertainties and imperfect physical assumptions. The methodology provides a robust way to perform forensic retrodiction, offering quantified uncertainty estimates for the initial liquid level based on final observations and known drainage durations.

## Key Contributions

- Proposes a Bayesian statistical inversion framework to estimate initial liquid levels in tanks post-leakage.
- Integrates Torricelli's law with an empirical discrepancy function to account for modeling inaccuracies and environmental uncertainties.
- Demonstrates the framework's effectiveness in quantifying uncertainty for initial volume estimation based on observed final states and drainage duration.

## Open Questions & Future Work

- [[physics-model-drainage-limitations]]

## Key Concepts

- [[inverse-cvae-for-retrodiction]]: A Bayesian framework for inferring past states of a physical system from final state observations and time-series data.

## Archivist Review

The paper presents a specific Bayesian retrodiction framework for physical systems. I have approved the framework concept and the identified open question regarding low-level fluid physics, as both are sufficiently generalizable for the vault. No datasets were proposed that meet the required standard of being a named, central, and reusable resource.

### Approved Concepts
- Inverse CVAE for Retrodiction: The paper provides a formal Bayesian approach to reverse dynamic state estimation, which is distinct from forward-time forecasting.

### Approved Open Questions
- Modeling drainage at low levels: Accurate estimation at low liquid levels is vital for environmental forensics and regulatory compliance, making the failure of standard physics-based models a key bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2605.29193)
- [PDF](https://arxiv.org/pdf/2605.29193)

