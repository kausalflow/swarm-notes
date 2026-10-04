---
# CSL-compatible fields
title: "Do Your Own Research: Learning to Forecast by Learning to Search"
author:
  - literal: "Yusuf Afifi"
  - literal: "Artur Kiulian"
  - literal: "Anton Polishko"
  - literal: "Mykola Khandoga"
  - literal: "Hamudi Naanaa"
  - literal: "Alina Krasnobrizha"
issued:
  date-parts:
    - [2026, 10, 1]
url: "https://arxiv.org/abs/2610.01955"

# Custom fields
paper_id: "2610.01955"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "reinforcement-learning"
  - "agent"
  - "autonomous-agent"
  - "reasoning"
  - "forecasting"
  - "evaluation"
  - "benchmark"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-04T10:48:35Z"
created_at: "2026-10-04T10:48:35Z"
---

# Do Your Own Research: Learning to Forecast by Learning to Search

**Authors**: Yusuf Afifi, Artur Kiulian, Anton Polishko, Mykola Khandoga, Hamudi Naanaa, Alina Krasnobrizha
**Date**: 2026-10-01
**Paper ID**: [openalex:2610.01955](https://arxiv.org/abs/2610.01955)

## Summary

This paper presents an agentic forecasting framework where language models learn to gather evidence via web search, page reading, and financial time series analysis under leak filtering constraints. By training Qwen3.5-35B-A3B using single-epoch GRPO with a Brier-score reward on over 2,100 resolved Polymarket questions, the model improves calibration by 30-40% and reduces inefficient search steps. Evaluated against frontier models, the trained agent outperforms Claude Opus 4.5 on evidence-based forecasting at a fraction of the inference cost, especially on high-uncertainty questions.

## Key Contributions

- Introduces an agentic forecasting environment and dataset of 2,100+ resolved Polymarket questions with leak filtering for rigorous temporal evaluation.
- Trains Qwen3.5-35B-A3B via outcome-based reinforcement learning (GRPO under Brier-score reward) to dynamically acquire evidence at rollout time.
- Demonstrates a 30-40% improvement in calibration and a reduction in redundant search attempts from 3.8 to 2.25 per rollout.
- Achieves superior evidence-based forecasting performance compared to frontier models including Claude Opus 4.5 at ~5% of the inference cost on a 265-question evaluation set.

## Limitations

Limited to the specified active parameter scale and evaluated primarily on Polymarket prediction markets.

## Archivist Review

No new concepts or open questions met the stringent inclusion threshold for permanent vault notes, as the submission primarily discusses an application of existing outcome-based RL (GRPO) and tool use to prediction markets.

### Rejected Candidates
- [open_question] Categorical Outcome Forecasting Environments (`categorical-outcome-forecasting`) - low_impact: The prompt notes that outcome forecasting environments should be extended to categorical outcomes, but this is a straightforward extension rather than a fundamental bottleneck or architectural research question.
- [open_question] Expanding Agent Action Space (`quantitative-model-action-space`) - low_impact: Expanding agent action spaces to include sandboxed quantitative models is a standard agentic development direction rather than a profound open theoretical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.01955)
- [PDF](https://arxiv.org/pdf/2610.01955)

