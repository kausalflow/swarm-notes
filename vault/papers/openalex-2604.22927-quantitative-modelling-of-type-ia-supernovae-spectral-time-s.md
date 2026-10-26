---
# CSL-compatible fields
title: "Quantitative modelling of type Ia supernovae spectral time series II:Exploring the diversity of thermonuclear explosion scenarios"
author:
  - literal: "M. Magee"
issued:
  date-parts:
    - [2026, 10, 24]
url: "https://arxiv.org/abs/2604.22927"

# Custom fields
paper_id: "2604.22927"
paper_source: "openalex"
domain: "biology"
tags:
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
processed_at: "2026-10-26T10:37:19Z"
created_at: "2026-10-26T10:37:19Z"
---

# Quantitative modelling of type Ia supernovae spectral time series II:Exploring the diversity of thermonuclear explosion scenarios

**Authors**: M. Magee
**Date**: 2026-10-24
**Paper ID**: [openalex:2604.22927](https://arxiv.org/abs/2604.22927)

## Summary

This paper presents enhancements to riddler, a machine learning framework for the automated and quantitative fitting of type Ia supernovae (SNe Ia) spectral time series. By combining neural network radiative transfer emulators with nested sampling, riddler models diverse thermonuclear explosion scenarios—such as pure deflagrations, delayed detonations, and violent mergers—enabling systematic physical parameter inference. The approach is validated on synthetic held-out spectra and applied to real observations of SN 2011fe, SN 2005hk, and SN 2018byg, demonstrating its capability to handle complex spectroscopic diversity.

## Key Contributions

- Introduced and expanded the riddler machine learning framework incorporating radiative transfer emulators and nested sampling for automated quantitative fitting of type Ia supernovae spectra.
- Demonstrated accurate recovery of input parameters and explosion scenarios across diverse thermonuclear explosion scenarios including pure deflagrations, delayed detonations, double detonations, gravitationally confined detonations, and violent mergers.
- Fitted observations of three distinct type Ia supernovae sub-classes (SN 2011fe, SN 2005hk, and SN 2018byg) to validate automated scenario identification.

## Limitations

Details several physical limitations and modeling assumptions inherent to emulated radiative transfer fitting that must be considered when scaling to large observational samples.

## Archivist Review

Strict adherence to review guidelines requires rejecting paper-local astrophysical software frameworks and domain-specific supernova physics questions, as they fall outside general machine learning and time-series methodology scope.

### Rejected Candidates
- [concept] riddler (`riddler`) - low_impact: Domain-specific astrophysics software framework for type Ia supernovae rather than a general machine learning or time-series forecasting mechanism.
- [open_question] Multi-dimensional Asymmetries in Supernova Emulators (`multidimensional-asymmetries-radiative-transfer-emulators`) - low_impact: Highly domain-specific astrophysical question regarding supernova ejecta asymmetries rather than a broad machine learning or time-series modeling bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2604.22927)
- [PDF](https://arxiv.org/pdf/2604.22927)

