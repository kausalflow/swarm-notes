---
# CSL-compatible fields
title: "Comparison of probabilistic nowcasts and forecasts of SARS-CoV-2 variant proportions made by hierarchical multinomial linear regression models"
author:
  - literal: "Isaac MacArthur"
  - literal: "Thomas Robacker"
  - literal: "Evan L. Ray"
  - literal: "Benjamin Rogers"
  - literal: "Nicholas G. Reich"
  - literal: "Maryclare Griffin"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.22676"

# Custom fields
paper_id: "2605.22676"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  - "us-sars-cov-2-variant-nowcast-hub"
concept_slugs:
  []
dataset_slugs:
  - "us-sars-cov-2-variant-nowcast-hub"
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:46:47Z"
created_at: "2026-05-24T07:46:47Z"
---

# Comparison of probabilistic nowcasts and forecasts of SARS-CoV-2 variant proportions made by hierarchical multinomial linear regression models

**Authors**: Isaac MacArthur, Thomas Robacker, Evan L. Ray, Benjamin Rogers, Nicholas G. Reich, Maryclare Griffin
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.22676](https://arxiv.org/abs/2605.22676)

## Summary

This paper evaluates the performance of hierarchical multinomial logistic regression (HMLR) models for the nowcasting and forecasting of circulating SARS-CoV-2 variant proportions. By leveraging two years of retrospective data from the US SARS-CoV-2 Variant Nowcast Hub, the authors demonstrate that HMLR models provide improved probabilistic and point accuracy compared to baseline models. The results indicate that model complexity should be adapted to the available data density, as more complex HMLR configurations excel in high-data regions while simpler models are more robust in data-sparse settings.

## Key Contributions

- Defined a class of Hierarchical Multinomial Logistic Regression (HMLR) models specifically for SARS-CoV-2 variant nowcasting and forecasting.
- Evaluated 12 HMLR models against a baseline using two years of weekly retrospective data (2022–2024) from the US SARS-CoV-2 Variant Nowcast Hub.
- Demonstrated that HMLR models outperform baselines in data-rich locations, while simpler HMLR variants exhibit superior performance in low-data environments.

## Open Questions & Future Work

- [[correlated-coefficients-in-hierarchical-forecasting]]

## Archivist Review

The paper evaluates hierarchical multinomial logistic regression (HMLR) for disease variant forecasting. I approved the US SARS-CoV-2 Variant Nowcast Hub as a central dataset and included a refined version of the open question regarding coefficient correlation, as it touches on a fundamental limitation of hierarchical modeling in non-stationary disease surveillance. No specific HMLR mechanism was approved as a concept, as these models are established statistical methods rather than novel machine learning architectures.

### Approved Open Questions
- Correlated coefficients in HMLR: This addresses a significant constraint in current hierarchical forecasting frameworks used for disease surveillance and has the potential to enhance performance where data is sparse.

### Rejected Candidates
- [open_question] Correlated coefficients in HMLR (`hmlr-correlated-coefficients-future-work`) - duplicate_existing: Renamed to a more canonical, descriptive slug and improved the background statement to be more universal.

## Datasets

- [[us-sars-cov-2-variant-nowcast-hub]]

## Links

- [Abstract](https://arxiv.org/abs/2605.22676)
- [PDF](https://arxiv.org/pdf/2605.22676)

