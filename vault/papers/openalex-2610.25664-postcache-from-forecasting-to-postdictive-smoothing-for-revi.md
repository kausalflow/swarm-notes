---
# CSL-compatible fields
title: "PoSTCache: From Forecasting to Postdictive Smoothing for Revisable Diffusion Caching"
author:
  - literal: "Liwei Lan"
  - literal: "Hui Chen"
  - literal: "Jungong Han"
  - literal: "Guiguang Ding"
issued:
  date-parts:
    - [2026, 10, 19]
url: "https://arxiv.org/abs/2610.25664"

# Custom fields
paper_id: "2610.25664"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "diffusion-model"
  - "model-compression"
architectures:
  []
datasets:
  []
concept_slugs:
  - "postcache"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-22T09:44:28Z"
created_at: "2026-10-22T09:44:28Z"
---

# PoSTCache: From Forecasting to Postdictive Smoothing for Revisable Diffusion Caching

**Authors**: Liwei Lan, Hui Chen, Jungong Han, Guiguang Ding
**Date**: 2026-10-19
**Paper ID**: [openalex:2610.25664](https://arxiv.org/abs/2610.25664)

## Summary

PoSTCache is a training-free framework for accelerating diffusion and flow matching models that reformulates caching as revisable trajectory inference using postdictive smoothing. Instead of enforcing a forward-only information flow, PoSTCache propagates correction signals backward from full-computation steps to refine preceding skipped-step approximations. It is paired with a Posterior Variance Reduction strategy for optimal anchor selection, improving the quality-efficiency trade-off for image and video generation.

## Key Contributions

- Proposes PoSTCache, a training-free framework that reformulates diffusion caching as revisable trajectory inference with backward correction.
- Introduces the Posterior Variance Reduction (PVR) strategy to select full-computation anchors based on expected reduction in surrogate trajectory uncertainty.
- Demonstrates consistent improvements in the quality-efficiency trade-off across representative image and video generation models compared to existing caching methods.

## Key Concepts

- [[postcache]]: A training-free and plug-and-play diffusion caching framework that uses postdictive smoothing to revise skipped step approximations via backward error propagation.

## Archivist Review

Approved the overarching PoSTCache framework as a distinct and reusable contribution to diffusion acceleration. Rejected subcomponents and open questions as paper-local or secondary extensions.

### Approved Concepts
- PoSTCache: It introduces a novel postdictive smoothing framework for diffusion caching, enabling backward correction of skipped step approximations.

### Rejected Candidates
- [concept] Posterior Variance Reduction (PVR) (`posterior-variance-reduction-pvr`) - subcomponent_of_broader_mechanism: Subcomponent of the broader PoSTCache framework that is specific to anchor selection strategy.
- [open_question] Sample-Adaptive Revisable Diffusion Caching (`sample-adaptive-revisable-diffusion-caching`) - paper_local: Paper-local future work direction for adapting anchor schedules online.

## Links

- [Abstract](https://arxiv.org/abs/2610.25664)
- [PDF](https://arxiv.org/pdf/2610.25664)

