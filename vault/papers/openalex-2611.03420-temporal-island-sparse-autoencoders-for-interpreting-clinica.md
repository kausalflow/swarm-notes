---
# CSL-compatible fields
title: "Temporal Island Sparse Autoencoders for Interpreting Clinical Time-Series Models"
author:
  - literal: "Muhan Yeo"
  - literal: "Bong Gyun Kang"
  - literal: "HyunGi Kim"
  - literal: "Sungroh Yoon"
issued:
  date-parts:
    - [2026, 11, 2]
url: "https://arxiv.org/abs/2611.03420"

# Custom fields
paper_id: "2611.03420"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "interpretability"
  - "explainability"
  - "sparse-autoencoders"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "temporal-island-sparse-autoencoders"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-05T12:51:49Z"
created_at: "2026-11-05T12:51:49Z"
---

# Temporal Island Sparse Autoencoders for Interpreting Clinical Time-Series Models

**Authors**: Muhan Yeo, Bong Gyun Kang, HyunGi Kim, Sungroh Yoon
**Date**: 2026-11-02
**Paper ID**: [openalex:2611.03420](https://arxiv.org/abs/2611.03420)

## Summary

The paper introduces Temporal Island Sparse Autoencoders (TI-SAE), a post-hoc interpretation framework for clinical time-series models that learns a patient-shared clinical concept dictionary from frozen model representations. TI-SAE models concepts using temporal Gaussian islands and sparse variable-composition vectors, combined with a decoupled selector for patient-specific attribution. Evaluated on MIMIC-III and MIMIC-IV across multiple backbones, TI-SAE generates coherent clinical concepts with strong faithfulness.

## Key Contributions

- Introduces Temporal Island Sparse Autoencoders (TI-SAE) to extract backbone-specific, patient-shared clinical concept dictionaries from frozen time-series predictive models.
- Defines dictionary latents using temporal Gaussian islands and sparse variable-composition vectors to capture temporal activation and cross-variable structure.
- Employs a decoupled selector to identify dictionary entries driving individual patient predictions, separating representation learning from attribution.
- Evaluates TI-SAE across five backbone architectures and six tasks on MIMIC-III and MIMIC-IV, demonstrating strong performance on faithfulness benchmarks.

## Open Questions & Future Work

- [[cross-institutional-generalization-ti-sae]]

## Key Concepts

- [[temporal-island-sparse-autoencoders]]: A sparse autoencoder variant that extracts temporally coherent, cross-variable concept dictionaries from frozen time-series representations.

## Archivist Review

Approved the novel Temporal Island Sparse Autoencoders (TI-SAE) concept and its cross-institutional generalization open question, while rejecting routine MIMIC dataset entries per the scarcity and novelty guidelines.

### Approved Concepts
- Temporal Island Sparse Autoencoders: Introduces a novel sparse autoencoder framework defining concept dictionaries via temporal Gaussian islands and sparse variable-composition vectors.

### Approved Open Questions
- Cross-Institutional Generalization of TI-SAE: Crucial for understanding whether learned clinical concept dictionaries and sparse spatiotemporal representations are robust across entirely different hospital environments and data collection practices.

### Rejected Candidates
- [dataset] MIMIC-III and MIMIC-IV (`mimic-iii-iv`) - not_novel: Routine medical benchmark datasets that are already widely known and not novel to this paper.

## Links

- [Abstract](https://arxiv.org/abs/2611.03420)
- [PDF](https://arxiv.org/pdf/2611.03420)

