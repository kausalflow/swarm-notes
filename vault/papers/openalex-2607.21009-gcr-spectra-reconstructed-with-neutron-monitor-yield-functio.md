---
# CSL-compatible fields
title: "GCR Spectra Reconstructed with Neutron Monitor Yield Function and Artificial Neural Networks: Comparison of Two Methods"
author:
  - literal: "Stepan Siruk"
  - literal: "Vladislav Alekseev"
  - literal: "Victor Kuzminov"
  - literal: "Rustam Yulbarisov"
  - literal: "Andrey Mayorov"
issued:
  date-parts:
    - [2026, 7, 23]
url: "https://arxiv.org/abs/2607.21009"

# Custom fields
paper_id: "2607.21009"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
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
processed_at: "2026-07-26T07:30:27Z"
created_at: "2026-07-26T07:30:27Z"
---

# GCR Spectra Reconstructed with Neutron Monitor Yield Function and Artificial Neural Networks: Comparison of Two Methods

**Authors**: Stepan Siruk, Vladislav Alekseev, Victor Kuzminov, Rustam Yulbarisov, Andrey Mayorov
**Date**: 2026-07-23
**Paper ID**: [openalex:2607.21009](https://arxiv.org/abs/2607.21009)

## Summary

This paper presents a framework for reconstructing time-resolved galactic cosmic-ray (GCR) proton and helium energy spectra from global neutron monitor network data without relying on direct satellite observations. Two distinct methodologies—a calibrated yield function combined with a force-field scheme, and artificial neural networks trained on multi-station count rates and heliophysical indices—are implemented and compared. The artificial neural networks demonstrate superior accuracy with a chi-squared per degree of freedom near unity, effectively reproducing both large solar-cycle modulations and short-term disturbances. Validation against PAMELA and AMS-02 data confirms the robustness of the approach for periods lacking daily spacecraft records.

## Key Contributions

- Developed a reconstruction framework combining global neutron monitor network count rates and heliophysical indices to estimate galactic cosmic-ray (GCR) proton and helium energy spectra.
- Compared a calibrated yield function plus force-field scheme against artificial neural networks for spectral reconstruction across historical periods lacking daily spacecraft data.
- Demonstrated that artificial neural networks achieve superior performance with lower mean absolute percentage error and chi-squared per degree of freedom near unity.
- Validated reconstructed spectral time series against PAMELA (2006-2011) and AMS-02 (2019-2022) observations, confirming robustness.

## Archivist Review

Applied strict vault criteria, rejecting the single domain-specific open question regarding Forbush decreases as paper-local space weather future work. No concepts or datasets met the bar.

### Rejected Candidates
- [open_question] Model Performance During Severe Storms (`storm-fd-model-performance`) - paper_local: Paper-local future work concerning space-weather extreme events (Forbush decreases) without a reusable methodological bottleneck for the general time-series vault.

## Links

- [Abstract](https://arxiv.org/abs/2607.21009)
- [PDF](https://arxiv.org/pdf/2607.21009)

