---
# CSL-compatible fields
title: "Causal-TS: A Python Library for Causal Discovery in High-Dimensional and Nonstationary Time Series"
author:
  - literal: "M. Fesanghary"
issued:
  date-parts:
    - [2026, 7, 27]
url: "https://arxiv.org/abs/2607.24673"

# Custom fields
paper_id: "2607.24673"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "causality"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-30T07:26:08Z"
created_at: "2026-07-30T07:26:08Z"
---

# Causal-TS: A Python Library for Causal Discovery in High-Dimensional and Nonstationary Time Series

**Authors**: M. Fesanghary
**Date**: 2026-07-27
**Paper ID**: [openalex:2607.24673](https://arxiv.org/abs/2607.24673)

## Summary

Causal-TS is an open-source Python library designed for causal discovery in high-dimensional and nonstationary multivariate time series. It integrates four specialized algorithms along with traditional baselines, built on top of a GPU-accelerated conditional independence testing layer. The library features a comprehensive regime discovery pipeline for handling structural breaks and offers end-to-end support ranging from synthetic data generation to downstream causal effect estimation via DoWhy.

## Key Contributions

- Introduces Causal-TS, an open-source Python library for causal discovery in high-dimensional and nonstationary multivariate time series.
- Provides four specialized algorithms (CDNOTS, CDNOTS+, CEDAR, and GRACE) alongside standard baseline wrappers sharing a unified GPU-accelerated conditional independence test layer.
- Implements a regime discovery pipeline that detects structural breaks via pluggable changepoint detectors and runs causal discovery per regime.
- Features an end-to-end pipeline with a command-line interface, synthetic data generators, and optional DoWhy integration for causal effect estimation.

## Archivist Review

Reviewed the single candidate concept 'Causal-TS'. Because it represents a software library rather than a fundamental algorithmic primitive or theoretical mechanism, it was rejected in accordance with vault standards. No open questions or datasets were provided.

### Rejected Candidates
- [concept] Causal-TS (`causal-ts`) - low_impact: Software libraries and toolkits do not qualify as permanent standalone conceptual vault notes unless they introduce a fundamentally new algorithmic primitive or theoretical framework.

## Links

- [Abstract](https://arxiv.org/abs/2607.24673)
- [PDF](https://arxiv.org/pdf/2607.24673)

