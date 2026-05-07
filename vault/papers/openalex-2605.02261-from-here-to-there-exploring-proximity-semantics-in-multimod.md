---
# CSL-compatible fields
title: "From 'Here' to 'There': Exploring Proximity Semantics in Multimodal Data Exploration"
author:
  - literal: "Dennis Bromley"
  - literal: "Diana Wang"
  - literal: "Vidya Setlur"
issued:
  date-parts:
    - [2026, 5, 4]
url: "https://arxiv.org/abs/2605.02261"

# Custom fields
paper_id: "2605.02261"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "vision-language-model"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "proximity-semantics"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-07T07:38:18Z"
created_at: "2026-05-07T07:38:18Z"
---

# From 'Here' to 'There': Exploring Proximity Semantics in Multimodal Data Exploration

**Authors**: Dennis Bromley, Diana Wang, Vidya Setlur
**Date**: 2026-05-04
**Paper ID**: [openalex:2605.02261](https://arxiv.org/abs/2605.02261)

## Summary

This paper investigates how users interact with multimodal data exploration tools using a combination of free-form sketching, natural language, and visual annotations. The authors develop a system architecture that fuses geometric sketch matching with visual language models to interpret these interleaved queries. Through a user study, they identify 'proximity semantics' as a mechanism where the relative spatial and temporal arrangement of user inputs is crucial for resolving intent, offering a new design paradigm for future multimodal analytical systems.

## Key Contributions

- Introduces a multimodal interaction probe that integrates sketching, natural language, and visual annotations for time-series and geospatial data exploration.
- Defines 'proximity semantics' as a conceptual framework where user intent is disambiguated through the spatial and temporal closeness of multimodal query elements.
- Demonstrates that users rely on spatial/temporal proximity to ground complex analytical queries that are otherwise difficult to specify with language alone.

## Open Questions & Future Work

- [[quantifying-proximity-thresholds-in-multimodal-interaction]]

## Key Concepts

- [[proximity-semantics]]: A conceptual lens for interpreting user intent in multimodal data exploration where meaning is derived from the relative placement of sketches, annotations, and text within a shared space.

## Archivist Review

I approved the concept of 'proximity semantics' as a foundational framework for multimodal interaction, as it offers a novel way to interpret user intent beyond traditional natural language queries. The open question regarding the quantification of proximity thresholds is also approved, as it addresses a fundamental ambiguity in implementing such semantic frameworks in real-world interfaces. No datasets were provided in the paper that meet the criteria for a standalone vault entry.

### Approved Concepts
- Proximity Semantics (PS): Introduces a conceptual framework for interpreting multimodal input based on the spatial and temporal proximity of user-provided elements.

### Approved Open Questions
- Quantifying Proximity Thresholds for Multimodal Interaction: Establishing these thresholds is critical for building robust multimodal systems that can reliably resolve ambiguous user queries without being overly restrictive or too inclusive.

## Links

- [Abstract](https://arxiv.org/abs/2605.02261)
- [PDF](https://arxiv.org/pdf/2605.02261)

