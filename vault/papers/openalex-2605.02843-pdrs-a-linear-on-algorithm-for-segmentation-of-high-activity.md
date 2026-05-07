---
# CSL-compatible fields
title: "PDRS : A Linear O(N) Algorithm for Segmentation of High-Activity Regions in Irregularly Sampled Time Series"
author:
  - literal: "Atal Agrawal"
issued:
  date-parts:
    - [2026, 5, 4]
url: "https://arxiv.org/abs/2605.02843"

# Custom fields
paper_id: "2605.02843"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  - "pdrs-peak-driven-region-segmentation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-07T07:37:20Z"
created_at: "2026-05-07T07:37:20Z"
---

# PDRS : A Linear O(N) Algorithm for Segmentation of High-Activity Regions in Irregularly Sampled Time Series

**Authors**: Atal Agrawal
**Date**: 2026-05-04
**Paper ID**: [openalex:2605.02843](https://arxiv.org/abs/2605.02843)

## Summary

The paper introduces Peak-Driven Region Segmentation (PDRS), an O(N) algorithm designed for fast identification of high-activity regions in irregularly sampled time series. By utilizing a gradient-aware multi-source breadth-first search initiated at statistically significant local maxima, PDRS efficiently partitions data while suppressing noise via saddle-point merging. The approach offers a scalable alternative to O(N^2) Bayesian methods, maintaining comparable accuracy for astronomical light curve analysis while remaining applicable to broader domains like seismic and industrial monitoring.

## Key Contributions

- Introduces PDRS, a linear-time O(N) algorithm for segmenting high-activity episodes in irregularly sampled time series.
- Reduces computational complexity from O(N^2) (standard Bayesian Blocks approach) to O(N), enabling analysis of high-volume astronomical datasets.
- Demonstrates performance comparable to Bayesian Blocks on SDSS Stripe 82 and ZTF DR23 datasets at significantly lower computational cost.

## Open Questions & Future Work

- [[automated-pdrs-parameter-tuning]]

## Key Concepts

- [[pdrs-peak-driven-region-segmentation]]: A linear-time algorithm for identifying and segmenting high-activity regions in irregularly sampled time series by seeding candidates at local maxima and employing a gradient-aware multi-source BFS.

## Archivist Review

I approved the core segmentation algorithm as it provides a clear, reusable, and computationally superior alternative to standard O(N^2) methods for irregular time series. I also approved the open question regarding automated parameter tuning, as it addresses a key usability barrier for deploying such signal processing algorithms in automated, high-volume environments. Routine survey datasets were rejected as they do not meet the criteria for critical, reusable benchmark references.

### Approved Concepts
- Peak-Driven Region Segmentation (PDRS): It provides an efficient O(N) alternative to existing O(N^2) segmentation methods for irregularly sampled signals.

### Approved Open Questions
- Automated PDRS Parameter Tuning: Automating hyperparameter selection would enhance the algorithm's scalability and reduce the burden of manual configuration when deploying the tool across heterogeneous domains.

### Rejected Candidates
- [dataset] SDSS Stripe 82 (`sdss-stripe-82`) - low_impact: Routine astronomical survey dataset, not sufficiently unique to justify a standalone note.
- [dataset] ZTF DR23 (`ztf-dr23`) - low_impact: Routine astronomical survey dataset, not sufficiently unique to justify a standalone note.

## Links

- [Abstract](https://arxiv.org/abs/2605.02843)
- [PDF](https://arxiv.org/pdf/2605.02843)

