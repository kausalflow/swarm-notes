---
# CSL-compatible fields
title: "Frequency Domain Resampling for Gridded Spatial Data"
author:
  - literal: "Souvick Bera"
  - literal: "Daniel J. Nordman"
  - literal: "Soutir Bandyopadhyay"
issued:
  date-parts:
    - [2026, 7, 28]
url: "https://arxiv.org/abs/2504.19337"

# Custom fields
paper_id: "2504.19337"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-31T07:44:33Z"
created_at: "2026-07-31T07:44:33Z"
---

# Frequency Domain Resampling for Gridded Spatial Data

**Authors**: Souvick Bera, Daniel J. Nordman, Soutir Bandyopadhyay
**Date**: 2026-07-28
**Paper ID**: [openalex:2504.19337](https://arxiv.org/abs/2504.19337)

## Summary

Frequency domain analysis for spatial data relies on spectral averages from periodograms, but existing resampling methods struggle to capture their complex sampling distributions and variances. This paper introduces a hybrid resampling approach combining spatial subsampling and spatial bootstrap to respectively capture variance and distributional shape. This procedure enables robust uncertainty quantification for spatial spectral inference under mild assumptions.

## Key Contributions

- Proposes a hybrid-resampling approach combining spatial subsampling and spatial bootstrap to approximate sampling distributions of spatial spectral averages in the frequency domain.
- Subsampling captures the complex variance of spatial spectral averages while bootstrap captures the distributional shape under mild spatial assumptions.
- Overcomes limitations of existing frequency domain bootstraps restricted to special processes like Gaussian or specific spatial statistics.

## Limitations

The abstract does not report specific empirical performance bounds or numerical benchmark outcomes.

## Open Questions & Future Work

- [[frequency-domain-resampling-irregular-spatial-data]]

## Archivist Review

Approved the open question regarding frequency domain resampling for irregular spatial data as it highlights a fundamental theoretical limitation and extension direction for spatial spectral analysis. No distinct general concepts were approved because the hybrid resampling technique is too paper-local and methodologically specific without established broad currency.

### Approved Open Questions
- Frequency Domain Resampling for Irregular Spatial Data: Real-world spatial data are frequently collected at irregular, non-gridded locations rather than regular integer lattices. Developing frequency domain bootstrap and subsampling methods for irregular spatial data is crucial for broadening the applicability of nonparametric spectral inference.

## Links

- [Abstract](https://arxiv.org/abs/2504.19337)
- [PDF](https://arxiv.org/pdf/2504.19337)

