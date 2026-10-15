---
# CSL-compatible fields
title: "Increasing Sensitivity to Trailed Solar System Objects in Archival JWST NIRCam Imaging with Group Differencing"
author:
  - literal: "Anthony Girmenia"
  - literal: "Stanimir Metchev"
issued:
  date-parts:
    - [2026, 10, 13]
url: "https://arxiv.org/abs/2609.27140"

# Custom fields
paper_id: "2609.27140"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "object-detection"
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
processed_at: "2026-10-15T09:30:10Z"
created_at: "2026-10-15T09:30:10Z"
---

# Increasing Sensitivity to Trailed Solar System Objects in Archival JWST NIRCam Imaging with Group Differencing

**Authors**: Anthony Girmenia, Stanimir Metchev
**Date**: 2026-10-13
**Paper ID**: [openalex:2609.27140](https://arxiv.org/abs/2609.27140)

## Summary

The authors propose a group differencing technique for archival JWST NIRCam exposures that transforms cumulative 'up-the-ramp' detector reads into a sequence of group difference images, reducing trail lengths for small solar system bodies and enabling higher-cadence trajectory searches from single exposures. By applying generalized least-squares fitting along predicted trajectories, the method significantly improves signal-to-noise ratio and detection completeness, achieving sensitivity gains between 1.1 and 1.4 magnitudes compared to standard pipeline calibrations.

## Key Contributions

- Demonstrates that transforming JWST NIRCam up-the-ramp groups into group difference images reduces per-image trail length for moving solar system bodies and yields a photometrically calibrated time series from a single exposure.
- Applies a generalized least-squares fit along moving source trajectories to recover source flux at a higher signal-to-noise ratio compared to standard ramp fits.
- Validates the method on 13 archival JWST NIRCam moving objects and injection/recovery simulations, showing sensitivity gains of ~1.1 to 1.4 magnitudes for typical integration lengths (N = 4 or 6).

## Archivist Review

Applied rigorous filtering against general ML and time-series criteria. The proposed concept and open question pertain specifically to astronomical image processing and sensor calibration (JWST NIRCam up-the-ramp reads), which are domain-local rather than reusable forecasting or machine learning methodologies.

### Rejected Candidates
- [open_question] Blind Covariance-Aware Shift-and-Stack (`blind-covariance-aware-shift-and-stack`) - low_impact: The open question is domain-specific to astronomical moving-object detection and falls outside general temporal/forecasting methodology.

## Links

- [Abstract](https://arxiv.org/abs/2609.27140)
- [PDF](https://arxiv.org/pdf/2609.27140)

