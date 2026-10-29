---
# CSL-compatible fields
title: "Evaluating Bayesian deep learning for robust biomedical time-series classification under distribution shift: A sleep scoring case study"
author:
  - literal: "Mads Birch Sørensen"
  - literal: "Ulrike Richter"
  - literal: "François Gastambide"
  - literal: "Michael Riis Andersen"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2610.35484"

# Custom fields
paper_id: "2610.35484"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "robustness"
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
processed_at: "2026-10-29T11:10:44Z"
created_at: "2026-10-29T11:10:44Z"
---

# Evaluating Bayesian deep learning for robust biomedical time-series classification under distribution shift: A sleep scoring case study

**Authors**: Mads Birch Sørensen, Ulrike Richter, François Gastambide, Michael Riis Andersen
**Date**: 2026-10-26
**Paper ID**: [openalex:2610.35484](https://arxiv.org/abs/2610.35484)

## Summary

This paper investigates the effectiveness of Bayesian model averaging (BMA) via nine approximate inference methods for improving the robustness and calibration of biomedical time-series classification under various distribution shifts, using rodent sleep scoring as a case study. The results indicate that multi-basin BMA methods consistently outperform single-basin alternatives and standard point estimates on out-of-distribution (OOD) accuracy, calibration, selective prediction, and artifact detection. However, BMA yields only modest gains on in-distribution data and shows little improvement in detecting inter-rater disagreement.

## Key Contributions

- Evaluates Bayesian model averaging (BMA) via nine approximate inference methods under distribution shifts in genotype, laboratory, and species using a rodent sleep scoring case study.
- Demonstrates that multi-basin BMA methods outperform single-basin approaches and point estimates in out-of-distribution (OOD) accuracy and calibration.
- Shows that BMA improves selective prediction as well as OOD and artifact detection, while showing limited impact on inter-rater disagreement detection.

## Archivist Review

The paper presents an empirical evaluation of Bayesian model averaging under various distribution shifts for biomedical time series. Since no novel concepts or unique architectures were introduced, and the open question is standard future-work boilerplate regarding generalizability, no vault items are approved.

### Rejected Candidates
- [open_question] Generalization of Bayesian Deep Learning to Diverse Biomedical Distribution Shifts (`generalization-biomedical-time-series-distribution-shift`) - weak_evidence: Standard future work suggestion calling for evaluation on additional datasets and domains without a specific technical bottleneck or novel mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2610.35484)
- [PDF](https://arxiv.org/pdf/2610.35484)

