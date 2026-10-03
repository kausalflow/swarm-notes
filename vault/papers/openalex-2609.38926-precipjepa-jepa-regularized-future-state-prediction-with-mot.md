---
# CSL-compatible fields
title: "PrecipJEPA: JEPA-Regularized Future-State Prediction with Motion-Source Rendering for Precipitation Nowcasting"
author:
  - literal: "Yufeng Zhu"
  - literal: "Dan Niu"
  - literal: "Qiliang Wu"
  - literal: "Weiwei Huang"
  - literal: "Yixiao Liang"
  - literal: "Yongchao Feng"
  - literal: "Chunlei Shi"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2609.38926"

# Custom fields
paper_id: "2609.38926"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "self-supervised-learning"
  - "spatio-temporal"
  - "radar-nowcasting"
architectures:
  []
datasets:
  - "sevir"
  - "meteonet"
concept_slugs:
  - "precipjepa"
  - "parallel-motion-source-renderer"
dataset_slugs:
  - "sevir"
  - "meteonet"
skill: "TimeSeriesSkill"
processed_at: "2026-10-03T10:08:57Z"
created_at: "2026-10-03T10:08:57Z"
---

# PrecipJEPA: JEPA-Regularized Future-State Prediction with Motion-Source Rendering for Precipitation Nowcasting

**Authors**: Yufeng Zhu, Dan Niu, Qiliang Wu, Weiwei Huang, Yixiao Liang, Yongchao Feng, Chunlei Shi
**Date**: 2026-09-30
**Paper ID**: [openalex:2609.38926](https://arxiv.org/abs/2609.38926)

## Summary

PrecipJEPA is a novel framework for precipitation nowcasting that integrates a structured forecasting path with an auxiliary History-Masked JEPA (H-JEPA) path to supervise the online encoder directly from radar history. It features a Task-Driven Future-State Predictor (TFP) and a Parallel Motion-Source Renderer (PMSR) that explicitly separate echo displacement from intensity changes. Evaluations on the SEVIR and MeteoNet datasets demonstrate large improvements in critical success index (CSI) at high rainfall thresholds and robust long-term forecasting performance.

## Key Contributions

- Proposes PrecipJEPA, a JEPA-regularized precipitation nowcasting framework that couples a structured forecasting path with an auxiliary history-masked self-supervised path.
- Introduces the Parallel Motion-Source Renderer (PMSR) to explicitly decode motion and source-sink fields for transforming observations into future frames.
- Achieves substantial performance improvements on SEVIR (118.6% higher highest-threshold CSI) and MeteoNet (35.1% higher highest-threshold CSI) over strong baselines.

## Key Concepts

- [[precipjepa]]: A JEPA-regularized future-state prediction framework for precipitation nowcasting that couples structured forecasting with history-masked self-supervised auxiliary encoding.
- [[parallel-motion-source-renderer]]: A decoding mechanism that converts predicted states into motion and source-sink fields to transform latest observations into future frames.

## Archivist Review

Approved the core framework PrecipJEPA and its motion-source rendering submodule as distinct reusable concepts in spatiotemporal precipitation nowcasting, along with SEVIR and MeteoNet datasets. Rejected the open question as generic boilerplate future work.

### Approved Concepts
- PrecipJEPA: Core framework proposed for precipitation nowcasting, combining JEPA self-supervised regularization with motion-source rendering.
- Parallel Motion-Source Renderer: A novel rendering mechanism that explicitly decouples echo displacement from intensity change for accurate radar-echo prediction.

### Rejected Candidates
- [open_question] Probabilistic Precipitation Nowcasting Extension (`probabilistic-precipitation-nowcasting`) - weak_evidence: Standard boilerplate future work proposing an extension to probabilistic forecasting without identifying a specific methodological bottleneck.

## Datasets

- [[sevir]]
- [[meteonet]]

## Links

- [Abstract](https://arxiv.org/abs/2609.38926)
- [PDF](https://arxiv.org/pdf/2609.38926)

