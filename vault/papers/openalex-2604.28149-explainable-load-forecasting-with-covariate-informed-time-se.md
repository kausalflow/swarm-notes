---
# CSL-compatible fields
title: "Explainable Load Forecasting with Covariate-Informed Time Series Foundation Models"
author:
  - literal: "Matthias Hertel"
  - literal: "Alexandra Nikoltchovska"
  - literal: "Sebastian Pütz"
  - literal: "Ralf Mikut"
  - literal: "Benjamin Schäfer"
  - literal: "Veit Hagenmeyer"
issued:
  date-parts:
    - [2026, 4, 30]
url: "https://arxiv.org/abs/2604.28149"

# Custom fields
paper_id: "2604.28149"
paper_source: "openalex"
domain: "time-series"
tags:
  - "llm"
  - "time-series"
  - "forecasting"
  - "interpretability"
  - "explainability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "tsfm-shap-explanation-algorithm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-03T07:13:45Z"
created_at: "2026-05-03T07:13:45Z"
---

# Explainable Load Forecasting with Covariate-Informed Time Series Foundation Models

**Authors**: Matthias Hertel, Alexandra Nikoltchovska, Sebastian Pütz, Ralf Mikut, Benjamin Schäfer, Veit Hagenmeyer
**Date**: 2026-04-30
**Paper ID**: [openalex:2604.28149](https://arxiv.org/abs/2604.28149)

## Summary

This paper addresses the interpretability challenge of Time Series Foundation Models (TSFMs) in critical energy infrastructure by introducing an efficient algorithm for computing SHAP values. By leveraging the flexible context length and covariate support inherent in TSFMs, the proposed method performs scalable temporal and covariate masking to attribute predictions. Experimental validation on a TSO day-ahead load forecasting task shows that both Chronos-2 and TabPFN-TS attain zero-shot performance competitive with dedicated models while providing explanations consistent with established domain knowledge.

## Key Contributions

- Proposes an efficient SHAP-based explanation algorithm tailored for Time Series Foundation Models by exploiting flexible input masking.
- Demonstrates that zero-shot Chronos-2 and TabPFN-TS models achieve predictive performance competitive with task-specific trained Transformers for day-ahead load forecasting.
- Validates that TSFM explanations align with domain-specific causal factors, specifically weather and calendar dependencies in energy grid operations.

## Open Questions & Future Work

- [[efficient-shap-tsfm-estimation]]

## Key Concepts

- [[tsfm-shap-explanation-algorithm]]: A scalable SHAP explanation method for TSFMs that utilizes temporal and covariate masking enabled by flexible input context lengths.

## Archivist Review

I approved the SHAP explanation algorithm for TSFMs as it provides a concrete, reusable methodology for interpretability in a high-stakes domain. I also approved the open question regarding efficient SHAP estimation, as the computational burden of SHAP is a universal bottleneck for deploying explainable foundation models. Other potential candidates were rejected for being too closely tied to specific case-study outcomes or representing generic implementation steps.

### Approved Concepts
- TSFM-SHAP Explanation Algorithm: Provides a critical transparency mechanism for black-box foundation models in high-stakes energy infrastructure where trust and explainability are mandatory.

### Approved Open Questions
- Efficient SHAP for TSFMs: The exponential complexity of exact SHAP currently limits its application in real-time or high-resolution forecasting environments.

## Links

- [Abstract](https://arxiv.org/abs/2604.28149)
- [PDF](https://arxiv.org/pdf/2604.28149)

