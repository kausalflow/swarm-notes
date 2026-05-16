---
# CSL-compatible fields
title: "HCSG: Human-Centric Semantic-Geometric Reasoning for Vision-Language Navigation"
author:
  - literal: "Haoxuan Xu"
  - literal: "Tianfu Li"
  - literal: "Wenbo Chen"
  - literal: "Yi ran Liu"
  - literal: "Jin Wu"
  - literal: "Huashuo Lei"
  - literal: "Yunfan Lou"
  - literal: "Lujia Wang"
  - literal: "Hesheng Wang"
  - literal: "Haoang Li"
issued:
  date-parts:
    - [2026, 5, 13]
url: "https://arxiv.org/abs/2605.13321"

# Custom fields
paper_id: "2605.13321"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "vision-language-model"
  - "navigation"
  - "agent"
  - "planning"
  - "benchmark"
architectures:
  - "encoder-decoder"
datasets:
  - "ha-vlnce"
concept_slugs:
  - "hcsg"
dataset_slugs:
  - "ha-vlnce"
skill: "TimeSeriesSkill"
processed_at: "2026-05-16T07:11:07Z"
created_at: "2026-05-16T07:11:07Z"
---

# HCSG: Human-Centric Semantic-Geometric Reasoning for Vision-Language Navigation

**Authors**: Haoxuan Xu, Tianfu Li, Wenbo Chen, Yi ran Liu, Jin Wu, Huashuo Lei, Yunfan Lou, Lujia Wang, Hesheng Wang, Haoang Li
**Date**: 2026-05-13
**Paper ID**: [openalex:2605.13321](https://arxiv.org/abs/2605.13321)

## Summary

HCSG is a new framework for Vision-Language Navigation (VLN) designed to handle dynamic, human-populated indoor environments by transitioning from simple obstacle avoidance to active human behavior understanding. It utilizes a unified Human Understanding Module that combines geometric trajectory forecasting with VLM-generated semantic action descriptions. These integrated representations are incorporated into a topological navigation map, supported by a social distance loss to ensure compliant interaction. Experimental results on the HA-VLNCE benchmark confirm that HCSG significantly improves navigation success and safety compared to existing methods.

## Key Contributions

- Proposed HCSG, a novel framework for VLN that integrates explicit human behavior understanding into navigation planning.
- Developed a unified Human Understanding Module that performs geometric trajectory forecasting and VLM-based action-intention interpretation.
- Achieved significant performance gains on the HA-VLNCE benchmark, specifically a 14% improvement in Success Rate and 34% reduction in Collision Rate.

## Open Questions & Future Work

- [[continuous-streaming-vln-design]]
- [[adaptive-social-distance-priors]]

## Key Concepts

- [[hcsg]]: A human-centric framework for vision-language navigation that integrates geometric trajectory forecasting with VLM-based semantic intention interpretation.

## Archivist Review

The paper introduces a well-defined human-centric reasoning framework for VLN. I approved the framework and its primary benchmark, while also capturing the key research bottlenecks identified regarding continuous navigation and context-aware social norms. The review policy was applied to ensure the vault remains focused on core structural mechanisms and meaningful research gaps rather than implementation-specific details.

### Approved Concepts
- HCSG: It introduces an explicit framework that shifts the paradigm from passive obstacle avoidance to active human behavior understanding in vision-language navigation.

### Approved Open Questions
- Continuous Streaming VLN Design: Transitioning to continuous streaming is critical for real-world deployment where robots cannot afford to pause indefinitely when navigating through busy environments.
- Adaptive Social Distance Priors: Static social distance metrics often fail to capture the nuance of human social norms, leading to either overly conservative or intrusive robot behavior.

## Datasets

- [[ha-vlnce]]

## Links

- [Abstract](https://arxiv.org/abs/2605.13321)
- [PDF](https://arxiv.org/pdf/2605.13321)

