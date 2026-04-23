---
# CSL-compatible fields
title: "Circadian Phase Locking of Epilepsy Seizures in Wearable Data: A Single-Patient Case Study"
author:
  - literal: "Berenika Ewart-James"
  - literal: "Matthew Wragg"
  - literal: "Nawid Keshtmand, Amberly Brigden"
  - literal: "Paul Marshall"
  - literal: "Raúl Santos‐Rodríguez"
issued:
  date-parts:
    - [2026, 4, 20]
url: "https://arxiv.org/abs/2604.18297"

# Custom fields
paper_id: "2604.18297"
paper_source: "openalex"
domain: "medicine"
tags:
  - "time-series"
  - "forecasting"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "physiological-phase-event-coupling"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-23T06:56:25Z"
created_at: "2026-04-23T06:56:25Z"
---

# Circadian Phase Locking of Epilepsy Seizures in Wearable Data: A Single-Patient Case Study

**Authors**: Berenika Ewart-James, Matthew Wragg, Nawid Keshtmand, Amberly Brigden, Paul Marshall, Raúl Santos‐Rodríguez
**Date**: 2026-04-20
**Paper ID**: [openalex:2604.18297](https://arxiv.org/abs/2604.18297)

## Summary

This study investigates whether seizure onsets in epilepsy patients are synchronized with endogenous circadian rhythms derived from wearable inter-beat interval (IBI) sensor data. By applying band-limited filtering and Hilbert-based phase estimation, the authors demonstrate that seizures exhibit significant concentration around specific circadian phases, providing an interpretable bridge between continuous physiological monitoring and sporadic clinical events. The findings suggest that explicit physiological phase representation is a promising avenue for improving seizure forecasting compared to standard linear or clock-based temporal models.

## Key Contributions

- Introduces a proof-of-concept framework for linking wearable-derived circadian phase (from IBI signals) to seizure event timing using circular statistics.
- Demonstrates significant seizure phase concentration at the circadian scale, surpassing simple clock-time features in a single-patient longitudinal dataset.
- Provides evidence that Hilbert-based phase estimation captures clinically relevant temporal structures that are typically missed by linear modeling of physiological signals.

## Open Questions & Future Work

- [[multi-scale-physiological-phase-locking]]

## Key Concepts

- [[physiological-phase-event-coupling]]: The quantification of event occurrence probability based on the phase of endogenous physiological rhythms extracted from continuous wearable monitoring.

## Archivist Review

I have approved a generalized concept, 'Physiological Phase-Event Coupling', which generalizes the specific focus on seizures to a broader class of event-monitoring problems in time series. I also approved a multi-scale open question that focuses on the transition from static, single-scale analysis to non-stationary, multi-scale oscillation modeling. The specific 'circadian' candidate was rejected as too narrow and redundant with the generalized concept.

### Approved Concepts
- Physiological Phase-Event Coupling: Provides a principled way to translate continuous sensor-derived oscillatory rhythms into predictive priors for sparse clinical events, moving beyond clock-time features.

### Approved Open Questions
- Multi-scale physiological phase locking: Moving from single-scale to multi-scale phase modeling is essential for developing clinically actionable forecasting tools that operate on biologically realistic, long-term cycles.

### Rejected Candidates
- [concept] Circadian Phase Locking of Seizures (`circadian-phase-locking-of-seizures`) - duplicate_existing: This is too paper-specific; 'Physiological Phase-Event Coupling' captures the underlying, reusable methodology.

## Links

- [Abstract](https://arxiv.org/abs/2604.18297)
- [PDF](https://arxiv.org/pdf/2604.18297)

