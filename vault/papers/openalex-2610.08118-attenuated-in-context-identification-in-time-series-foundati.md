---
# CSL-compatible fields
title: "Attenuated in-context identification in time-series foundation models: diagnosis under counterfactual inputs and repair by synthetic forced-system fine-tuning"
author:
  - literal: "Hong-In Won"
issued:
  date-parts:
    - [2026, 10, 6]
url: "https://arxiv.org/abs/2610.08118"

# Custom fields
paper_id: "2610.08118"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "in-context-learning"
  - "foundation-model"
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
processed_at: "2026-10-09T11:34:42Z"
created_at: "2026-10-09T11:34:42Z"
---

# Attenuated in-context identification in time-series foundation models: diagnosis under counterfactual inputs and repair by synthetic forced-system fine-tuning

**Authors**: Hong-In Won
**Date**: 2026-10-06
**Paper ID**: [openalex:2610.08118](https://arxiv.org/abs/2610.08118)

## Summary

This paper diagnoses the limitations of covariate-aware time-series foundation models (TSFMs) like Chronos-2, TimesFM-2.5, and TabPFN-TS when performing training-free what-if counterfactual predictions on forced engineering systems. The study reveals that TimesFM-2.5 and TabPFN-TS are memoryless, while Chronos-2 attenuates dynamics in context. A proposed fine-tuning strategy using synthetic forced systems successfully restores response magnitude and improves counterfactual accuracy, though it highlights trade-offs with univariate forecasting performance.

## Key Contributions

- Evaluated covariate-aware time-series foundation models (Chronos-2, TimesFM-2.5, TabPFN-TS) on forced engineering systems with exact counterfactuals, revealing memorylessness in TimesFM-2.5 and TabPFN-TS, and dynamic attenuation in Chronos-2.
- Demonstrated that context dither at inference reduces what-if prediction error across synthetic classes without retraining.
- Showed that a 26-minute fine-tune on synthetic forced systems restores response magnitude and outperforms structure-agnostic identification on Wiener-Hammerstein and friction classes.
- Identified trade-offs where fine-tuning sacrifices part of the univariate forecasting skill and classical identification remains superior on three of four measured plants.

## Limitations

Fine-tuned models sacrifice part of their univariate forecasting skill, and classical identification remains superior on three of four measured plants.

## Open Questions & Future Work

- [[preventing-catastrophic-forgetting-tsfm]]

## Archivist Review

Applied strict selectivity: no new vault concepts or datasets met the threshold for permanent standalone storage. The open question on catastrophic forgetting in TSFMs is a duplication or overlaps with broader adaptation and fine-tuning trade-off questions already existing in the vault, and therefore was rejected as duplicate existing.

### Approved Open Questions
- Preventing Catastrophic Forgetting in TSFMs: Replay therefore largely kept the what-if gains but did not prevent forgetting; it made univariate forecasting worse still (one run). Preventing forgetting remains open.

### Rejected Candidates
- [open_question] Preventing Catastrophic Forgetting in TSFMs (`preventing-catastrophic-forgetting-tsfm`) - duplicate_existing: duplicate_existing

## Links

- [Abstract](https://arxiv.org/abs/2610.08118)
- [PDF](https://arxiv.org/pdf/2610.08118)

