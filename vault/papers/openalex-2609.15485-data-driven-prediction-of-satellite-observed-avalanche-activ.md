---
# CSL-compatible fields
title: "Data-driven Prediction of Satellite-observed Avalanche Activity from Snowpack Simulations"
author:
  - literal: "Jakob Grah"
  - literal: "Filippo Maria Bianchi"
  - literal: "Bert Kruyt"
  - literal: "Karsten Müller"
issued:
  date-parts:
    - [2026, 9, 14]
url: "https://arxiv.org/abs/2609.15485"

# Custom fields
paper_id: "2609.15485"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "time-series"
  - "forecasting"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:45:04Z"
created_at: "2026-09-17T09:45:04Z"
---

# Data-driven Prediction of Satellite-observed Avalanche Activity from Snowpack Simulations

**Authors**: Jakob Grah, Filippo Maria Bianchi, Bert Kruyt, Karsten Müller
**Date**: 2026-09-14
**Paper ID**: [openalex:2609.15485](https://arxiv.org/abs/2609.15485)

## Summary

This paper explores whether physical SNOWPACK simulations can predict satellite-observed avalanche activity mapped via Sentinel-1 synthetic aperture radar across Norway and Sweden. The authors propose a transformer model that processes five days of grid-level SNOWPACK outputs to predict the subsequent day's SAR-detected Avalanche Activity Index (SAR-AAI). Evaluated across multiple winters, the model achieves strong regional correlation (r = 0.803) over averaged periods, though cell-scale agreement is weaker and extreme activity is underestimated.

## Key Contributions

- Compiled five winters of Sentinel-1 avalanche detections across Norway and Sweden paired with SNOWPACK simulations driven by numerical weather predictions.
- Proposed a transformer-based framework taking 5 days of SNOWPACK outputs to predict the next day's SAR-detected Avalanche Activity Index (SAR-AAI).
- Achieved a regional mean correlation of r = 0.803 over six-day evaluation periods, demonstrating that regional snowpack simulations capture broad temporal and spatial variations in satellite-observed avalanche activity.

## Limitations

The model produces smoother predictions, underestimates the strongest activity, has weaker cell-scale agreement (r = 0.549), and was evaluated without an untouched test winter, leaving operational forecast skill unestablished.

## Archivist Review

In accordance with the stringent selection criteria and skill context, all candidates were evaluated for general reusability across ML time series and forecasting literature. The open question is specific to avalanche forecasting validation rather than a foundational ML bottleneck, and no concepts met the threshold for permanent archival.

### Rejected Candidates
- [open_question] Operational Forecast Skill and Untouched Winters (`operational-forecast-skill-untouched-winters`) - paper_local: This question is domain-specific to avalanche forecasting and dataset validation rather than a broadly reusable methodological bottleneck in ML time series.

## Links

- [Abstract](https://arxiv.org/abs/2609.15485)
- [PDF](https://arxiv.org/pdf/2609.15485)

