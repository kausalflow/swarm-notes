---
# CSL-compatible fields
title: "AlphaRJM: Reward-Jump Memory for Stochastic Return-Guided Alpha Discovery"
author:
  - literal: "Sayan Dhan"
  - literal: "Selvaraju Natarajan"
issued:
  date-parts:
    - [2026, 9, 8]
url: "https://arxiv.org/abs/2609.08581"

# Custom fields
paper_id: "2609.08581"
paper_source: "openalex"
domain: "finance"
tags:
  - "reinforcement-learning"
  - "forecasting"
  - "symbolic-search"
architectures:
  []
datasets:
  []
concept_slugs:
  - "reward-jump-memory"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-11T09:14:32Z"
created_at: "2026-09-11T09:14:32Z"
---

# AlphaRJM: Reward-Jump Memory for Stochastic Return-Guided Alpha Discovery

**Authors**: Sayan Dhan, Selvaraju Natarajan
**Date**: 2026-09-08
**Paper ID**: [openalex:2609.08581](https://arxiv.org/abs/2609.08581)

## Summary

AlphaRJM is introduced as a novel framework for formulaic alpha discovery that addresses delayed evaluation feedback in symbolic search through Reward-Jump Memory and an action-conditioned SDE return critic. The Reward-Jump Memory maintains an event-driven latent state updated exclusively at terminal evaluation events, while stochastic particles model future discounted discovery returns under a distributional Bellman objective. Empirical evaluations show that AlphaRJM achieves strong and stable performance gains across various equity universes and forecasting horizons.

## Key Contributions

- Introduces AlphaRJM, a framework for formulaic alpha discovery using Reward-Jump Memory and an action-conditioned SDE return critic.
- Addresses delayed feedback in symbolic search via an event-driven latent state that updates only at terminal evaluation events.
- Employs an action-conditioned SDE return critic with stochastic particles learned through a distributional Bellman objective combining energy-distance matching, mean calibration, and jump regularization.
- Demonstrates strong and stable empirical gains across multiple equity universes and forecasting horizons.

## Key Concepts

- [[reward-jump-memory]]: An event-driven latent state that remains fixed during token construction and updates at terminal evaluation events using realized pool rewards and evaluation outcomes.

## Archivist Review

Approved the core framework concept 'Reward-Jump Memory' because it offers a specific architectural mechanism for handling delayed feedback in symbolic search and formulaic alpha discovery. No datasets or open questions met the rigorous scarcity or naming criteria.

### Approved Concepts
- Reward-Jump Memory: Core architectural novelty proposed to handle delayed feedback in symbolic formulaic alpha discovery.

## Links

- [Abstract](https://arxiv.org/abs/2609.08581)
- [PDF](https://arxiv.org/pdf/2609.08581)

