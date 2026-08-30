---
# CSL-compatible fields
title: "Multi-Person Human Motion Forecasting in Complex Scenes"
author:
  - literal: "Serdar Ozsoy"
  - literal: "Lars Doorenbos"
  - literal: "Jüergen Gall"
  - literal: "Serdar Ozsoy"
  - literal: "Lars Doorenbos"
  - literal: "Jüergen Gall"
issued:
  date-parts:
    - [2026, 8, 27]
url: "https://arxiv.org/abs/2608.27039"

# Custom fields
paper_id: "2608.27039"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "diffusion-model"
  - "generative-model"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "object-conditioned-social-diffusion-ocsd"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-30T10:10:31Z"
created_at: "2026-08-30T10:10:31Z"
---

# Multi-Person Human Motion Forecasting in Complex Scenes

**Authors**: Serdar Ozsoy, Lars Doorenbos, Jüergen Gall, Serdar Ozsoy, Lars Doorenbos, Jüergen Gall
**Date**: 2026-08-27
**Paper ID**: [openalex:2608.27039](https://arxiv.org/abs/2608.27039)

## Summary

The paper proposes Object-Conditioned Social Diffusion (OCSD), a conditional diffusion model for multi-person human motion forecasting in complex scenes. OCSD integrates motion history, multi-person interactions, and object cues through a timestep-modulated object-conditioning mechanism and a dedicated social encoder. Extensive experiments demonstrate state-of-the-art performance on the Humans in Kitchens (HiK) and HOI-M3 benchmarks, significantly reducing path error and producing realistic long-term forecasts.

## Key Contributions

- Proposes Object-Conditioned Social Diffusion (OCSD), a unified conditional diffusion model that integrates motion history, multi-person interactions, and object cues.
- Introduces an object-conditioning mechanism that modulates denoising at every timestep for fine-grained human-object reasoning.
- Achieves state-of-the-art performance, reducing the two-second path error by 31.3% on Humans in Kitchens (HiK) and 33.2% on HOI-M3.

## Open Questions & Future Work

- [[dynamic-object-position-forecasting]]

## Key Concepts

- [[object-conditioned-social-diffusion-ocsd]]: A conditional diffusion model that integrates motion history, multi-person interactions, and object cues via an object-conditioning mechanism.

## Archivist Review

Approved the core OCSD framework as a reusable diffusion-based multi-agent conditioning mechanism and retained the dynamic object position forecasting open question. The open-vocabulary question was pruned as a routine vision-language integration task.

### Approved Concepts
- Object-Conditioned Social Diffusion (OCSD): Central core framework proposed by the paper for multi-person human motion forecasting in complex scenes combining object conditioning and social interactions.

### Approved Open Questions
- Dynamic Object Position Forecasting: Essential for expanding motion forecasting capabilities from controlled environments with static furniture to realistic, dynamic real-world environments where objects are manipulated or relocated by humans.

### Rejected Candidates
- [open_question] Open-Vocabulary Object Representations (`open-vocabulary-object-representations`) - low_impact: Describes routine integration of vision-language embeddings rather than a deep unresolved modeling bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2608.27039)
- [PDF](https://arxiv.org/pdf/2608.27039)

