---
# CSL-compatible fields
title: "Distillation of Synthetic Data for Time Series Foundation Models"
author:
  - literal: "Niloy Biswas"
  - literal: "Noureddine El Karoui"
issued:
  date-parts:
    - [2026, 9, 9]
url: "https://arxiv.org/abs/2609.09586"

# Custom fields
paper_id: "2609.09586"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "pre-training"
  - "foundation-model"
  - "scaling-law"
architectures:
  []
datasets:
  []
concept_slugs:
  - "synthetic-data-distillation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-12T08:55:32Z"
created_at: "2026-09-12T08:55:32Z"
---

# Distillation of Synthetic Data for Time Series Foundation Models

**Authors**: Niloy Biswas, Noureddine El Karoui
**Date**: 2026-09-09
**Paper ID**: [openalex:2609.09586](https://arxiv.org/abs/2609.09586)

## Summary

The paper introduces synthetic data distillation (SDD), a novel pre-training loss objective for time series foundation models that evaluates outputs against conditional forecast distributions rather than realized future values. By framing SDD as a Rao-Blackwellization of standard training objectives, the authors prove it reduces stochastic gradient covariance while preserving expectations. Empirical evaluations across models ranging from 4M to 2.5B parameters show that SDD accelerates validation loss convergence and reduces required training iterations by 10% to 40% on Gaussian Process data.

## Key Contributions

- Proposes Synthetic Data Distillation (SDD), a training objective for time series foundation models that compares outputs to conditional forecast distributions instead of realized future values.
- Proves that SDD acts as a Rao-Blackwellization of the training objective, reducing stochastic gradient covariance under the Loewner partial ordering without changing gradient expectations.
- Demonstrates faster validation loss convergence across model sizes ranging from 4M to 2.5B parameters, requiring 10% to 40% fewer training iterations on Gaussian Process data.

## Limitations

Evaluated primarily on Gaussian Process data; broader generalizability across diverse real-world synthetic generators remains to be fully explored.

## Open Questions & Future Work

- [[production-scale-mixtures-evaluation]]

## Key Concepts

- [[synthetic-data-distillation]]: A training objective for time series foundation models that compares model outputs to conditional forecast distributions using Rao-Blackwellization to reduce gradient covariance.

## Archivist Review

We approved the central conceptual contribution (synthetic data distillation) and its key future scaling question, as they introduce a rigorous statistical variance-reduction framework for time series foundation model pre-training that is broadly reusable across architectures.

### Approved Concepts
- Synthetic Data Distillation: It introduces a novel Rao-Blackwellization based training objective for time series foundation models that compares outputs to conditional forecast distributions.

### Approved Open Questions
- Production-Scale Data Mixtures Evaluation: Crucial for establishing the practical utility of data distillation techniques in real-world large-scale foundation model pre-training pipelines that blend real and synthetic data.

## Links

- [Abstract](https://arxiv.org/abs/2609.09586)
- [PDF](https://arxiv.org/pdf/2609.09586)

