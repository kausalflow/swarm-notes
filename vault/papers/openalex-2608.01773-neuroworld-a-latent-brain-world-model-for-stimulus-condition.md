---
# CSL-compatible fields
title: "NeuroWorld: A Latent Brain World Model for Stimulus-Conditioned Human Brain Dynamics"
author:
  - literal: "Zijian Dong"
  - literal: "Jianxiong Zhou"
  - literal: "Kwun Kei Ng"
  - literal: "Jan Paolo Macapinlac Balagtas"
  - literal: "Zhizhou Li"
  - literal: "Zijiao Chen"
  - literal: "Juan Zhou"
issued:
  date-parts:
    - [2026, 8, 3]
url: "https://arxiv.org/abs/2608.01773"

# Custom fields
paper_id: "2608.01773"
paper_source: "openalex"
domain: "biology"
tags:
  - "multimodal"
  - "time-series"
  - "forecasting"
  - "robustness"
  - "benchmark"
  - "dataset"
  - "evaluation"
architectures:
  []
datasets:
  - "sg-mind"
concept_slugs:
  []
dataset_slugs:
  - "sg-mind"
skill: "TimeSeriesSkill"
processed_at: "2026-08-06T07:32:20Z"
created_at: "2026-08-06T07:32:20Z"
---

# NeuroWorld: A Latent Brain World Model for Stimulus-Conditioned Human Brain Dynamics

**Authors**: Zijian Dong, Jianxiong Zhou, Kwun Kei Ng, Jan Paolo Macapinlac Balagtas, Zhizhou Li, Zijiao Chen, Juan Zhou
**Date**: 2026-08-03
**Paper ID**: [openalex:2608.01773](https://arxiv.org/abs/2608.01773)

## Summary

NeuroWorld is a latent brain world model designed to forecast human brain functional dynamics under continuous sensory drive while strictly preventing future stimulus leakage. The method uses a two-stage approach: Latent Dynamics Learning (LDL) to learn causal state transitions without raw signal reconstruction, and Latent Rollout Decoding (LRD) to autoregressively roll latent states forward and decode them into whole-brain fMRI responses. Evaluated across three naturalistic movie-fMRI benchmarks including the new SG-MIND dataset, NeuroWorld achieves state-of-the-art multi-step rollout performance with high robustness to long-horizon drift.

## Key Contributions

- Introduces NeuroWorld, a latent brain world model for stimulus-conditioned human brain dynamics forecasting that strictly prevents future stimulus leakage.
- Proposes a two-stage framework consisting of Latent Dynamics Learning (LDL) for causal next-latent prediction and Latent Rollout Decoding (LRD) for autoregressive rollout from an fMRI prefix.
- Evaluates on three naturalistic movie-fMRI benchmarks including the newly collected SG-MIND dataset, achieving state-of-the-art multi-step rollout performance and robustness against long-horizon drift.

## Open Questions & Future Work

- [[generalizing-brain-world-models]]

## Archivist Review

Strictly adhered to sparseness and novelty review criteria. The SG-MIND dataset is approved as a key neuroimaging dataset contribution, and the open question regarding generalizing brain world models to unseen cohorts and longer rollouts is retained as a valuable methodological direction. No new domain concepts were approved since the paper's framework is domain-specific to fMRI brain modeling rather than a general time-series forecasting vault concept.

### Approved Open Questions
- Generalizing Brain World Models: Crucial for validating the generalizability, scalability, and clinical or cognitive utility of brain world models across diverse populations and imaging settings.

### Rejected Candidates
- [dataset] SG-MIND Dataset (`sg-mind`) - duplicate_existing: Already approved as sg-mind dataset.

## Datasets

- [[sg-mind]]

## Links

- [Abstract](https://arxiv.org/abs/2608.01773)
- [PDF](https://arxiv.org/pdf/2608.01773)

