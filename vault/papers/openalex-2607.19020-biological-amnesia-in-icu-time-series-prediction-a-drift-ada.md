---
# CSL-compatible fields
title: "Biological Amnesia in ICU Time-Series Prediction: A Drift-Adaptive Two-Stream Architecture with Temporal Retrieval"
author:
  - literal: "Fatema Ferdous Tamanna"
  - literal: "K. M. Merajul Arefin"
  - literal: "Md Abdul Masud"
issued:
  date-parts:
    - [2026, 7, 21]
url: "https://arxiv.org/abs/2607.19020"

# Custom fields
paper_id: "2607.19020"
paper_source: "openalex"
domain: "medicine"
tags:
  - "time-series"
  - "retrieval-augmented-generation"
  - "rag"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  - "mimic-iv"
concept_slugs:
  []
dataset_slugs:
  - "mimic-iv"
skill: "TimeSeriesSkill"
processed_at: "2026-07-24T07:24:56Z"
created_at: "2026-07-24T07:24:56Z"
---

# Biological Amnesia in ICU Time-Series Prediction: A Drift-Adaptive Two-Stream Architecture with Temporal Retrieval

**Authors**: Fatema Ferdous Tamanna, K. M. Merajul Arefin, Md Abdul Masud
**Date**: 2026-07-21
**Paper ID**: [openalex:2607.19020](https://arxiv.org/abs/2607.19020)

## Summary

The paper introduces a drift-adaptive two-stream architecture for ICU time-series prediction that structurally separates stable patient physiology from evolving treatment representations. By restricting parameter updates to the treatment stream upon specific distribution and accuracy triggers, and integrating an attribution-driven Temporal RAG module for literature grounding, the framework adapts to institutional drift without distorting learned patient biology. Evaluated on 84,792 MIMIC-IV stays, the method demonstrates superior discrimination and calibration in high-stakes clinical tasks like septic shock prediction compared to standard monolithic retraining.

## Key Contributions

- Proposed an adaptive clinical intelligence architecture that structurally decouples physiological from treatment representations in ICU time-series prediction.
- Confined parameter updates exclusively to the treatment stream based on a dual distributional and accuracy trigger.
- Introduced an attribution-driven Temporal RAG module to ground predictions in patient-specific, era-matched biomedical literature.
- Evaluated on 84,792 MIMIC-IV stays (2008-2022) under a strict chronological split, showing superior septic shock discrimination and calibration compared to static or fully retrained baselines.

## Limitations

Future work could explore broader institutional deployments and alternative streaming protocols to further test the decoupling efficacy.

## Open Questions & Future Work

- [[prospective-multicenter-evaluation-adaptive-cdss]]

## Archivist Review

Approved the canonical MIMIC-IV dataset and the explicit open question regarding prospective multi-center evaluation of drift-adaptive CDSS architectures. No new standalone vault concepts met the strict novelty and reusability bar for time-series forecasting and clinical adaptation.

### Approved Open Questions
- Prospective and Multi-Center CDSS Evaluation: Evaluating adaptive architectures prospectively and across multi-center cohorts is vital for verifying whether structural decoupling and evidence retrieval improvements translate reliably to bedside patient safety in diverse clinical settings.

### Rejected Candidates
- [dataset] MIMIC-IV (`mimic-iv`) - duplicate_existing: MIMIC-IV is already tracked in the vault.

## Datasets

- [[mimic-iv]]

## Links

- [Abstract](https://arxiv.org/abs/2607.19020)
- [PDF](https://arxiv.org/pdf/2607.19020)

