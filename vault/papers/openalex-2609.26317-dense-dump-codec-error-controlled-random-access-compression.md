---
# CSL-compatible fields
title: "Dense Dump Codec: Error-Controlled, Random-Access Compression of GRMHD Time Series for Slow-Light Radiative Transfer"
author:
  - literal: "Zelin Zhang"
  - literal: "Zhenyu Zhang"
  - literal: "Bin Chen"
issued:
  date-parts:
    - [2026, 9, 22]
url: "https://arxiv.org/abs/2609.26317"

# Custom fields
paper_id: "2609.26317"
paper_source: "openalex"
domain: "astrophysics"
tags:
  - "time-series"
  - "compression"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-25T09:54:31Z"
created_at: "2026-09-25T09:54:31Z"
---

# Dense Dump Codec: Error-Controlled, Random-Access Compression of GRMHD Time Series for Slow-Light Radiative Transfer

**Authors**: Zelin Zhang, Zhenyu Zhang, Bin Chen
**Date**: 2026-09-22
**Paper ID**: [openalex:2609.26317](https://arxiv.org/abs/2609.26317)

## Summary

The paper introduces Dense Dump Codec (DDC), an error-controlled, random-access compression method designed for dense general relativistic magnetohydrodynamics (GRMHD) time series used in slow-light radiative transfer modeling. DDC leverages exact anchor states and compact intermediate representations to achieve high compression ratios (roughly 10x smaller than original dense outputs) while permitting direct access to specific times and variables. By integrating a native DDC reader into polarized radiative transfer calculations, the method significantly reduces Stokes-image errors compared to traditional sparse sampling strategies.

## Key Contributions

- Introduces Dense Dump Codec (DDC), a compression method for dense GRMHD time series that stores exact anchor states and represents intermediate evolution compactly with random access.
- Achieves roughly 10x smaller archives compared to original dense data and ~50% smaller size than standard 0.5M sparse output sequences.
- Integrates a native DDC reader into polarized slow-light radiative transfer, reducing aggregate Stokes-image errors by 54-79% across 86, 230, and 345 GHz compared to 0.5M inputs.

## Archivist Review

The proposed concept (Dense Dump Codec) and open question are highly domain-specific to astrophysics (GRMHD simulations and radiative transfer) and do not fit the general-purpose machine learning, forecasting, or time-series methodology criteria required for permanent inclusion in the knowledge vault.

### Rejected Candidates
- [concept] Dense Dump Codec (`dense-dump-codec`) - not_reusable: Domain-specific simulation compression codec tailored specifically for GRMHD time series and radiative transfer, lacking broader machine learning or time-series forecasting applicability.
- [open_question] Generalization of GRMHD Compression Profiles (`grmhd-compression-profile-generalization`) - low_impact: Extremely specialized to GRMHD astrophysical simulations and radiative transfer workflows rather than general time series analysis or forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2609.26317)
- [PDF](https://arxiv.org/pdf/2609.26317)

