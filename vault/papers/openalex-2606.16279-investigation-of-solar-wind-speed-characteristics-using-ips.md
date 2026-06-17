---
# CSL-compatible fields
title: "Investigation of Solar Wind Speed Characteristics Using IPS Observations and the PFSS+SCS Model"
author:
  - literal: "Kyogo Tokoro"
  - literal: "Munehito Shoda"
  - literal: "Shinsuke Imada"
issued:
  date-parts:
    - [2026, 6, 15]
url: "https://arxiv.org/abs/2606.16279"

# Custom fields
paper_id: "2606.16279"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-17T09:27:39Z"
created_at: "2026-06-17T09:27:39Z"
---

# Investigation of Solar Wind Speed Characteristics Using IPS Observations and the PFSS+SCS Model

**Authors**: Kyogo Tokoro, Munehito Shoda, Shinsuke Imada
**Date**: 2026-06-15
**Paper ID**: [openalex:2606.16279](https://arxiv.org/abs/2606.16279)

## Summary

This paper investigates the relationship between global solar wind speed and coronal magnetic field configurations to improve space-weather forecasting and solar acceleration diagnostics. By combining global IPS wind speed observations with the refined PFSS+SCS model, the authors improve the accuracy of connectivity between solar wind and its coronal origins. The study demonstrates that a specific parameter, f_SS/B_sun, effectively bifurcates solar wind behavior into two groups linked to different underlying acceleration mechanisms, characterized by their proximity to coronal hole boundaries.

## Key Contributions

- Introduces a comprehensive statistical analysis of solar wind speed by integrating Interplanetary Scintillation (IPS) observations with the PFSS+SCS coronal magnetic field model.
- Identifies a parameter, f_SS/B_sun, that successfully bifurcates solar wind speed into two distinct groups exhibiting different correlations, which are better organized by footpoint magnetic field strength and coronal hole boundary distance.
- Provides evidence suggesting that the observed bifurcation in solar wind speed characteristics indicates the presence of fundamentally different acceleration mechanisms in the solar corona.

## Open Questions & Future Work

- [[unifying-solar-wind-acceleration-mechanisms]]

## Archivist Review

The paper provides a domain-specific physical analysis. I rejected the IPS observational data and the PFSS+SCS model as they are specific to solar physics research rather than general ML forecasting mechanisms. I approved the open question regarding the unification of acceleration mechanisms as it represents a fundamental scientific bottleneck in space weather forecasting that aligns with the vault's interest in physical dynamics.

### Approved Open Questions
- Unifying Solar Wind Acceleration Mechanisms: Determining if a single physical framework can unify the observed behavior across different solar magnetic regimes is central to building predictive models for space weather and understanding the fundamental plasma physics of the corona.

### Rejected Candidates
- [concept] PFSS+SCS model (`pfss-scs-model`) - paper_local: The model is a domain-specific physical simulation framework rather than a general-purpose forecasting or ML architecture.
- [dataset] Interplanetary Scintillation (IPS) observations (`ips-observations`) - low_impact: This refers to a broad class of observational data rather than a specific, named, reusable dataset.

## Links

- [Abstract](https://arxiv.org/abs/2606.16279)
- [PDF](https://arxiv.org/pdf/2606.16279)

