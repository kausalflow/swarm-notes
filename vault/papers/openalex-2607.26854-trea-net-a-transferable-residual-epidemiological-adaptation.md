---
# CSL-compatible fields
title: "TREA-Net: A Transferable Residual Epidemiological Adaptation Network for Dengue Incidence Forecasting"
author:
  - literal: "Inesh Shukla"
  - literal: "Madhurima Panja"
  - literal: "Tanujit Chakraborty"
  - literal: "Chittaranjan Hens"
issued:
  date-parts:
    - [2026, 7, 29]
url: "https://arxiv.org/abs/2607.26854"

# Custom fields
paper_id: "2607.26854"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "forecasting"
  - "zero-shot-learning"
  - "transfer-learning"
  - "conformal-prediction"
  - "uncertainty-quantification"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-01T07:22:46Z"
created_at: "2026-08-01T07:22:46Z"
---

# TREA-Net: A Transferable Residual Epidemiological Adaptation Network for Dengue Incidence Forecasting

**Authors**: Inesh Shukla, Madhurima Panja, Tanujit Chakraborty, Chittaranjan Hens
**Date**: 2026-07-29
**Paper ID**: [openalex:2607.26854](https://arxiv.org/abs/2607.26854)

## Summary

TREA-Net is a transferable residual epidemiological adaptation network designed for multi-week dengue forecasting under data-scarce conditions. It combines neural forecasting backbones with Environmental Time-Series SIR model projections and learns a lightweight gated residual correction transferable across regions. Evaluated across multiple neural backbones and transfer settings, TREA-Net significantly improves forecasting accuracy and reduces prediction interval widths when integrated with conformal prediction.

## Key Contributions

- Proposed TREA-Net, a transferable residual epidemiological adaptation network that augments neural forecasting backbones with SIR projections and a lightweight gated residual correction.
- Achieved consistent improvements across 5 neural backbones and 10 transfer settings, significantly outperforming baselines when transferring from Colombia and Nicaragua to Mexico and Malaysia.
- Integrated with TiRex to achieve the lowest mean absolute error across target datasets, while conformal prediction reduced 8-week prediction interval width by 29.6% in Mexico.

## Archivist Review

Reviewed the proposed candidates for TREA-Net. The model architecture TREA-Net is tied closely to epidemiological transfer learning for dengue and lacks general time-series methodology reusability. Similarly, the open question focuses on domain-specific transfer extensions for infectious diseases rather than a fundamental theoretical bottleneck. Both candidates were rejected to maintain vault selectivity.

### Rejected Candidates
- [concept] TREA-Net (`trea-net`) - paper_local: TREA-Net is a paper-specific architecture and application-specific hybrid model for dengue forecasting rather than a broadly reusable time-series mechanism.
- [open_question] Generalizing Epidemic Transfer Learning (`generalizing-epidemic-transfer-learning-to-new-diseases-and-disrupted-histories`) - low_impact: This open question is tailored to the specific application domain of epidemiological surveillance transfer learning rather than a foundational time-series or ML bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2607.26854)
- [PDF](https://arxiv.org/pdf/2607.26854)

