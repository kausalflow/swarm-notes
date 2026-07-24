---
# CSL-compatible fields
title: "Calibration of the AdvancedVirgo+ Gravitational Wave Detector and Reconstruction of the Detector Strain h(t) during the Observing Run O4"
author:
  - literal: "Virgo Collaboration"
issued:
  date-parts:
    - [2026, 7, 21]
url: "https://arxiv.org/abs/2607.19273"

# Custom fields
paper_id: "2607.19273"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "robustness"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-24T07:25:29Z"
created_at: "2026-07-24T07:25:29Z"
---

# Calibration of the AdvancedVirgo+ Gravitational Wave Detector and Reconstruction of the Detector Strain h(t) during the Observing Run O4

**Authors**: Virgo Collaboration
**Date**: 2026-07-21
**Paper ID**: [openalex:2607.19273](https://arxiv.org/abs/2607.19273)

## Summary

This paper describes the calibration and strain $h(t)$ reconstruction for the AdvancedVirgo+ gravitational wave detector during the O4 observing run. The authors detail the online processing pipeline, which achieved a latency of roughly 10 seconds with linear noise subtraction, and the offline generation of AnalysisReady strain data. The resulting strain time series achieved amplitude uncertainties around 2-3% and phase uncertainties below 30 mrad in the 10-2000 Hz frequency band, enabling downstream gravitational-wave analyses.

## Key Contributions

- Detailed the calibration and strain h(t) reconstruction procedures for the AdvancedVirgo+ gravitational wave detector during the O4 observing run.
- Achieved online strain h(t) reconstruction with a latency of approximately 10 seconds including linear noise subtraction.
- Produced AnalysisReady strain data with frequency-dependent uncertainties around 2-3% in amplitude and below 30 mrad in phase across the 10-2000 Hz frequency band.

## Limitations

Detector sensitivity was limited around 55 Mpc during the observing run, with elevated uncertainties around specific frequencies (50 Hz and 150 Hz).

## Open Questions & Future Work

- [[unified-detector-calibration-convention]]

## Archivist Review

Applied strict selectivity. No reusable time-series forecasting concepts qualify, and the gravitational-wave calibration convention question is too domain-specific to the LIGO-Virgo-KAGRA detector instrumentation pipeline rather than general time-series methodology.

### Approved Open Questions
- Unified Gravitational-Wave Calibration Convention: Essential for eliminating systematic reporting discrepancies in multi-detector gravitational-wave astronomy and joint parameter estimation pipelines.

### Rejected Candidates
- [open_question] Unified Gravitational-Wave Calibration Convention (`unified-detector-calibration-convention`) - low_impact: The open question is domain-specific to gravitational-wave detector calibration conventions and does not address general time-series forecasting, anomaly detection, or statistical methodology.

## Links

- [Abstract](https://arxiv.org/abs/2607.19273)
- [PDF](https://arxiv.org/pdf/2607.19273)

