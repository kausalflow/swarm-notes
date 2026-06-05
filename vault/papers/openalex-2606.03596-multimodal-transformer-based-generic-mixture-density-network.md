---
# CSL-compatible fields
title: "Multimodal Transformer Based Generic Mixture Density Network for Scattering Timescale Estimation of Fast Radio Bursts"
author:
  - literal: "Bikash Kharel"
  - literal: "Emmanuel Fonseca"
  - literal: "Srinjoy Das"
  - literal: "Mason Ng"
  - literal: "Paul Scholz"
  - literal: "Mawson W. Simmons"
  - literal: "Lordrick Kahinga"
  - literal: "Afrokk Khan"
issued:
  date-parts:
    - [2026, 6, 2]
url: "https://arxiv.org/abs/2606.03596"

# Custom fields
paper_id: "2606.03596"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "transformer"
  - "mixture-density-network"
  - "astrophysics"
architectures:
  - "encoder-decoder"
datasets:
  - "chime-frb"
concept_slugs:
  - "mt-gmdn"
dataset_slugs:
  - "chime-frb"
skill: "TimeSeriesSkill"
processed_at: "2026-06-05T08:39:24Z"
created_at: "2026-06-05T08:39:24Z"
---

# Multimodal Transformer Based Generic Mixture Density Network for Scattering Timescale Estimation of Fast Radio Bursts

**Authors**: Bikash Kharel, Emmanuel Fonseca, Srinjoy Das, Mason Ng, Paul Scholz, Mawson W. Simmons, Lordrick Kahinga, Afrokk Khan
**Date**: 2026-06-02
**Paper ID**: [openalex:2606.03596](https://arxiv.org/abs/2606.03596)

## Summary

The paper introduces the Multimodal Transformer Based Generic Mixture Density Network (MT-GMDN) to address the bottleneck of scattering timescale estimation in fast radio bursts (FRBs). By processing both dynamic spectra and time-series profiles through parallel transformer encoders, the model effectively fuses multimodal information. Its mixture density formulation allows for the estimation of scattering timescales while simultaneously handling zero-inflated populations where scattering is unresolvable. Experimental results on CHIME/FRB data demonstrate high predictive accuracy and the ability to output reliable confidence intervals through heteroskedastic error estimation.

## Key Contributions

- Introduces MT-GMDN, a multimodal transformer architecture that integrates dynamic spectra and time-series profiles to estimate scattering timescales.
- Utilizes a generic mixture-density formulation to model zero-inflated FRB scattering populations, enabling robust parameter estimation for bursts with unresolvable scattering.
- Achieves a 94% R^2 for measurable scattering and 90% recall on the CHIME/FRB test set while providing predictive confidence intervals via heteroskedastic error modeling.

## Key Concepts

- [[mt-gmdn]]: A multimodal transformer-based architecture that utilizes a mixture density network to estimate the distribution of target variables while accounting for zero-inflated populations.

## Archivist Review

I approved the MT-GMDN concept as it introduces a specialized architecture for zero-inflated regression via mixture density networks in a multimodal setting, which is a reusable pattern for scientific parameter estimation. I also approved the CHIME/FRB dataset due to its role as a primary, large-scale source for FRB evaluation. Other proposed components were rejected as they represent subcomponents of the primary framework.

### Approved Concepts
- Multimodal Transformer Based Generic Mixture Density Network (MT-GMDN): This architecture provides a structured way to perform regression with zero-inflated target variables (common in astrophysical signals) by combining multimodal inputs through parallel attention encoders and a probabilistic mixture density head.

### Rejected Candidates
- [concept] Parallel transformer encoders for multimodal FRB fusion (`mt-gmdn-subcomponents`) - subcomponent_of_broader_mechanism: The individual encoding architecture is a standard component of the proposed MT-GMDN framework, which is the primary contribution.

## Datasets

- [[chime-frb]]

## Links

- [Abstract](https://arxiv.org/abs/2606.03596)
- [PDF](https://arxiv.org/pdf/2606.03596)

