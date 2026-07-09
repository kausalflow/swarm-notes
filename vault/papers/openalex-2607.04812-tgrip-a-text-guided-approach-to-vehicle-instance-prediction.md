---
# CSL-compatible fields
title: "TGRIP: A Text-Guided Approach to Vehicle Instance Prediction in Autonomous Driving"
author:
  - literal: "Miguel Antunes-García"
  - literal: "Santiago Montiel-Marín"
  - literal: "Fabio Sánchez-García"
  - literal: "Rodrigo Gutiérrez-Moreno"
  - literal: "Rafael Barea"
  - literal: "Luis M. Bergasa"
issued:
  date-parts:
    - [2026, 7, 6]
url: "https://arxiv.org/abs/2607.04812"

# Custom fields
paper_id: "2607.04812"
paper_source: "openalex"
domain: "robotics"
tags:
  - "multimodal"
  - "vision-language-model"
  - "robotics"
  - "autonomous-agent"
  - "trajectory-prediction"
architectures:
  []
datasets:
  - "nuscenes"
concept_slugs:
  - "tgrip-framework"
dataset_slugs:
  - "nuscenes"
skill: "TimeSeriesSkill"
processed_at: "2026-07-09T08:19:25Z"
created_at: "2026-07-09T08:19:25Z"
---

# TGRIP: A Text-Guided Approach to Vehicle Instance Prediction in Autonomous Driving

**Authors**: Miguel Antunes-García, Santiago Montiel-Marín, Fabio Sánchez-García, Rodrigo Gutiérrez-Moreno, Rafael Barea, Luis M. Bergasa
**Date**: 2026-07-06
**Paper ID**: [openalex:2607.04812](https://arxiv.org/abs/2607.04812)

## Summary

TGRIP addresses the limitations of purely geometric Bird's-Eye View (BEV) instance prediction by incorporating semantic priors from Vision-Language Foundation Models. The proposed teacher-student architecture uses these semantic-enhanced maps as auxiliary training supervision to improve the model's ability to handle complex agent behaviors like intersections and overtaking. Experimental results on the nuScenes dataset demonstrate that this semantic enrichment leads to more robust motion prediction compared to existing geometrically-focused models.

## Key Contributions

- Introduces TGRIP, a framework that integrates vision-language semantic priors into end-to-end BEV instance prediction.
- Employs a teacher-student training pipeline where foundation-model-generated semantic maps provide auxiliary supervision.
- Surpasses state-of-the-art performance on the nuScenes dataset by improving spatio-temporal representations for complex agent behaviors.

## Open Questions & Future Work

- [[open-vocabulary-bev-supervision-bottleneck-label-dependency]]

## Key Concepts

- [[tgrip-framework]]: A training framework that leverages vision-language foundation models to provide auxiliary semantic supervision for end-to-end Bird's-Eye View instance prediction.

## Archivist Review

I approved the TGRIP framework as it introduces a reusable paradigm for semantic distillation in autonomous navigation tasks. The open question was approved for capturing the critical limitation of relying on labeled 3D data for semantic map construction. The nuScenes dataset was approved as the primary benchmark referenced in the work.

### Approved Concepts
- Text-Guided Representation for Instance Prediction (TGRIP): It proposes a concrete methodology for integrating semantic priors from vision-language models into end-to-end spatiotemporal forecasting, a task traditionally constrained to geometric supervision.

### Approved Open Questions
- Open-Vocabulary BEV Supervision Bottleneck: Removing dependency on manually labeled 3D boxes is essential for scaling autonomous driving perception to long-tail, real-world scenarios where unanticipated objects or rare categories frequently occur.

## Datasets

- [[nuscenes]]

## Links

- [Abstract](https://arxiv.org/abs/2607.04812)
- [PDF](https://arxiv.org/pdf/2607.04812)

