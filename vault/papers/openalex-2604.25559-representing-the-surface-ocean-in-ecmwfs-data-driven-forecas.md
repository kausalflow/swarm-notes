---
# CSL-compatible fields
title: "Representing the Surface Ocean in ECMWF's data-driven forecasting system AIFS"
author:
  - literal: "Sara Hahner"
  - literal: "Lorenzo Zampieri"
  - literal: "Jean‐Raymond Bidlot"
  - literal: "Philip Browne"
  - literal: "Matthew Chantry"
  - literal: "Mariana C. A. Clare"
  - literal: "Harrison Cook"
  - literal: "Peter Dueben"
  - literal: "Rachel Furner"
  - literal: "Sarah Keeley"
  - literal: "Josh Kousal"
  - literal: "Simon Lang"
  - literal: "Christian Lessig"
  - literal: "Gert Mertes"
  - literal: "Kristian Mogensen"
  - literal: "Gabriel Moldovan"
  - literal: "Charles Pelletier"
  - literal: "Florian Pinault"
  - literal: "Ana Prieto Nemesio"
  - literal: "Baudouin Raoult"
  - literal: "Irina Sandu"
  - literal: "Mario Santa Cruz"
  - literal: "Jakob Schloer"
  - literal: "Steffen Tietsche"
  - literal: "Hao Zuo"
issued:
  date-parts:
    - [2026, 4, 28]
url: "https://arxiv.org/abs/2604.25559"

# Custom fields
paper_id: "2604.25559"
paper_source: "openalex"
domain: "nlp"
tags:
  - "multimodal"
  - "language-model"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-01T07:22:23Z"
created_at: "2026-05-01T07:22:23Z"
---

# Representing the Surface Ocean in ECMWF's data-driven forecasting system AIFS

**Authors**: Sara Hahner, Lorenzo Zampieri, Jean‐Raymond Bidlot, Philip Browne, Matthew Chantry, Mariana C. A. Clare, Harrison Cook, Peter Dueben, Rachel Furner, Sarah Keeley, Josh Kousal, Simon Lang, Christian Lessig, Gert Mertes, Kristian Mogensen, Gabriel Moldovan, Charles Pelletier, Florian Pinault, Ana Prieto Nemesio, Baudouin Raoult, Irina Sandu, Mario Santa Cruz, Jakob Schloer, Steffen Tietsche, Hao Zuo
**Date**: 2026-04-28
**Paper ID**: [openalex:2604.25559](https://arxiv.org/abs/2604.25559)

## Summary

The AIFS framework is extended to jointly model atmospheric and surface ocean processes, including waves and sea ice, moving beyond separate numerical modeling approaches. By training on cross-component relationships, the model captures complex interactions at the air-sea interface using a component-agnostic architecture. Evaluation shows significant improvements in medium-range marine forecasting skill and physical consistency under out-of-distribution initial conditions.

## Key Contributions

- Extends the ECMWF AIFS framework to a joint atmosphere-ocean model by learning cross-component correlations in a component-agnostic manner.
- Demonstrates a one-day improvement in medium-range forecast skill for marine variables compared to traditional physics-based models.
- Addresses design challenges in coupled Earth system modeling including spatial missing values, multi-scale dynamics, and training loss scaling.

## Open Questions & Future Work

- [[predicting-trend-dominated-ocean-variables]]
- [[mitigating-representational-competition-joint-models]]

## Archivist Review

The paper describes a compelling scaling of a foundational atmospheric forecasting model (AIFS) to encompass coupled Earth system dynamics. I approved the two open questions as they represent significant structural challenges for hybrid machine-learning Earth system modeling: handling long-term physical trends in predictive models and addressing latent capacity competition in joint-component architectures. No new concepts were approved as the architectural contributions were presented as extensions of existing AIFS infrastructure.

### Approved Open Questions
- Predicting Trend-Dominated Ocean Variables: This is a crucial technical challenge for integrating long-term climate-relevant variables into short-term, data-driven forecasting systems, as it directly impacts prediction accuracy for essential ocean metrics.
- Mitigating Representational Competition: Addressing this competition is essential for scaling data-driven models to fully integrated, high-fidelity Earth system representations without sacrificing existing forecast skill.

## Links

- [Abstract](https://arxiv.org/abs/2604.25559)
- [PDF](https://arxiv.org/pdf/2604.25559)

