---
# CSL-compatible fields
title: "Consensus Stability of Community Notes on X"
author:
  - literal: "Yuwei Chuai"
  - literal: "Gabriele Lenzini"
  - literal: "Nicolas Pröllochs"
issued:
  date-parts:
    - [2026, 4, 9]
url: "https://arxiv.org/abs/2601.14002"

# Custom fields
paper_id: "2601.14002"
paper_source: "openalex"
domain: "nlp"
tags:
  - "social-media"
  - "misinformation"
  - "fact-checking"
  - "moderation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-11T05:55:47Z"
created_at: "2026-04-11T05:55:47Z"
---

# Consensus Stability of Community Notes on X

**Authors**: Yuwei Chuai, Gabriele Lenzini, Nicolas Pröllochs
**Date**: 2026-04-09
**Paper ID**: [openalex:2601.14002](https://arxiv.org/abs/2601.14002)

## Summary

This paper investigates the long-term stability of community-based fact-checking systems, specifically Community Notes on X. By analyzing a large-scale dataset of ratings, the researchers demonstrate that notes are susceptible to post-display polarization, where rating behavior shifts significantly after a note becomes public. The findings show that this polarized feedback loop frequently causes notes to lose their helpful status and be removed, identifying a critical vulnerability in consensus-based moderation mechanisms.

## Key Contributions

- Empirical analysis of 437,396 Community Notes reveals that 30.2% of displayed notes eventually lose their helpful status and disappear.
- Evidence that note visibility triggers polarized rating dynamics, where users with viewpoints similar to the author reinforce the note, while dissimilar users increase negative ratings.
- Demonstration through counterfactual analysis that post-display polarization is a primary driver of note disappearance in consensus-based moderation systems.

## Open Questions & Future Work

- [[mechanisms-of-note-disappearance]]

## Archivist Review

I have approved the open question regarding note disappearance mechanisms as it identifies a clear, unresolved bottleneck in the design of consensus-based moderation systems. Other candidates were rejected because they described specific social behaviors or empirical findings that do not constitute reusable ML methodology or structural frameworks.

### Approved Open Questions
- Mechanisms of Note Disappearance: Distinguishing between organic disagreement and strategic manipulation is critical for designing more resilient moderation algorithms that can maintain high-quality fact-checking while resisting polarized or coordinated attacks.

### Rejected Candidates
- [concept] Post-display polarization (`post-display-polarization`) - generic: This is a descriptive behavioral phenomenon rather than a reusable algorithmic mechanism or technical framework.

## Links

- [Abstract](https://arxiv.org/abs/2601.14002)
- [PDF](https://arxiv.org/pdf/2601.14002)

