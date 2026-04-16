---
# CSL-compatible fields
title: "Representations Before Pixels: Semantics-Guided Hierarchical Video Prediction"
author:
  - literal: "Efstathios Karypidis"
  - literal: "Spyros Gidaris"
  - literal: "Nikos Komodakis"
issued:
  date-parts:
    - [2026, 4, 13]
url: "https://arxiv.org/abs/2604.11707"

# Custom fields
paper_id: "2604.11707"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "diffusion-model"
  - "video-prediction"
  - "representation-learning"
  - "multimodal"
architectures:
  []
datasets:
  []
concept_slugs:
  - "semantics-guided-hierarchical-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-16T06:28:59Z"
created_at: "2026-04-16T06:28:59Z"
---

# Representations Before Pixels: Semantics-Guided Hierarchical Video Prediction

**Authors**: Efstathios Karypidis, Spyros Gidaris, Nikos Komodakis
**Date**: 2026-04-13
**Paper ID**: [openalex:2604.11707](https://arxiv.org/abs/2604.11707)

## Summary

Re2Pix is a hierarchical video prediction framework that improves generation quality and consistency by decomposing the task into two distinct stages: forecasting future scene semantics in a frozen vision foundation model's feature space, followed by representation-conditioned visual synthesis. This approach bypasses the difficulty of direct pixel-space autoregression by focusing first on scene dynamics. To handle error accumulation during inference, the authors introduce nested dropout and mixed supervision strategies, significantly improving robustness to imperfect representation predictions. Experiments demonstrate that this semantics-first design achieves superior temporal consistency and efficiency in complex dynamic scenes.

## Key Contributions

- Introduces Re2Pix, a hierarchical video prediction framework that decouples future forecasting into semantic representation prediction and subsequent pixel synthesis.
- Proposes two conditioning strategies, nested dropout and mixed supervision, to mitigate train-test mismatch between ground-truth and autoregressively predicted features.
- Demonstrates improved temporal semantic consistency, perceptual quality, and training efficiency over strong diffusion-based video prediction baselines in complex dynamic driving environments.

## Open Questions & Future Work

- [[broadening-vfm-feature-guidance-granularity]]

## Key Concepts

- [[semantics-guided-hierarchical-forecasting]]: A framework for video prediction that decouples the task into forecasting semantic representations of a vision foundation model followed by representation-conditioned visual synthesis.

## Archivist Review

The approved concept captures the overarching 'semantics-first' decomposition strategy, which is highly reusable and central to the contribution. The approved open question addresses the foundational research challenge of how to better leverage structured semantic priors in hierarchical video generation. Specific model instances (Re2Pix) and incremental tuning tasks (guidance optimization) were rejected as paper-local or low-impact.

### Approved Concepts
- Semantics-Guided Hierarchical Forecasting: This architecture decomposes the high-dimensional video forecasting task into a manageable structure-prediction task followed by a synthesis task, which is a major paradigm shift for autoregressive video generation.

### Approved Open Questions
- Expanding VFM feature guidance: This is a key architectural bottleneck identified by the authors as the next logical step to improve the structural accuracy of hierarchical video prediction beyond existing VFM feature approaches.

### Rejected Candidates
- [concept] Re2Pix (`re2pix`) - paper_local: This is a specific framework instance (paper-local implementation); the underlying mechanism is captured by the approved concept 'semantics-guided-hierarchical-forecasting'.
- [open_question] Optimizing hierarchical representation guidance (`cfgs-style-representation-guidance-optimization`) - low_impact: This is a specific tuning/optimization question for a specific guidance approach rather than a fundamental open research problem in the field.

## Links

- [Abstract](https://arxiv.org/abs/2604.11707)
- [PDF](https://arxiv.org/pdf/2604.11707)

