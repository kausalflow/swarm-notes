---
# CSL-compatible fields
title: "FoReco and FoRecoML: A Unified Toolbox for Forecast Reconciliation in R"
author:
  - literal: "Daniele Girolimetto"
  - literal: "Jeroen Rombouts"
  - literal: "Ines Wilms"
  - literal: "Yangzhuoran Fin Yang"
issued:
  date-parts:
    - [2026, 4, 30]
url: "https://arxiv.org/abs/2604.27696"

# Custom fields
paper_id: "2604.27696"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "forecast-reconciliation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-03T07:14:02Z"
created_at: "2026-05-03T07:14:02Z"
---

# FoReco and FoRecoML: A Unified Toolbox for Forecast Reconciliation in R

**Authors**: Daniele Girolimetto, Jeroen Rombouts, Ines Wilms, Yangzhuoran Fin Yang
**Date**: 2026-04-30
**Paper ID**: [openalex:2604.27696](https://arxiv.org/abs/2604.27696)

## Summary

The paper introduces two R packages, FoReco and FoRecoML, designed to bridge the gap in comprehensive software tools for forecast reconciliation. While FoReco focuses on classical and regression-based linear methods, FoRecoML provides a unified interface for non-linear, machine learning-based reconciliation techniques. Together, these tools support cross-sectional, temporal, and cross-temporal hierarchical structures, offering both simplified default settings and extensive customization for researchers and practitioners.

## Key Contributions

- Introduces FoReco, an R package implementing classical and regression-based linear forecast reconciliation methods for cross-sectional, temporal, and cross-temporal hierarchies.
- Introduces FoRecoML, an R package providing a unified machine learning interface for non-linear forecast reconciliation.
- Provides a comprehensive framework that integrates cross-sectional, temporal, and cross-temporal reconciliation into a single software suite.

## Key Concepts

- [[forecast-reconciliation]]: A process of adjusting independent forecasts of linearly constrained time series to ensure they satisfy underlying hierarchical or grouped relationships.

## Archivist Review

I approved the central concept of 'Forecast Reconciliation' because it is a foundational methodology in hierarchical time series analysis. I rejected the R packages FoReco and FoRecoML as they are implementation tools and not distinct, reusable architectural or methodological concepts. No open questions or datasets were provided or warranted by the content.

### Approved Concepts
- Forecast Reconciliation: The paper introduces a unified software framework for the established but fragmented field of forecast reconciliation.

### Rejected Candidates
- [concept] FoReco R Package (`foreco-r-package`) - paper_local: This is a software-specific implementation package rather than a methodological concept.
- [concept] FoRecoML R Package (`forecoml-r-package`) - paper_local: This is a software-specific implementation package rather than a methodological concept.

## Links

- [Abstract](https://arxiv.org/abs/2604.27696)
- [PDF](https://arxiv.org/pdf/2604.27696)

