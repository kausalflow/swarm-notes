---
# CSL-compatible fields
title: "DF$^3$: World Modeling via Decoder-Free Feature Forecasting in Autonomous Navigation"
author:
  - literal: "Jiaming Chen"
  - literal: "Guoan Xu"
  - literal: "Aoshen Huang"
  - literal: "Haozhuo Zhang"
  - literal: "Yang Li"
  - literal: "Wei Pan"
issued:
  date-parts:
    - [2026, 8, 3]
url: "https://arxiv.org/abs/2608.02428"

# Custom fields
paper_id: "2608.02428"
paper_source: "openalex"
domain: "robotics"
tags:
  - "multimodal"
  - "vision-language-model"
  - "robotics"
  - "agent"
  - "autonomous-agent"
  - "world-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "decoder-free-feature-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-06T07:32:14Z"
created_at: "2026-08-06T07:32:14Z"
---

# DF$^3$: World Modeling via Decoder-Free Feature Forecasting in Autonomous Navigation

**Authors**: Jiaming Chen, Guoan Xu, Aoshen Huang, Haozhuo Zhang, Yang Li, Wei Pan
**Date**: 2026-08-03
**Paper ID**: [openalex:2608.02428](https://arxiv.org/abs/2608.02428)

## Summary

This paper introduces DF^3, a decoder-free feature forecasting framework for world modeling in autonomous navigation that operates entirely within the latent space. By injecting learnable spatial queries into a frozen vision foundation model and using a Motion-Aware Context Fusion mechanism, DF^3 directly predicts future state representations and task outputs without the computational bottleneck of a heavy decoder. Experiments show high efficiency and strong zero-shot performance in robotic simulation.

## Key Contributions

- Proposes Decoder-Free Feature Forecasting (DF^3) which models world evolution entirely in latent space without a decoder.
- Introduces a Motion-Aware Context Fusion (MACF) mechanism combining coarse flow warping and fine-grained latent cross-correlation for feature alignment and forecasting.
- Demonstrates superior efficiency and zero-shot deployment in a robotic simulator while maintaining competitive performance with state-of-the-art generative methods.

## Open Questions & Future Work

- [[action-conditional-latent-world-modeling]]

## Key Concepts

- [[decoder-free-feature-forecasting]]: A world modeling framework that forecasts future states entirely within the latent space and directly derives task outputs without a decoder.

## Archivist Review

Selected the central conceptual framework of decoder-free latent world modeling along with its direct action-conditioning open question, while keeping rejections focused on paper-local subcomponents like MACF.

### Approved Concepts
- Decoder-Free Feature Forecasting: Introduces a paradigm for world modeling that bypasses heavy decoders entirely by operating in latent space and extracting task outputs directly via spatial queries.

### Approved Open Questions
- Action-Conditional Latent World Modeling: Action-conditioning is vital for transforming observational feature forecasting models into active world models capable of end-to-end policy learning and robotic planning.

## Links

- [Abstract](https://arxiv.org/abs/2608.02428)
- [PDF](https://arxiv.org/pdf/2608.02428)

