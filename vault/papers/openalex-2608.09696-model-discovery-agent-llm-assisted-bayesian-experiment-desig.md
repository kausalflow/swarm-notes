---
# CSL-compatible fields
title: "Model Discovery Agent: LLM-assisted Bayesian experiment design for data-efficient discovery of mechanistic world models"
author:
  - literal: "Kevin Murphy"
issued:
  date-parts:
    - [2026, 8, 10]
url: "https://arxiv.org/abs/2608.09696"

# Custom fields
paper_id: "2608.09696"
paper_source: "openalex"
domain: "reinforcement-learning"
tags:
  - "llm"
  - "bayesian"
  - "active-learning"
  - "causal-discovery"
  - "simulation-based-inference"
  - "reinforcement-learning"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-13T06:10:28Z"
created_at: "2026-08-13T06:10:28Z"
---

# Model Discovery Agent: LLM-assisted Bayesian experiment design for data-efficient discovery of mechanistic world models

**Authors**: Kevin Murphy
**Date**: 2026-08-10
**Paper ID**: [openalex:2608.09696](https://arxiv.org/abs/2608.09696)

## Summary

The paper presents the Model Discovery Agent (MDA), which integrates large language models as structural proposers with Bayesian machinery including sequential Monte Carlo, simulation-based inference, and value-of-information for data-efficient discovery of mechanistic world models. MDA handles the M-open setting by employing predictive checks to detect hypothesis inadequacy, dynamically expanding the hypothesis space, and using designed interventions to identify parameters. Evaluated on physics, chemistry, and a new electrophysiology benchmark, MDA establishes a new state of the art in data-efficient model learning and interventional forecasting.

## Key Contributions

- Introduced Model Discovery Agent (MDA) combining LLMs as structural proposers with Bayesian machinery (SMC, SBI, VoI) for data-efficient discovery of mechanistic world models.
- Implemented an M-open setting recovery mechanism via predictive checks that trigger hypothesis space expansion and targeted experiment design.
- Demonstrated state-of-the-art data-efficient model learning and interventional forecasting across physics (DPbench), chemistry (CHEMbench), and a new single-neuron electrophysiology benchmark (HHbench).

## Archivist Review

Reviewed the candidate concept (Model Discovery Agent) and determined it represents a paper-local system/framework name rather than a standalone, reusable algorithmic primitive or vault note concept. Applied strict scarcity and novelty filters.

### Rejected Candidates
- [concept] Model Discovery Agent (`model-discovery-agent`) - paper_local: Paper-local agentic framework and terminology rather than a broadly reusable methodological primitive.

## Links

- [Abstract](https://arxiv.org/abs/2608.09696)
- [PDF](https://arxiv.org/pdf/2608.09696)

