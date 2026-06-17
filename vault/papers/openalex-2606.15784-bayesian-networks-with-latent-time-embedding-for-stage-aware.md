---
# CSL-compatible fields
title: "Bayesian Networks with Latent Time Embedding for Stage-Aware Causal Modeling of Alzheimer's Disease Progression"
author:
  - literal: "Nguyen Linh Dan Le"
issued:
  date-parts:
    - [2026, 6, 14]
url: "https://arxiv.org/abs/2606.15784"

# Custom fields
paper_id: "2606.15784"
paper_source: "openalex"
domain: "medicine"
tags:
  - "time-series"
  - "causal-inference"
  - "bayesian-inference"
  - "medical-imaging"
architectures:
  []
datasets:
  - "alzheimers-disease-neuroimaging-initiative"
concept_slugs:
  - "bayesian-networks-with-latent-time-embedding-bn-lte"
dataset_slugs:
  - "alzheimers-disease-neuroimaging-initiative"
skill: "TimeSeriesSkill"
processed_at: "2026-06-17T09:26:53Z"
created_at: "2026-06-17T09:26:53Z"
---

# Bayesian Networks with Latent Time Embedding for Stage-Aware Causal Modeling of Alzheimer's Disease Progression

**Authors**: Nguyen Linh Dan Le
**Date**: 2026-06-14
**Paper ID**: [openalex:2606.15784](https://arxiv.org/abs/2606.15784)

## Summary

BN-LTE is a Bayesian structural framework designed to model Alzheimer's disease progression by incorporating pseudotime estimation and AT(N)-constrained dependencies. Unlike black-box forecasting, the model uses posterior spline-varying structural equations to link initial biomarker profiles to future regional tau-PET changes. Evaluation on the ADNI dataset demonstrates its efficacy in spatial reconstruction and its ability to uncover stage-dependent amyloid sensitivity.

## Key Contributions

- Introduces BN-LTE, a framework that integrates latent pseudotime estimation with AT(N)-biologically constrained structural equations for AD progression.
- Uses posterior spline-varying structural equations to map initial multimodal biomarker measurements to future regional tau-PET change.
- Demonstrates superior spatial reconstruction of tau progression on the ADNI dataset and identifies a mid-pseudotime window of amyloid sensitivity.

## Open Questions & Future Work

- [[scaling-stage-aware-disease-progression-modeling]]

## Key Concepts

- [[bayesian-networks-with-latent-time-embedding-bn-lte]]: A Bayesian structural framework that uses estimated pseudotime and domain-specific structural constraints for stage-aware longitudinal progression modeling.

## Archivist Review

I approved the BN-LTE framework as a novel synthesis of latent pseudotime estimation and biologically-constrained structural modeling in clinical time series. The ADNI dataset was approved using its standard canonical name already present in the vault. The open question was generalized to 'Scaling stage-aware disease progression modeling' to better capture the broader research bottleneck beyond a single disease.

### Approved Concepts
- Bayesian Networks with Latent Time Embedding (BN-LTE): This framework provides a structured alternative to black-box forecasting in clinical applications by integrating pseudotime with biologically-constrained structural equations.

### Approved Open Questions
- Scaling stage-aware disease progression modeling: Improving the generalizability and robustness of stage-aware causal modeling is necessary for practical deployment in clinical diagnostics beyond specific experimental cohorts.

### Rejected Candidates
- [open_question] Scaling stage-aware AD modeling (`scalable-stage-aware-ad-modeling`) - other: Replaced with a more generalized title that better reflects the broader applicability to clinical progression modeling beyond just AD.
- [dataset] ADNI (`adni`) - duplicate_existing: Existing canonical name is 'alzheimers-disease-neuroimaging-initiative'.

## Datasets

- [[alzheimers-disease-neuroimaging-initiative]]

## Links

- [Abstract](https://arxiv.org/abs/2606.15784)
- [PDF](https://arxiv.org/pdf/2606.15784)

