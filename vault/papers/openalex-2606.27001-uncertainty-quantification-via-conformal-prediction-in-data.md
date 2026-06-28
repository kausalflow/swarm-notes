---
# CSL-compatible fields
title: "Uncertainty quantification via conformal prediction in data assimilation"
author:
  - literal: "Catherine George"
  - literal: "Alireza Javanmardi"
  - literal: "Tijana Janjić"
  - literal: "Eyke Hüllermeier"
issued:
  date-parts:
    - [2026, 6, 25]
url: "https://arxiv.org/abs/2606.27001"

# Custom fields
paper_id: "2606.27001"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "conformal-prediction"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-28T08:17:05Z"
created_at: "2026-06-28T08:17:05Z"
---

# Uncertainty quantification via conformal prediction in data assimilation

**Authors**: Catherine George, Alireza Javanmardi, Tijana Janjić, Eyke Hüllermeier
**Date**: 2026-06-25
**Paper ID**: [openalex:2606.27001](https://arxiv.org/abs/2606.27001)

## Summary

This paper explores the utility of conformal prediction (CP) for uncertainty quantification in numerical weather prediction, specifically within data assimilation cycles. Using a one-dimensional modified shallow water model, the study compares various CP variants—Standard, Normalized, and Conformalized Quantile Regression—against traditional ensemble-based uncertainty measures. The evaluation focuses on metrics such as empirical coverage and interval length, illustrating the potential for CP to supplement existing ensemble forecasting techniques.

## Key Contributions

- Evaluates three conformal prediction (CP) variants—Standard CP, Normalized CP, and Conformalized Quantile Regression—for uncertainty quantification in numerical weather prediction models.
- Provides a comparative analysis of CP-derived uncertainty intervals against traditional ensemble-based methods using the one-dimensional modified shallow water model.
- Demonstrates the integration of CP-derived uncertainty estimates into the data assimilation cycle through CP perturbations.

## Open Questions & Future Work

- [[conformal-prediction-under-non-exchangeability]]
- [[uncertainty-decomposition-for-forecasting]]

## Archivist Review

The paper provides a standard application of conformal prediction to weather forecasting, which is a known area of research; therefore, no new concepts were approved. The open questions regarding non-exchangeability and uncertainty decomposition are highly relevant to the provided skill context and represent significant, non-boilerplate research challenges in temporal forecasting.

### Approved Open Questions
- Conformal Prediction Non-Exchangeability: The lack of formal theoretical guarantees under non-exchangeable settings limits the reliability of conformal prediction in real-world atmospheric modeling and other high-stakes time-series applications.
- Decomposing Aleatoric and Epistemic Uncertainty: Separating these uncertainty sources is crucial for identifying whether forecasting errors originate from model deficiencies or intrinsic system randomness, which directly informs whether model architecture improvements or better observational coverage is required.

## Links

- [Abstract](https://arxiv.org/abs/2606.27001)
- [PDF](https://arxiv.org/pdf/2606.27001)

