---
# CSL-compatible fields
title: "Rehearse: Stepping Back from the Confidence Cliff in Self-Improving Autoresearch"
author:
  - literal: "Jiazhen Ji"
  - literal: "Shouhong Ding"
issued:
  date-parts:
    - [2026, 7, 30]
url: "https://arxiv.org/abs/2607.27687"

# Custom fields
paper_id: "2607.27687"
paper_source: "openalex"
domain: "nlp"
tags:
  - "agent"
  - "autonomous-agent"
  - "llm"
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
processed_at: "2026-08-02T07:27:15Z"
created_at: "2026-08-02T07:27:15Z"
---

# Rehearse: Stepping Back from the Confidence Cliff in Self-Improving Autoresearch

**Authors**: Jiazhen Ji, Shouhong Ding
**Date**: 2026-07-30
**Paper ID**: [openalex:2607.27687](https://arxiv.org/abs/2607.27687)

## Summary

The paper investigates pre-execution judgment reliability in self-improving machine-learning autoresearch loops and identifies a 'confidence cliff', where an LLM judge's selective accuracy sharply declines late in the iteration loop despite continued high confidence. To mitigate this, the authors propose Rehearse, a lightweight skill that equips autoresearch agents with a focused memory of similar past attempts and outcomes, successfully recovering late selective judgment accuracy and improving final performance across nanochat, image classification, and time-series forecasting benchmarks under fixed training-run budgets.

## Key Contributions

- Identifies the 'confidence cliff' phenomenon in self-improving autoresearch loops, where selective pre-execution judgment accuracy falls from 82.8% to 56.9% late in the loop.
- Introduces Rehearse, a lightweight autoresearch skill featuring focused memory of past similar attempts and outcomes.
- Demonstrates that Rehearse raises late selective accuracy to 83.5% and improves endpoint performance across nanochat, image classification, and time-series forecasting under fixed training budgets.

## Archivist Review

Both candidate items pertain to autonomous agent code search and software engineering iteration loops rather than time-series forecasting or statistical machine learning theory. In accordance with vault scoping, they were rejected as low impact for this repository.

### Rejected Candidates
- [concept] Rehearse (`rehearse`) - low_impact: This paper is about autonomous agent code optimization loops (autoresearch) rather than time-series forecasting, predictive modeling, or core ML methodology.
- [open_question] Stronger Retrieval Architectures for Autoresearch (`stronger-retrieval-architectures-autoresearch`) - low_impact: The open question is focused on software engineering agent loops and LLM code search rather than time-series or machine learning forecasting problems.

## Links

- [Abstract](https://arxiv.org/abs/2607.27687)
- [PDF](https://arxiv.org/pdf/2607.27687)

