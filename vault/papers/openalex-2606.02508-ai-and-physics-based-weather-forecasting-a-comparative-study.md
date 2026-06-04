---
# CSL-compatible fields
title: "AI and physics-based weather forecasting: A comparative study"
author:
  - literal: "Mátyás Kocsis"
  - literal: "Sándor Baran"
issued:
  date-parts:
    - [2026, 6, 1]
url: "https://arxiv.org/abs/2606.02508"

# Custom fields
paper_id: "2606.02508"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
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
processed_at: "2026-06-04T08:43:22Z"
created_at: "2026-06-04T08:43:22Z"
---

# AI and physics-based weather forecasting: A comparative study

**Authors**: Mátyás Kocsis, Sándor Baran
**Date**: 2026-06-01
**Paper ID**: [openalex:2606.02508](https://arxiv.org/abs/2606.02508)

## Summary

This paper conducts a systematic performance comparison between ECMWF's operational physics-based Integrated Forecasting System (IFS) and its data-driven Artificial Intelligence Forecasting System (AIFS) for medium-range wind-speed ensemble forecasting. The authors evaluate raw and post-processed forecasts (using EMOS and quantile regression) across over 9000 global synoptic stations. The study finds that while physics-based models currently maintain superior raw predictive skill, post-processing techniques effectively mitigate performance differences. These findings highlight the significant trade-off between the superior raw performance of traditional numerical weather prediction and the extreme computational efficiency of modern AI-based ensemble systems.

## Key Contributions

- Systematic comparative evaluation of the operational AI-based AIFS against the physics-based IFS for medium-range wind-speed ensemble forecasting.
- Demonstrated that raw physics-based IFS forecasts significantly outperform AI-based AIFS predictions across all forecast horizons.
- Validated that post-processing via EMOS and quantile regression substantially narrows the performance gap between AI and physics-based models, especially for longer lead times.

## Open Questions & Future Work

- [[comparative-evaluation-ai-physics-weather-forecasts]]

## Archivist Review

I applied a high bar for novelty. No specific reusable architectural concepts or datasets were identified that were not already generic industry knowledge (e.g., EMOS and Quantile Regression are established statistical methods). I approved the open question regarding comparative AI-physics weather forecasting as it captures the strategic research agenda for a field currently in transition.

### Approved Open Questions
- Comparative Evaluation of AI and Physics Weather Forecasts: As weather services transition toward hybrid forecasting systems combining NWP and AI, it is critical to determine the strengths and weaknesses of each approach across diverse operational scenarios to guide future model development and integration strategies.

### Rejected Candidates
- [open_question] Comparative Evaluation of AI and Physics Weather Forecasts (`comparative-evaluation-ai-physics-weather-forecasts`) - other: The question is well-posed but the title/slug is slightly redundant for the vault; the core issue is evaluating the skill of physics-based vs AI models in a comparative framework. (Self-Correction: I am approving this as a core open question as it frames the research agenda for hybrid forecasting).

## Links

- [Abstract](https://arxiv.org/abs/2606.02508)
- [PDF](https://arxiv.org/pdf/2606.02508)

