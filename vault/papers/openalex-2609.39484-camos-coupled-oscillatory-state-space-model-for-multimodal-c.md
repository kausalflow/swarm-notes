---
# CSL-compatible fields
title: "CAMOS: Coupled Oscillatory State-Space Model for Multimodal Clinical Time-Series"
author:
  - literal: "Maxx Richard Rahman"
  - literal: "Mostafa Hammouda"
  - literal: "Wolfgang Maaß"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2609.39484"

# Custom fields
paper_id: "2609.39484"
paper_source: "openalex"
domain: "medicine"
tags:
  - "state-space-model"
  - "ssm"
  - "multimodal"
  - "time-series"
  - "forecasting"
  - "long-context"
  - "robustness"
  - "benchmark"
architectures:
  - "mamba"
datasets:
  []
concept_slugs:
  - "coupled-oscillatory-state-space-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-03T10:07:59Z"
created_at: "2026-10-03T10:07:59Z"
---

# CAMOS: Coupled Oscillatory State-Space Model for Multimodal Clinical Time-Series

**Authors**: Maxx Richard Rahman, Mostafa Hammouda, Wolfgang Maaß
**Date**: 2026-09-30
**Paper ID**: [openalex:2609.39484](https://arxiv.org/abs/2609.39484)

## Summary

The paper identifies a fundamental representational limitation in linear state-space models when handling missing modalities in longitudinal clinical data, proving that static transition operators fail to capture interactions between jointly present or absent modalities. To resolve this, the authors propose CAMOS (Coupled Oscillatory State-Space Model), which introduces second-order oscillators coupled through an availability-gated differential equation transition matrix. Through mathematical stabilization via Gershgorin budgets and channel factorization ensuring parallel scans, CAMOS achieves superior performance on ADNI staging, landmark prediction, and longitudinal forecasting, while exhibiting robust zero-shot transfer on OASIS-3.

## Key Contributions

- Proves that standard linear state-space models with static transition operators cannot represent cross-modal presence interactions when modalities are missing.
- Proposes CAMOS, a coupled oscillatory state-space model where second-order oscillators are coupled through a matrix gated by modality availability inside the differential equation.
- Introduces a per-channel Gershgorin budget, energy bounds for availability transitions, and channel factorization enabling exact associative parallel scans.
- Outperforms uncoupled oscillatory SSMs and clinical fusion models on ADNI across same-visit staging, landmark prediction, and longitudinal forecasting, and avoids zero-shot collapse on OASIS-3.

## Limitations

Future work could extend coupled oscillatory state-space models to higher-dimensional or streaming real-time clinical monitoring environments beyond longitudinal cohorts.

## Open Questions & Future Work

- [[multimodal-clinical-time-series-forecasting]]

## Key Concepts

- [[coupled-oscillatory-state-space-model]]: A state-space model for multimodal clinical time series where second-order oscillators are coupled via an availability-gated differential equation transition operator.

## Archivist Review

Approved the core architectural concept of the coupled oscillatory state-space model and a focused open question on multimodal clinical time-series forecasting. Rejected the ADNI dataset candidate as it is already an existing vault dataset.

### Approved Concepts
- Coupled Oscillatory State-Space Model: Central architecture novelty replacing fixed linear transitions with availability-gated coupled oscillators to capture cross-modal presence interactions in irregular clinical time series.

### Approved Open Questions

### Rejected Candidates
- [dataset] ADNI Dataset (`adni-dataset`) - duplicate_existing: Dataset is an existing benchmark already present in the vault.

## Links

- [Abstract](https://arxiv.org/abs/2609.39484)
- [PDF](https://arxiv.org/pdf/2609.39484)

