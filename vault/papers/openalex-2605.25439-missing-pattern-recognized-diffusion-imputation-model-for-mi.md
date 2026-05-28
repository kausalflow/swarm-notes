---
# CSL-compatible fields
title: "Missing Pattern Recognized Diffusion Imputation Model for Missing Not At Random"
author:
  - literal: "Gyuwon Sim"
  - literal: "Sumin Lee"
  - literal: "Heesun Bae"
  - literal: "Byeonghu Na"
  - literal: "Doyun Kwon"
  - literal: "Ju-Hee Hwang"
  - literal: "Jae-Young Lim"
  - literal: "Il-Chul Moon"
issued:
  date-parts:
    - [2026, 5, 25]
url: "https://arxiv.org/abs/2605.25439"

# Custom fields
paper_id: "2605.25439"
paper_source: "openalex"
domain: "nlp"
tags:
  - "diffusion-model"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "prdim"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-28T08:38:23Z"
created_at: "2026-05-28T08:38:23Z"
---

# Missing Pattern Recognized Diffusion Imputation Model for Missing Not At Random

**Authors**: Gyuwon Sim, Sumin Lee, Heesun Bae, Byeonghu Na, Doyun Kwon, Ju-Hee Hwang, Jae-Young Lim, Il-Chul Moon
**Date**: 2026-05-25
**Paper ID**: [openalex:2605.25439](https://arxiv.org/abs/2605.25439)

## Summary

This paper introduces the Missing Pattern Recognized Diffusion Imputation Model (PRDIM) to address data imputation under Missing Not at Random (MNAR) conditions. By leveraging an Expectation-Maximization framework, the model iteratively maximizes the joint likelihood of observed values and their corresponding missing masks. A dedicated pattern recognizer is incorporated to guide the diffusion-based imputation process, ensuring more accurate and contextually aware results. Empirical evaluations confirm that PRDIM consistently outperforms standard baselines across diverse data modalities.

## Key Contributions

- Introduces PRDIM, a novel diffusion-based framework designed specifically for Missing Not at Random (MNAR) data imputation.
- Integrates a pattern recognizer within an EM algorithm to provide guidance for diffusion model inference, improving the plausibility of imputed values.
- Demonstrates superior imputation performance under MNAR settings across multiple modalities, including time-series and image data.

## Open Questions & Future Work

- [[mnar-aware-discrete-diffusion]]

## Key Concepts

- [[prdim]]: A diffusion-based imputation framework that iteratively maximizes the joint likelihood of observed data and missing masks using a pattern-recognizer guidance.

## Archivist Review

I have approved the core framework (PRDIM) as a novel mechanism for handling MNAR data imputation, along with one open research question regarding its extension to discrete state-space diffusion models. These items meet the strict criteria for novelty, reusability, and addressing substantial unresolved bottlenecks in temporal and multimodal data processing. Other candidates were not deemed sufficiently distinct or were classified as local implementation details.

### Approved Concepts
- Missing Pattern Recognized Diffusion Imputation Model (PRDIM): PRDIM addresses the challenging Missing Not at Random (MNAR) data imputation problem by jointly modeling the data and the missing mask.

### Approved Open Questions
- MNAR-aware Discrete Diffusion Imputation: Many real-world datasets contain a mixture of continuous and discrete features, and current continuous-only diffusion methods are insufficient for comprehensive multi-modal imputation.

## Links

- [Abstract](https://arxiv.org/abs/2605.25439)
- [PDF](https://arxiv.org/pdf/2605.25439)

