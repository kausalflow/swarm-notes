---
# CSL-compatible fields
title: "Short-term load forecasting under EU-AI Act Requirements in Safety-Critical Environments: Results from a 41-day live challenge on the aggregated German transmission-grid load"
author:
  - literal: "Thomas Bartz-Beielstein"
issued:
  date-parts:
    - [2026, 8, 5]
url: "https://arxiv.org/abs/2608.05018"

# Custom fields
paper_id: "2608.05018"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-08T05:35:08Z"
created_at: "2026-08-08T05:35:08Z"
---

# Short-term load forecasting under EU-AI Act Requirements in Safety-Critical Environments: Results from a 41-day live challenge on the aggregated German transmission-grid load

**Authors**: Thomas Bartz-Beielstein
**Date**: 2026-08-05
**Paper ID**: [openalex:2608.05018](https://arxiv.org/abs/2608.05018)

## Summary

This paper presents results from a 41-day live challenge evaluating a short-term load forecasting pipeline for the aggregated German transmission-grid load under EU-AI Act compliance requirements. Using the open-source spotforecast2-safe library, the pipeline incorporates anomaly detection, gap-aware preprocessing, covariate integration, and recursive multi-step forecasting. Results demonstrate that this compliant, transparent local approach beats the official ENTSO-E day-ahead baseline and performs competitively against 100M-parameter foundation models like chronos-2.

## Key Contributions

- Evaluates a complete short-term load forecasting pipeline on a 41-day live challenge for the aggregated German transmission-grid load.
- Demonstrates that the EU-AI Act compliant spotforecast2-safe pipeline outperforms the official ENTSO-E day-ahead baseline.
- Shows that transparent, low-cost local models (macl2l) are competitive with 100M+ parameter foundation models like chronos-2 while ensuring auditability and compliance.

## Archivist Review

All candidates were rejected because they represent paper-local software packages or administrative/legal interpretation questions rather than core, reusable technical machine learning concepts or fundamental research bottlenecks.

### Rejected Candidates
- [concept] spotforecast2-safe (`spotforecast2-safe`) - paper_local: This is a specific software library implementation and package name rather than a reusable theoretical or algorithmic machine learning concept.
- [open_question] Formalizing Legal Requirements for STLF (`regulatory-requirements-formalization-stlf`) - low_impact: This question pertains to legal and regulatory interpretation of policy frameworks rather than a technical machine learning or forecasting research bottleneck.
- [open_question] Richer Covariates and Weather Ensembles (`richer-covariates-weather-ensembles-stlf`) - low_impact: This is a routine empirical exploration of adding meteorological features and weather ensembles to a forecasting pipeline.

## Links

- [Abstract](https://arxiv.org/abs/2608.05018)
- [PDF](https://arxiv.org/pdf/2608.05018)

