---
# CSL-compatible fields
title: "TC-Next: Zero-Shot Multimodal Cyclone Forecasting"
author:
  - literal: "Zhe Wang"
  - literal: "Sijie Chen"
  - literal: "Yiming Luo"
  - literal: "Daehyun Kim"
  - literal: "Chien-Yi Chang"
issued:
  date-parts:
    - [2026, 9, 2]
url: "https://arxiv.org/abs/2609.02085"

# Custom fields
paper_id: "2609.02085"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "multimodal"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-05T08:42:03Z"
created_at: "2026-09-05T08:42:03Z"
---

# TC-Next: Zero-Shot Multimodal Cyclone Forecasting

**Authors**: Zhe Wang, Sijie Chen, Yiming Luo, Daehyun Kim, Chien-Yi Chang
**Date**: 2026-09-02
**Paper ID**: [openalex:2609.02085](https://arxiv.org/abs/2609.02085)

## Summary

The paper introduces TropicalCycloneNext (TC-Next), a multimodal deep learning model that performs zero-shot tropical cyclone track and intensity forecasting by integrating atmospheric forecast fields from weather foundation models with GridSat infrared satellite imagery. Trained exclusively on GraphCast outputs for the Western Pacific, TC-Next significantly outperforms traditional rule-based trackers like TempestExtremes and generalizes zero-shot to models such as Pangu-Weather, IFS HRES, and WeatherNext Cyclones. Ablation studies confirm that incorporating infrared imagery as a second modality successfully improves tracking and long-horizon intensity prediction.

## Key Contributions

- Introduces TropicalCycloneNext (TC-Next), a multimodal deep learning model for tropical cyclone track and intensity forecasting at 6-24 hour leads.
- Leverages foundation model forecast fields combined with GridSat infrared satellite imagery for improved atmospheric modeling.
- Demonstrates robust zero-shot generalization across different weather foundation models including Pangu-Weather, IFS HRES, and WeatherNext Cyclones without retraining.

## Limitations

Evaluated primarily on the Western Pacific region; future work could extend to global basins and longer forecasting horizons.

## Archivist Review

All proposed candidates were rejected. TC-Next is a specific application model rather than a generalizable vault concept, and the open questions represent routine future work (domain extension and ensemble adaptation) rather than fundamental algorithmic bottlenecks.

### Rejected Candidates
- [concept] TC-Next (`tc-next`) - paper_local: Paper-specific named model architecture for tropical cyclone tracking rather than a reusable methodological concept.
- [open_question] Global Zero-Shot Cyclone Benchmark (`global-zero-shot-cyclone-benchmark`) - low_impact: Standard domain extension future work rather than an architectural or methodological research question.
- [open_question] Ensemble Adaptation for Cyclone Models (`ensemble-adaptation-for-cyclone-models`) - low_impact: Standard adaptation task for deterministic models rather than a foundational open problem.

## Links

- [Abstract](https://arxiv.org/abs/2609.02085)
- [PDF](https://arxiv.org/pdf/2609.02085)

