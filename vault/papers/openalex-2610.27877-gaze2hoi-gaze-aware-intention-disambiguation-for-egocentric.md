---
# CSL-compatible fields
title: "Gaze2HOI: Gaze-Aware Intention Disambiguation for Egocentric Hand-Object Interaction Forecasting"
author:
  - literal: "Chuanyang Ma"
  - literal: "Chenye Wang"
  - literal: "Yixuan Wang"
  - literal: "Huiling Zhou"
  - literal: "Xingqun Qi"
  - literal: "Muyi Sun"
  - literal: "Man Zhang"
  - literal: "Caifeng Shan"
  - literal: "Zhenan Sun"
issued:
  date-parts:
    - [2026, 10, 20]
url: "https://arxiv.org/abs/2610.27877"

# Custom fields
paper_id: "2610.27877"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "multimodal"
  - "vision-language-model"
  - "diffusion-model"
  - "benchmark"
  - "evaluation"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "gaze2hoi"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-23T09:40:24Z"
created_at: "2026-10-23T09:40:24Z"
---

# Gaze2HOI: Gaze-Aware Intention Disambiguation for Egocentric Hand-Object Interaction Forecasting

**Authors**: Chuanyang Ma, Chenye Wang, Yixuan Wang, Huiling Zhou, Xingqun Qi, Muyi Sun, Man Zhang, Caifeng Shan, Zhenan Sun
**Date**: 2026-10-20
**Paper ID**: [openalex:2610.27877](https://arxiv.org/abs/2610.27877)

## Summary

Gaze2HOI is a hierarchical framework for egocentric hand-object interaction forecasting that resolves semantic and geometric ambiguities by integrating gaze cues. It modulates VLM visual representations using fixation strength and recency via Temporal Gaze Saliency Modulation (TGSM), grounds anticipated contacts, and uses a diffusion model to generate future hand motions and object trajectories. Evaluated on the EgoAIM benchmark, Gaze2HOI achieves state-of-the-art performance in both intention inference and motion forecasting.

## Key Contributions

- Proposed Gaze2HOI, a hierarchical framework for egocentric hand-object interaction forecasting via gaze-aware intention disambiguation.
- Introduced Temporal Gaze Saliency Modulation (TGSM) to weight gaze cues and modulate VLM visual representations for reducing semantic ambiguity.
- Developed an Anticipatory Contact Grounding (ACG) module to map structured intentions into explicit contact, support, and placement fields.
- Introduced EgoAIM, a phase-aware benchmark with fine-grained intention annotations for egocentric hand-object interactions.

## Limitations

Future work could explore scaling to more unconstrained environments and broader multi-modal wearable sensor setups.

## Open Questions & Future Work

- [[uncertainty-aware-object-placement-refinement-in-hoi-forecasting]]

## Key Concepts

- [[gaze2hoi]]: A hierarchical framework for egocentric hand-object interaction forecasting using gaze-aware intention disambiguation.

## Archivist Review

Approved the overarching framework 'Gaze2HOI' as a core reusable concept in egocentric hand-object interaction forecasting and the substantive open question regarding object placement refinement uncertainty. Rejected internal subcomponents (TGSM) and the paper-local benchmark dataset (EgoAIM) per vault policy.

### Approved Concepts
- Gaze2HOI: Core framework introduced for gaze-aware egocentric hand-object interaction forecasting.

### Approved Open Questions
- Uncertainty-Aware Object Placement Refinement: Placement accuracy is a major bottleneck in interactive AR/VR systems where objects must be set down accurately on supporting surfaces, making robust modeling of uncertainty and joint spatial-contact refinement technically critical.

### Rejected Candidates
- [concept] Temporal Gaze Saliency Modulation (`temporal-gaze-saliency-modulation`) - subcomponent_of_broader_mechanism: Subcomponent of the broader Gaze2HOI framework without sufficient standalone novelty demonstrated in the abstract alone.
- [dataset] EgoAIM (`egoaim`) - not_reusable: Newly introduced benchmark dataset without established broad external reusability yet.

## Links

- [Abstract](https://arxiv.org/abs/2610.27877)
- [PDF](https://arxiv.org/pdf/2610.27877)

