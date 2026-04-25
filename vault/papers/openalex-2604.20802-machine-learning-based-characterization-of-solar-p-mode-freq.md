---
# CSL-compatible fields
title: "Machine Learning-Based Characterization of Solar p-Mode Frequency Shifts during Solar Cycle 25"
author:
  - literal: "Rekha Jain"
  - literal: "Akash Kumar"
  - literal: "Sushanta C. Tripathy"
issued:
  date-parts:
    - [2026, 4, 22]
url: "https://arxiv.org/abs/2604.20802"

# Custom fields
paper_id: "2604.20802"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-25T06:15:44Z"
created_at: "2026-04-25T06:15:44Z"
---

# Machine Learning-Based Characterization of Solar p-Mode Frequency Shifts during Solar Cycle 25

**Authors**: Rekha Jain, Akash Kumar, Sushanta C. Tripathy
**Date**: 2026-04-22
**Paper ID**: [openalex:2604.20802](https://arxiv.org/abs/2604.20802)

## Summary

This paper investigates the use of machine learning to model and forecast solar p-mode frequency shifts, which exhibit an 11-year cyclic behavior correlated with solar activity indices. By characterizing these shifts, the authors aim to provide a more robust link between internal solar dynamics and space weather proxies. The approach offers a new, independent method for tracking the ascending and descending phases of solar cycle 25. The results enhance our understanding of how interior acoustic oscillations can serve as precursors for heliospheric plasma conditions.

## Key Contributions

- Developed a machine-learning framework to characterize solar p-mode frequency shifts, establishing them as an independent indicator for solar activity phases.
- Provided long-term predictions for p-mode frequency shifts for the remainder of solar cycle 25, linking interior solar dynamics to external activity proxies.
- Demonstrated the utility of p-mode shifts as a robust, quantitative tool for tracing energy drivers from the solar interior to geospace.

## Open Questions & Future Work

- [[improving-ml-qbo-solar-forecasting]]

## Archivist Review

The paper applies existing ML forecasting methods to a specific heliospheric task. As such, no novel reusable concepts were identified that merit a permanent vault entry. One open question regarding the failure of current ML architectures to capture specific sub-decadal oscillatory phenomena (QBOs) in solar time-series was approved, as it addresses a broader technical limitation in time-series modeling of physical processes.

### Approved Open Questions
- Enhancing ML for QBOs in Solar Forecasting: The inability to capture QBOs limits the diagnostic utility of these forecasting models for evaluating solar dynamo theories and understanding the coupling between the solar interior and its exterior, which is critical for space weather prediction.

### Rejected Candidates
- [concept] P-mode frequency shift modeling framework (`p-mode-frequency-shift-modeling`) - paper_local: This refers to the specific domain application rather than a reusable machine learning methodology or architectural novelty.

## Links

- [Abstract](https://arxiv.org/abs/2604.20802)
- [PDF](https://arxiv.org/pdf/2604.20802)

