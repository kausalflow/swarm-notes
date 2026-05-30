---
# CSL-compatible fields
title: "Dr-CiK: A Testbed for Foresight-Driven Agents"
author:
  - literal: "Yihong Tang"
  - literal: "Andrew Williams"
  - literal: "Arjun Ashok"
  - literal: "Vincent Zhihao Zheng"
  - literal: "Lijun Sun"
  - literal: "Alexandre Drouin"
  - literal: "Issam H. Laradji"
  - literal: "Étienne Marcotte"
  - literal: "Valentina Zantedeschi"
issued:
  date-parts:
    - [2026, 5, 27]
url: "https://arxiv.org/abs/2605.27904"

# Custom fields
paper_id: "2605.27904"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "agent"
  - "retrieval-augmented-generation"
  - "benchmark"
architectures:
  []
datasets:
  - "drcik-benchmark"
concept_slugs:
  - "drcik-benchmark"
dataset_slugs:
  - "drcik-benchmark"
skill: "TimeSeriesSkill"
processed_at: "2026-05-30T07:36:23Z"
created_at: "2026-05-30T07:36:23Z"
---

# Dr-CiK: A Testbed for Foresight-Driven Agents

**Authors**: Yihong Tang, Andrew Williams, Arjun Ashok, Vincent Zhihao Zheng, Lijun Sun, Alexandre Drouin, Issam H. Laradji, Étienne Marcotte, Valentina Zantedeschi
**Date**: 2026-05-27
**Paper ID**: [openalex:2605.27904](https://arxiv.org/abs/2605.27904)

## Summary

Dr-CiK is a novel benchmark designed to evaluate agents' ability to discover, filter, and integrate external, noisy context for time-series forecasting. By requiring agents to navigate document corpora to find relevant evidence, the benchmark bridges the gap between passive forecasting models and active information-seeking agents. Empirical evaluation reveals that current research agents exhibit poor performance, frequently failing to identify ground-truth evidence and suffering from distractor interference, which highlights a critical need for more robust, foresight-driven retrieval architectures.

## Key Contributions

- Introduces Dr-CiK, a comprehensive benchmark designed to evaluate agentic capabilities in retrieving and distilling external context for time-series forecasting.
- Demonstrates that current deep research agents struggle with context-aided forecasting, retrieving less than 5% of ground-truth evidence while being highly susceptible to distractor noise.
- Establishes that without specialized foresight-driven architectures, retrieved context often degrades, rather than improves, forecasting accuracy.

## Open Questions & Future Work

- [[foresight-driven-retrieval-robustness]]

## Key Concepts

- [[drcik-benchmark]]: A benchmark for evaluating agentic abilities to retrieve, filter, and synthesize forecasting-relevant context from external document corpora.

## Archivist Review

I approved the Dr-CiK benchmark as a concept and dataset because it shifts the focus of time-series evaluation from passive model-based forecasting to active, agentic information-seeking. I also identified an open question regarding retrieval robustness, which addresses the paper's central finding that current agents are easily misled by noise and distractors during the retrieval process. The review followed strict scarcity constraints, focusing only on the core contributions of this specific testbed.

### Approved Concepts
- Dr-CiK Benchmark: It establishes a new paradigm for evaluating agents on their ability to retrieve and synthesize forecasting context from external sources rather than assuming context is pre-provided.

### Approved Open Questions
- Foresight-Driven Retrieval Robustness: This is a fundamental challenge for the development of autonomous agents capable of performing reliable, context-aware forecasting in real-world scenarios.

## Datasets

- [[drcik-benchmark]]

## Links

- [Abstract](https://arxiv.org/abs/2605.27904)
- [PDF](https://arxiv.org/pdf/2605.27904)

