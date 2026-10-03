---
# CSL-compatible fields
title: "MAGiDiff: Sampling the Photospheric Vector Field from UV/EUV Filtergrams"
author:
  - literal: "Ruoyu Wang"
  - literal: "David F. Fouhey"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2609.40043"

# Custom fields
paper_id: "2609.40043"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "diffusion-model"
  - "multimodal"
  - "generative-adversarial-network"
architectures:
  []
datasets:
  []
concept_slugs:
  - "magidiff"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-03T10:09:19Z"
created_at: "2026-10-03T10:09:19Z"
---

# MAGiDiff: Sampling the Photospheric Vector Field from UV/EUV Filtergrams

**Authors**: Ruoyu Wang, David F. Fouhey
**Date**: 2026-09-30
**Paper ID**: [openalex:2609.40043](https://arxiv.org/abs/2609.40043)

## Summary

The paper introduces MAGiDiff, a denoising diffusion model designed to estimate photospheric vector magnetograms directly from UV/EUV filtergrams (such as those from SDO/AIA) without requiring full polarization measurements. By framing the indirect and ill-posed mapping as a generative task, MAGiDiff successfully reconstructs vector magnetograms mimicking Hinode SOT-SP ground-truth data, generalizes across solar cycles, and adapts to other EUV instruments like STEREO and GOES-R.

## Key Contributions

- Introduces MAGiDiff, a denoising diffusion model to estimate photospheric vector magnetograms from SDO/AIA UV/EUV filtergrams.
- Demonstrates accurate mimicry of Hinode SOT-SP ground-truth vector magnetic fields without direct polarization input.
- Shows generalization across solar cycles and successful fine-tuning to other EUV instruments like STEREO/EUVI and GOES-R/SUVI.

## Limitations

Not a direct substitute for a dedicated spectropolarimetric instrument, but opens new capabilities for solar activity forecasting and modeling.

## Open Questions & Future Work

- [[improving-polarity-disambiguation-in-uv-euv-magnetogram-estimation]]

## Key Concepts

- [[magidiff]]: A denoising diffusion model-based method that estimates photospheric vector magnetograms from UV/EUV filtergrams.

## Archivist Review

Approved the central generative framework MAGiDiff and its corresponding open question regarding polarity disambiguation in cross-modal solar physics mapping. Kept approvals strictly minimal per policy.

### Approved Concepts
- MAGiDiff: Core proposed method for estimating photospheric vector magnetic fields from UV/EUV filtergrams using diffusion models.

### Approved Open Questions
- Improving Polarity Disambiguation in UV/EUV Magnetogram Estimation: Polarity ambiguity is an intrinsic physical challenge when mapping sign-invariant UV/EUV observations to directional magnetic fields; improving models' ability to correctly assign vector orientations is essential for reliable space-weather forecasting and coronal modeling.

## Links

- [Abstract](https://arxiv.org/abs/2609.40043)
- [PDF](https://arxiv.org/pdf/2609.40043)

