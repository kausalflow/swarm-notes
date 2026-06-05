---
# CSL-compatible fields
title: "Systematic Gray-Box Identification Methodology for Voltage Source Converters"
author:
  - literal: "Nicolae Darii"
  - literal: "Luis A. Garcia-Reyes"
  - literal: "Ignasi Ventura Nadal"
  - literal: "Oscar Saborio Romano"
  - literal: "Ranjan Sharma"
  - literal: "Oriol Gomis-Bellmunt"
  - literal: "Nicolaos A. Cutululis"
issued:
  date-parts:
    - [2026, 6, 2]
url: "https://arxiv.org/abs/2606.03567"

# Custom fields
paper_id: "2606.03567"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "interpretability"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "systematic-gray-box-identification-methodology"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-05T08:39:49Z"
created_at: "2026-06-05T08:39:49Z"
---

# Systematic Gray-Box Identification Methodology for Voltage Source Converters

**Authors**: Nicolae Darii, Luis A. Garcia-Reyes, Ignasi Ventura Nadal, Oscar Saborio Romano, Ranjan Sharma, Oriol Gomis-Bellmunt, Nicolaos A. Cutululis
**Date**: 2026-06-02
**Paper ID**: [openalex:2606.03567](https://arxiv.org/abs/2606.03567)

## Summary

This paper presents a systematic gray-box identification framework for voltage-source converters (VSC) that integrates physical white-box models with iterative time-domain calibration. By leveraging terminal time-series data, the method accurately estimates controller parameters to mimic the behavior of complex electromagnetic transient (EMT) black-box models. The approach is validated through rigorous frequency-domain metrics, including Nyquist analysis and singular value decomposition, providing a reliable tool for stability analysis of proprietary converter systems. The methodology proves robust against increasing levels of structural uncertainty, offering a viable alternative to traditional frequency-domain identification.

## Key Contributions

- Introduced a gray-box identification framework that calibrates physics-informed white-box models to terminal black-box time-series data.
- Developed time-domain calibration techniques to improve surrogate model accuracy and stability across wide operating ranges.
- Proposed quantitative frequency-domain validation metrics using Nyquist analysis and singular value decomposition for assessing model divergence.
- Demonstrated accuracy in recovering parameters under varying degrees of structural uncertainty, suitable for IP-protected converter models.

## Open Questions & Future Work

- [[hybrid-time-frequency-domain-identification]]

## Key Concepts

- [[systematic-gray-box-identification-methodology]]: A method for calibrating physics-based converter models using only terminal time-series observations.

## Archivist Review

I approved the core gray-box identification framework as it provides a robust, reusable approach to surrogate modeling for physical systems under structural uncertainty. I also approved the open question regarding hybrid time-frequency optimization because it identifies a critical, unresolved research bottleneck in maintaining stability guarantees for gray-box models. No datasets were approved as none were specifically named or highlighted as a reusable contribution.

### Approved Concepts
- Systematic Gray-Box Identification Methodology: Provides a framework for bridging physical white-box models with black-box terminal data, crucial for protecting intellectual property while maintaining model fidelity.

### Approved Open Questions
- Hybrid Time-Frequency Identification Framework: This addresses the fundamental tension between achieving time-domain replication and maintaining the structural integrity required for valid frequency-domain small-signal stability analysis.

## Links

- [Abstract](https://arxiv.org/abs/2606.03567)
- [PDF](https://arxiv.org/pdf/2606.03567)

