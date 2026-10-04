---
# CSL-compatible fields
title: "ANOVATS: a subsampling-based test to detect differences among short time series in marine studies"
author:
  - literal: "Yuichi Goto"
  - literal: "Hiroko Kato Solvang"
  - literal: "Masanobu Taniguchi"
  - literal: "Tone Falkenhaug"
issued:
  date-parts:
    - [2026, 10, 3]
url: "https://arxiv.org/abs/2511.08070"

# Custom fields
paper_id: "2511.08070"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "anovats"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-04T10:48:47Z"
created_at: "2026-10-04T10:48:47Z"
---

# ANOVATS: a subsampling-based test to detect differences among short time series in marine studies

**Authors**: Yuichi Goto, Hiroko Kato Solvang, Masanobu Taniguchi, Tone Falkenhaug
**Date**: 2026-10-03
**Paper ID**: [openalex:2511.08070](https://arxiv.org/abs/2511.08070)

## Summary

This paper introduces ANOVATS, a novel subsampling-based ANOVA framework designed to detect regional differences in small-sample time series data without requiring spectral density estimation. The method overcomes limitations inherent in classical asymptotic time series techniques when applied to short observational records spanning only a few decades. Additionally, a post hoc grouping procedure is proposed to cluster areas based on homogeneity test results. Empirical evaluation on zooplankton biomass data from the North Sea demonstrates its capability to quantify regional ecosystem differences without requiring prior expert knowledge.

## Key Contributions

- Introduces ANOVATS (ANOVA for small-sample time series data), a subsampling-based statistical test designed to detect regional differences among short time series without requiring spectral density estimation.
- Devises a post hoc grouping procedure following the ANOVATS homogeneity test to cluster geographical or regional areas.
- Demonstrates the method's effectiveness on zooplankton biomass data from the North Sea, successfully identifying species differences across regions without relying on expert prior knowledge.

## Limitations

Limited to small-sample time series data with a fixed number of groups.

## Open Questions & Future Work

- [[anovats-post-hoc-clustering-theory]]

## Key Concepts

- [[anovats]]: A subsampling-based ANOVA method to detect regional differences in short time series data without spectral density estimation.

## Archivist Review

Approved the core ANOVATS concept and its theoretical open question regarding post hoc clustering guarantees for short time series. No datasets met the threshold for vault inclusion since the North Sea zooplankton data is a domain-specific case study rather than a standard benchmark.

### Approved Concepts
- ANOVATS: Introduces a novel subsampling-based ANOVA framework specifically tailored for short time series data without requiring spectral density estimation.

### Approved Open Questions
- Theoretical Guarantees for Post-ANOVATS Clustering: Crucial for providing theoretical validity and error control when grouping marine strata or other spatial regions after rejecting the global null hypothesis.

## Links

- [Abstract](https://arxiv.org/abs/2511.08070)
- [PDF](https://arxiv.org/pdf/2511.08070)

