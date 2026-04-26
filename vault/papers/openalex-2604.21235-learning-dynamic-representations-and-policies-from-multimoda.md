---
# CSL-compatible fields
title: "Learning Dynamic Representations and Policies from Multimodal Clinical Time-Series with Informative Missingness"
author:
  - literal: "Zihan Liang"
  - literal: "Ziwen Pan"
  - literal: "Ruoxuan Xiong"
issued:
  date-parts:
    - [2026, 4, 23]
url: "https://arxiv.org/abs/2604.21235"

# Custom fields
paper_id: "2604.21235"
paper_source: "openalex"
domain: "medicine"
tags:
  - "multimodal"
  - "time-series"
  - "representation-learning"
  - "bayesian-filtering"
  - "reinforcement-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "informative-missingness-in-clinical-time-series"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-26T06:54:22Z"
created_at: "2026-04-26T06:54:22Z"
---

# Learning Dynamic Representations and Policies from Multimodal Clinical Time-Series with Informative Missingness

**Authors**: Zihan Liang, Ziwen Pan, Ruoxuan Xiong
**Date**: 2026-04-23
**Paper ID**: [openalex:2604.21235](https://arxiv.org/abs/2604.21235)

## Summary

This paper introduces a representation learning framework designed for multimodal clinical time-series, which often suffer from irregular, sparse, and informative missingness. The authors propose a system comprising a multimodal encoder and a Bayesian filtering module to jointly process clinical measurements and textual notes while conditioning on the recording process itself. This approach enables more accurate latent state estimation, leading to improved offline treatment policy optimization and patient outcome prediction in ICU environments. Experimental results across major clinical datasets confirm that explicitly modeling the informative nature of missing data significantly enhances performance in both predictive and policy-oriented tasks.

## Key Contributions

- Introduced a multimodal patient representation framework that integrates structured and unstructured clinical records while explicitly modeling the underlying observation process.
- Developed a Bayesian filtering module to dynamically update patient latent states based on asynchronously observed multimodal clinical signals.
- Achieved superior performance in offline reinforcement learning (FQE: 0.679 vs 0.528) and mortality prediction (AUROC: 0.886) on ICU sepsis cohorts using MIMIC-III.

## Open Questions & Future Work

- [[multimodal-informative-missingness-learning]]

## Key Concepts

- [[informative-missingness-in-clinical-time-series]]: A modeling paradigm where the pattern and timing of data collection in clinical time-series are treated as informative features rather than mere noise or nuisance variables.

## Archivist Review

I approved the concept of 'Informative Missingness' as it provides a clear, reusable framing for clinical time-series research that treats observation patterns as data. The open question was approved to highlight the persistent challenge of integrating asynchronous multimodal data while avoiding negative transfer in multi-task learning. MIMIC and eICU were rejected as they are routine, well-known datasets already heavily represented in the field.

### Approved Concepts
- Informative Missingness in Clinical Time-Series: The paper explicitly formalizes the 'informative missingness' of clinical observations—where the timing and presence of records depend on the patient's latent state—as a source of predictive signal.

### Approved Open Questions
- Learning from Informative Missingness: This is crucial for developing reliable, data-efficient, and generalizable AI-driven decision support systems in clinical settings, where data quality and completeness are significant bottlenecks.

### Rejected Candidates
- [concept] Multimodal Patient Representation Framework (`multimodal-patient-representation-framework`) - paper_local: This is a descriptive summary of the specific model architecture rather than a foundational or widely reusable conceptual advancement.
- [concept] Bayesian Filtering for Multimodal Signals (`bayesian-filtering-for-multimodal-signals`) - subcomponent_of_broader_mechanism: This is a standard methodological choice in the domain; the specific implementation here is a subcomponent of the broader proposed framework.

## Links

- [Abstract](https://arxiv.org/abs/2604.21235)
- [PDF](https://arxiv.org/pdf/2604.21235)

