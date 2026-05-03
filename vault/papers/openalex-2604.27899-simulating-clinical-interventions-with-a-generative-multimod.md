---
# CSL-compatible fields
title: "Simulating clinical interventions with a generative multimodal model of human physiology"
author:
  - literal: "Guy Lutsker"
  - literal: "Gal Sapir"
  - literal: "Jordi Merino"
  - literal: "Smadar Shilo"
  - literal: "Anastasia Godneva"
  - literal: "Eli Meirom"
  - literal: "Shie Mannor, Hagai Rossman"
  - literal: "Gal Chechik"
  - literal: "Eran Segal"
issued:
  date-parts:
    - [2026, 4, 30]
url: "https://arxiv.org/abs/2604.27899"

# Custom fields
paper_id: "2604.27899"
paper_source: "openalex"
domain: "medicine"
tags:
  - "transformer"
  - "multimodal"
  - "llm"
  - "language-model"
  - "forecasting"
architectures:
  - "decoder-only"
datasets:
  - "human-phenotype-project"
concept_slugs:
  - "healthformer"
dataset_slugs:
  - "human-phenotype-project"
skill: "TimeSeriesSkill"
processed_at: "2026-05-03T07:14:39Z"
created_at: "2026-05-03T07:14:39Z"
---

# Simulating clinical interventions with a generative multimodal model of human physiology

**Authors**: Guy Lutsker, Gal Sapir, Jordi Merino, Smadar Shilo, Anastasia Godneva, Eli Meirom, Shie Mannor, Hagai Rossman, Gal Chechik, Eran Segal
**Date**: 2026-04-30
**Paper ID**: [openalex:2604.27899](https://arxiv.org/abs/2604.27899)

## Summary

HealthFormer is a generative, decoder-only transformer trained on longitudinal data from over 15,000 individuals to model complex physiological trajectories across seven clinical domains. By treating health forecasting as a generative task, the model enables zero-shot prediction of disease and mortality risk, as well as in silico simulation of clinical interventions. It demonstrates superior predictive performance over traditional clinical risk scores and aligns with experimental results across a wide range of clinical trial comparisons. The model serves as a foundational health world model capable of facilitating the development of advanced clinical digital twins.

## Key Contributions

- Introduces HealthFormer, a generative, decoder-only transformer that models complex human physiological trajectories across 667 diverse health measurements.
- Demonstrates robust zero-shot transfer performance on four independent cohorts for 27 of 30 incident-disease and mortality endpoints, outperforming standard clinical risk scores.
- Validates in silico intervention simulation capabilities, successfully predicting individual biomarker changes in nutrition trials and aligning with observed effect directions in 41 clinical trials.

## Open Questions & Future Work

- [[fidelity-of-in-silico-intervention-simulation]]

## Key Concepts

- [[healthformer]]: A generative, decoder-only transformer trained on longitudinal clinical data to simulate physiological trajectories and evaluate health interventions in silico.

## Archivist Review

I have approved HealthFormer as a foundational model for clinical digital twins, the Human Phenotype Project as a representative dataset for multi-domain physiological modeling, and a new open question regarding the fidelity of in silico intervention simulation. I rejected generic ML terminology and routine benchmark descriptions to keep the vault focused on high-impact methodologies.

### Approved Concepts
- HealthFormer: It represents a novel application of generative decoder-only transformers as health world models for multi-domain physiological trajectory modeling and intervention simulation.

### Approved Open Questions
- Clinical intervention simulation fidelity: Validating the causal fidelity and reliability of in silico intervention simulation is critical before such models can be safely integrated into clinical decision-support workflows.

## Datasets

- [[human-phenotype-project]]

## Links

- [Abstract](https://arxiv.org/abs/2604.27899)
- [PDF](https://arxiv.org/pdf/2604.27899)

