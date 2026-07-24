---
# CSL-compatible fields
title: "On the sensitivity of machine-learned probabilistic weather forecast models to scale-aware scoring rules"
author:
  - literal: "Simon Lang"
  - literal: "Martin Leutbecher"
  - literal: "Sam Hatfield"
issued:
  date-parts:
    - [2026, 7, 21]
url: "https://arxiv.org/abs/2607.19161"

# Custom fields
paper_id: "2607.19161"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "evaluation"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-24T07:25:14Z"
created_at: "2026-07-24T07:25:14Z"
---

# On the sensitivity of machine-learned probabilistic weather forecast models to scale-aware scoring rules

**Authors**: Simon Lang, Martin Leutbecher, Sam Hatfield
**Date**: 2026-07-21
**Paper ID**: [openalex:2607.19161](https://arxiv.org/abs/2607.19161)

## Summary

This paper presents a preliminary study evaluating the sensitivity of machine-learned probabilistic weather forecast models to different univariate and multivariate scale-aware scoring rules, such as fair CRPS, global energy scores, and graph energy scores. Comparing these variants within the AIFS-CRPS global weather forecast model reveals broadly similar forecast skill across standard verification metrics, though graph energy scores show slight improvements in the tropics. Furthermore, the analysis demonstrates that explicit scale-awareness in loss functions enhances the spectral realism of predicted weather fields.

## Key Contributions

- Compared univariate and multivariate scoring rules including fair CRPS, fair global energy score, and graph energy score for training AIFS-CRPS global weather forecast models
- Demonstrated that multivariate scores are a viable alternative to CRPS-based training with broadly similar forecast skill across standard verification metrics
- Showed that incorporating explicit scale-awareness in loss functions improves the spectral realism of forecast fields

## Limitations

Preliminary study focusing on comparison of specific scoring rules and their impact on spectral realism and forecast skill.

## Open Questions & Future Work

- [[scaling-localization-scale-awareness-ml-weather]]

## Archivist Review

Reviewed the paper examining scoring rules in probabilistic weather forecasting and approved the explicit open question regarding localization and scale awareness in weather models, while rejecting local scoring rule concepts as application-specific.

### Approved Open Questions
- Scaling and Localization in ML Weather Forecasting: Understanding the interplay between scale awareness, localization, architecture, and resolution is critical for scaling data-driven weather forecasting systems to higher grid resolutions without degrading spatial coherence or physical realism.

### Rejected Candidates
- [concept] Graph Energy Score Training (`graph-energy-score-training`) - not_reusable: This is a specific scoring rule application rather than a broadly reusable architectural or algorithmic concept.

## Links

- [Abstract](https://arxiv.org/abs/2607.19161)
- [PDF](https://arxiv.org/pdf/2607.19161)

