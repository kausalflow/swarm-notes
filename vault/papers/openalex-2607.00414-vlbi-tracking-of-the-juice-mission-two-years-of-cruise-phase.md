---
# CSL-compatible fields
title: "VLBI Tracking of the JUICE Mission: Two Years of Cruise Phase Operations and Performance Analysis"
author:
  - literal: "O. R. White"
  - literal: "Guifré Molera Calvés"
  - literal: "Jasper Edwards"
  - literal: "Giuseppe Cimò"
  - literal: "Dominic Dirkx"
issued:
  date-parts:
    - [2026, 7, 1]
url: "https://arxiv.org/abs/2607.00414"

# Custom fields
paper_id: "2607.00414"
paper_source: "openalex"
domain: "robotics"
tags:
  - "time-series"
  - "robotics"
architectures:
  []
datasets:
  []
concept_slugs:
  - "doppler-residual-characterisation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-04T07:37:59Z"
created_at: "2026-07-04T07:37:59Z"
---

# VLBI Tracking of the JUICE Mission: Two Years of Cruise Phase Operations and Performance Analysis

**Authors**: O. R. White, Guifré Molera Calvés, Jasper Edwards, Giuseppe Cimò, Dominic Dirkx
**Date**: 2026-07-01
**Paper ID**: [openalex:2607.00414](https://arxiv.org/abs/2607.00414)

## Summary

This paper analyzes two years of Very Long Baseline Interferometry (VLBI) tracking data for the ESA JUICE mission during its cruise phase toward Jupiter. The authors demonstrate that VLBI provides crucial geometric diversity and precision for orbit determination, complementing existing tracking infrastructure. The work encompasses Doppler residual characterization, performance indicator extraction, and the application of radio tracking to solar wind scintillation analysis and space weather monitoring.

## Key Contributions

- Characterizes over 100 VLBI tracking sessions of the JUICE mission during its first two years of cruise.
- Demonstrates the utility of VLBI networks for precision orbit determination and spacecraft health diagnosis.
- Provides a Southern Hemisphere-based complement to traditional deep space tracking infrastructure.

## Key Concepts

- [[doppler-residual-characterisation]]: A methodology for analyzing radio frequency variations along a signal path to isolate spacecraft orbital and performance anomalies.

## Archivist Review

The paper details the use of VLBI for deep space navigation. I have approved 'Doppler residual characterisation' as it represents a core technique for state estimation and anomaly detection in aerospace time-series analysis. Other proposed concepts were rejected as they are either application-specific goals or belong to the domain of radio astronomy rather than generalizable ML methodology.

### Approved Concepts
- Doppler residual characterisation: Serves as a fundamental approach for precision orbit determination and spacecraft state estimation in deep space navigation.

### Rejected Candidates
- [concept] Mission performance indicator extraction (`mission-performance-indicator-extraction`) - not_novel: This is an application-specific analytical goal rather than a distinct, reusable methodology.
- [concept] Solar wind scintillation pattern analysis (`solar-wind-scintillation-pattern-analysis`) - not_reusable: This is a domain-specific scientific analysis technique belonging to radio astronomy/space physics rather than a general-purpose ML concept.

## Links

- [Abstract](https://arxiv.org/abs/2607.00414)
- [PDF](https://arxiv.org/pdf/2607.00414)

