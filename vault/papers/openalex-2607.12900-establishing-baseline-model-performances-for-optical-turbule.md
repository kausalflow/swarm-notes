---
# CSL-compatible fields
title: "Establishing baseline model performances for optical turbulence forecasting"
author:
  - literal: "M. De Sepibus"
  - literal: "E. Masciadri"
  - literal: "C. Weinberger"
  - literal: "C. Veillet"
  - literal: "S. Ragland"
issued:
  date-parts:
    - [2026, 7, 14]
url: "https://arxiv.org/abs/2607.12900"

# Custom fields
paper_id: "2607.12900"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
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
processed_at: "2026-07-17T07:09:44Z"
created_at: "2026-07-17T07:09:44Z"
---

# Establishing baseline model performances for optical turbulence forecasting

**Authors**: M. De Sepibus, E. Masciadri, C. Weinberger, C. Veillet, S. Ragland
**Date**: 2026-07-14
**Paper ID**: [openalex:2607.12900](https://arxiv.org/abs/2607.12900)

## Summary

This paper establishes critical performance baselines for optical turbulence (OT) forecasting, which is essential for maximizing the efficiency of ground-based adaptive optics systems. By evaluating two distinct baseline methods—one for time-averaged parameter forecasting and one for temporal evolution—across multi-year datasets from the Very Large Telescope (VLT) and Large Binocular Telescope (LBT), the study provides reference thresholds for various astroclimatic parameters. The results demonstrate that forecasting performance is inherently context-dependent, relying on the specific site, parameter, and forecast timescale, thereby invalidating absolute benchmarks for OT forecasting models.

## Key Contributions

- Establishes baseline performance thresholds for optical turbulence (OT) forecasting relevant to ground-based adaptive optics.
- Demonstrates that baseline predictive performance varies significantly based on observational site, specific atmospheric parameter, forecast horizon, and target task (mean vs. temporal evolution).
- Argues against absolute performance metrics in OT forecasting, advocating for context-dependent benchmarking.

## Open Questions & Future Work

- [[physical-drivers-of-turbulence-forecast-variability]]

## Archivist Review

The paper provides an empirical study of baseline performance for optical turbulence, which is valuable but does not introduce a novel forecasting mechanism or representation that requires a permanent concept entry. The proposed open question regarding physical drivers of forecast variability is a substantial unresolved research direction in the field of astroclimatic time-series forecasting. No specific datasets were proposed for independent vault entry as the ones mentioned are broad, site-specific records rather than standardized benchmarks.

### Approved Open Questions
- Physical drivers of turbulence forecasting variability: Understanding the physical drivers of forecast performance variability is critical to determine if site-specific forecasting improvements are possible or if performance is fundamentally limited by local atmospheric dynamics.

### Rejected Candidates
- [open_question] Physical drivers of turbulence forecasting variability (`physical-drivers-of-turbulence-forecast-variability`) - other: Re-submitted, approved as is.

## Links

- [Abstract](https://arxiv.org/abs/2607.12900)
- [PDF](https://arxiv.org/pdf/2607.12900)

