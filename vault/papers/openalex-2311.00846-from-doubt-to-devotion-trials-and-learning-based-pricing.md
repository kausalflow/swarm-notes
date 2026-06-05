---
# CSL-compatible fields
title: "From Doubt to Devotion: Trials and Learning-Based Pricing"
author:
  - literal: "Tan Gan"
  - literal: "Nicholas C. Wu"
issued:
  date-parts:
    - [2026, 6, 2]
url: "https://arxiv.org/abs/2311.00846"

# Custom fields
paper_id: "2311.00846"
paper_source: "openalex"
domain: "finance"
tags:
  - "reinforcement-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-05T08:39:42Z"
created_at: "2026-06-05T08:39:42Z"
---

# From Doubt to Devotion: Trials and Learning-Based Pricing

**Authors**: Tan Gan, Nicholas C. Wu
**Date**: 2026-06-02
**Paper ID**: [openalex:2311.00846](https://arxiv.org/abs/2311.00846)

## Summary

This paper explores dynamic mechanism design for selling experience goods where an informed seller holds partial information about product match quality. The analysis reveals that the disparity in beliefs between the seller and the buyer, combined with the buyer's active learning, naturally incentivizes trial-based or tiered pricing strategies. A significant finding is that contrary to common intuition, access to more consumer data may lower equilibrium revenue because sellers use that information to over-optimize the mechanism relative to the buyer's learning process.

## Key Contributions

- Characterizes equilibrium mechanisms for dynamic informed principal problems in the context of experience goods.
- Demonstrates that a belief gap between sellers and buyers leads to trial-based or tiered pricing models observed in digital markets.
- Establishes the counterintuitive finding that consumer data access can decrease seller revenue by enabling precise calibration of the seller's dynamic screening mechanism against buyer learning.

## Open Questions & Future Work

- [[tractability-of-non-poisson-learning-in-informed-principal-models]]
- [[dynamic-mechanisms-for-bad-news-learning]]

## Archivist Review

The paper provides an economic analysis of dynamic mechanism design rather than a time-series forecasting algorithm. Consequently, no new forecasting concepts are identified as novel or reusable. The open questions regarding the tractability of informed principal problems with non-Poisson or bad-news learning structures were approved as they address fundamental methodological challenges in dynamic mechanism design.

### Approved Open Questions
- Tractability of General Learning Models: This is a fundamental methodological bottleneck in mechanism design for experience goods, determining whether 'trials' are a robust phenomenon or a specific artifact of Poisson information structures.
- Mechanisms for Bad News Learning: Many experience goods reveal information through negative experiences, making understanding bad news mechanisms essential for the broader applicability of the theory.

## Links

- [Abstract](https://arxiv.org/abs/2311.00846)
- [PDF](https://arxiv.org/pdf/2311.00846)

