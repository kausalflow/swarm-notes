---
# CSL-compatible fields
title: "DiaSeg: Diagonal Segment Extraction from DTW Paths for Interpretable Gait Analysis"
author:
  - literal: "Tresor Y. Koffi"
  - literal: "Amel Hidouri"
  - literal: "Corentin Legrand"
  - literal: "Aurélie Bertaux"
issued:
  date-parts:
    - [2026, 9, 21]
url: "https://arxiv.org/abs/2609.24223"

# Custom fields
paper_id: "2609.24223"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "interpretability"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "diaseg"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-24T09:39:34Z"
created_at: "2026-09-24T09:39:34Z"
---

# DiaSeg: Diagonal Segment Extraction from DTW Paths for Interpretable Gait Analysis

**Authors**: Tresor Y. Koffi, Amel Hidouri, Corentin Legrand, Aurélie Bertaux
**Date**: 2026-09-21
**Paper ID**: [openalex:2609.24223](https://arxiv.org/abs/2609.24223)

## Summary

The authors propose DiaSeg, a framework that extracts diagonal segments from Dynamic Time Warping (DTW) paths using controlled breaks and five geometric features to enable unsupervised pattern discovery and interpretable clinical gait analysis. Evaluated on 91 subjects across six neurodegenerative and clinical conditions, DiaSeg uncovers consistent biomechanical phase patterns and achieves high classification accuracy (up to 91.7% when combined with cycle-level features) while localizing coordination breakdowns within the gait cycle.

## Key Contributions

- Introduced DiaSeg, a framework that extracts diagonal segments from Dynamic Time Warping (DTW) paths with controlled breaks and characterizes them via five geometric features for unsupervised pattern discovery.
- Demonstrated near-perfect separation of healthy and pathological gait with an Adjusted Rand Index (ARI) of up to 0.986 using unsupervised pattern discovery on 91 subjects across six clinical conditions.
- Showed that combining diagonal segment features with cycle-level features improves classification accuracy to 91.7% while providing phase-specific interpretability for neurodegenerative disease assessment.

## Limitations

Cycle-based methods achieved slightly higher raw accuracy (91% vs 69-75%) compared to standalone diagonal segment features, though segments offer unique local interpretability.

## Open Questions & Future Work

- [[richer-feature-sets-segment-analysis]]

## Key Concepts

- [[diaseg]]: A framework that extracts diagonal segments from Dynamic Time Warping paths with controlled breaks, characterizing them by geometric features for unsupervised pattern discovery and interpretable gait analysis.

## Archivist Review

Approved the core methodological concept 'diaseg' for extracting interpretable diagonal segments from Dynamic Time Warping paths, and the open question regarding richer geometric feature sets. No datasets met the strict standard for a vault entry since the evaluation cohort was described locally without a standard benchmark name.

### Approved Concepts
- DiaSeg: It is the core methodological contribution of the paper, transforming black-box Dynamic Time Warping paths into interpretable temporal features for gait analysis.

### Approved Open Questions
- Richer Feature Sets for Segment Analysis: Understanding how to expand the feature space without inducing overfitting is vital for extending segment-based alignment methods to highly heterogeneous clinical datasets.

## Links

- [Abstract](https://arxiv.org/abs/2609.24223)
- [PDF](https://arxiv.org/pdf/2609.24223)

