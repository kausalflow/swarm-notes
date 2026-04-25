---
# CSL-compatible fields
title: "Markov reads Pushkin, again: A statistical journey into the poetic world of Evgenij Onegin"
author:
  - literal: "Angelo Maria Sabatini"
issued:
  date-parts:
    - [2026, 4, 22]
url: "https://arxiv.org/abs/2604.20221"

# Custom fields
paper_id: "2604.20221"
paper_source: "openalex"
domain: "nlp"
tags:
  - "language-model"
  - "autoregressive"
  - "embedding"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-25T06:16:24Z"
created_at: "2026-04-25T06:16:24Z"
---

# Markov reads Pushkin, again: A statistical journey into the poetic world of Evgenij Onegin

**Authors**: Angelo Maria Sabatini
**Date**: 2026-04-22
**Paper ID**: [openalex:2604.20221](https://arxiv.org/abs/2604.20221)

## Summary

This study revisits the application of Markovian modeling to literary analysis by encoding the phonological structure of Pushkin's Eugene Onegin into binary vowel/consonant (V/C) sequences. The paper shows that a compact four-state Markov model can effectively capture local dependencies and large-scale sequential patterns, revealing distinct memory depth profiles when comparing the original text to an Italian translation. Additionally, the author introduces phonological probes to bridge the gap between graphemic structure and thematic development, providing a framework for comparative poetics through simplified linguistic representations.

## Key Contributions

- Applies minimalist four-state Markov chain modeling to phonological V/C sequences of Eugene Onegin.
- Demonstrates that binary V/C encoding captures essential structural features like autocorrelation and memory depth in poetic text.
- Identifies structural divergence between Russian original and Italian translation via phonological probes linked to narrative-relevant cues.

## Open Questions & Future Work

- [[integrating-semantic-modeling-with-symbolic-time-series]]

## Archivist Review

The paper applies Markov modeling to a niche literary domain, which is inherently exploratory and distant from the core forecasting mechanisms of interest. I approved the proposed open question as it identifies a critical bottleneck in bridging surface-level symbolic statistics with semantic narrative depth, which is a relevant challenge in sequence modeling. I rejected the concept candidates as they describe domain-specific feature engineering rather than reusable methodological contributions.

### Approved Open Questions
- Integrating Semantic Modeling with Symbolic Time-Series: This represents the primary methodological transition from surface-level symbolic/graphemic modeling to semantic/thematic modeling, which is the most significant unresolved challenge in using statistical models for literary analysis.

### Rejected Candidates
- [concept] Phonological Probes (`phonological-probes`) - paper_local: This is a paper-local tool for tracking specific linguistic patterns rather than a broad, reusable forecasting or ML mechanism.
- [concept] Binary Vowel/Consonant Encoding (`binary-v-c-encoding`) - not_reusable: A specific encoding scheme for poetic text is too narrow to be considered a general-purpose concept in time-series forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2604.20221)
- [PDF](https://arxiv.org/pdf/2604.20221)

