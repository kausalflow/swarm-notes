---
# CSL-compatible fields
title: "Joint Retrieval of Radial Wind, Terminal Fall Velocity, and Median Diameter From Single-Polarization Fast-Scanning Weather Radar"
author:
  - literal: "Tworit Dash"
  - literal: "Hans Driessen"
  - literal: "Oleg A. Krasnov"
  - literal: "Alexander G. Yarovoy"
issued:
  date-parts:
    - [2026, 8, 3]
url: "https://arxiv.org/abs/2608.02364"

# Custom fields
paper_id: "2608.02364"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-06T07:32:40Z"
created_at: "2026-08-06T07:32:40Z"
---

# Joint Retrieval of Radial Wind, Terminal Fall Velocity, and Median Diameter From Single-Polarization Fast-Scanning Weather Radar

**Authors**: Tworit Dash, Hans Driessen, Oleg A. Krasnov, Alexander G. Yarovoy
**Date**: 2026-08-03
**Paper ID**: [openalex:2608.02364](https://arxiv.org/abs/2608.02364)

## Summary

This paper addresses the inverse problem of precipitation retrieval using Doppler power spectral density measurements from a fast-scanning single-polarization weather radar under short coherent processing intervals. By treating gamma drop-size distribution parameters as latent intermediate variables rather than primary targets due to weak identifiability, the method stably estimates radial wind, terminal fall velocity, and median volume diameter. Both simulated and real-data experiments—including spatial likelihood pooling and comparisons with ground disdrometers—demonstrate the effectiveness of the proposed spectral forward model approach.

## Key Contributions

- Addresses the inverse problem of precipitation retrieval from Doppler power spectral density measurements using a fast-scanning single-polarization X-band weather radar under short coherent processing intervals.
- Demonstrates that gamma drop-size distribution parameters exhibit weak identifiability as primary retrieval products, motivating their role as latent intermediate variables within a spectral forward model.
- Formulates stable derived quantities including radial-wind mean, spectral width, reflectivity-weighted terminal fall velocity, and median volume diameter.
- Validates the approach using simulated data and real-data experiments involving same-scan spatial likelihood pooling and multi-scan time-series comparisons against ground disdrometers.

## Limitations

Radar-disdrometer discrepancies remain physically meaningful even under reasonable spectral fits and temporal evolution.

## Archivist Review

Applied strict scarcity and reusability criteria. The open question regarding weather radar clutter suppression is too domain-specific and narrow to warrant a permanent vault entry. No concepts or datasets met the threshold for inclusion.

### Rejected Candidates
- [open_question] Clutter-Aware Precipitation Spectrum Recovery (`clutter-aware-precipitation-recovery`) - paper_local: Paper-specific future work on radar clutter suppression near zero Doppler bins without broad methodological generalizability across time series forecasting or general machine learning.

## Links

- [Abstract](https://arxiv.org/abs/2608.02364)
- [PDF](https://arxiv.org/pdf/2608.02364)

