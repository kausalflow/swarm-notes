---
# CSL-compatible fields
title: "End-to-End Identifiable and Consistent Recurrent Switching Dynamical Systems"
author:
  - literal: "Carles Balsells-Rodas"
  - literal: "Zhengrui Xiang"
  - literal: "Xavier Sumba"
  - literal: "Yingzhen Li"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.06315"

# Custom fields
paper_id: "2605.06315"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "forecasting"
  - "variational-autoencoder"
  - "vae"
  - "generative-adversarial-network"
  - "interpretability"
  - "stochastic-attention"
architectures:
  []
datasets:
  []
concept_slugs:
  - "omegasds"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:22:50Z"
created_at: "2026-05-10T07:22:50Z"
---

# End-to-End Identifiable and Consistent Recurrent Switching Dynamical Systems

**Authors**: Carles Balsells-Rodas, Zhengrui Xiang, Xavier Sumba, Yingzhen Li
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.06315](https://arxiv.org/abs/2605.06315)

## Summary

Learning identifiable representations in sequential data with regime-switching dynamics is often limited by VAE-based approximation gaps and restrictive stationarity assumptions. This paper provides theoretical identifiability guarantees for a generalized class of recurrent nonlinear switching dynamical systems. To bridge the practical gap, the authors propose ΩSDS, a flow-based estimator that enables exact likelihood optimization through expectation-maximisation. Experimental results confirm that ΩSDS provides better latent disentanglement and more accurate dynamics forecasting than traditional variational approaches.

## Key Contributions

- Establishes theoretical identifiability for a broad class of recurrent nonlinear switching dynamical systems under flexible assumptions.
- Introduces ΩSDS, a flow-based estimator facilitating exact likelihood optimization via expectation-maximisation, surpassing VAE-based approximations.
- Demonstrates superior latent disentanglement and forecasting accuracy on both synthetic and real-world sequential datasets compared to existing VAE-based methods.

## Key Concepts

- [[omegasds]]: A flow-based estimator for recurrent nonlinear switching dynamical systems that utilizes expectation-maximisation to achieve exact likelihood optimization.

## Archivist Review

The paper makes a significant methodological advancement by replacing VAE-based approximation with an exact likelihood-based EM approach for switching dynamical systems. I have approved the proposed ΩSDS estimator as it provides a clear, reusable framework for researchers working on identifiable sequential representations. I rejected 'recurrent nonlinear switching dynamical systems' as it is a broad mathematical model rather than a specific contribution of the paper.

### Approved Concepts
- ΩSDS: It serves as a novel alternative to VAE-based approaches for learning identifiable representations in switching dynamical systems by enabling exact likelihood estimation.

### Rejected Candidates
- [concept] Recurrent Nonlinear Switching Dynamical Systems (`recurrent-nonlinear-switching-dynamical-systems`) - not_novel: This is a standard class of mathematical models and not a novel concept introduced by the paper.

## Links

- [Abstract](https://arxiv.org/abs/2605.06315)
- [PDF](https://arxiv.org/pdf/2605.06315)

