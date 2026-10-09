---
# CSL-compatible fields
title: "MORA: Modeling Observed Changes for Drift-Robust Time-Series Anomaly Detection"
author:
  - literal: "Xudong Mou"
  - literal: "Tiejun Wang"
  - literal: "Rui Wang"
  - literal: "Hui Wang"
  - literal: "Liu Pin"
  - literal: "Tianyu Wo"
  - literal: "Xudong Liu"
  - literal: "Ryu Yang"
issued:
  date-parts:
    - [2026, 10, 7]
url: "https://arxiv.org/abs/2610.09473"

# Custom fields
paper_id: "2610.09473"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "robustness"
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
processed_at: "2026-10-09T11:34:30Z"
created_at: "2026-10-09T11:34:30Z"
---

# MORA: Modeling Observed Changes for Drift-Robust Time-Series Anomaly Detection

**Authors**: Xudong Mou, Tiejun Wang, Rui Wang, Hui Wang, Liu Pin, Tianyu Wo, Xudong Liu, Ryu Yang
**Date**: 2026-10-07
**Paper ID**: [openalex:2610.09473](https://arxiv.org/abs/2610.09473)

## Summary

Time-series anomaly detection in non-stationary environments often struggles to distinguish between distribution drift and true anomalies because both produce similar local deviations. This paper introduces MORA, a drift-robust time-series anomaly detection framework that resolves this ambiguity via temporal change disambiguation using paired short- and long-term views. By evaluating reconstruction gaps between these views through a conservative correction mechanism, MORA reduces false alarms caused by distributional shifts without requiring drift annotations or online adaptation. Experiments on four benchmarks confirm that MORA achieves robust performance under non-stationarity while retaining high sensitivity to genuine anomalies.

## Key Contributions

- Identifies the temporal change disambiguation problem in time-series anomaly detection where distribution drift and true anomalies cause similar local changes.
- Proposes MORA, a drift-robust TSAD framework that reconstructs local targets from paired short- and long-term views to measure contextual support.
- Introduces a data-dependent correction mechanism that conservatively adjusts primary local anomaly scores based on reconstruction gaps without requiring drift annotations or online adaptation.
- Demonstrates strong robustness to non-stationarity and preservation of anomaly sensitivity across four TSAD benchmarks.

## Archivist Review

After reviewing the submission against vault standards, the proposed open question was rejected due to its incremental and paper-specific nature, while no concepts or datasets were submitted or warranted inclusion. Strict selectivity was maintained.

### Rejected Candidates
- [open_question] Adaptive Context Selection and Routing (`adaptive-context-selection-tsad`) - low_impact: The open question focuses on incremental extensions and routing improvements rather than addressing a fundamental theoretical bottleneck or distinct open problem.

## Links

- [Abstract](https://arxiv.org/abs/2610.09473)
- [PDF](https://arxiv.org/pdf/2610.09473)

