---
# CSL-compatible fields
title: "QuaNAS: Uncertainty-Aware Reuse of Earlier Searches for Query-Efficient Neural Architecture Search"
author:
  - literal: "Brama Seta Putra Satria"
  - literal: "Dwi Sunaryono"
  - literal: "Misbakhul Munir Irfan Subakti"
  - literal: "Irzal Ahmad Sabilla"
  - literal: "Laras Suciningtyas"
issued:
  date-parts:
    - [2026, 10, 22]
url: "https://arxiv.org/abs/2610.31251"

# Custom fields
paper_id: "2610.31251"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "neural-architecture-search,nas,gaussian-process,zero-shot-learning,benchmark,evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-25T09:30:05Z"
created_at: "2026-10-25T09:30:05Z"
---

# QuaNAS: Uncertainty-Aware Reuse of Earlier Searches for Query-Efficient Neural Architecture Search

**Authors**: Brama Seta Putra Satria, Dwi Sunaryono, Misbakhul Munir Irfan Subakti, Irzal Ahmad Sabilla, Laras Suciningtyas
**Date**: 2026-10-22
**Paper ID**: [openalex:2610.31251](https://arxiv.org/abs/2610.31251)

## Summary

QuaNAS is an uncertainty-aware neural architecture search method that reuses earlier search libraries as explicit priors over candidate architectures, updating trust via a Gaussian process without requiring new labels. Evaluated across 12 image, time-series, text, and tabular datasets, it significantly reduces anytime regret compared to methods that start from scratch and achieves strong non-inferiority performance.

## Key Contributions

- QuaNAS uses a library of earlier searches as explicit uncertain priors combined with a Gaussian process to eliminate starting from scratch in neural architecture search.
- It lowers anytime regret on short-training objectives 2.7- to 3.9-fold relative to five pre-specified NAS baselines across 12 image, time-series, text, and tabular datasets.
- Its selected prior optimum matches or exceeds matched-recipe reference models on nine out of 12 datasets without requiring a single evaluation.

## Archivist Review

Applied strict selectivity: no concepts or datasets met the rigorous standards for permanent vault notes, and the proposed open questions were too paper-local or general.

### Rejected Candidates
- [open_question] Correcting Low-Fidelity Training Signals (`correcting-low-fidelity-signals-nas`) - not_reusable: Paper-local and task-specific future work direction in neural architecture search.
- [open_question] Cross-Search-Space Architecture Transfer (`cross-search-space-transfer-nas`) - low_impact: General automated machine learning goal that lacks specific technical formulation in this time-series/NAS paper.

## Links

- [Abstract](https://arxiv.org/abs/2610.31251)
- [PDF](https://arxiv.org/pdf/2610.31251)

