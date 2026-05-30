---
# CSL-compatible fields
title: "Universal Time Series Generation with Neural Controlled Differential Equations"
author:
  - literal: "Torben Berndt"
  - literal: "Elyes Farjallah"
  - literal: "Leif Seute"
  - literal: "Raeid Saqur"
  - literal: "Benjamin Walker"
  - literal: "Jan Stühmer"
issued:
  date-parts:
    - [2026, 5, 27]
url: "https://arxiv.org/abs/2605.28507"

# Custom fields
paper_id: "2605.28507"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "generative-model"
  - "state-space-model"
  - "ssm"
  - "continuous-time-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "generative-slices-g-slices"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-30T07:35:06Z"
created_at: "2026-05-30T07:35:06Z"
---

# Universal Time Series Generation with Neural Controlled Differential Equations

**Authors**: Torben Berndt, Elyes Farjallah, Leif Seute, Raeid Saqur, Benjamin Walker, Jan Stühmer
**Date**: 2026-05-27
**Paper ID**: [openalex:2605.28507](https://arxiv.org/abs/2605.28507)

## Summary

This paper addresses the generative modeling of time series by leveraging the sequence universality of state space models. The authors prove that Structured Linear Controlled Differential Equations (SLiCEs) act as universal time-series generators for continuous causal pushforwards on latent sets. They introduce Generative SLiCEs (G-SLiCEs), a flow-matching framework on path-space, and show that this architecture achieves robust performance in probabilistic forecasting, particularly on irregular observation grids.

## Key Contributions

- Proved that Structured Linear Controlled Differential Equations (SLiCEs) are universal time-series generators, capable of approximating path laws of continuous causal pushforwards.
- Proposed Generative SLiCEs (G-SLiCEs), a continuous-time framework for flow matching on path-space.
- Demonstrated that G-SLiCEs improve performance in probabilistic forecasting and handle irregular observation grids better than fixed-grid models.

## Open Questions & Future Work

- [[efficient-structured-matrix-exponentials]]
- [[theoretical-reachability-path-space-flows]]

## Key Concepts

- [[generative-slices-g-slices]]: A continuous-time flow-matching framework on path-space derived from structured linear controlled differential equations.

## Archivist Review

I have approved the core Generative SLiCEs framework as a novel and reusable concept for time series generation. I have also approved two open questions that highlight the specific computational and theoretical challenges associated with using differential equations for generative time-series modeling. No datasets were approved as none met the criteria for a central, named resource.

### Approved Concepts
- Generative SLiCEs (G-SLiCEs): This is the core generative model framework introduced in the paper for continuous-time path-space flow matching, extending SSM universality to generative settings.

### Approved Open Questions
- Efficient Structured Matrix Exponentials: The matrix exponential is a fundamental operation in structured differential equation models; its optimized implementation is essential for widespread adoption and scaling of these methods.
- Theoretical Reachability of Flows: Establishing theoretical reachability is crucial for understanding the limitations of continuous-time generative frameworks and providing formal guarantees.

## Links

- [Abstract](https://arxiv.org/abs/2605.28507)
- [PDF](https://arxiv.org/pdf/2605.28507)

