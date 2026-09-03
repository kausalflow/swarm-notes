---
# CSL-compatible fields
title: "A neural network architecture and training algorithm to predict viscoelastic stresses from vortical data"
author:
  - literal: "Lu Zhu"
  - literal: "Jacob Page"
issued:
  date-parts:
    - [2026, 8, 31]
url: "https://arxiv.org/abs/2608.30926"

# Custom fields
paper_id: "2608.30926"
paper_source: "openalex"
domain: "time-series"
tags:
  - "convolutional-neural-network"
  - "time-series"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-03T09:17:29Z"
created_at: "2026-09-03T09:17:29Z"
---

# A neural network architecture and training algorithm to predict viscoelastic stresses from vortical data

**Authors**: Lu Zhu, Jacob Page
**Date**: 2026-08-31
**Paper ID**: [openalex:2608.30926](https://arxiv.org/abs/2608.30926)

## Summary

This paper introduces a neural network architecture and assimilation-based training algorithm to predict viscoelastic polymer conformation tensors directly from vorticity time series in fluid flows. The approach uses a convolutional neural network to output positive definite tensors and is trained without offline reference conformation fields by enforcing consistency with vorticity measurements over time. Evaluated on two-dimensional Kolmogorov flow across traveling wave to chaotic regimes, the method outperforms standard variational assimilation and generalises robustly to larger spatial domains.

## Key Contributions

- Introduces a convolutional neural network architecture that maps vorticity fields to positive definite polymer conformation tensors in viscoelastic fluid flows.
- Adapts an assimilation-based training algorithm requiring only vorticity measurements without needing pre-generated offline reference conformation fields.
- Demonstrates robust polymer stretch prediction across Kolmogorov flow regimes from traveling waves to fully chaotic states, outperforming standard unregularised variational assimilation.
- Shows successful zero-shot generalisation of trained networks to much larger spatial domains than the minimal training units in chaotic regimes.

## Open Questions & Future Work

- [[learning-constitutive-models-and-parameters]]

## Archivist Review

Applied strict selectivity, approving only the open question regarding the learning of unknown constitutive models and parameters from partial observations, while keeping concepts and datasets empty to protect vault quality.

### Approved Open Questions
- Learning constitutive models and parameters: Enables data-driven discovery of constitutive equations and physical parameters directly from partial flow observations without requiring offline training libraries.

### Rejected Candidates
- [concept] Learning constitutive models and parameters (`learning-constitutive-models-and-parameters`) - duplicate_existing: The proposed concept duplicates or strongly overlaps with the open question of the same name.

## Links

- [Abstract](https://arxiv.org/abs/2608.30926)
- [PDF](https://arxiv.org/pdf/2608.30926)

