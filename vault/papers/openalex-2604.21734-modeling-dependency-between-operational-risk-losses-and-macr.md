---
# CSL-compatible fields
title: "Modeling dependency between operational risk losses and macroeconomic variables using Hidden Markov Models"
author:
  - literal: "Nikeethan Selvaratnam"
  - literal: "Dorinel Bastide"
  - literal: "Clément Fernandes"
  - literal: "Wojciech Pieczynski"
issued:
  date-parts:
    - [2026, 4, 23]
url: "https://arxiv.org/abs/2604.21734"

# Custom fields
paper_id: "2604.21734"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "hmm-with-auxiliary-economic-covariates"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-26T06:54:56Z"
created_at: "2026-04-26T06:54:56Z"
---

# Modeling dependency between operational risk losses and macroeconomic variables using Hidden Markov Models

**Authors**: Nikeethan Selvaratnam, Dorinel Bastide, Clément Fernandes, Wojciech Pieczynski
**Date**: 2026-04-23
**Paper ID**: [openalex:2604.21734](https://arxiv.org/abs/2604.21734)

## Summary

This paper addresses the difficulty of predicting operational risk losses in financial institutions, which are often characterized by complex, time-dependent, and heterogeneous structures. The authors introduce an extension of multivariate Hidden Markov Models (HMMs) that incorporates an auxiliary variable specifically to capture the influence of macroeconomic covariates on these losses. Calibration of the model is performed using the Expectation-Maximization (EM) algorithm, with empirical validation showing the benefit of integrating these economic variables for different risk-event types.

## Key Contributions

- Proposes a modified multivariate Hidden Markov Model (HMM) architecture that incorporates an auxiliary variable to model the dependency between macroeconomic indicators and operational risk losses.
- Provides an Expectation-Maximization (EM) algorithm-based calibration procedure specifically tailored to handle heterogeneous operational risk datasets.
- Demonstrates the relevance and performance impact of including macroeconomic covariates across various defined risk-event categories.

## Open Questions & Future Work

- [[heavy-tailed-hmm-operational-risk]]

## Key Concepts

- [[hmm-with-auxiliary-economic-covariates]]: An extension of Hidden Markov Models that integrates auxiliary macroeconomic variables into the state-transition process for improved operational risk prediction.

## Archivist Review

The paper contributes a specialized HMM extension for incorporating exogenous covariates. This is a reusable concept in financial and environmental modeling. I have also approved a question regarding heavy-tailed distributions as it addresses a structural limitation common to Gaussian-based HMMs. I rejected the open question regarding alternative covariates because feature selection is an empirical exercise specific to the data at hand rather than a foundational research problem.

### Approved Concepts
- Hidden Markov Models with auxiliary economic covariates: Provides a novel extension to HMMs to explicitly incorporate exogenous time-series covariates for financial risk modeling.

### Approved Open Questions
- Heavy-tailed distributions in HMMs: Improving the tail risk representation is critical for accurate capital requirement estimation in banking, where underestimating extreme losses can lead to severe financial instability.

### Rejected Candidates
- [open_question] Alternative covariates for risk (`optimal-covariates-operational-risk`) - low_impact: Determining appropriate covariates for a specific domain is a routine empirical task rather than a fundamental open research question.

## Links

- [Abstract](https://arxiv.org/abs/2604.21734)
- [PDF](https://arxiv.org/pdf/2604.21734)

