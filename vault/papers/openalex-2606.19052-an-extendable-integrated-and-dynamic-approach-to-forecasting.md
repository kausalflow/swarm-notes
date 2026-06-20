---
# CSL-compatible fields
title: "An extendable, integrated, and dynamic approach to forecasting and stress-testing credit risk"
author:
  - literal: "Marcel Müller"
  - literal: "Arno Botha"
  - literal: "Conrad Beyers"
issued:
  date-parts:
    - [2026, 6, 17]
url: "https://arxiv.org/abs/2606.19052"

# Custom fields
paper_id: "2606.19052"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-20T08:17:55Z"
created_at: "2026-06-20T08:17:55Z"
---

# An extendable, integrated, and dynamic approach to forecasting and stress-testing credit risk

**Authors**: Marcel Müller, Arno Botha, Conrad Beyers
**Date**: 2026-06-17
**Paper ID**: [openalex:2606.19052](https://arxiv.org/abs/2606.19052)

## Summary

This paper introduces an integrated, extendable approach to loan portfolio stress-testing that bridges the gap between loan production and credit risk assessment. By utilizing a multistate probabilistic framework, the method simulates uncertain cash flows and computes portfolio-level risk metrics like default and loss rates. The framework employs a Monte Carlo simulation setup to incorporate stress scenarios and can dynamically model loan parameters as functions of input variables. This approach enables more flexible and dynamic credit risk forecasting than traditional, disjointed methods.

## Key Contributions

- Proposes an integrated framework that combines loan production simulation with credit risk forecasting to enable holistic stress-testing of loan portfolios.
- Introduces a multistate probabilistic framework to generate uncertain cash flow histories, allowing for the simulation of diverse portfolio conditions under varying loan parameters.
- Demonstrates a Monte Carlo-based stress-testing methodology that captures the correlation structure between risk metrics, outperforming classical approaches that isolate production and risk components.

## Open Questions & Future Work

- [[integrated-dynamic-credit-risk-calibration]]

## Archivist Review

The paper proposes a specific simulation framework for credit risk that is highly domain-specific and lacks a generalized algorithmic contribution suitable for permanent archival as a concept. I have approved the open question regarding the calibration of integrated risk models, as it highlights a significant, non-trivial limitation in current financial forecasting and stress-testing methodologies that transcends the scope of this particular paper.

### Approved Open Questions
- Calibrating integrated risk models: Current credit risk models often simplify these dynamics, leading to inaccurate stress-test results in real-world retail portfolios. Bridging the gap between simulation-based theoretical frameworks and empirical, data-driven applications is critical for robust financial risk management.

### Rejected Candidates
- [concept] Integrated loan production and credit risk framework (`integrated-framework-for-loan-production-and-credit-risk-forecasting`) - paper_local: This describes an application-specific architecture rather than a generic, reusable forecasting method or mechanism.
- [concept] Multistate probabilistic framework for cash flows (`multistate-probabilistic-framework-for-cash-flow-history-generation`) - paper_local: While useful, this is a specific implementation choice for credit modeling rather than a general forecasting mechanism likely to recur.

## Links

- [Abstract](https://arxiv.org/abs/2606.19052)
- [PDF](https://arxiv.org/pdf/2606.19052)

