---
# CSL-compatible fields
title: "When is a closed-form RGB->S/P ratio adequate? A hyperspectral characterization on natural scenes for mesopic display"
author:
  - literal: "Naoyuki Uchida"
issued:
  date-parts:
    - [2026, 9, 21]
url: "https://arxiv.org/abs/2609.24819"

# Custom fields
paper_id: "2609.24819"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "evaluation"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-24T09:39:53Z"
created_at: "2026-09-24T09:39:53Z"
---

# When is a closed-form RGB->S/P ratio adequate? A hyperspectral characterization on natural scenes for mesopic display

**Authors**: Naoyuki Uchida
**Date**: 2026-09-21
**Paper ID**: [openalex:2609.24819](https://arxiv.org/abs/2609.24819)

## Summary

This paper evaluates whether a low-cost closed-form linear-RGB to scotopic-to-photopic (S/P) luminance ratio estimator—commonly used for mesopic and low-light display transforms—is adequate for natural, broadband display content using hyperspectral imagery. By analyzing daylight radiance time-series and an independent fifty-scene hyperspectral dataset, the author shows that a six-scalar closed form achieves a median error below 0.03, provided the RGB input is chromatically adapted to D65. The results indicate that while closed-form S/P estimation fails on spectrally sparse or narrowband sources, it is highly accurate and robust for spectrally smooth natural scenes.

## Key Contributions

- Demonstrates that a six-scalar closed-form linear-RGB to S/P ratio estimator achieves a median error of ~0.07 on daylight radiance time-series when chromatically adapted to D65, and generalizes to a median error of 0.024 on an independent fifty-scene hyperspectral dataset.
- Identifies that chromatic adaptation to D65 is the critical enabling step for time-invariant accuracy, preventing a color-temperature tilt that otherwise produces ~0.19 median error in un-adapted sRGB.
- Reveals that closed-form three-channel S/P projection accuracy is highly dependent on spectral smoothness, maintaining high fidelity on broadband natural scenes while failing on spectrally sparse or narrowband surfaces (such as floral close-ups).

## Limitations

Does not claim observer-validated appearance fidelity or adequacy on narrowband sources.

## Open Questions & Future Work

- [[observer-validated-appearance-fidelity]]

## Archivist Review

The paper examines a closed-form RGB-to-S/P luminance ratio estimator for mesopic displays using hyperspectral imagery. The proposed open question regarding observer-validated appearance fidelity is domain-specific to display colorimetry and computer vision color science rather than general ML or time-series forecasting methodology, so it is rejected. No concepts or datasets met the strict vault inclusion criteria.

### Approved Open Questions
- Observer-Validated Appearance Fidelity Evaluation: Crucial for confirming whether physical closed-form approximations of S/P translate to actual perceptual accuracy in mesopic image display applications.

### Rejected Candidates
- [open_question] Observer-Validated Appearance Fidelity Evaluation (`observer-validated-appearance-fidelity`) - low_impact: The question asks for psychophysical validation of a specific display transform, which is overly application-specific and lacks generalizability to core ML time-series or forecasting methodology.

## Links

- [Abstract](https://arxiv.org/abs/2609.24819)
- [PDF](https://arxiv.org/pdf/2609.24819)

