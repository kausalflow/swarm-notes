---
# CSL-compatible fields
title: "Season-Aware Hybrid Convolutional-Transformer for Antarctic Sea Ice Concentration Forecasting"
author:
  - literal: "Danyang Li"
  - literal: "John Taylor"
  - literal: "Thang Bui"
  - literal: "Quanling Deng"
issued:
  date-parts:
    - [2026, 8, 31]
url: "https://arxiv.org/abs/2608.30654"

# Custom fields
paper_id: "2608.30654"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "attention-mechanism"
  - "self-attention"
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
processed_at: "2026-09-03T09:17:19Z"
created_at: "2026-09-03T09:17:19Z"
---

# Season-Aware Hybrid Convolutional-Transformer for Antarctic Sea Ice Concentration Forecasting

**Authors**: Danyang Li, John Taylor, Thang Bui, Quanling Deng
**Date**: 2026-08-31
**Paper ID**: [openalex:2608.30654](https://arxiv.org/abs/2608.30654)

## Summary

This paper presents a hybrid Convolutional-Transformer framework for monthly Antarctic sea ice concentration (SIC) forecasting, addressing the challenge of capturing both complex spatial structures and long-range temporal dependencies. The model combines convolutional encoding with factorised self-attention, and further incorporates two seasonal prior mechanisms: month-aware positional encoding and a seasonal temporal bias. Experimental evaluations demonstrate superior performance over conventional convolutional and recurrent baselines across short- and long-horizon prediction metrics.

## Key Contributions

- Proposes a hybrid Convolutional-Transformer forecasting framework for monthly Antarctic sea ice concentration (SIC) forecasting that integrates convolutional spatial encoding with factorised self-attention.
- Introduces two seasonal prior mechanisms—month-aware positional encoding and seasonal temporal bias—to explicitly incorporate calendar-month information and encourage attention to periodically related historical states.
- Demonstrates through experiments and ablation studies that the proposed framework outperforms conventional convolutional and recurrent baselines across classification and regression metrics for both short- and long-horizon predictions.

## Open Questions & Future Work

- [[physics-guided-extensions-for-polar-forecasting]]

## Archivist Review

Approved the open question on physics-guided polar forecasting because it identifies a substantial unresolved methodological bottleneck regarding thermodynamic constraints and physical consistency. Rejected the concept candidates as paper-local architectural mechanisms.

### Approved Open Questions
- Physics-Guided Extensions for Polar Forecasting: Incorporating physical laws into data-driven polar forecasting is critical to prevent unphysical predictions, maintain robustness under climate change extremes, and accurately capture sharp boundary dynamics.

### Rejected Candidates
- [concept] Month-Aware Positional Encoding and Seasonal Temporal Bias (`month-aware-positional-encoding-and-seasonal-temporal-bias`) - subcomponent_of_broader_mechanism: These are paper-local architectural subcomponents rather than reusable core primitives.

## Links

- [Abstract](https://arxiv.org/abs/2608.30654)
- [PDF](https://arxiv.org/pdf/2608.30654)

