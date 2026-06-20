---
# CSL-compatible fields
title: "SMART: A Flexible, Interpretable, and Scalable Spatio-temporal Brain Atlas from High-Resolution Imaging Data"
author:
  - literal: "John Kalkhof"
  - literal: "Boris Gutman"
  - literal: "Emile d’Angremont"
  - literal: "Daniel C. Alexander"
  - literal: "Marco Lorenzi"
issued:
  date-parts:
    - [2026, 6, 17]
url: "https://arxiv.org/abs/2606.18753"

# Custom fields
paper_id: "2606.18753"
paper_source: "openalex"
domain: "medicine"
tags:
  - "multimodal"
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "smart-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-20T08:18:31Z"
created_at: "2026-06-20T08:18:31Z"
---

# SMART: A Flexible, Interpretable, and Scalable Spatio-temporal Brain Atlas from High-Resolution Imaging Data

**Authors**: John Kalkhof, Boris Gutman, Emile d’Angremont, Daniel C. Alexander, Marco Lorenzi
**Date**: 2026-06-17
**Paper ID**: [openalex:2606.18753](https://arxiv.org/abs/2606.18753)

## Summary

The SMART framework offers a scalable and interpretable solution for constructing spatio-temporal brain atlases from longitudinal medical imaging data. It explicitly decouples global disease dynamics, modeled through regional differential equations, from personalized anatomical changes via diffeomorphic displacements. Evaluated across extensive longitudinal MRI cohorts, the method demonstrates superior forecasting accuracy and temporal consistency compared to prevailing generative approaches.

## Key Contributions

- Introduced SMART, an interpretable framework that decouples global regional disease progression dynamics from patient-specific anatomical manifestations.
- Utilizes region-specific differential equations for disease trajectories and multi-scale Neural Cellular Automata for diffeomorphic anatomical personalization.
- Achieves state-of-the-art forecasting accuracy on longitudinal MRI datasets including ADNI, OASIS-3, and AIBL.

## Key Concepts

- [[smart-framework]]: A framework for constructing interpretable spatio-temporal brain atlases by decoupling global disease dynamics from patient-specific anatomical variations.

## Archivist Review

The SMART framework is approved as it introduces a novel, reusable paradigm for spatio-temporal medical image modeling by decoupling disease dynamics from anatomical personalization. Standard medical datasets (ADNI, OASIS, AIBL) were rejected as they are widely used, established cohorts and do not constitute unique, reusable research artifacts in the context of this vault's selective policy.

### Approved Concepts
- SMART Framework: Central framework proposed for spatio-temporal brain atlas construction.

### Rejected Candidates
- [dataset] ADNI (`adni`) - not_novel: Generic medical imaging dataset cohort frequently used in literature.
- [dataset] OASIS-3 (`oasis-3`) - not_novel: Generic medical imaging dataset cohort frequently used in literature.
- [dataset] AIBL (`aibl`) - not_novel: Generic medical imaging dataset cohort frequently used in literature.

## Links

- [Abstract](https://arxiv.org/abs/2606.18753)
- [PDF](https://arxiv.org/pdf/2606.18753)

