---
# CSL-compatible fields
title: "Near real-time monitoring of global land-ocean cover dynamics"
author:
  - literal: "Lixing Wang"
  - literal: "Tao E. Li"
  - literal: "Xinyu Dou"
  - literal: "Zhu Liu"
issued:
  date-parts:
    - [2026, 4, 7]
url: "https://arxiv.org/abs/2604.05384"

# Custom fields
paper_id: "2604.05384"
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
  - "earth-system-safety-threshold-monitoring"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-10T06:27:27Z"
created_at: "2026-04-10T06:27:27Z"
---

# Near real-time monitoring of global land-ocean cover dynamics

**Authors**: Lixing Wang, Tao E. Li, Xinyu Dou, Zhu Liu
**Date**: 2026-04-07
**Paper ID**: [openalex:2604.05384](https://arxiv.org/abs/2604.05384)

## Summary

This paper introduces an integrated monitoring framework to track global land-ocean cover dynamics with 5-day temporal resolution using multi-source remote sensing data. By generating a 2018-2025 time series, the authors perform a coupled analysis of land vegetation and sea ice coverage, uncovering significant regional and latitudinal patterns. The study further quantifies the proximity of key ecological indicators to Earth system safety thresholds, demonstrating that both forest cover and Arctic sea ice are approaching critical limits. This approach serves as a robust tool for early-warning assessment in climate adaptation and sustainable policymaking.

## Key Contributions

- Developed an integrated global monitoring framework fusing multi-source remote sensing and reanalysis data at 5-day temporal resolution.
- Generated a consistent 2018-2025 time series for both land cover and sea ice, enabling coupled analysis.
- Identified that global forest cover (~60%) and September Arctic sea ice (23%) are approaching critical safety thresholds, providing actionable data for climate policy.

## Key Concepts

- [[earth-system-safety-threshold-monitoring]]: A monitoring framework that integrates spatiotemporal land-ocean cover dynamics with the quantification of proximity to Earth system safety thresholds.

## Archivist Review

The paper is essentially a domain application; the proposed monitoring approach is useful but represents an application of existing time-series methodology rather than a new algorithmic architecture. I have approved the 'Earth system safety threshold monitoring' concept as it represents a distinct approach to ecological forecasting and early-warning systems that can be reused across climate domains. No specific datasets or open questions were sufficiently novel or reusable to warrant vault entry.

### Approved Concepts
- Earth system safety threshold monitoring: Provides a quantitative framework for early-warning assessment by mapping environmental time-series indicators to established critical planetary safety limits.

### Rejected Candidates
- [concept] Earth system safety thresholds monitoring (`earth-system-safety-thresholds-monitoring`) - duplicate_existing: Renamed to a cleaner slug and title for better vault categorization.

## Links

- [Abstract](https://arxiv.org/abs/2604.05384)
- [PDF](https://arxiv.org/pdf/2604.05384)

