---
# CSL-compatible fields
title: "Forecasting the Emergence and Evolution of Crash Hotspots: A Unified Deep Learning Framework for Proactive Traffic Safety"
author:
  - literal: "Jingwen Zhu"
  - literal: "Keshu Wu"
  - literal: "Pei Li"
  - literal: "Steven T. Parker"
  - literal: "Bin Ran"
  - literal: "David A. Noyce"
issued:
  date-parts:
    - [2026, 7, 27]
url: "https://arxiv.org/abs/2607.24168"

# Custom fields
paper_id: "2607.24168"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "attention-mechanism"
  - "time-series"
  - "forecasting"
  - "mixture-of-experts"
  - "moe"
  - "spatial-attention"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-30T07:26:46Z"
created_at: "2026-07-30T07:26:46Z"
---

# Forecasting the Emergence and Evolution of Crash Hotspots: A Unified Deep Learning Framework for Proactive Traffic Safety

**Authors**: Jingwen Zhu, Keshu Wu, Pei Li, Steven T. Parker, Bin Ran, David A. Noyce
**Date**: 2026-07-27
**Paper ID**: [openalex:2607.24168](https://arxiv.org/abs/2607.24168)

## Summary

The paper introduces HERALD, a unified deep learning framework for proactive traffic safety that models the emergence, evolution, and life-cycle dynamics of crash hotspots. Utilizing a CNN-Transformer with a mixture-of-experts mechanism, HERALD processes weekly county-level risk maps to forecast future hotspot locations across both urban and rural environments. Evaluated on six Wisconsin counties, HERALD outperforms multiple baselines in forecasting accuracy and early risk detection, shifting traffic management from reactive mapping to proactive anticipation.

## Key Contributions

- Introduces HERALD, a unified deep learning framework for proactive traffic safety that simultaneously detects hotspot birth, forecasts future locations, and tracks life-cycle dynamics.
- Employs a CNN-Transformer architecture with a mixture-of-experts to handle heterogeneous settings ranging from dense urban cores to sparse rural corridors.
- Outperforms five identically trained baselines across six heterogeneous Wisconsin counties in forecasting accuracy, hotspot localization precision, and early risk flagging.

## Limitations

Tested primarily across six Wisconsin counties; generalization to broader national or international transportation networks with varying reporting standards remains to be evaluated.

## Archivist Review

Reviewed the candidate concept HERALD Framework and rejected it as paper-local application machinery for traffic safety rather than a broad, reusable time-series forecasting primitive. No datasets or open questions were proposed or required.

### Rejected Candidates
- [concept] HERALD Framework (`herald-framework`) - paper_local: Paper-local application framework for traffic crash hotspots lacking independent technical reusability beyond its specific transportation setting.

## Links

- [Abstract](https://arxiv.org/abs/2607.24168)
- [PDF](https://arxiv.org/pdf/2607.24168)

