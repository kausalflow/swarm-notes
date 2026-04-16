---
# CSL-compatible fields
title: "Statistical Study of Balmer Continuum Enhancement in Solar Flares"
author:
  - literal: "Pranjali Sharma"
  - literal: "Lucia Kleint"
  - literal: "Jonas Zbinden"
issued:
  date-parts:
    - [2026, 4, 13]
url: "https://arxiv.org/abs/2604.11276"

# Custom fields
paper_id: "2604.11276"
paper_source: "openalex"
domain: "physics"
tags:
  - "dataset"
  - "evaluation"
architectures:
  []
datasets:
  - "IRIS"
concept_slugs:
  []
dataset_slugs:
  - "iris"
skill: "TimeSeriesSkill"
processed_at: "2026-04-16T06:29:44Z"
created_at: "2026-04-16T06:29:44Z"
---

# Statistical Study of Balmer Continuum Enhancement in Solar Flares

**Authors**: Pranjali Sharma, Lucia Kleint, Jonas Zbinden
**Date**: 2026-04-13
**Paper ID**: [openalex:2604.11276](https://arxiv.org/abs/2604.11276)

## Summary

This study investigates the near-ultraviolet (NUV) continuum enhancements in solar flares using 234 IRIS observations. The authors introduce a robust dual-pipeline detection approach that filters false positives by verifying temporal and spatial coherence with FUV emissions. Their findings characterize the occurrence of these enhancements at flare ribbon edges and during both the impulsive and decay phases, providing empirical constraints for future flare heating simulations.

## Key Contributions

- Quantified occurrence statistics, spatial distribution, and temporal characteristics of NUV continuum enhancements across 234 solar flares using IRIS observations.
- Developed a dual-pipeline detection framework that leverages spatiotemporal correspondence between NUV and FUV emission to filter false positives in flare time series data.
- Demonstrated that NUV enhancement magnitude correlates with flare class, providing new empirical constraints for chromospheric energy transport and flare simulation models.

## Open Questions & Future Work

- [[nuv-enhancement-ribbon-front-coupling-mechanisms]]
- [[nuv-fuv-continuum-coupling-mechanisms]]

## Archivist Review

I have approved the IRIS dataset as it is a standard, critical observational instrument in solar physics used here as the primary data source. I have also approved the two open questions regarding NUV/FUV coupling and ribbon front physics, as they address significant, unresolved gaps in solar flare modeling that will persist across future studies. I rejected all concept candidates as they were either generic pipeline descriptions or local to the implementation of the study and not broadly reusable across machine learning or physics modeling.

### Approved Open Questions
- NUV Enhancement and Ribbon Coupling: Establishing this spatial relationship would provide a critical observational constraint for validating radiative hydrodynamic flare models.
- NUV and FUV Continuum Coupling: Understanding this shared formation is essential for accurately modeling energy transport in the solar chromosphere.

### Rejected Candidates
- [open_question] NUV Enhancement and Ribbon Fronts (`nuv-enhancement-ribbon-front-coupling`) - duplicate_existing: Renamed for better consistency and clarity.

## Datasets

- [[iris]]

## Links

- [Abstract](https://arxiv.org/abs/2604.11276)
- [PDF](https://arxiv.org/pdf/2604.11276)

