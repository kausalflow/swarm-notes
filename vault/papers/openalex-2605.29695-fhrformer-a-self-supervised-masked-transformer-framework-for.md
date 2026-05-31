---
# CSL-compatible fields
title: "FHRFormer: A Self-Supervised Masked Transformer Framework for Fetal Heart Rate Time-Series Inpainting and Forecasting"
author:
  - literal: "Kjersti Engan"
  - literal: "Neel Kanwal"
  - literal: "Anita Yeconia"
  - literal: "Ladislaus Blacy"
  - literal: "Yuda Munyaw"
  - literal: "Estomih Mduma"
  - literal: "Hege Ersdal"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.29695"

# Custom fields
paper_id: "2605.29695"
paper_source: "openalex"
domain: "medicine"
tags:
  - "transformer"
  - "masked-autoencoder"
  - "time-series"
  - "forecasting"
  - "self-supervised-learning"
  - "medicine"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:08:50Z"
created_at: "2026-05-31T08:08:50Z"
---

# FHRFormer: A Self-Supervised Masked Transformer Framework for Fetal Heart Rate Time-Series Inpainting and Forecasting

**Authors**: Kjersti Engan, Neel Kanwal, Anita Yeconia, Ladislaus Blacy, Yuda Munyaw, Estomih Mduma, Hege Ersdal
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.29695](https://arxiv.org/abs/2605.29695)

## Summary

FHRFormer is a self-supervised masked transformer autoencoder designed to address signal dropout in fetal heart rate (FHR) monitoring, a common issue in wearable prenatal care devices. By capturing both temporal and frequency dynamics, the model effectively reconstructs missing signal segments better than traditional interpolation methods. This framework enables more robust AI-based analysis and risk prediction for clinical FHR datasets by ensuring data integrity through inpainting and forecasting capabilities.

## Key Contributions

- Introduces FHRFormer, a masked transformer-based autoencoder specifically designed for fetal heart rate signal inpainting and forecasting.
- Addresses signal dropout in wearable FHR monitoring by reconstructing gaps while preserving local temporal and frequency characteristics.
- Provides a robust alternative to traditional interpolation techniques for preprocessing large-scale clinical time-series datasets.

## Open Questions & Future Work

- [[uncertainty-quantification-in-fetal-heart-rate-modeling]]

## Archivist Review

I have rejected the FHRFormer concept as it is a domain-specific application of masked autoencoders, which is already a established concept. I have also rejected the multimodal integration question as it is a generic extension, but approved the uncertainty quantification question due to its specific clinical importance for high-stakes medical monitoring reliability.

### Approved Open Questions
- Uncertainty Quantification in FHR Modeling: Without uncertainty quantification, clinicians cannot assess the reliability of model-generated reconstructions, which is a major barrier to clinical adoption in high-stakes environments like labor monitoring.

### Rejected Candidates
- [open_question] Multimodal Fetal Monitoring Integration (`multimodal-fetal-monitoring-integration`) - low_impact: This is a generic future work direction suggesting multimodal fusion, which is a standard research trajectory in medical AI.

## Links

- [Abstract](https://arxiv.org/abs/2605.29695)
- [PDF](https://arxiv.org/pdf/2605.29695)

