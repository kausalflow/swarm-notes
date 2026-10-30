---
# CSL-compatible fields
title: "Ground-to-Satellite Knowledge Distillation for Crop Classification under Temporal and Geographic Shift"
author:
  - literal: "Miro Miranda"
  - literal: "Rocco Sedona"
  - literal: "Valerio Marsocci"
  - literal: "Gabriele Cavallaro"
  - literal: "Claudia Paris"
issued:
  date-parts:
    - [2026, 10, 27]
url: "https://arxiv.org/abs/2610.37021"

# Custom fields
paper_id: "2610.37021"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "multimodal"
  - "knowledge-distillation"
  - "clip"
  - "embedding"
  - "pre-training"
  - "robustness"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-30T11:06:00Z"
created_at: "2026-10-30T11:06:00Z"
---

# Ground-to-Satellite Knowledge Distillation for Crop Classification under Temporal and Geographic Shift

**Authors**: Miro Miranda, Rocco Sedona, Valerio Marsocci, Gabriele Cavallaro, Claudia Paris
**Date**: 2026-10-27
**Paper ID**: [openalex:2610.37021](https://arxiv.org/abs/2610.37021)

## Summary

This paper investigates ground-to-satellite knowledge distillation to improve crop classification under temporal and geographic shift by leveraging ground-level field photographs as privileged supervision during training. Using a photo teacher based on frozen CLIP features to supervise models built on pretrained satellite representations (such as AlphaEarth and TESSERA), the approach enhances classification robustness and performance without altering inference-time requirements. Experiments on a paired dataset demonstrate significant improvements in macro-F1 under temporal shift and geographic holdouts compared to satellite-only training.

## Key Contributions

- Proposes a ground-to-satellite knowledge distillation framework where a photo teacher (using frozen CLIP features) supervises satellite-based classifiers during training only.
- Demonstrates that ground-view supervision improves robustness under temporal shift, increasing macro-F1 by up to +5.5 points on frozen satellite embeddings.
- Shows enhanced generalisation in geographic holdout evaluations (+3.7 macro-F1 improvement compared to +3.0 in-distribution).
- Achieves improved classification performance without altering inference requirements (using only satellite data at test time).

## Archivist Review

Applied strict scarcity and novelty filters. No concepts or datasets were proposed, and the single open question was rejected as being a paper-local evaluation limitation rather than a broader foundational research question.

### Rejected Candidates
- [open_question] Global Geographic Generalization of Ground-to-Satellite Knowledge Distillation (`global-geographic-generalization-ground-kd`) - paper_local: The question of generalizing ground-to-satellite distillation across geographic regions is paper-local and tied directly to the specific ecoregion holdouts tested in the paper.

## Links

- [Abstract](https://arxiv.org/abs/2610.37021)
- [PDF](https://arxiv.org/pdf/2610.37021)

