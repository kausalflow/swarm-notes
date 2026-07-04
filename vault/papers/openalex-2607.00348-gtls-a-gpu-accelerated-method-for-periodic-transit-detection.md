---
# CSL-compatible fields
title: "GTLS: A GPU-accelerated method for periodic transit detection"
author:
  - literal: "Quanquan Hu"
  - literal: "Jian Ge"
  - literal: "Luoxi Jin"
  - literal: "Kevin Willis"
issued:
  date-parts:
    - [2026, 7, 1]
url: "https://arxiv.org/abs/2607.00348"

# Custom fields
paper_id: "2607.00348"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "gtls"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-04T07:37:53Z"
created_at: "2026-07-04T07:37:53Z"
---

# GTLS: A GPU-accelerated method for periodic transit detection

**Authors**: Quanquan Hu, Jian Ge, Luoxi Jin, Kevin Willis
**Date**: 2026-07-01
**Paper ID**: [openalex:2607.00348](https://arxiv.org/abs/2607.00348)

## Summary

GTLS is a GPU-accelerated implementation of the Transit Least Squares (TLS) algorithm, designed to handle the massive data volumes of modern photometric surveys by parallelizing time-consuming steps like phase folding, duration evaluation, and chi-squared calculation. Benchmarks on 3000-day light curves show that GTLS provides a speedup of over 20x compared to the standard CPU-based TLS implementation, while maintaining comparable detection precision and recall. This tool effectively bridges the gap between high-sensitivity transit searches and the computational constraints of large-scale astronomical data.

## Key Contributions

- Introduces GTLS, a GPU-accelerated implementation of the Transit Least Squares algorithm that achieves significant speedups over CPU-based counterparts.
- Demonstrates that GTLS processes a 3000-day light curve in 138s (vs 3289s for CPU-based TLS) while maintaining statistically consistent detection performance.
- Shows scalability of GTLS on multi-GPU systems, further reducing runtime for large-scale periodic transit searches.

## Open Questions & Future Work

- [[tls-in-transit-bottleneck-optimization]]

## Key Concepts

- [[gtls]]: A GPU-accelerated implementation of the Transit Least Squares (TLS) algorithm for efficient periodic transit detection in astronomical light curves.

## Archivist Review

I have approved the GTLS framework as it represents a significant, reusable architectural improvement for astronomical transit searches, and the identified open question highlights a substantial and well-defined computational bottleneck in time-series analysis that is likely to persist across future large-scale photometric missions. I rejected the Kepler dataset because it is a routine, well-known, and widely accessible data source in the field that does not require a standalone entry.

### Approved Concepts
- GTLS: It addresses the critical computational bottleneck of searching for planetary transits in high-cadence astronomical photometric surveys by providing a GPU-accelerated alternative to the standard CPU-based Transit Least Squares (TLS) algorithm.

### Approved Open Questions
- Optimizing In-Transit Chi-Squared Calculation: This is a critical bottleneck preventing the scaling of TLS-style searches to the next generation of large-scale, high-cadence photometric surveys. Solving this would directly enable faster pipelines for future missions like PLATO and ET.

## Links

- [Abstract](https://arxiv.org/abs/2607.00348)
- [PDF](https://arxiv.org/pdf/2607.00348)

