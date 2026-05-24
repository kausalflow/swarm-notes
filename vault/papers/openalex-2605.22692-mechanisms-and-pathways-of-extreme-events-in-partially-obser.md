---
# CSL-compatible fields
title: "Mechanisms and Pathways of Extreme Events in Partially-Observed Stochastic Dynamical Systems"
author:
  - literal: "Charlotte Moser"
  - literal: "Nan Chen"
  - literal: "Marios Andreou"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.22692"

# Custom fields
paper_id: "2605.22692"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "event-conditioned-latent-pathway-analysis"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:48:07Z"
created_at: "2026-05-24T07:48:07Z"
---

# Mechanisms and Pathways of Extreme Events in Partially-Observed Stochastic Dynamical Systems

**Authors**: Charlotte Moser, Nan Chen, Marios Andreou
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.22692](https://arxiv.org/abs/2605.22692)

## Summary

This paper introduces a mathematical framework for analyzing extreme events in stochastic dynamical systems where some variables remain hidden. By combining data assimilation with information-theoretic diagnostics, the authors infer latent precursor dynamics and map how these influences propagate to observable extremes. The method employs both trajectory-wise smoothing analysis and statistical clustering of event-conditioned states to isolate distinct event pathways, such as damping-induced or forcing-driven triggers. Numerical experiments validate the approach on complex systems, including nonlinear topographic flows.

## Key Contributions

- Proposes a mathematical framework for diagnosing mechanisms and pathways of extreme events in partially-observed stochastic dynamical systems using latent variable inference.
- Integrates data assimilation with trajectory-wise diagnostics and statistical clustering of event-conditioned hidden-state distributions.
- Demonstrates effectiveness in identifying precursor dynamics and distinct event pathways across intermittent, forcing-driven, and nonlinear topographic-flow stochastic models.

## Open Questions & Future Work

- [[scalable-extreme-event-diagnostics-general-nonlinear-systems]]

## Key Concepts

- [[event-conditioned-latent-pathway-analysis]]: A diagnostic framework for identifying mechanisms and precursor pathways of extreme events by clustering event-conditioned hidden-state distributions in partially-observed dynamical systems.

## Archivist Review

I have approved the concept 'Event-Conditioned Latent Pathway Analysis' as it provides a novel, reusable methodology for identifying hidden mechanisms underlying extreme events, which is a central contribution. I also approved the open question regarding the scalability of extreme-event diagnostics in non-Gaussian nonlinear systems, as it addresses a fundamental limitation in the current analytical framework for complex real-world application. Other potential contributions were deemed either too specific to the paper's models or subcomponents of the broader framework.

### Approved Concepts
- Event-Conditioned Latent Pathway Analysis: It provides a formal, reusable methodology for discovering latent causal drivers of extreme events in partially observed systems, bridging data assimilation and diagnostic analysis.

### Approved Open Questions
- Scalable Extreme-Event Diagnostics: This is critical for moving beyond analytically tractable models and enabling the application of trajectory-based extreme event diagnostics to real-world high-dimensional systems, such as complex climate and fluid dynamics models, where non-Gaussianity and strong nonlinearities are present.

## Links

- [Abstract](https://arxiv.org/abs/2605.22692)
- [PDF](https://arxiv.org/pdf/2605.22692)

