---
# CSL-compatible fields
title: "The Thousand-Pulsar-Array programme on MeerKAT XIX: Single-pulse data analysis, nulling and pulse energy distributions"
author:
  - literal: "MICHAEL J. KEITH"
  - literal: "Patrick Weltevrede"
  - literal: "Lucy Oswald"
  - literal: "A. Karastergiou"
  - literal: "X Song"
  - literal: "Haoyue Wang"
  - literal: "Jui-An Hsu"
  - literal: "Simon Johnston"
  - literal: "Geoff Wright"
  - literal: "Matthew Bailes"
  - literal: "M. Serylak"
issued:
  date-parts:
    - [2026, 6, 9]
url: "https://arxiv.org/abs/2606.10807"

# Custom fields
paper_id: "2606.10807"
paper_source: "openalex"
domain: "speech"
tags:
  - "dataset"
  - "time-series"
architectures:
  []
datasets:
  - "thousand-pulsar-array-tpa-dataset"
concept_slugs:
  []
dataset_slugs:
  - "thousand-pulsar-array-tpa-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-06-12T08:55:05Z"
created_at: "2026-06-12T08:55:05Z"
---

# The Thousand-Pulsar-Array programme on MeerKAT XIX: Single-pulse data analysis, nulling and pulse energy distributions

**Authors**: MICHAEL J. KEITH, Patrick Weltevrede, Lucy Oswald, A. Karastergiou, X Song, Haoyue Wang, Jui-An Hsu, Simon Johnston, Geoff Wright, Matthew Bailes, M. Serylak
**Date**: 2026-06-09
**Paper ID**: [openalex:2606.10807](https://arxiv.org/abs/2606.10807)

## Summary

This paper introduces the Thousand Pulsar Array (TPA) dataset, a comprehensive collection of single-pulse observations for 1192 pulsars captured by the MeerKAT telescope. Alongside the dataset, the authors present the MeerTime Single Pulse pipeline, an automated tool for processing and cleaning radio astronomy time-series signals. Through a Bayesian framework, the study characterises the diversity of pulsar energy distributions and nulling behaviour, revealing significant population-level trends linked to spin period and spin-down luminosity. These findings underscore the limitations of using standard phase-averaged metrics to capture the inherent variability of pulsar emission.

## Key Contributions

- Released the Thousand Pulsar Array (TPA) dataset, containing single-pulse time-series observations for 1192 pulsars from the MeerKAT telescope.
- Introduced the MeerTime Single Pulse software pipeline for automated calibration and RFI excision in pulsar signal data.
- Conducted a large-scale population study identifying that ~50% of pulsars exhibit multi-component intrinsic energy distributions.
- Demonstrated systematic correlations between nulling fraction, spin period, and spin-down luminosity across the pulsar population.

## Open Questions & Future Work

- [[phase-resolved-pulsar-emission-modeling]]

## Archivist Review

The paper provides a significant astronomical dataset but lacks novel machine learning methodology. The TPA dataset is approved as a foundational resource for time-series astronomy, and the open question regarding phase-resolved modeling is approved for its scientific impact in moving beyond aggregate statistics. Other concepts were rejected as domain-specific engineering implementations rather than reusable ML paradigms.

### Approved Open Questions
- Phase-Resolved Pulsar Emission Modeling: Developing a comprehensive understanding of pulsar emission requires bridging the gap between aggregate statistical models and the phase-dependent morphology of individual pulses, which current phase-averaged methods obscure.

### Rejected Candidates
- [concept] MeerTime Single Pulse pipeline (`meertime-single-pulse-pipeline`) - paper_local: This is an application-specific software implementation rather than a general-purpose forecasting or machine learning concept.

## Datasets

- [[thousand-pulsar-array-tpa-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2606.10807)
- [PDF](https://arxiv.org/pdf/2606.10807)

