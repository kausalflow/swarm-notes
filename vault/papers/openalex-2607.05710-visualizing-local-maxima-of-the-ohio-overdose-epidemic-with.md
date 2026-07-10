---
# CSL-compatible fields
title: "Visualizing Local Maxima of the Ohio overdose epidemic with Vineyards"
author:
  - literal: "Nicholas Bermingham"
  - literal: "David White"
  - literal: "Nathan Willey"
issued:
  date-parts:
    - [2026, 7, 7]
url: "https://arxiv.org/abs/2607.05710"

# Custom fields
paper_id: "2607.05710"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "vineyards-in-topological-data-analysis"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-10T08:16:04Z"
created_at: "2026-07-10T08:16:04Z"
---

# Visualizing Local Maxima of the Ohio overdose epidemic with Vineyards

**Authors**: Nicholas Bermingham, David White, Nathan Willey
**Date**: 2026-07-07
**Paper ID**: [openalex:2607.05710](https://arxiv.org/abs/2607.05710)

## Summary

This paper investigates the application of vineyards, a topological data analysis (TDA) tool, for modeling and visualizing the evolution of spatiotemporal patterns in public health data. The authors propose statistical tests to evaluate the suitability of using vineyards for a given dataset and verify the significance of identified topological features. The methodology is applied to analyze drug overdose death trends in Ohio, effectively visualizing the temporal development of localized epidemic hotspots.

## Key Contributions

- Proposed a statistical testing framework to assess the suitability of using vineyards for spatiotemporal dataset analysis.
- Demonstrated the use of vineyards to visualize and track the evolution of overdose hotspots in Ohio over time.
- Developed statistical tests to verify the significance of topological features extracted from vineyard diagrams.

## Open Questions & Future Work

- [[tda-forecasting-covariates]]

## Key Concepts

- [[vineyards-in-topological-data-analysis]]: A topological data analysis technique that tracks the evolution of local hotspots in spatiotemporal datasets over time.

## Archivist Review

I approved the concept of 'Vineyards' in TDA as it introduces a distinct topological lens for time-series analysis that is likely to be reusable in other spatiotemporal monitoring contexts. The open question regarding covariate integration is approved because it addresses a fundamental limitation in transitioning TDA from descriptive visualization to predictive modeling. Other potential candidates were rejected for being overly domain-specific or lacking sufficient generalizability.

### Approved Concepts
- Vineyards in Topological Data Analysis: This paper formalizes the application of vineyards to spatiotemporal public health data, providing a new methodological bridge between TDA and time-series analysis.

### Approved Open Questions
- Integrating Covariates in TDA Forecasting: Current TDA forecasting methods are limited by their focus on internal topological properties; integrating domain-specific covariates is essential for moving from descriptive topological analysis to actionable, policy-relevant predictive tools.

## Links

- [Abstract](https://arxiv.org/abs/2607.05710)
- [PDF](https://arxiv.org/pdf/2607.05710)

