---
# CSL-compatible fields
title: "High-resolution Calibrated Probabilistic Hourly Precipitation from a Deterministic Forecast"
author:
  - literal: "Thomas M. Hamill"
issued:
  date-parts:
    - [2026, 8, 13]
url: "https://arxiv.org/abs/2608.12685"

# Custom fields
paper_id: "2608.12685"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "attention-mechanism"
  - "evaluation"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-16T05:18:00Z"
created_at: "2026-08-16T05:18:00Z"
---

# High-resolution Calibrated Probabilistic Hourly Precipitation from a Deterministic Forecast

**Authors**: Thomas M. Hamill
**Date**: 2026-08-13
**Paper ID**: [openalex:2608.12685](https://arxiv.org/abs/2608.12685)

## Summary

This paper describes an Attention Residual U-Net method for probabilistic quantitative precipitation forecasting (PQPF) that predicts the hourly probability of precipitation alongside positive precipitation distributions modeled via a mixture of two Gamma distributions. Trained on numerical weather prediction outputs from GRAF and GFS models using NOAA MRMS radar data as targets, the network optimizes negative log-likelihood with climatological initialization. Applied across the contiguous United States, the model generates spatially detailed, highly reliable, and skillful probabilistic forecasts, particularly in regions with complex terrain variation.

## Key Contributions

- Proposes an Attention Residual U-Net for probabilistic quantitative precipitation forecasting (PQPF) using numerical weather prediction inputs
- Predicts hourly precipitation probability and positive precipitation distribution using a weighted mixture of two Gamma distributions
- Demonstrates reliable and skillful forecasts across the contiguous United States (CONUS) with superior performance over simpler reference methods and climatology

## Archivist Review

Applied rigorous selection standards, rejecting domain-specific weather forecasting features and questions that lack broad reuse across general machine learning and time-series forecasting.

### Rejected Candidates
- [open_question] Optimal Feature Selection for PQPF (`optimal-feature-selection-and-lagged-ensembles-for-pqpf`) - low_impact: Too domain-specific to weather post-processing and peripheral to general time-series methodology.

## Links

- [Abstract](https://arxiv.org/abs/2608.12685)
- [PDF](https://arxiv.org/pdf/2608.12685)

