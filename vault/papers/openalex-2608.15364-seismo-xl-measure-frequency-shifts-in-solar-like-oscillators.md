---
# CSL-compatible fields
title: "seismo-xl: Measure frequency shifts in solar-like oscillators using filtered cross-correlation method."
author:
  - literal: "Samarth G. Kashyap"
issued:
  date-parts:
    - [2026, 8, 24]
url: "https://arxiv.org/abs/2608.15364"

# Custom fields
paper_id: "2608.15364"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "filtered-cross-correlation-method"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-27T15:59:02Z"
created_at: "2026-08-27T15:59:02Z"
---

# seismo-xl: Measure frequency shifts in solar-like oscillators using filtered cross-correlation method.

**Authors**: Samarth G. Kashyap
**Date**: 2026-08-24
**Paper ID**: [openalex:2608.15364](https://arxiv.org/abs/2608.15364)

## Summary

This paper introduces seismo-xl, a filtered cross-correlation method designed to measure frequency shifts in solar-like oscillators for distinct spherical harmonic degrees. By applying tailored filters, the approach isolates mode frequency changes while overcoming poor signal-to-noise ratios and preventing bias from neighboring modes. The method is validated on solar data from SOHO/VIRGO and BiSON, and its applicability is demonstrated on the Kepler star KIC 8006161.

## Key Contributions

- Introduced seismo-xl, a filtered cross-correlation method to disentangle p-mode frequency changes for different spherical harmonic degrees in solar-like oscillators.
- Designed filters to isolate mode frequency shifts while preventing bias from neighboring modes given known stellar rotation and inclination.
- Validated the method on solar data (SOHO/VIRGO and BiSON) and demonstrated application to the Kepler target KIC 8006161.

## Limitations

Assumes inclination angle and rotation rate are already measured.

## Open Questions & Future Work

- [[refined-weight-derivation-and-high-frequency-filters]]

## Key Concepts

- [[filtered-cross-correlation-method]]: A computationally efficient enhancement to cross-correlation that isolates p-mode frequency shifts for distinct spherical harmonic degrees in solar-like oscillators.

## Archivist Review

Approved the core methodological concept 'filtered-cross-correlation-method' as a distinct, reusable time-series/asteroseismology technique, and retained one substantive open question on high-frequency filter refinement while pruning routine pipeline extensions.

### Approved Concepts
- Filtered Cross-Correlation Method: Central methodological contribution for measuring degree-dependent frequency shifts in stellar oscillators by avoiding blending across neighboring modes.

### Approved Open Questions
- Refining Mode Weights and Filters: Refining mode filters and weight derivations is critical to accurately capturing high-frequency mode variability and accounting for rotational splitting, which limits the precision of inferred active latitudes and magnetic activity cycles in Sun-like stars.

### Rejected Candidates
- [open_question] Integrated Seismic Parameter Pipeline (`integrated-seismic-parameter-pipeline`) - low_impact: Speculative engineering extension about integrating independent measurements rather than a foundational algorithmic limitation.

## Links

- [Abstract](https://arxiv.org/abs/2608.15364)
- [PDF](https://arxiv.org/pdf/2608.15364)

