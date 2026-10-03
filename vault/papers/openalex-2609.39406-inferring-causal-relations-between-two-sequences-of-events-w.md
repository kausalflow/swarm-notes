---
# CSL-compatible fields
title: "Inferring Causal Relations between Two Sequences of Events with Language Models"
author:
  - literal: "Nishchal Prasad"
  - literal: "Éric Gaussier"
  - literal: "Émilie Devijver"
  - literal: "Alexander Obeid Guzman"
  - literal: "Armen Aghasaryan"
  - literal: "Gregor Gößler"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2609.39406"

# Custom fields
paper_id: "2609.39406"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "causal-discovery"
  - "time-series"
  - "evaluation"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-03T10:09:08Z"
created_at: "2026-10-03T10:09:08Z"
---

# Inferring Causal Relations between Two Sequences of Events with Language Models

**Authors**: Nishchal Prasad, Éric Gaussier, Émilie Devijver, Alexander Obeid Guzman, Armen Aghasaryan, Gregor Gößler
**Date**: 2026-09-30
**Paper ID**: [openalex:2609.39406](https://arxiv.org/abs/2609.39406)

## Summary

This paper investigates causal discovery from single observations of event sequences, a challenging setting common in rare alarm detection where standard methods fail. The authors show that Large Language Models can leverage their predictive power to effectively infer causal relations between pairs of event sequences. Validated on both synthetic and real-world time-series data, the LLM-based approach outperforms traditional causal discovery algorithms even when operating on limited single sequences.

## Key Contributions

- Demonstrates that Large Language Models can be leveraged to infer causal relations between pairs of event sequences from single observations.
- Evaluates the proposed approach on both synthetic and real-world datasets involving sparse or rare event data like alarm sequences.
- Outperforms standard causal discovery algorithms on several time-series datasets converted into single observed sequences.

## Limitations

Not explicitly detailed in the abstract beyond focusing on pairwise event sequences from single observations.

## Open Questions & Future Work

- [[full-causal-graph-recovery]]
- [[temporal-information-causal-scoring]]

## Archivist Review

Archivist review kept only candidates judged central to the paper and reusable across future work. Approved 0 concept(s), 2 open question(s), and 0 dataset(s), with 0 rejected candidate note(s).

### Approved Open Questions
- Full Causal Graph Recovery: Moving from pairwise causal direction discovery to full graph recovery is a critical scaling step for practical applications like root-cause diagnosis in complex IT and telecommunications networks.
- Temporal Information in Causal Scoring: Integrating explicit temporal information is technically important because many real-world event sequences depend heavily on exact timing and delays rather than purely discrete sequential ordering.

## Links

- [Abstract](https://arxiv.org/abs/2609.39406)
- [PDF](https://arxiv.org/pdf/2609.39406)

