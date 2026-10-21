---
# CSL-compatible fields
title: "Integration of a CME Flux Rope Model with Magnetic Field Draping in Heliospheric Simulations"
author:
  - literal: "Ranadeep Sarkar"
  - literal: "Jens Pomoell"
  - literal: "Emilia K. J. Kilpua"
  - literal: "Eleanna Asvestari"
issued:
  date-parts:
    - [2026, 10, 19]
url: "https://arxiv.org/abs/2610.16004"

# Custom fields
paper_id: "2610.16004"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
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
processed_at: "2026-10-21T09:43:49Z"
created_at: "2026-10-21T09:43:49Z"
---

# Integration of a CME Flux Rope Model with Magnetic Field Draping in Heliospheric Simulations

**Authors**: Ranadeep Sarkar, Jens Pomoell, Emilia K. J. Kilpua, Eleanna Asvestari
**Date**: 2026-10-19
**Paper ID**: [openalex:2610.16004](https://arxiv.org/abs/2610.16004)

## Summary

Accurate prediction of interplanetary coronal mass ejection (ICME) magnetic structures is critical for space weather forecasting, yet difficult to achieve with standard global MHD models. This paper presents FROST (Flux Rope embedded in the Solar Magnetic Field), a new model implemented within EUHFORIA that integrates an initially force-free toroidal flux rope with a novel self-consistent magnetic draping embedding technique. Validated on the April 11, 2013 CME event, the model successfully reproduces in situ magnetic field measurements at 1 AU with high correlation coefficients across all vector components.

## Key Contributions

- Introduces the FROST (Flux Rope embedded in the Solar Magnetic Field) model within EUHFORIA for improved ICME magnetic structure prediction.
- Implements a novel embedding technique that self-consistently generates a draping magnetic field around the flux rope, ensuring magnetic field boundary continuity.
- Demonstrates strong agreement with in situ magnetic field measurements at 1 AU for the 2013 April 11 CME event, with component correlation coefficients between 0.64 and 0.95.

## Limitations

Future work will focus on further validating the model across a broader range of ICME events and refining lower-corona advection constraints.

## Archivist Review

The submitted concepts and open questions are highly domain-specific to solar physics and heliospheric MHD simulations (FROST model and CME density assumptions) rather than general machine learning or time-series forecasting methodology. Following the strict vault selection criteria, they have been rejected to maintain a clean, reusable machine learning knowledge base.

### Rejected Candidates
- [concept] Flux Rope embedded in the Solar Magnetic Field (`flux-rope-embedded-in-the-solar-magnetic-field-frost`) - low_impact: FROST is a highly specialized domain-specific physics model (solar physics/heliospheric simulation) rather than a general machine learning or time-series forecasting mechanism.
- [open_question] Uniform density assumption in flux-ropes (`uniform-density-assumption-cme`) - low_impact: This open question is extremely narrow and specific to MHD solar physics simulations rather than general time-series forecasting or machine learning methodologies.

## Links

- [Abstract](https://arxiv.org/abs/2610.16004)
- [PDF](https://arxiv.org/pdf/2610.16004)

