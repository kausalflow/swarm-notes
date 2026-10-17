---
# CSL-compatible fields
title: "DeepPV-MRF: End-to-End Partial-Volume Fraction Estimation from MR Fingerprinting Time Series"
author:
  - literal: "Tianyi Ding"
  - literal: "Yang Gao"
  - literal: "Zhuang Xiong"
  - literal: "Feng Liu"
  - literal: "Martijn A. Cloos"
  - literal: "Jin Jin"
  - literal: "Hongfu Sun"
issued:
  date-parts:
    - [2026, 10, 14]
url: "https://arxiv.org/abs/2610.19894"

# Custom fields
paper_id: "2610.19894"
paper_source: "openalex"
domain: "medicine"
tags:
  - "time-series"
  - "deep-learning"
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
processed_at: "2026-10-17T08:55:08Z"
created_at: "2026-10-17T08:55:08Z"
---

# DeepPV-MRF: End-to-End Partial-Volume Fraction Estimation from MR Fingerprinting Time Series

**Authors**: Tianyi Ding, Yang Gao, Zhuang Xiong, Feng Liu, Martijn A. Cloos, Jin Jin, Hongfu Sun
**Date**: 2026-10-14
**Paper ID**: [openalex:2610.19894](https://arxiv.org/abs/2610.19894)

## Summary

The authors propose DeepPV-MRF, a cascaded spatial-temporal deep learning framework that estimates subvoxel tissue fractions directly from raw magnetic resonance fingerprinting (MRF) time series, avoiding errors from intermediate parametric maps. By combining temporal encoding with a spatial U-Net refinement trained on Bloch simulations, DeepPV-MRF outperforms traditional dictionary matching and pseudoinverse estimation in both simulation and in vivo settings.

## Key Contributions

- Introduced DeepPV-MRF, a cascaded spatial-temporal deep learning framework that directly estimates voxel-wise tissue fractions from raw MRF signals without intermediate parametric maps.
- Achieved superior accuracy in single-shot simulations, yielding CSF/WM/GM mean absolute errors of 0.0418/0.0744/0.0757 compared to 0.1281/0.2443/0.2958 for partial-volume dictionary matching.
- Demonstrated enhanced in vivo results exhibiting sharper anatomical boundaries, smoother tissue transitions, and improved cross-shot consistency across volunteers.

## Limitations

Further validation is required prior to clinical deployment.

## Open Questions & Future Work

- [[self-supervised-partial-volume-estimation-mrf]]

## Archivist Review

The paper proposes a specialized deep learning framework for magnetic resonance fingerprinting (MRF), which is too domain-specific and paper-local to justify a permanent vault concept note. However, the open question on self-supervised partial volume estimation represents a substantive methodological challenge worth tracking.

### Approved Open Questions
- Self-Supervised Partial Volume Estimation: Developing self-supervised or unsupervised approaches removes the bottleneck of requiring high-resolution multi-echo reference segmentations for training data generation, improving clinical adaptability across diverse imaging protocols and scanners.

### Rejected Candidates
- [concept] DeepPV-MRF (`deeppv-mrf`) - paper_local: Paper-local application and architecture specific to magnetic resonance fingerprinting partial volume estimation.

## Links

- [Abstract](https://arxiv.org/abs/2610.19894)
- [PDF](https://arxiv.org/pdf/2610.19894)

