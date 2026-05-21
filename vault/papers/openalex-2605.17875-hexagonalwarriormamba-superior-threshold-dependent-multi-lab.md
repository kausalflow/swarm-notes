---
# CSL-compatible fields
title: "HexagonalWarriorMamba: Superior Threshold-Dependent Multi-label Classification of 12-Lead ECG Cardiac Abnormalities"
author:
  - literal: "Huawei Jiang"
  - literal: "Husna Mutahira"
  - literal: "Shibo Wei"
  - literal: "Jiahang Li"
  - literal: "Vladimir Shin"
  - literal: "Juneho Yi"
  - literal: "Dongryeol Ryu"
  - literal: "Wonyoung Park"
  - literal: "Mannan Saeed Muhammad"
issued:
  date-parts:
    - [2026, 5, 18]
url: "https://arxiv.org/abs/2605.17875"

# Custom fields
paper_id: "2605.17875"
paper_source: "openalex"
domain: "medicine"
tags:
  - "mamba"
  - "ssm"
  - "state-space-model"
  - "multimodal"
  - "benchmark"
architectures:
  - "mamba"
datasets:
  - "physionet-2021-challenge"
concept_slugs:
  - "2d-selective-scan-for-time-series"
dataset_slugs:
  - "physionet-2021-challenge"
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:40:04Z"
created_at: "2026-05-21T08:40:04Z"
---

# HexagonalWarriorMamba: Superior Threshold-Dependent Multi-label Classification of 12-Lead ECG Cardiac Abnormalities

**Authors**: Huawei Jiang, Husna Mutahira, Shibo Wei, Jiahang Li, Vladimir Shin, Juneho Yi, Dongryeol Ryu, Wonyoung Park, Mannan Saeed Muhammad
**Date**: 2026-05-18
**Paper ID**: [openalex:2605.17875](https://arxiv.org/abs/2605.17875)

## Summary

HexagonalWarriorMamba (HWMamba) is a novel deep learning framework designed for multi-label cardiac abnormality detection in 12-lead ECGs. Unlike traditional methods that treat ECGs as 1D time series, HWMamba frames the signal as a single-channel 2D image and utilizes a hierarchical Mamba-based 2D Selective Scan mechanism to capture complex global and spatial dependencies. Empirical evaluation on the PhysioNet/Computing in Cardiology Challenge 2021 dataset confirms that HWMamba outperforms current SOTA models on critical threshold-dependent metrics while maintaining strong performance on Macro AUROC.

## Key Contributions

- Introduces HexagonalWarriorMamba (HWMamba), which processes 12-lead ECGs as single-channel 2D images using a hierarchical Mamba-based 2D Selective Scan.
- Achieves state-of-the-art performance on the PhysioNet/Computing in Cardiology Challenge 2021 dataset across five threshold-dependent metrics, including Challenge Score and Subset Accuracy.
- Demonstrates robust multi-label classification capability by balancing discriminative performance with optimized threshold selection in complex, multi-institution cardiac datasets.

## Open Questions & Future Work

- [[threshold-robustness-in-multi-label-biomedical-classification]]

## Key Concepts

- [[2d-selective-scan-for-time-series]]: A technique that treats multichannel temporal signals as 2D spatial images to leverage 2D-selective-scan SSMs for global dependency modeling.

## Archivist Review

I approved the 2D signal transformation mechanism as it represents a significant, reusable architectural shift for time-series modeling. I also approved a broader open question regarding threshold robustness in multi-label classification to replace the overly specific architectural suggestion. The PhysioNet 2021 dataset was approved for its importance as a foundational benchmark for 12-lead ECG analysis.

### Approved Concepts
- 2D Selective Scan for Time Series: Represents a paradigm shift from 1D temporal to 2D structural modeling for multichannel signals, enabling the Mamba SSM architecture to capture spatial relationships alongside global context.

### Approved Open Questions
- Biomedical Multi-label Threshold Robustness: Current model performance in clinical settings is highly sensitive to threshold selection; improving robustness to shifts between training and test distributions is a significant clinical and technical bottleneck.

### Rejected Candidates
- [concept] HexagonalWarriorMamba (HWMamba) (`hexagonalwarriormamba-hwmamba`) - subcomponent_of_broader_mechanism: This is a specific model implementation; the underlying mechanism of 2D transformation for SSMs is the reusable contribution.
- [open_question] Improving Threshold Robustness for ECGs (`improving-threshold-robustness-mamba-unet-hybrid`) - other: Renamed to be more general and descriptive, as the original title was tied to specific architectures.

## Datasets

- [[physionet-2021-challenge]]

## Links

- [Abstract](https://arxiv.org/abs/2605.17875)
- [PDF](https://arxiv.org/pdf/2605.17875)

