---
# CSL-compatible fields
title: "Robust and Efficient Noisy-Label Time-Series Classification via Dynamic Time Warping Based Granular Ball Computing"
author:
  - literal: "Ziqiang Li"
  - literal: "Yun Liu"
  - literal: "Gouhei Tanaka"
issued:
  date-parts:
    - [2026, 8, 12]
url: "https://arxiv.org/abs/2608.11704"

# Custom fields
paper_id: "2608.11704"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "robustness"
  - "classification"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dtw-based-granular-ball-computing"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-15T05:15:06Z"
created_at: "2026-08-15T05:15:06Z"
---

# Robust and Efficient Noisy-Label Time-Series Classification via Dynamic Time Warping Based Granular Ball Computing

**Authors**: Ziqiang Li, Yun Liu, Gouhei Tanaka
**Date**: 2026-08-12
**Paper ID**: [openalex:2608.11704](https://arxiv.org/abs/2608.11704)

## Summary

The paper introduces DTW-based Granular Ball Computing (DTW-GBC), a robust and efficient approach for time-series classification in the presence of noisy labels. By grouping temporally similar training samples into granular balls using Dynamic Time Warping, the method performs classification at the granule level, mitigating label noise degradation while significantly reducing inference comparisons compared to standard 1-NN. Experiments across four benchmark datasets demonstrate an effective balance between robustness and computational efficiency.

## Key Contributions

- Proposes DTW-based Granular Ball Computing (DTW-GBC) to organize temporally similar time-series training samples into granular balls for granule-level classification.
- Develops two novel granular-ball construction strategies tailored for DTW-GBC.
- Demonstrates through experiments on four benchmark datasets with symmetric label noise that DTW-GBC mitigates performance degradation from label noise while requiring substantially fewer comparisons than DTW-based 1-NN during inference.

## Limitations

Evaluated specifically under symmetric label noise across four benchmark datasets; further exploration on asymmetric noise and larger-scale datasets could be investigated.

## Open Questions & Future Work

- [[robust-granular-ball-time-series-extensions]]

## Key Concepts

- [[dtw-based-granular-ball-computing]]: A classification framework that organizes temporally similar time-series samples into granular balls using dynamic time warping to achieve robustness against label noise and high inference efficiency.

## Archivist Review

Approved the core methodology concept (DTW-based Granular Ball Computing) and its direct extension open question because they represent a distinctive, reusable approach to noisy-label time-series classification and efficiency. No standard datasets were approved since generic benchmark datasets were not explicitly named with specific repository keys.

### Approved Concepts
- DTW-based Granular Ball Computing: Central algorithmic framework combining dynamic time warping with granular ball computing for robust and efficient time-series classification.

### Approved Open Questions
- Robust Granular-Ball Time-Series Extensions: Hyperparameter selection under noise remains a key bottleneck in robust granular-ball computing, and extending the framework to other time-series tasks broadens its utility in machine learning applications.

## Links

- [Abstract](https://arxiv.org/abs/2608.11704)
- [PDF](https://arxiv.org/pdf/2608.11704)

