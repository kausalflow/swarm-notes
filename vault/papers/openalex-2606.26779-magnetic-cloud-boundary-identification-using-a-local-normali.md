---
# CSL-compatible fields
title: "Magnetic Cloud Boundary Identification Using a Local-Normalized Magnetic Field Parameter"
author:
  - literal: "Z Zhangqin Huang"
  - literal: "Zhenjun Zhou"
  - literal: "Wei Su"
  - literal: "Y. Ye"
  - literal: "Yuming Wang"
issued:
  date-parts:
    - [2026, 6, 25]
url: "https://arxiv.org/abs/2606.26779"

# Custom fields
paper_id: "2606.26779"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  - "local-normalized-magnetic-field-parameter-lnm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-28T08:16:59Z"
created_at: "2026-06-28T08:16:59Z"
---

# Magnetic Cloud Boundary Identification Using a Local-Normalized Magnetic Field Parameter

**Authors**: Z Zhangqin Huang, Zhenjun Zhou, Wei Su, Y. Ye, Yuming Wang
**Date**: 2026-06-25
**Paper ID**: [openalex:2606.26779](https://arxiv.org/abs/2606.26779)

## Summary

This paper introduces the Local-Normalized Magnetic field parameter (LNM), a metric defined as the log-ratio of total magnetic field strength to its 5-minute running median, designed to standardize the identification of magnetic cloud (MC) boundaries. By quantifying deviations from local magnetic background, the LNM reveals sharp contrasts between the structured environment within MCs and the turbulent ambient solar wind. The authors demonstrate the utility of this approach using a semi-automated identification method and validate the physical significance of the identified boundaries through power spectral density and slab fraction analysis on 76 MC events.

## Key Contributions

- Proposes the LNM parameter to provide a quantitative, reproducible criterion for identifying magnetic cloud (MC) boundaries.
- Develops a semi-automated MC boundary identification method utilizing LNM and Time Series Scalogram visualization.
- Demonstrates that LNM successfully captures the transition from coherent MC structures to variable ambient solar wind across 76 analyzed events.
- Provides physical evidence of MC boundary validity through spectral index and slab fraction analysis, confirming suppressed small-scale variability inside MCs.

## Open Questions & Future Work

- [[physical-mechanisms-mc-turbulence-suppression]]
- [[mc-boundary-identification-interacting-cme]]

## Key Concepts

- [[local-normalized-magnetic-field-parameter-lnm]]: A time-series parameter that quantifies short-timescale magnetic field variability relative to a local median to distinguish coherent magnetic structures.

## Archivist Review

I approved the Local-Normalized Magnetic Field Parameter (LNM) as a reusable diagnostic tool for time-series boundary detection. I also approved two research questions focused on the physics of solar wind turbulence and the practical challenge of identifying boundaries in complex, interacting coronal mass ejections. All other candidates were rejected as either too specialized or lacking sufficient standalone utility.

### Approved Concepts
- Local-Normalized Magnetic Field Parameter (LNM): Provides a quantitative, reproducible metric to identify magnetic cloud boundaries by isolating field strength variability from local background.

### Approved Open Questions
- Physical Basis for MC Turbulence Suppression: Understanding these physical mechanisms is essential for confirming the validity of magnetic cloud identification methods and for developing a more comprehensive theoretical framework for solar wind-ICME interactions.
- Boundary Identification in Interacting ICMEs: Most geoeffective events involve complex ICME interactions; therefore, developing tools that accurately identify boundaries in these environments is critical for space weather forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2606.26779)
- [PDF](https://arxiv.org/pdf/2606.26779)

