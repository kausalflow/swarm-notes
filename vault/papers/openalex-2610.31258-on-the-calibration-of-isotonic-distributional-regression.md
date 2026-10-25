---
# CSL-compatible fields
title: "On the Calibration of Isotonic Distributional Regression"
author:
  - literal: "Tobias Biegert"
  - literal: "Johannes Resin"
  - literal: "Alexander Jordan"
  - literal: "Sebastian Lerch"
issued:
  date-parts:
    - [2026, 10, 22]
url: "https://arxiv.org/abs/2610.31258"

# Custom fields
paper_id: "2610.31258"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "calibration"
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
processed_at: "2026-10-25T09:29:59Z"
created_at: "2026-10-25T09:29:59Z"
---

# On the Calibration of Isotonic Distributional Regression

**Authors**: Tobias Biegert, Johannes Resin, Alexander Jordan, Sebastian Lerch
**Date**: 2026-10-22
**Paper ID**: [openalex:2610.31258](https://arxiv.org/abs/2610.31258)

## Summary

Isotonic distributional regression (IDR) is a non-parametric technique for probabilistic forecasting that estimates conditional distributions under order restrictions. This paper documents a previously overlooked out-of-sample artifact in IDR, where probability integral transform (PIT) values appear as rational fractions resembling Thomae's function. The authors demonstrate this spiking behavior empirically using meteorological data and simulations, provide a theoretical explanation linking it to the discrete structure of isotonic fits, and discuss smoothing mitigation strategies.

## Key Contributions

- Documented a peculiar out-of-sample artifact in isotonic distributional regression (IDR) where probability integral transform (PIT) values are rational fractions resembling Thomae's function.
- Demonstrated the out-of-sample spiking phenomenon empirically using meteorological data and a simulation study.
- Provided a theoretical explanation linking the spiking behavior to the discrete structure of isotonic fits and discussed smoothing mitigation approaches.

## Limitations

Future work could focus on comprehensive mitigation strategies and smoothing techniques to eliminate the discrete artifact without sacrificing calibration performance.

## Open Questions & Future Work

- [[smoothing-calibrated-isotonic-distributional-regression]]

## Archivist Review

Approved the open question regarding smoothing strategies for isotonic distributional regression to mitigate PIT spiking artifacts. No standalone concepts were approved as IDR itself is an existing method and the specific spiking artifact is an analytical observation rather than a standalone generalizable ML method.

### Approved Open Questions
- Calibrated Smoothing for Isotonic Distributional Regression: Crucial for deploying non-parametric probabilistic forecasting models reliably across domains like meteorology and energy without suffering from hidden calibration artifacts caused by discreteness.

## Links

- [Abstract](https://arxiv.org/abs/2610.31258)
- [PDF](https://arxiv.org/pdf/2610.31258)

