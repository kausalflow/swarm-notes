---
# CSL-compatible fields
title: "Gaia method paper: an algorithm to detect flare events in Gaia time-series"
author:
  - literal: "E. Distefano"
  - literal: "A. C. Lanzafame"
  - literal: "A. F. Lanza"
  - literal: "S. Messina"
  - literal: "I. Pagano"
  - literal: "M. Audard"
  - literal: "G. Jevardat de Fombelle"
  - literal: "B. Holl"
  - literal: "I. Lecoeur-Taibi"
  - literal: "N. Mowlavi"
  - literal: "K. Nienartowicz"
  - literal: "L. Rimoldini"
  - literal: "D. W. Evans"
  - literal: "M. Riello"
  - literal: "P. García-Lario"
  - literal: "P. Gavra"
  - literal: "L. Eyer"
issued:
  date-parts:
    - [2026, 9, 17]
url: "https://arxiv.org/abs/2609.20417"

# Custom fields
paper_id: "2609.20417"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "dataset"
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
processed_at: "2026-09-19T09:03:32Z"
created_at: "2026-09-19T09:03:32Z"
---

# Gaia method paper: an algorithm to detect flare events in Gaia time-series

**Authors**: E. Distefano, A. C. Lanzafame, A. F. Lanza, S. Messina, I. Pagano, M. Audard, G. Jevardat de Fombelle, B. Holl, I. Lecoeur-Taibi, N. Mowlavi, K. Nienartowicz, L. Rimoldini, D. W. Evans, M. Riello, P. García-Lario, P. Gavra, L. Eyer
**Date**: 2026-09-17
**Paper ID**: [openalex:2609.20417](https://arxiv.org/abs/2609.20417)

## Summary

The paper presents a dedicated flare-detection algorithm designed to identify and characterize stellar flares within sparsely sampled multi-band photometric time-series from the Gaia space mission. By leveraging simultaneous measurements in the G, GBP, and GRP bands alongside consistency checks for brightness increases and blueing, the pipeline successfully detects 3217 flares in the gdr3_rotmod catalogue of magnetically active stars. The methodology enables robust flare identification and property characterization across large all-sky stellar samples, complementing high-cadence missions like Kepler and TESS.

## Key Contributions

- Developed a dedicated flare-detection pipeline exploiting simultaneous multi-band photometry (G, GBP, and GRP) to identify stellar flares in sparsely sampled Gaia time series.
- Identified 3217 flares across 2818 stars from the gdr3_rotmod catalogue of 474026 magnetically active stars.
- Estimated effective temperatures using black-body approximations for 348 flares and isolated 29 hyper-flares predominantly occurring in M dwarfs.

## Limitations

Restricted by the sparse temporal sampling of Gaia photometric time series, necessitating multi-band consistency criteria to filter calibration artefacts.

## Archivist Review

Applied rigorous selection criteria, rejecting domain-specific astrophysical inquiries that do not directly address core machine learning or general time-series methodology bottlenecks. No concepts or datasets met the strict reuse threshold for permanent vault notes.

### Rejected Candidates
- [open_question] Physical Origin of HR Diagram Displacement (`physical-origin-of-hr-diagram-displacement-for-hr-diagram-displacement`) - low_impact: Domain-specific astrophysical question regarding stellar evolution and HR diagram positioning rather than a general time-series methodology or machine learning bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.20417)
- [PDF](https://arxiv.org/pdf/2609.20417)

