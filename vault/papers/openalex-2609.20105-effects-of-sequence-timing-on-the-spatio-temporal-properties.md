---
# CSL-compatible fields
title: "Effects of Sequence Timing on the Spatio-Temporal Properties of 3D BOLD fMRI: A Formal Framework and Analysis"
author:
  - literal: "Samuel Bianchi"
  - literal: "Klaas P. Pruessmann"
issued:
  date-parts:
    - [2026, 9, 17]
url: "https://arxiv.org/abs/2609.20105"

# Custom fields
paper_id: "2609.20105"
paper_source: "openalex"
domain: "medicine"
tags:
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-20T09:30:35Z"
created_at: "2026-09-20T09:30:35Z"
---

# Effects of Sequence Timing on the Spatio-Temporal Properties of 3D BOLD fMRI: A Formal Framework and Analysis

**Authors**: Samuel Bianchi, Klaas P. Pruessmann
**Date**: 2026-09-17
**Paper ID**: [openalex:2609.20105](https://arxiv.org/abs/2609.20105)

## Summary

This paper presents a formal theoretical framework to model the effects of sequence timing on 3D BOLD fMRI data properties, addressing a gap in literature regarding segmented k-space acquisitions. By formulating spatial encoding and image reconstruction as spatio-temporal filter operators, the authors analyze how sequence timing mixes signal content and attenuates high-frequency BOLD signals more than low-frequency components. Simulations reveal that while total variance in 3D time series is reduced, spatio-temporal fidelity is impaired, shedding light on the heightened sensitivity of 3D sequences to physiological noise.

## Key Contributions

- Presented a formal theoretical framework modeling sequence timing effects in 3D BOLD fMRI caused by segmented k-space acquisition over extended periods.
- Defined three key images—reconstructed image, optimal reference image unaffected by timing, and an error image—using spatio-temporal filter operators.
- Demonstrated through simulations that sequence timing reduces total variance of 3D image time series while compromising spatio-temporal fidelity, affecting high-frequency BOLD signals more than low-frequency content.

## Limitations

The impact of subject motion and system instabilities on image time series needs to be studied further.

## Archivist Review

Reviewed the paper and its analysis. The paper is an advanced theoretical physics contribution in neuroimaging (3D BOLD fMRI sequence timing), which lacks broad, reusable machine learning or general time-series forecasting concepts or standard named datasets. Therefore, no concepts or open questions met the rigorous standard for vault inclusion.

### Rejected Candidates
- [open_question] Generalizing 3D fMRI Timing GLMs (`generalizing-3d-fmri-timing-glms`) - low_impact: The question is highly specialized to physical neuroimaging sequence timing and GLM estimation in 3D BOLD fMRI, falling outside general machine learning or time-series forecasting methodology.

## Links

- [Abstract](https://arxiv.org/abs/2609.20105)
- [PDF](https://arxiv.org/pdf/2609.20105)

