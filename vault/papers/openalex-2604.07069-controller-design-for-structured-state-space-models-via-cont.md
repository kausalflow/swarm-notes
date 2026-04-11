---
# CSL-compatible fields
title: "Controller Design for Structured State-space Models via Contraction Theory"
author:
  - literal: "Muhammad Zakwan"
  - literal: "Vaibhav Gupta"
  - literal: "Alireza Karimi"
  - literal: "Efe C. Balta"
  - literal: "Giancarlo Ferrari-Trecate"
issued:
  date-parts:
    - [2026, 4, 8]
url: "https://arxiv.org/abs/2604.07069"

# Custom fields
paper_id: "2604.07069"
paper_source: "openalex"
domain: "robotics"
tags:
  - "ssm"
  - "state-space-model"
  - "robotics"
  - "control-theory"
architectures:
  - "mamba"
datasets:
  []
concept_slugs:
  - "contraction-theory-based-ssm-control"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-11T05:55:13Z"
created_at: "2026-04-11T05:55:13Z"
---

# Controller Design for Structured State-space Models via Contraction Theory

**Authors**: Muhammad Zakwan, Vaibhav Gupta, Alireza Karimi, Efe C. Balta, Giancarlo Ferrari-Trecate
**Date**: 2026-04-08
**Paper ID**: [openalex:2604.07069](https://arxiv.org/abs/2604.07069)

## Summary

This paper introduces a data-driven output feedback control framework for nonlinear systems using Structured State-space Models (SSMs) as surrogates. By deriving the controllability and observability properties of SSMs, the authors develop a scalable synthesis approach leveraging Linear Matrix Inequalities and contraction theory. Furthermore, a separation principle is proven, facilitating the independent design of stable observers and controllers, which is verified through nonlinear system identification and control simulation.

## Key Contributions

- Provides the first analytical framework for controllability and observability of structured state-space models (SSMs).
- Introduces a scalable control design method using Linear Matrix Inequalities (LMIs) and contraction theory for nonlinear system stabilization.
- Establishes a separation principle for SSM-based output feedback, allowing for modular design of observers and state-feedback controllers with proven exponential stability.

## Open Questions & Future Work

- [[internal-model-principle-ssm-integration]]

## Key Concepts

- [[contraction-theory-based-ssm-control]]: A controller synthesis framework that utilizes contraction theory and LMIs to ensure exponential stability in structured state-space models.

## Archivist Review

I have approved the core methodological contribution of contraction-based control for SSMs, as it provides a formal analytical bridge between sequence modeling architectures and stable control theory. The open question regarding the internal model principle is also approved, as it addresses a necessary structural extension for practical tracking applications, distinguishing this work from simple stabilization. All other candidates were either implied by these selections or too localized to the paper's specific numerical implementation.

### Approved Concepts
- Contraction-Theory-Based-SSM-Control: It bridges the gap between state-space models and formal control theory by providing stability guarantees for nonlinear systems using contraction principles.

### Approved Open Questions
- Internal Model Principle Integration: This integration is critical for transitioning the proposed SSM control framework from stabilization to high-performance tracking and disturbance rejection in practical, real-world control applications.

## Links

- [Abstract](https://arxiv.org/abs/2604.07069)
- [PDF](https://arxiv.org/pdf/2604.07069)

