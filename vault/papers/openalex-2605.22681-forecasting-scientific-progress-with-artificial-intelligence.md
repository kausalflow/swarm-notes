---
# CSL-compatible fields
title: "Forecasting Scientific Progress with Artificial Intelligence"
author:
  - literal: "Sean Wu"
  - literal: "Pan Lu"
  - literal: "Yupeng Chen"
  - literal: "Jonathan Bragg"
  - literal: "Yutaro Yamada"
  - literal: "Peter Clark"
  - literal: "David Clifton"
  - literal: "Philip Torr"
  - literal: "James Zou"
  - literal: "Junchi Yu"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.22681"

# Custom fields
paper_id: "2605.22681"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "benchmark"
  - "evaluation"
  - "reasoning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "cusp-benchmark"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:46:23Z"
created_at: "2026-05-24T07:46:23Z"
---

# Forecasting Scientific Progress with Artificial Intelligence

**Authors**: Sean Wu, Pan Lu, Yupeng Chen, Jonathan Bragg, Yutaro Yamada, Peter Clark, David Clifton, Philip Torr, James Zou, Junchi Yu
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.22681](https://arxiv.org/abs/2605.22681)

## Summary

This paper investigates the capacity of frontier AI systems to predict scientific progress using a new benchmark, CUSP (Cutoff-conditioned Unseen Scientific Progress). The evaluation across 4,760 scientific events reveals that current models systematically struggle with predicting the realization and timing of scientific breakthroughs, demonstrating high overconfidence and strong domain-dependent performance gaps. Crucially, the authors show that these failures persist regardless of knowledge exposure relative to training cutoffs, indicating that the limitations are rooted in poor predictive reasoning rather than simply a lack of historical data.

## Key Contributions

- Introduces CUSP, a multi-disciplinary, event-level benchmark comprising 4,760 scientific events for assessing AI forecasting capabilities.
- Demonstrates that current frontier models exhibit systematic limitations, failing to reliably predict the occurrence or timing of scientific advances despite possessing pre-cutoff knowledge.
- Identifies significant heterogeneity in forecasting performance across scientific domains, with AI progress being more predictable than developments in biology, chemistry, and physics.
- Reveals that model performance is largely insensitive to training data cutoffs and characterized by overconfidence, suggesting fundamental reasoning failures rather than mere data limitations.

## Key Concepts

- [[cusp-benchmark]]: A temporally grounded benchmark for evaluating the ability of AI systems to forecast scientific progress through feasibility assessment, mechanistic reasoning, and temporal prediction.

## Archivist Review

The paper introduces a structured evaluation framework for forecasting scientific progress. I approved the CUSP benchmark as a standalone concept because it provides a rigorous, reusable methodology for assessing predictive reasoning in scientific domains, which is distinct from generic forecasting benchmarks. No other concepts or datasets met the strict novelty and reusability requirements for the vault.

### Approved Concepts
- CUSP (Cutoff-conditioned Unseen Scientific Progress): It is the core evaluation framework introduced by the paper to test AI systems on their ability to forecast scientific milestones under controlled conditions.

## Links

- [Abstract](https://arxiv.org/abs/2605.22681)
- [PDF](https://arxiv.org/pdf/2605.22681)

