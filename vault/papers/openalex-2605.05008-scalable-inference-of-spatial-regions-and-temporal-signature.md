---
# CSL-compatible fields
title: "Scalable inference of spatial regions and temporal signatures from time series"
author:
  - literal: "Jiayu Weng"
  - literal: "Alec Kirkley"
issued:
  date-parts:
    - [2026, 5, 6]
url: "https://arxiv.org/abs/2605.05008"

# Custom fields
paper_id: "2605.05008"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "spatial-analysis"
architectures:
  []
datasets:
  []
concept_slugs:
  - "mdl-based-regionalization"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-09T07:01:44Z"
created_at: "2026-05-09T07:01:44Z"
---

# Scalable inference of spatial regions and temporal signatures from time series

**Authors**: Jiayu Weng, Alec Kirkley
**Date**: 2026-05-06
**Paper ID**: [openalex:2605.05008](https://arxiv.org/abs/2605.05008)

## Summary

This paper introduces an efficient, nonparametric framework for the regionalization of spatial time series using the minimum description length (MDL) principle. Unlike traditional clustering methods that often require an a priori specification of the number of regions or rely on ad hoc spatial regularization, this approach jointly infers contiguous spatial partitions and representative temporal archetypes. The method achieves log-linear runtime complexity, making it scalable to large spatiotemporal datasets. Experimental results on synthetic and real-world air quality and vegetation data demonstrate the method's ability to extract interpretable, data-driven structural regularities.

## Key Contributions

- Proposes a fully nonparametric, MDL-based framework for spatiotemporal regionalization that avoids a priori constraints on the number of regions.
- Introduces a joint inference approach for spatial partitioning and representative time series "drivers" with log-linear runtime complexity.
- Demonstrates superior recovery of structural regularities in large-scale empirical air quality and vegetation index data compared to traditional methods.

## Open Questions & Future Work

- [[multivariate-spatiotemporal-regionalization]]

## Key Concepts

- [[mdl-based-regionalization]]: A nonparametric spatial regionalization framework that uses the minimum description length principle to jointly infer spatial partitions and representative time series archetypes.

## Archivist Review

The paper introduces a novel application of the Minimum Description Length (MDL) principle to achieve nonparametric, log-linear regionalization of spatiotemporal data. The MDL-based regionalization concept is approved for its principled approach to avoiding ad-hoc regularization. The multivariate extension open question is approved as it addresses a key limitation in current spatiotemporal clustering research. Other candidates were rejected to maintain the required scarcity of the knowledge vault.

### Approved Concepts
- Minimum Description Length Based Regionalization: Provides a principled, nonparametric alternative to ad hoc regularization methods for spatiotemporal partitioning.

### Approved Open Questions
- Multivariate Spatiotemporal Regionalization Frameworks: Many real-world spatiotemporal processes are driven by the interaction of multiple variables; a univariate approach is limited in capturing such complex relationships.

## Links

- [Abstract](https://arxiv.org/abs/2605.05008)
- [PDF](https://arxiv.org/pdf/2605.05008)

