---
# CSL-compatible fields
title: "Comparing data assimilation and likelihood-based inference on latent state estimation in agent-based models"
author:
  - literal: "Blas Kolic"
  - literal: "Corrado Monti"
  - literal: "Gianmarco De Francisci Morales"
  - literal: "Marco Pangallo"
issued:
  date-parts:
    - [2026, 5, 19]
url: "https://arxiv.org/abs/2509.17625"

# Custom fields
paper_id: "2509.17625"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "da-vs-lbi-for-abm-latent-estimation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:36:29Z"
created_at: "2026-05-21T08:36:29Z"
---

# Comparing data assimilation and likelihood-based inference on latent state estimation in agent-based models

**Authors**: Blas Kolic, Corrado Monti, Gianmarco De Francisci Morales, Marco Pangallo
**Date**: 2026-05-19
**Paper ID**: [openalex:2509.17625](https://arxiv.org/abs/2509.17625)

## Summary

This paper presents the first systematic comparison between Data Assimilation (DA) and Likelihood-Based Inference (LBI) for estimating latent states in Agent-Based Models (ABMs). While DA offers a model-agnostic approach suitable for aggregate time-series forecasting, LBI provides higher precision for recovering latent agent-level states by explicitly utilizing model likelihoods. The authors evaluate these methods on the Bounded-Confidence Model, providing empirical evidence on when each approach is preferable based on the required level of inference granularity.

## Key Contributions

- Systematic empirical comparison between Data Assimilation (DA) and Likelihood-Based Inference (LBI) for latent state estimation in Agent-Based Models (ABMs).
- Demonstration that LBI outperforms DA in latent agent-level opinion recovery and individual-level forecasting in the Bounded-Confidence Model.
- Evidence that both DA and LBI yield comparable aggregate-level performance, establishing DA as a competitive, model-agnostic alternative for aggregate forecasting tasks.

## Open Questions & Future Work

- [[lbi-robustness-in-asymmetric-abms]]

## Key Concepts

- [[da-vs-lbi-for-abm-latent-estimation]]: A comparative framework evaluating model-agnostic data assimilation against likelihood-leveraging inference for recovering latent states in simulation models.

## Archivist Review

I approved a single concept to capture the core methodological tension between model-agnostic data assimilation and model-specific likelihood inference in simulation-based state recovery. I also approved the open question regarding the robustness of these inference strategies, as it directly addresses the limitations of relying on symmetry-heavy models for broader complex system modeling. No datasets were approved as none were presented as novel or critical benchmarks.

### Approved Concepts
- Data Assimilation vs. Likelihood-Based Inference for ABM Latent Estimation: The comparison highlights the trade-off between model-agnostic generality (DA) and granularity/precision (LBI) in state-space recovery for simulation-based models, a critical concern for neural surrogate and world model design.

### Approved Open Questions
- Robustness of LBI in Asymmetric ABMs: This is technically important because it determines whether LBI's robustness is a fundamental feature of the inference approach or a byproduct of specific model geometry, influencing its suitability for more realistic, heterogeneous social systems.

## Links

- [Abstract](https://arxiv.org/abs/2509.17625)
- [PDF](https://arxiv.org/pdf/2509.17625)

