---
# CSL-compatible fields
title: "BioFormer: Rethinking Cross-Subject Generalization via Spectral Structural Alignment in Biomedical Time-Series"
author:
  - literal: "Guikang Du"
  - literal: "Haoran Li"
  - literal: "Xinyu Liu"
  - literal: "Zhibo Zhang"
  - literal: "Xiaoli Gong"
  - literal: "Jin Zhang"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.22468"

# Custom fields
paper_id: "2605.22468"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "biomedical-time-series"
  - "spectral-structural-alignment"
  - "generalization"
architectures:
  []
datasets:
  []
concept_slugs:
  - "frequency-band-alignment-module-fbam"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:46:19Z"
created_at: "2026-05-24T07:46:19Z"
---

# BioFormer: Rethinking Cross-Subject Generalization via Spectral Structural Alignment in Biomedical Time-Series

**Authors**: Guikang Du, Haoran Li, Xinyu Liu, Zhibo Zhang, Xiaoli Gong, Jin Zhang
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.22468](https://arxiv.org/abs/2605.22468)

## Summary

BioFormer addresses the cross-subject generalization challenge in biomedical time-series by modeling subject-specific variability as spectral drift rather than implicit noise. The architecture utilizes a novel Frequency-Band Alignment Module (FBAM) to adaptively adjust signal amplitude and phase, effectively aligning spectral oscillatory structures. Combined with sample-conditional normalization, BioFormer demonstrates superior generalization performance by avoiding reliance on explicit subject labels during inference.

## Key Contributions

- Introduces spectral drift as a novel perspective to characterize and model subject-specific variability in biomedical time-series.
- Proposes the Frequency-Band Alignment Module (FBAM) to explicitly align oscillatory spectral structures across different subjects.
- Outperforms 12 existing baselines with a 6% absolute F1-score improvement across six benchmark datasets for cross-subject generalization.

## Open Questions & Future Work

- [[automated-frequency-band-partitioning-bts]]

## Key Concepts

- [[frequency-band-alignment-module-fbam]]: A mechanism that adaptively modulates the amplitude and phase of spectral components to align oscillatory structure across subjects or domains.

## Archivist Review

I have approved the FBAM concept and the corresponding open question regarding automated frequency partitioning. These address the paper's primary novelty—explicitly modeling spectral drift to improve cross-subject generalization—in a way that is conceptually reusable for other time-series analysis tasks. Other subcomponents were omitted to maintain the vault's focus on overarching, generalizable mechanisms.

### Approved Concepts
- Frequency-Band Alignment Module (FBAM): It provides a mechanism for explicit spectral structural alignment by modulating amplitude and phase based on frequency distribution, offering a more interpretative alternative to black-box domain adaptation.

### Approved Open Questions
- Automated Frequency Band Partitioning: This question highlights a critical bottleneck in deploying spectral alignment models across diverse physiological datasets where optimal frequency bands are unknown.

## Links

- [Abstract](https://arxiv.org/abs/2605.22468)
- [PDF](https://arxiv.org/pdf/2605.22468)

