---
# CSL-compatible fields
title: "A multimodal and temporal foundation model for virtual patient representations at healthcare system scale"
author:
  - literal: "Andrew Zhang"
  - literal: "Tong Ding"
  - literal: "Sophia Wagner"
  - literal: "Caiwei Tian"
  - literal: "Ming Y. Lu"
  - literal: "R. Pettit"
  - literal: "Joshua E. Lewis"
  - literal: "Alexandre Misrahi"
  - literal: "Dandan Mo"
  - literal: "Long P. Le"
  - literal: "Faisal Mahmood"
issued:
  date-parts:
    - [2026, 4, 20]
url: "https://arxiv.org/abs/2604.18570"

# Custom fields
paper_id: "2604.18570"
paper_source: "openalex"
domain: "medicine"
tags:
  - "multimodal"
  - "language-model"
  - "llm"
  - "embedding"
  - "vision-language-model"
  - "semantic-search"
  - "forecasting"
  - "long-context"
architectures:
  []
datasets:
  []
concept_slugs:
  - "virtual-patient-representation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-23T06:57:31Z"
created_at: "2026-04-23T06:57:31Z"
---

# A multimodal and temporal foundation model for virtual patient representations at healthcare system scale

**Authors**: Andrew Zhang, Tong Ding, Sophia Wagner, Caiwei Tian, Ming Y. Lu, R. Pettit, Joshua E. Lewis, Alexandre Misrahi, Dandan Mo, Long P. Le, Faisal Mahmood
**Date**: 2026-04-20
**Paper ID**: [openalex:2604.18570](https://arxiv.org/abs/2604.18570)

## Summary

Apollo is a large-scale multimodal temporal foundation model designed to synthesize longitudinal patient clinical records into unified virtual patient representations. By integrating structured medical events, clinical text, and medical imaging, the model creates a comprehensive computational substrate for clinical reasoning. It demonstrates robust performance across a diverse set of 322 medical prognosis and retrieval tasks, proving its utility for long-term disease forecasting and clinical search at a healthcare system scale.

## Key Contributions

- Introduces Apollo, a multimodal foundation model trained on 25 billion records from 7.2 million patients across 28 medical modalities.
- Establishes a unified representation space for 100,000+ medical events, including images and clinical text, to generate virtual patient embeddings.
- Demonstrates generalized clinical forecasting performance across 322 tasks, including multi-year disease onset prediction, progression, and treatment response.

## Open Questions & Future Work

- [[clinical-foundation-model-generalization-limits]]

## Key Concepts

- [[virtual-patient-representation]]: A unified embedding of a patient's historical and current clinical data (structured, text, and imaging) designed to facilitate multimodal forecasting and semantic retrieval.

## Archivist Review

The review process focused on identifying the abstract, reusable modeling paradigm (virtual patient representation) rather than the specific model name (Apollo). An open question regarding clinical model generalization was approved to address the critical, unresolved bottleneck of institutional bias in healthcare foundation models. Routine metrics and specific model implementations were rejected as per the review guidelines.

### Approved Concepts
- Virtual Patient Representation: Captures the central paradigm of embedding longitudinal, multimodal, and unstructured clinical data into a unified, queryable, and predictive latent space.

### Approved Open Questions
- Clinical Foundation Model Generalization: Generalization is the primary hurdle for the clinical deployment of foundation models; understanding cross-institutional representation drift is critical for 'computable medicine'.

### Rejected Candidates
- [concept] Apollo (Foundation Model) (`apollo-foundation-model`) - paper_local: "Apollo" is a specific model instance rather than a foundational architecture or abstract mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2604.18570)
- [PDF](https://arxiv.org/pdf/2604.18570)

