---
# CSL-compatible fields
title: "Transfer Learning using 66 Diseases for Disease Forecasting Applications"
author:
  - literal: "Lauren J. Beesley"
  - literal: "Alexander C. Murph"
  - literal: "Dave Osthus"
  - literal: "Lauren A Castro"
issued:
  date-parts:
    - [2026, 5, 26]
url: "https://arxiv.org/abs/2605.27269"

# Custom fields
paper_id: "2605.27269"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "dataset"
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
processed_at: "2026-05-29T08:37:41Z"
created_at: "2026-05-29T08:37:41Z"
---

# Transfer Learning using 66 Diseases for Disease Forecasting Applications

**Authors**: Lauren J. Beesley, Alexander C. Murph, Dave Osthus, Lauren A Castro
**Date**: 2026-05-26
**Paper ID**: [openalex:2605.27269](https://arxiv.org/abs/2605.27269)

## Summary

This paper explores the utility of large-scale transfer learning for infectious disease forecasting by training models across 66 different diseases and multiple reporting data streams. The study systematically evaluates the performance impact of integrating auxiliary data streams, finding consistent improvements in most scenarios but noting potential performance degradation when the added data lacks sufficient domain similarity. To support future research, the authors release a comprehensive, publicly-available database curated from these disease reporting sources.

## Key Contributions

- Compiled a large-scale, publicly-available database of 66 infectious diseases and multiple data streams for community-wide forecasting research.
- Demonstrated that multi-source data integration improves disease forecasting performance in approximately 84.9% of evaluated time series and model configurations.
- Identified that the quality and relevance of supplemental data are critical, as incorporating data that are highly dissimilar to the target stream can negatively impact forecasting accuracy.

## Open Questions & Future Work

- [[principled-data-selection-transfer-learning]]

## Archivist Review

The paper provides a significant empirical investigation into the effects of multi-source transfer learning in epidemiology. I approved the open question regarding principled data selection because it addresses a fundamental, recurring bottleneck in cross-domain time-series forecasting. No specific new concepts or datasets were approved as they were either too domain-specific or did not meet the rigorous bar for standalone permanence in the vault.

### Approved Open Questions
- Principled Data Selection for Transfer Learning: The absence of systematic data selection frameworks prevents reliable wide-scale adoption of cross-pathogen transfer learning, as current methods cannot predict if auxiliary data will be beneficial or detrimental to model robustness.

## Links

- [Abstract](https://arxiv.org/abs/2605.27269)
- [PDF](https://arxiv.org/pdf/2605.27269)

