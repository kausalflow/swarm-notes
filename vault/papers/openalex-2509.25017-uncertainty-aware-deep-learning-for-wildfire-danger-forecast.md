---
# CSL-compatible fields
title: "Uncertainty-aware deep learning for wildfire danger forecasting"
author:
  - literal: "Spyros Kondylatos"
  - literal: "Gustau Camps‐Valls"
  - literal: "Ioannis Papoutsis"
issued:
  date-parts:
    - [2026, 7, 13]
url: "https://arxiv.org/abs/2509.25017"

# Custom fields
paper_id: "2509.25017"
paper_source: "openalex"
domain: "time-series,"
tags:
  - "time-series,"
  - "forecasting,"
  - "uncertainty-quantification,"
architectures:
  []
datasets:
  []
concept_slugs:
  - "uncertainty-aware-wildfire-forecasting-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-16T07:14:20Z"
created_at: "2026-07-16T07:14:20Z"
---

# Uncertainty-aware deep learning for wildfire danger forecasting

**Authors**: Spyros Kondylatos, Gustau Camps‐Valls, Ioannis Papoutsis
**Date**: 2026-07-13
**Paper ID**: [openalex:2509.25017](https://arxiv.org/abs/2509.25017)

## Summary

This paper proposes an uncertainty-aware deep learning framework designed to improve the reliability of wildfire danger forecasting by jointly modeling epistemic and aleatoric uncertainties. The approach enhances predictive performance metrics—such as F1 score and Expected Calibration Error—compared to deterministic baselines. By analyzing uncertainty dynamics over a ten-day horizon, the study reveals distinct behaviors between model and data uncertainty, offering a mechanism for creating trustworthy, uncertainty-calibrated wildfire danger maps for decision support.

## Key Contributions

- Introduces a joint epistemic and aleatoric uncertainty-aware DL framework for wildfire danger prediction.
- Achieves a 2.3% F1 score improvement and 2.1% Expected Calibration Error (ECE) reduction over deterministic baselines for next-day forecasting.
- Demonstrates that aleatoric uncertainty grows with lead time while epistemic uncertainty remains stable, providing actionable insights for longer-term (up to 10-day) hazard planning.

## Open Questions & Future Work

- [[uncertainty-disentanglement-limits]]

## Key Concepts

- [[uncertainty-aware-wildfire-forecasting-framework]]: A deep learning framework for wildfire danger forecasting that performs joint epistemic and aleatoric uncertainty quantification to improve predictive reliability.

## Archivist Review

I approved the uncertainty-aware framework and the open question regarding disentanglement. The concepts reflect a reusable methodology for environmental forecasting, and the open question addresses a fundamental limitation in uncertainty quantification models. No datasets were approved as none were specifically named or centralized in the research claims.

### Approved Concepts
- Uncertainty-aware Deep Learning for Wildfire Danger Forecasting: The framework provides a dual-source uncertainty decomposition (epistemic and aleatoric) specifically tailored for wildfire risk, which is critical for trustworthy decision-making in environmental hazards.

### Approved Open Questions
- Reliable Disentanglement of Uncertainties: Effective disentanglement is critical for downstream decision-making: epistemic uncertainty suggests the need for more data or better model architecture, whereas aleatoric uncertainty highlights irreducible noise in the system that requires different management strategies.

## Links

- [Abstract](https://arxiv.org/abs/2509.25017)
- [PDF](https://arxiv.org/pdf/2509.25017)

