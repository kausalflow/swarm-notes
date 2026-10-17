---
# CSL-compatible fields
title: "Predicting Unseen Scientific Interactions: Conditional Flow Models Hallucinate Non-Additive Effects"
author:
  - literal: "Sam Christian Jan Gijsen"
  - literal: "Moritz Vinzent Seiler"
  - literal: "Kerstin Ritter"
issued:
  date-parts:
    - [2026, 10, 14]
url: "https://arxiv.org/abs/2610.20288"

# Custom fields
paper_id: "2610.20288"
paper_source: "openalex"
domain: "biology"
tags:
  - "diffusion-model"
  - "evaluation"
  - "biology"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-17T08:55:55Z"
created_at: "2026-10-17T08:55:55Z"
---

# Predicting Unseen Scientific Interactions: Conditional Flow Models Hallucinate Non-Additive Effects

**Authors**: Sam Christian Jan Gijsen, Moritz Vinzent Seiler, Kerstin Ritter
**Date**: 2026-10-14
**Paper ID**: [openalex:2610.20288](https://arxiv.org/abs/2610.20288)

## Summary

This paper investigates how conditional generative flow-matching models learn and extrapolate non-additive scientific interactions across various domains, including physiological time series, drug responses, cell perturbations, and molecular conformers. The authors reveal that conditional flow models learn individual effects significantly faster than interaction effects and often hallucinate non-additive interactions where none exist. Furthermore, they demonstrate that aggregate fidelity metrics often conceal failures in interaction recovery, and that hallucinations increase when targets are less identifiable.

## Key Contributions

- Evaluated interaction recovery in conditional flow-matching models using physiological time-series simulators, drug dose-response data, combinatorial cell perturbations, and molecular conformer generations.
- Demonstrated that individual effects are learned earlier than interactions and that models frequently hallucinate non-additive interaction structures where none exist.
- Showed that hallucination rates increase as target identifiability decreases and that aggregate fidelity metrics fail to reflect whether models genuinely capture interactions.

## Open Questions & Future Work

- [[conditional-flow-models-interaction-hallucination]]

## Archivist Review

Approved a single high-impact open question regarding interaction hallucination in conditional flow-matching models. No concepts or datasets met the strict novelty and reusability criteria for permanent vault inclusion.

### Approved Open Questions
- Interaction Hallucination in Conditional Flow Models: Understanding how generative models extrapolate interaction effects is critical for high-stakes scientific discovery, as models can appear accurate overall while incorrectly predicting the combinatorial or synergistic effects that motivate experiments.

## Links

- [Abstract](https://arxiv.org/abs/2610.20288)
- [PDF](https://arxiv.org/pdf/2610.20288)

