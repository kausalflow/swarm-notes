---
# CSL-compatible fields
title: "Differentiable latent structure discovery for interpretable forecasting in clinical time series"
author:
  - literal: "Ivan Lerner"
  - literal: "Jean Feydy"
  - literal: "Alexandre Kalimouttou"
  - literal: "Anita Burgun"
  - literal: "Francis Bach"
issued:
  date-parts:
    - [2026, 4, 30]
url: "https://arxiv.org/abs/2604.27967"

# Custom fields
paper_id: "2604.27967"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "interpretability"
  - "forecasting"
architectures:
  []
datasets:
  - "mimic-iv"
concept_slugs:
  - "structgp"
  - "latent-pathway-model"
dataset_slugs:
  - "mimic-iv"
skill: "TimeSeriesSkill"
processed_at: "2026-05-03T07:13:52Z"
created_at: "2026-05-03T07:13:52Z"
---

# Differentiable latent structure discovery for interpretable forecasting in clinical time series

**Authors**: Ivan Lerner, Jean Feydy, Alexandre Kalimouttou, Anita Burgun, Francis Bach
**Date**: 2026-04-30
**Paper ID**: [openalex:2604.27967](https://arxiv.org/abs/2604.27967)

## Summary

StructGP is a continuous-time multi-task Gaussian process designed to address the challenges of irregularly sampled clinical EHR data by learning sparse directed acyclic graphs (DAGs) of variable dependencies. By augmenting this with LP-StructGP, the framework incorporates latent pathways that use subject-specific coupling filters to identify common progression patterns across patient populations. The models maintain principled uncertainty estimates while achieving state-of-the-art forecasting accuracy and interpretability in both simulated and real-world clinical datasets.

## Key Contributions

- Introduces StructGP, a continuous-time Gaussian process framework that enforces sparsity and acyclicity constraints for interpretable DAG structure learning in clinical time series.
- Proposes LP-StructGP to capture cross-patient progression patterns using subject-specific coupling filters and latent shared trajectories.
- Demonstrates significant performance gains in short-horizon clinical forecasting (e.g., MIMIC-IV septic shock) and maintains superior uncertainty calibration compared to unstructured baselines.

## Open Questions & Future Work

- [[non-gaussian-likelihood-clinical-time-series]]
- [[scalability-of-latent-structure-models]]

## Key Concepts

- [[structgp]]: A continuous-time multi-task Gaussian process framework that uses differentiable structure learning to recover sparse, directed acyclic graphs of variable dependencies.
- [[latent-pathway-model]]: A mechanism for modeling shared cross-patient progression patterns through subject-specific coupling filters and temporally shifted latent trajectories.

## Archivist Review

The paper introduces a significant framework (StructGP) for interpretable structural forecasting. I have approved StructGP and the general concept of latent pathways as they provide reusable mechanisms for clinical and multivariate time series. Datasets were filtered to retain only MIMIC-IV as the primary evaluation standard. Open questions were refined to highlight the substantial technical bottlenecks in likelihood flexibility and scalability.

### Approved Concepts
- StructGP: Represents a novel integration of continuous-time Gaussian processes with differentiable DAG structure learning, providing both uncertainty quantification and interpretability for multivariate time series.
- Latent Pathways Model: Introduces a mechanism for cross-patient trajectory modeling via learnable, temporally shifted pathways, addressing the limitation of individual patient models.

### Approved Open Questions
- Non-Gaussian clinical likelihoods: Most real-world clinical variables (e.g., categorical medications, mortality events) violate Gaussian assumptions, making this a critical extension for model utility.
- Scalability of latent structures: Scalability remains a primary bottleneck for deploying high-fidelity structure-learning models on large-scale EHR datasets with high-dimensional feature spaces.

### Rejected Candidates
- [concept] LP-StructGP (`lp-structgp`) - subcomponent_of_broader_mechanism: Replaced by the more descriptive and reusable 'Latent Pathway Model' which captures the mechanism itself.

## Datasets

- [[mimic-iv]]

## Links

- [Abstract](https://arxiv.org/abs/2604.27967)
- [PDF](https://arxiv.org/pdf/2604.27967)

