---
# CSL-compatible fields
title: "Indirect Estimation of SINR via SSB and CSI-RS RSRP in 5G NR"
author:
  - literal: "Leonardo Spampinato"
  - literal: "Mahamadou Togola"
  - literal: "Matteo Bernabè"
  - literal: "Azim Akhtarshenas"
  - literal: "Lorenzo Mario Amorosa"
  - literal: "David López-Pérez"
issued:
  date-parts:
    - [2026, 9, 3]
url: "https://arxiv.org/abs/2609.03488"

# Custom fields
paper_id: "2609.03488"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "dataset"
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
processed_at: "2026-09-05T08:42:17Z"
created_at: "2026-09-05T08:42:17Z"
---

# Indirect Estimation of SINR via SSB and CSI-RS RSRP in 5G NR

**Authors**: Leonardo Spampinato, Mahamadou Togola, Matteo Bernabè, Azim Akhtarshenas, Lorenzo Mario Amorosa, David López-Pérez
**Date**: 2026-09-03
**Paper ID**: [openalex:2609.03488](https://arxiv.org/abs/2609.03488)

## Summary

This paper proposes a data-driven machine learning approach to predict downlink SINR in 5G NR networks using only standardized SSB and CSI-RS RSRP measurements. By formulating the task as a supervised learning problem on a 3GPP-compliant synthetic dataset, the authors evaluate different input representations. Their findings show that activity-aware filtering based on active CSI-RS beams drastically reduces dimensionality while improving prediction accuracy.

## Key Contributions

- Proposes a data-driven framework for indirect downlink SINR prediction using standardized SSB and CSI-RS RSRP measurements in 5G NR networks.
- Formulates SINR prediction as a supervised learning task evaluated on a 3GPP-compliant synthetic dataset.
- Demonstrates that filtering input measurements based on active CSI-RS beams significantly improves prediction accuracy while reducing input dimensionality.

## Limitations

Evaluated primarily on synthetic 3GPP-compliant data; empirical validation on live operational cellular networks remains future work.

## Open Questions & Future Work

- [[real-world-dataset-validation-sinr-prediction]]

## Archivist Review

Evaluated the paper under strict archiving standards. No reusable core forecasting or time-series concepts met the threshold for standalone vault inclusion. One open question regarding real-world dataset validation for wireless performance prediction was approved as a valuable research tracking entry.

### Approved Open Questions
- Real-World Validation for SINR Prediction: Validating data-driven wireless performance predictors on real-world measurements is critical to confirm their operational viability beyond synthetic channel models.

### Rejected Candidates
- [concept] Activity-Aware CSI-RS Filtering (`activity-aware-csi-rs-filtering`) - paper_local: Domain-specific preprocessing rule for 5G reference signals rather than a broad, reusable machine learning or time-series concept.

## Links

- [Abstract](https://arxiv.org/abs/2609.03488)
- [PDF](https://arxiv.org/pdf/2609.03488)

