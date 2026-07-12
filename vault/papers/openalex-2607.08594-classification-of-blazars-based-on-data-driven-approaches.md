---
# CSL-compatible fields
title: "Classification of blazars based on data-driven approaches"
author:
  - literal: "Simone Vaccaro"
  - literal: "M. I. Carnerero"
  - literal: "Claudia M. Raiteri"
  - literal: "M. Brescia"
  - literal: "Y. Maruccia"
  - literal: "Natale De Bonis"
  - literal: "Giuseppe Riccio"
  - literal: "Stefano Cavuoti"
issued:
  date-parts:
    - [2026, 7, 9]
url: "https://arxiv.org/abs/2607.08594"

# Custom fields
paper_id: "2607.08594"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "text-classification"
  - "evaluation"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  - "boostboruta-algorithm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-12T07:27:58Z"
created_at: "2026-07-12T07:27:58Z"
---

# Classification of blazars based on data-driven approaches

**Authors**: Simone Vaccaro, M. I. Carnerero, Claudia M. Raiteri, M. Brescia, Y. Maruccia, Natale De Bonis, Giuseppe Riccio, Stefano Cavuoti
**Date**: 2026-07-09
**Paper ID**: [openalex:2607.08594](https://arxiv.org/abs/2607.08594)

## Summary

This paper presents a data-driven approach to classify blazars and non-blazar Active Galactic Nuclei (AGN) using solely optical light curves from GAIA and Pan-STARRS. By extracting time-series features and employing a Light Gradient-Boosting Machine (LightGBM), the authors achieve 86% classification accuracy. Furthermore, they implement the BoostBoruta algorithm to optimize the feature space, reducing it from 70 to 13 key features while maintaining high predictive performance. The effectiveness of this methodology is confirmed through a self-training experiment on unknown AGN candidates, suggesting the reliability of pseudo-labeling for celestial classification.

## Key Contributions

- Introduces a classification framework for blazars using only optical light curve variability, eliminating the need for multiwavelength data.
- Utilizes the LightGBM model to achieve 86% accuracy in distinguishing blazars from non-blazar AGNs.
- Demonstrates that the BoostBoruta algorithm effectively reduces the feature space from 70 to 13 features without significant performance degradation.
- Validates the robustness of the approach through a self-learning experiment, achieving 85% accuracy on unlabeled AGN candidates.

## Open Questions & Future Work

- [[mitigating-optical-feature-overlap-blazars]]

## Key Concepts

- [[boostboruta-algorithm]]: A gradient-boosted feature selection method designed to identify the most predictive features within high-dimensional input spaces.

## Archivist Review

The paper presents a domain-specific application of well-established time-series feature engineering and model selection. The BoostBoruta algorithm is approved as a reusable concept for feature selection, and the open question regarding optical feature overlap is approved as a critical limitation in celestial classification. Astronomical surveys like GAIA and Pan-STARRS were rejected as datasets because they are massive repositories rather than specific machine learning benchmarks.

### Approved Concepts
- BoostBoruta Algorithm: It is the central methodology for achieving dimensionality reduction while maintaining classification accuracy.

### Approved Open Questions
- Mitigating optical feature overlap: Distinguishing blazar signals from other AGN variability is a fundamental astrophysical classification bottleneck.

### Rejected Candidates
- [dataset] GAIA (`gaia`) - other: This is a broad astronomical survey dataset, not a specific, curated benchmark for machine learning time-series tasks.
- [dataset] Pan-STARRS (`pan-starrs`) - other: This is a broad astronomical survey dataset rather than a curated machine learning benchmark.

## Links

- [Abstract](https://arxiv.org/abs/2607.08594)
- [PDF](https://arxiv.org/pdf/2607.08594)

