---
# CSL-compatible fields
title: "Investigating Forecasting Capabilities of Narrative Networks on Emerging Stories"
author:
  - literal: "Ravi Teja Karumuri"
  - literal: "Steven R. Corman"
  - literal: "Huan Liu"
  - literal: "Joshua Garland"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2610.35628"

# Custom fields
paper_id: "2610.35628"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "graph-neural-network"
  - "gnn"
  - "information-extraction"
  - "semantic-search"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-29T11:10:51Z"
created_at: "2026-10-29T11:10:51Z"
---

# Investigating Forecasting Capabilities of Narrative Networks on Emerging Stories

**Authors**: Ravi Teja Karumuri, Steven R. Corman, Huan Liu, Joshua Garland
**Date**: 2026-10-26
**Paper ID**: [openalex:2610.35628](https://arxiv.org/abs/2610.35628)

## Summary

This paper investigates whether the structural properties of narrative networks—constructed from news articles using a Large Language Model-based Semantic Edge Parser—can predict emerging links as storylines evolve. Evaluating standard link predictors across three distinct real-world events (the 2022 Canadian Freedom Convoy, Hurricane Melissa, and the 2025-26 Iranian protests), the authors find that Preferential Attachment effectively forecasts next-day links with a mean ROC-AUC of 0.76-0.79, outperforming a memorization baseline. The findings demonstrate that narrative network structure encodes predictable relational dynamics, though this forecasting power is concentrated among highly connected entities.

## Key Contributions

- Constructs narrative networks from news articles using a Semantic Edge Parser (SEP) powered by a Large Language Model to capture interactions among narrative elements.
- Evaluates the predictive capability of narrative network structures on emerging storyline links using rolling time windows across three real-world events (2022 Canadian Freedom Convoy, Hurricane Melissa, and 2025-26 Iranian protests).
- Demonstrates that Preferential Attachment achieves a mean ROC-AUC of 0.76-0.79 for predicting next-day emergent narrative links, outperforming an EdgeBank memorization baseline by 11.3-14.5 points.
- Reveals that predictive advantage in narrative networks is primarily concentrated among the most frequently mentioned, highly connected entities.

## Limitations

Predictive advantage is primarily concentrated among highly connected, frequently mentioned entities rather than sparse or emerging peripheral elements.

## Open Questions & Future Work

- [[rigorous-evaluations-emergent-narratives]]
- [[forecasting-new-narrative-elements]]

## Archivist Review

The paper applies standard link prediction heuristics to text-derived narrative networks. The Semantic Edge Parser and general task are paper-local or routine wrappers around LLM text graphs, so no concepts are approved. However, the two explicit future directions regarding rigorous negative sampling for emergent networks and forecasting brand-new cold-start narrative elements are high-value, non-trivial open questions that merit standalone vault notes.

### Approved Open Questions
- Rigorous Evaluation for Emergent Narratives: Crucial for establishing whether narrative network forecasting captures true underlying relational dynamics rather than artifactual degree correlations driven by entity salience and random negative sampling.
- Forecasting New Narrative Elements: Essential for real-world crisis and news forecasting applications where breaking developments constantly introduce previously unknown actors and events.

### Rejected Candidates
- [concept] Semantic Edge Parser (`semantic-edge-parser`) - subcomponent_of_broader_mechanism: A routine wrapper for extracting graph edges using an LLM, lacking standalone reusable architectural novelty.
- [concept] Narrative Network Forecasting (`narrative-network-forecasting`) - generic: Too broad and descriptive of the general task domain rather than a distinct algorithmic contribution.

## Links

- [Abstract](https://arxiv.org/abs/2610.35628)
- [PDF](https://arxiv.org/pdf/2610.35628)

