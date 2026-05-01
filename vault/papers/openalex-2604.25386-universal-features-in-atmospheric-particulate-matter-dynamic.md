---
# CSL-compatible fields
title: "Universal Features in Atmospheric Particulate Matter Dynamics"
author:
  - literal: "Suchismita Banerjee"
  - literal: "Koyena Ghosh"
  - literal: "Urna Basu"
  - literal: "Banasri Basu"
issued:
  date-parts:
    - [2026, 4, 28]
url: "https://arxiv.org/abs/2604.25386"

# Custom fields
paper_id: "2604.25386"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  - "exponentially-modified-gaussian-scaling"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-01T07:22:35Z"
created_at: "2026-05-01T07:22:35Z"
---

# Universal Features in Atmospheric Particulate Matter Dynamics

**Authors**: Suchismita Banerjee, Koyena Ghosh, Urna Basu, Banasri Basu
**Date**: 2026-04-28
**Paper ID**: [openalex:2604.25386](https://arxiv.org/abs/2604.25386)

## Summary

This paper investigates the statistical properties of atmospheric PM2.5 concentration fluctuations using six years of daily data from fifty-four Indian cities. The authors discover universal behavior in the residual dynamics after accounting for long-term trends and seasonality, characterized by collapse onto a single exponentially modified Gaussian distribution. They further characterize the dynamics through robust auto-correlation decay and 1/f power spectral densities. A minimal stochastic model is introduced to explain these observed universal features.

## Key Contributions

- Demonstrates that PM2.5 fluctuations across 54 Indian cities exhibit universal statistical behavior in their probability density functions and temporal dynamics.
- Identifies that after trend and seasonal removal, PM2.5 residual fluctuations follow an exponentially modified Gaussian distribution.
- Proposes a minimal stochastic model that successfully recovers observed universal stationary distributions, autocorrelation decay, and 1/f spectral scaling.

## Key Concepts

- [[exponentially-modified-gaussian-scaling]]: A universal distribution model for residual fluctuations in time series data after seasonal and trend removal.

## Archivist Review

I approved the exponentially modified gaussian scaling concept but generalized the name and definition to be a reusable statistical framework for time series residuals. The paper-specific concept was rejected in favor of this broader, more reusable entry. No new datasets or open questions were proposed or approved.

### Approved Concepts
- Exponentially Modified Gaussian Scaling for Time Series: Provides a robust, universal statistical prior for atmospheric and potentially other environmental time-series residuals after trend/seasonality removal.

### Rejected Candidates
- [concept] Exponentially Modified Gaussian PM2.5 Scaling (`exponentially-modified-gaussian-pm2.5-scaling`) - other: Renamed for generality to be more reusable as a statistical concept beyond specific PM2.5 application.

## Links

- [Abstract](https://arxiv.org/abs/2604.25386)
- [PDF](https://arxiv.org/pdf/2604.25386)

