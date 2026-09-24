---
# CSL-compatible fields
title: "Toward GPU-Resident Climate Models: A Feasibility Study on Lossy Compression for the Spherical Harmonic Transform's Communication Bottleneck"
author:
  - literal: "Lorenzo Breschi"
  - literal: "Flavio Vella"
issued:
  date-parts:
    - [2026, 9, 21]
url: "https://arxiv.org/abs/2609.24294"

# Custom fields
paper_id: "2609.24294"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "distributed-training"
  - "model-compression"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-24T09:39:20Z"
created_at: "2026-09-24T09:39:20Z"
---

# Toward GPU-Resident Climate Models: A Feasibility Study on Lossy Compression for the Spherical Harmonic Transform's Communication Bottleneck

**Authors**: Lorenzo Breschi, Flavio Vella
**Date**: 2026-09-21
**Paper ID**: [openalex:2609.24294](https://arxiv.org/abs/2609.24294)

## Summary

This paper investigates GPU-resident lossy compression to overcome the communication bottleneck caused by global pencil transpositions in the Spherical Harmonic Transform during operational climate modeling. By combining measured GPU compression throughput with SimGrid network simulations on DYAMOND high-resolution fields, the authors show that ZFP compression at rate-16 matches float16 communication speedup with 1600x lower mean relative error, whereas rate-8 achieves 1.93x greater speedup than float16 while keeping 4x lower error.

## Key Contributions

- Investigates GPU-resident lossy compression to alleviate the communication bottleneck of the Spherical Harmonic Transform in GPU-resident climate models.
- Demonstrates via SimGrid simulation and DYAMOND high-resolution data that ZFP compression at rate-16 matches float16 communication speedups while delivering approximately 1600x lower mean relative error.
- Shows that ZFP at rate-8 achieves roughly 1.93x the speedup of float16 while retaining 4x lower mean relative error.

## Open Questions & Future Work

- [[end-to-end-compressed-sht-transpositions]]
- [[downstream-forecast-accuracy-lossy-communication]]

## Archivist Review

Applied strict selection standards: no concepts or datasets were approved as they represent paper-local engineering evaluations rather than reusable core mechanisms or distinct named benchmarks. Two open questions concerning end-to-end compressed communications and downstream forecast drift were approved for tracking numerical weather prediction bottlenecks.

### Approved Open Questions
- End-to-End Compressed SHT Transpositions: Understanding the compound performance and error propagation of compressing multiple successive communication phases in spectral transforms is crucial for end-to-end GPU-resident climate model optimization.
- Downstream Forecast Accuracy with Lossy Communication: Ensuring that aggressive communication compression does not lead to unphysical numerical drift or degraded forecast skill over production integration windows is vital for operational deployment.

## Links

- [Abstract](https://arxiv.org/abs/2609.24294)
- [PDF](https://arxiv.org/pdf/2609.24294)

