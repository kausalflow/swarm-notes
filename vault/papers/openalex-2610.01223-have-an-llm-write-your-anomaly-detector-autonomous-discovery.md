---
# CSL-compatible fields
title: "Have an LLM Write Your Anomaly Detector: Autonomous Discovery of Compact, Interpretable Detectors for Time Series"
author:
  - literal: "David Berghaus"
issued:
  date-parts:
    - [2026, 10, 1]
url: "https://arxiv.org/abs/2610.01223"

# Custom fields
paper_id: "2610.01223"
paper_source: "openalex"
domain: "time-series"
tags:
  - "llm"
  - "anomaly-detection"
  - "time-series"
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
processed_at: "2026-10-04T10:48:58Z"
created_at: "2026-10-04T10:48:58Z"
---

# Have an LLM Write Your Anomaly Detector: Autonomous Discovery of Compact, Interpretable Detectors for Time Series

**Authors**: David Berghaus
**Date**: 2026-10-01
**Paper ID**: [openalex:2610.01223](https://arxiv.org/abs/2610.01223)

## Summary

This paper introduces an autonomous research loop where a large language model iteratively writes and edits short NumPy programs to discover compact, interpretable time-series anomaly detectors. Operating under a leakage-free objective without neural network training or GPUs, the approach discovers univariate and multivariate detectors based on local spectral features and covariance-aware distance. Evaluated on the TSB-AD benchmark, these discovered detectors outperform strong classical, deep, and foundation-model baselines like Time-RCD while offering high computational efficiency and full transparency.

## Key Contributions

- Proposes an autonomous research loop where an LLM repeatedly edits a short NumPy program under a leakage-free objective to discover compact, interpretable time-series anomaly detectors
- Discovers univariate and multivariate detectors using local spectral features and covariance-aware distance against the training-region distribution
- Achieves state-of-the-art performance on the TSB-AD benchmark, outperforming classical, deep, and foundation-model baselines including Time-RCD without training any neural network or using a GPU

## Archivist Review

Applied strict selectivity: no concepts or open questions met the high bar for permanent standalone vault entries, as the methodology of LLM program search is general but the specific anomaly detection details are local to this paper.

### Rejected Candidates
- [open_question] Synthetic Generator Generalization Limits (`synthetic-generator-generalization-limits`) - paper_local: paper_local

## Links

- [Abstract](https://arxiv.org/abs/2610.01223)
- [PDF](https://arxiv.org/pdf/2610.01223)

