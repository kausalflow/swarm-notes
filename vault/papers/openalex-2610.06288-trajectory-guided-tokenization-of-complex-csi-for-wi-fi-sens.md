---
# CSL-compatible fields
title: "Trajectory-Guided Tokenization of Complex CSI for Wi-Fi Sensing"
author:
  - literal: "Ziyi Wang"
  - literal: "Kenuo Xu"
  - literal: "Jichu Jiang"
  - literal: "Yumeng Yang"
  - literal: "Zheng Chen"
  - literal: "Xiaofei Bai"
  - literal: "Muge Chen"
  - literal: "Xuyang Chen"
  - literal: "Jinglei He"
  - literal: "Jannik Hammel Nielsen"
  - literal: "Stefan Schmid"
issued:
  date-parts:
    - [2026, 10, 5]
url: "https://arxiv.org/abs/2610.06288"

# Custom fields
paper_id: "2610.06288"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "time-series"
  - "multimodal"
  - "representation-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "trajectory-guided-tokenization"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-08T11:41:50Z"
created_at: "2026-10-08T11:41:50Z"
---

# Trajectory-Guided Tokenization of Complex CSI for Wi-Fi Sensing

**Authors**: Ziyi Wang, Kenuo Xu, Jichu Jiang, Yumeng Yang, Zheng Chen, Xiaofei Bai, Muge Chen, Xuyang Chen, Jinglei He, Jannik Hammel Nielsen, Stefan Schmid
**Date**: 2026-10-05
**Paper ID**: [openalex:2610.06288](https://arxiv.org/abs/2610.06288)

## Summary

Wi-Fi channel state information (CSI) provides rich signals for contactless sensing, but its high-dimensional complex-valued nature demands specialized tokenization techniques. To address this, the authors propose Trajectory-Guided Tokenization (TGT), which uses an orthonormal Helmert transform and asymmetric attention to decompose temporal patches and compress them into compact tokens. Evaluated on both a self-collected dataset and public benchmarks like EHUNAM and Widar, TGT combined with TokenMLP achieves state-of-the-art accuracy for presence detection and gesture recognition.

## Key Contributions

- Proposes Trajectory-Guided Tokenization (TGT) to compress high-dimensional complex-valued CSI time series while preserving informative temporal variations.
- Combines an orthonormal Helmert transform for complex trajectory decomposition with asymmetric attention for compact token construction.
- Achieves a mean accuracy of 92.83% using TGT with TokenMLP on a self-collected dataset, outperforming evaluated frontend-backend alternatives.
- Demonstrates robust applicability across cross-domain presence detection and gesture recognition on EHUNAM and Widar datasets.

## Open Questions & Future Work

- [[phase-quality-and-representation-encoding]]

## Key Concepts

- [[trajectory-guided-tokenization]]: A tokenization framework for complex-valued CSI time series that combines orthonormal Helmert transform trajectory decomposition with asymmetric attention.

## Archivist Review

Approved the core methodology concept 'Trajectory-Guided Tokenization' (TGT) and the open question concerning phase representation and robustness in Wi-Fi sensing. Rejected the standard benchmark datasets as they do not meet the high threshold for standalone cataloging.

### Approved Concepts
- Trajectory-Guided Tokenization: TGT is the core proposed methodology, combining complex trajectory decomposition with asymmetric attention to tokenize high-dimensional CSI time series.

### Approved Open Questions
- Phase Quality and Representation Encoding: Phase information is notoriously noisy and hardware-dependent in Wi-Fi CSI; understanding how to properly represent and utilize phase without degrading cross-domain performance is a critical foundational challenge for robust wireless sensing.

### Rejected Candidates
- [dataset] EHUNAM Dataset (`ehunam-dataset`) - low_impact: Secondary benchmark dataset lacking enough prominence for a dedicated vault note.
- [dataset] Widar Dataset (`widar-dataset`) - low_impact: Standard benchmark dataset used for evaluation but not newly introduced or uniquely characterized in the abstract.

## Links

- [Abstract](https://arxiv.org/abs/2610.06288)
- [PDF](https://arxiv.org/pdf/2610.06288)

