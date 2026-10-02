---
# CSL-compatible fields
title: "CLOAK: Contrastive Guidance for Latent Diffusion-Based Data Obfuscation"
author:
  - literal: "Xin Yang"
  - literal: "Omid Ardakanian"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2512.12086"

# Custom fields
paper_id: "2512.12086"
paper_source: "openalex"
domain: "time-series"
tags:
  - "diffusion-model"
  - "contrastive-learning"
  - "time-series"
  - "privacy"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "cloak"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-02T10:47:52Z"
created_at: "2026-10-02T10:47:52Z"
---

# CLOAK: Contrastive Guidance for Latent Diffusion-Based Data Obfuscation

**Authors**: Xin Yang, Omid Ardakanian
**Date**: 2026-09-30
**Paper ID**: [openalex:2512.12086](https://arxiv.org/abs/2512.12086)

## Summary

The paper introduces CLOAK, a contrastive guidance framework for latent diffusion-based data obfuscation designed to mitigate attribute inference attacks on sensor and image data. By leveraging contrastive learning to extract disentangled representations, CLOAK guides the latent diffusion process to retain utility while masking private information with minimal user retraining. Extensive evaluations on four public time-series datasets and a facial image dataset show that CLOAK consistently improves both privacy-utility trade-offs and computational efficiency.

## Key Contributions

- Proposes CLOAK, a novel latent diffusion-based framework for time-series and image data obfuscation using contrastive guidance.
- Employs contrastive learning to extract disentangled representations that guide the latent diffusion process to conceal private attributes while preserving utility.
- Demonstrates that CLOAK outperforms state-of-the-art obfuscation techniques, reducing utility loss by up to 7.21% and privacy loss by up to 5.76% across multiple public datasets.

## Open Questions & Future Work

- [[formal-privacy-guarantees-diffusion-obfuscation-bounds]]

## Key Concepts

- [[cloak]]: A latent diffusion-based data obfuscation framework that uses contrastive guidance to balance privacy and utility for time-series and image data.

## Archivist Review

Strictly adhered to vault guidelines by approving only the primary framework concept and one foundational open question regarding formal privacy guarantees. No datasets met the strict threshold for standalone vault inclusion.

### Approved Concepts
- CLOAK: Core method introduced in the paper for contrastive guidance in latent diffusion-based data obfuscation.

### Approved Open Questions
- Formal Privacy Guarantees for Obfuscation: Crucial for moving generative privacy frameworks from heuristic, empirical evaluations toward certifiable and verifiable privacy guarantees.

## Links

- [Abstract](https://arxiv.org/abs/2512.12086)
- [PDF](https://arxiv.org/pdf/2512.12086)

