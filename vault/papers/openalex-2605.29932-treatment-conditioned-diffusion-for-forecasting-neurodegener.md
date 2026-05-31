---
# CSL-compatible fields
title: "Treatment-Conditioned Diffusion for Forecasting Neurodegenerative Disease Progression"
author:
  - literal: "Danylo Boiko"
  - literal: "Viktoriia Mishkurova"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.29932"

# Custom fields
paper_id: "2605.29932"
paper_source: "openalex"
domain: "medicine"
tags:
  - "diffusion-model"
  - "transformer"
  - "multimodal"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "treatment-conditioned-diffusion"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:09:40Z"
created_at: "2026-05-31T08:09:40Z"
---

# Treatment-Conditioned Diffusion for Forecasting Neurodegenerative Disease Progression

**Authors**: Danylo Boiko, Viktoriia Mishkurova
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.29932](https://arxiv.org/abs/2605.29932)

## Summary

This paper presents a treatment-conditioned diffusion framework designed to forecast the progression of neurodegenerative diseases using high-fidelity longitudinal neuroimaging. By conditioning the generative process on screening DaTscan images and pharmacological interventions (levodopa equivalent daily dose), the model effectively simulates future brain states while preserving critical anatomical details. The approach integrates a Transformer-based encoder to capture complex pharmacological dynamics and uses a region-of-interest masking strategy to enhance clinical fidelity, outperforming traditional generative baselines in both error metrics and image structural similarity.

## Key Contributions

- Introduced a treatment-conditioned diffusion framework that incorporates screening DaTscan images and levodopa dosages to forecast neurodegenerative progression.
- Proposed a Transformer-based encoder for capturing non-linear pharmacological dynamics alongside a multi-weight region-of-interest mask to preserve anatomical sharpness.
- Achieved 14.0% lower MSE, 7.2% lower MAE, and 4.9% higher SSIM compared to baseline generative approaches on neuroimaging progression tasks.

## Open Questions & Future Work

- [[integrating-latent-biological-factors-forecasting]]

## Key Concepts

- [[treatment-conditioned-diffusion]]: A diffusion-based generative model that predicts future states by conditioning on baseline imagery and longitudinal intervention covariates.

## Archivist Review

I approved the overarching treatment-conditioned diffusion framework as a reusable approach for clinical time-series generation, along with an open question addressing the limitations of relying on macroscopic proxies in pharmacological forecasting. The ROI mask subcomponent was rejected as it represents an implementation-level optimization rather than a standalone methodology.

### Approved Concepts
- Treatment-Conditioned Diffusion: This framework allows for personalized forecasting of neurodegenerative progression by explicitly incorporating pharmacological interventions into the diffusion generation process.

### Approved Open Questions
- Integrating Latent Biological Factors: Current models rely on aggregated clinical metrics (like LEDD) which are insufficient for personalized forecasting; bridging this gap is essential for clinical applicability and addressing inter-patient heterogeneity.

### Rejected Candidates
- [concept] Multi-weight region-of-interest mask (`multi-weight-region-of-interest-mask`) - subcomponent_of_broader_mechanism: This is a model-specific implementation detail for training stability rather than a reusable architecture or mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2605.29932)
- [PDF](https://arxiv.org/pdf/2605.29932)

