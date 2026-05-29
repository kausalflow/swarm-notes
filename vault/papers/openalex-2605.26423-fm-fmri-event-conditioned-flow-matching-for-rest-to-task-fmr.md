---
# CSL-compatible fields
title: "FM-fMRI: Event Conditioned Flow Matching for Rest-to-Task fMRI Time-Series Synthesis"
author:
  - literal: "Peiyu Duan"
  - literal: "Jiyao Wang"
  - literal: "Nicha C. Dvornek"
  - literal: "Junlin Yang"
  - literal: "Ziqi Gao"
  - literal: "Lawrence H. Staib"
  - literal: "James S. Duncan"
issued:
  date-parts:
    - [2026, 5, 26]
url: "https://arxiv.org/abs/2605.26423"

# Custom fields
paper_id: "2605.26423"
paper_source: "openalex"
domain: "biology"
tags:
  - "multimodal"
  - "time-series"
  - "diffusion-model"
  - "gan"
  - "vae"
  - "dataset"
architectures:
  []
datasets:
  - "human-connectome-project"
concept_slugs:
  - "event-conditioned-flow-matching"
dataset_slugs:
  - "human-connectome-project"
skill: "TimeSeriesSkill"
processed_at: "2026-05-29T08:37:54Z"
created_at: "2026-05-29T08:37:54Z"
---

# FM-fMRI: Event Conditioned Flow Matching for Rest-to-Task fMRI Time-Series Synthesis

**Authors**: Peiyu Duan, Jiyao Wang, Nicha C. Dvornek, Junlin Yang, Ziqi Gao, Lawrence H. Staib, James S. Duncan
**Date**: 2026-05-26
**Paper ID**: [openalex:2605.26423](https://arxiv.org/abs/2605.26423)

## Summary

FM-fMRI is a generative framework that synthesizes task-based fMRI ROI time series from widely available resting-state fMRI using event-conditioned flow matching. By learning a continuous-time conditional vector field, the model enables efficient ODE-based sampling while handling complex, heterogeneous task event schedules. Experimental results on the Human Connectome Project and BioPoint cohorts demonstrate that FM-fMRI provides stronger spectral and connectivity fidelity than traditional generative baselines, effectively augmenting clinical datasets for improved downstream diagnostic classification.

## Key Contributions

- Introduced FM-fMRI, an event-conditioned flow matching model for synthesizing task-evoked fMRI signals from resting-state fMRI.
- Enabled fast ODE-based sampling for signal synthesis with flexible conditioning on diverse task event schedules.
- Demonstrated superior performance over diffusion models, GANs, and VAEs in spectral, connectome, and distributional benchmarks across HCP and BioPoint datasets.
- Validated the clinical utility of synthesized data by improving downstream autism classification in limited-data scenarios.

## Open Questions & Future Work

- [[robust-fmri-conditioning-strategies]]

## Key Concepts

- [[event-conditioned-flow-matching]]: A continuous-time generative model that synthesizes task-specific fMRI signals from resting-state data by conditioning on task event schedules through learned vector fields.

## Archivist Review

I approved the Event Conditioned Flow Matching concept as it represents a novel application of generative flow-matching techniques to neuroscience. I also approved a refined open question regarding fMRI conditioning robustness. The Human Connectome Project dataset was approved as a standard benchmark in this domain, while other candidates were rejected for being overly specific or lacking sufficient novelty for a standalone note.

### Approved Concepts
- Event Conditioned Flow Matching: The core methodological contribution is the adaptation of flow matching for task-evoked fMRI synthesis by conditioning on heterogeneous event schedules.

### Approved Open Questions
- Robust fMRI Conditioning Strategies: Effective conditioning is the primary bottleneck for scaling fMRI synthesis across clinical and cognitive experiments with varying temporal event structures.

### Rejected Candidates
- [open_question] Advanced fMRI Conditioning Strategies (`advanced-conditioning-robustness-fMRI`) - duplicate_existing: The candidate was rewritten to be more concise and aligned with naming conventions, effectively replacing the original submission.

## Datasets

- [[human-connectome-project]]

## Links

- [Abstract](https://arxiv.org/abs/2605.26423)
- [PDF](https://arxiv.org/pdf/2605.26423)

