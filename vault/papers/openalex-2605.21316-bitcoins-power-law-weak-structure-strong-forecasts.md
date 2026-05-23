---
# CSL-compatible fields
title: "Bitcoin's Power Law: Weak Structure, Strong Forecasts"
author:
  - literal: "Carlos Baquero"
  - literal: "Raquel Menezes"
issued:
  date-parts:
    - [2026, 5, 20]
url: "https://arxiv.org/abs/2605.21316"

# Custom fields
paper_id: "2605.21316"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "fit-prediction-tradeoff-in-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-23T07:25:26Z"
created_at: "2026-05-23T07:25:26Z"
---

# Bitcoin's Power Law: Weak Structure, Strong Forecasts

**Authors**: Carlos Baquero, Raquel Menezes
**Date**: 2026-05-20
**Paper ID**: [openalex:2605.21316](https://arxiv.org/abs/2605.21316)

## Summary

This paper evaluates the validity of the power law hypothesis for Bitcoin price evolution by testing its structural and predictive robustness. The authors find that while the power law is not a structurally sound descriptor of the data—failing tests for specification robustness—it paradoxically serves as a superior long-horizon forecaster (12-24 months) compared to more complex descriptive models. The work highlights a fundamental fit-prediction tradeoff, where sophisticated models that accurately capture historical wave shapes perform poorly when extrapolated over long durations.

## Key Contributions

- Demonstrates that Bitcoin price series exhibits a distinct cross-asset separation where simple power law models outperform complex descriptive growth curves in 12-24 month horizon forecasts.
- Introduces three principled time-domain adaptations of the Clauset-Shalizi-Newman protocol to test structural specification robustness of power law claims.
- Shows that while the simple power law model lacks formal structural validity (e.g., it is not specification-robust), it dominates standard baselines like ARIMA and ETS in long-term forecasting due to its aversion to committing to transient wave shapes.

## Open Questions & Future Work

- [[generative-mechanisms-for-complex-growth-waves]]

## Key Concepts

- [[fit-prediction-tradeoff-in-forecasting]]: A phenomenon where models optimizing for historical structural fit perform worse in long-horizon forecasting than simpler, less descriptive global trend models.

## Archivist Review

I have approved the core 'Fit-prediction Tradeoff' concept as it represents a vital, recurring theme in time-series forecasting where in-sample model complexity often hurts long-horizon reliability. I also approved one open question concerning the search for generative mechanisms for observed complex growth structures, as this is a fundamental theoretical challenge for time-series modeling. Other candidates were rejected either due to being too paper-specific, lacking sufficient impact, or being redundant with broader, more standardized research questions.

### Approved Concepts
- Fit-prediction Tradeoff in Forecasting: Highlights a fundamental forecasting phenomenon where descriptive in-sample accuracy, particularly with complex curves like sigmoids, often correlates with poor generalization over long horizons compared to simpler, robust global trends.

### Approved Open Questions
- Generative mechanisms for growth waves: Understanding these mechanisms is necessary to distinguish between structural properties of asset adoption and transient historical artifacts.

### Rejected Candidates
- [open_question] Generative mechanism for wave structure (`bitcoin-wave-structure-generative-mechanism`) - duplicate_existing: The concept is redundant with the approved question on generative mechanisms, and the approved slug is more descriptive and generalized.
- [open_question] Series-specific null models for comparison (`cross-series-structural-comparison-baselines`) - low_impact: The proposed research direction is essentially a localized request for more robust statistical testing, which is standard procedure rather than a central, long-lived open research bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2605.21316)
- [PDF](https://arxiv.org/pdf/2605.21316)

