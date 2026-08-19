---
# CSL-compatible fields
title: "A Diffusion-Based Framework for High-Resolution Precipitation Forecasting over CONUS"
author:
  - literal: "Marina Vicens-Miquel"
  - literal: "Amy McGovern"
  - literal: "Aaron J. Hill"
  - literal: "Efi Foufoula‐Georgiou"
  - literal: "Clément Guilloteau"
  - literal: "Samuel S. P. Shen"
issued:
  date-parts:
    - [2026, 8, 17]
url: "https://arxiv.org/abs/2512.09059"

# Custom fields
paper_id: "2512.09059"
paper_source: "openalex"
domain: "time-series"
tags:
  - "diffusion-model"
  - "forecasting"
  - "time-series"
  - "uncertainty-quantification"
  - "autoregressive"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-19T05:19:31Z"
created_at: "2026-08-19T05:19:31Z"
---

# A Diffusion-Based Framework for High-Resolution Precipitation Forecasting over CONUS

**Authors**: Marina Vicens-Miquel, Amy McGovern, Aaron J. Hill, Efi Foufoula‐Georgiou, Clément Guilloteau, Samuel S. P. Shen
**Date**: 2026-08-17
**Paper ID**: [openalex:2512.09059](https://arxiv.org/abs/2512.09059)

## Summary

This paper proposes a diffusion-based deep learning framework for high-resolution precipitation forecasting over CONUS at a 1-km spatial resolution, extending up to 12 hours via autoregressive rollouts. The authors systematically compare three residual prediction strategies utilizing past MRMS observations, HRRR numerical weather predictions, or a hybrid combination of both. Results indicate that the hybrid model performs best at short lead times, whereas the HRRR-corrective model excels at longer lead times, consistently outperforming the HRRR baseline when paired with physically-informed uncertainty quantification.

## Key Contributions

- Introduces a diffusion-based deep learning framework for high-resolution precipitation forecasting over the Continental United States (CONUS) at 1-km spatial resolution.
- Systematically compares three residual prediction strategies: a fully data-driven model using MRMS observations, a corrective model using HRRR numerical weather predictions, and a hybrid model combining both data sources.
- Extends forecasts up to 12 hours using autoregressive rollouts, demonstrating that the hybrid model excels at short lead times while the HRRR-corrective model maintains superior skill at longer lead times.
- Incorporates physically-informed uncertainty quantification tailored to the residual learning setup to assess forecast reliability.

## Archivist Review

Evaluated the paper against our rigorous selectivity standards. The paper applies diffusion models and residual learning to meteorological precipitation forecasting, comparing hybrid vs. corrective strategies. As no novel standalone architectural or conceptual primitives were proposed, and the open question is standard exploratory future work, all candidates were rejected to maintain knowledge vault quality.

### Rejected Candidates
- [open_question] Investigating Residual Biases in AI Weather Correction (`investigating-residual-biases-in-ai-weather-correction`) - weak_evidence: Standard future work exploring error sources in meteorological models without formulating a distinct, reusable theoretical problem.

## Links

- [Abstract](https://arxiv.org/abs/2512.09059)
- [PDF](https://arxiv.org/pdf/2512.09059)

