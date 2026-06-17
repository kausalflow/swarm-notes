---
# CSL-compatible fields
title: "Can LLM Coding Agents Reason About Time Series?"
author:
  - literal: "Filip Rechtorík"
  - literal: "Ondřej Dušek"
  - literal: "Zdeněk Kasner"
issued:
  date-parts:
    - [2026, 6, 15]
url: "https://arxiv.org/abs/2606.16545"

# Custom fields
paper_id: "2606.16545"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "agent"
  - "code-generation"
  - "time-series"
  - "benchmark"
  - "evaluation"
  - "reasoning"
  - "tool-use"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-17T09:25:25Z"
created_at: "2026-06-17T09:25:25Z"
---

# Can LLM Coding Agents Reason About Time Series?

**Authors**: Filip Rechtorík, Ondřej Dušek, Zdeněk Kasner
**Date**: 2026-06-15
**Paper ID**: [openalex:2606.16545](https://arxiv.org/abs/2606.16545)

## Summary

This paper investigates the effectiveness of LLM-based agents in analyzing time series data across three distinct interaction paradigms: raw data input, code-based querying, and hybrid approaches. Evaluation across two time series benchmarks indicates that code-access agents yield superior performance over raw numerical input, yet maintain a high error rate of 22-34%. The authors utilize an LLM judge to probe these failures, identifying that coding agents effectively automate statistical testing but frequently fail to capture contextual data nuances that raw data processing approaches manage through heuristic reasoning.

## Key Contributions

- Systematically evaluated LLM agents on time series analysis, comparing raw numerical input against iterative Python code-based query strategies.
- Demonstrated that coding agents outperform direct numerical input models by up to 10% on time series benchmarks, though significant reasoning gaps persist.
- Performed a qualitative analysis via a strong LLM judge to reveal that while coding agents excel at statistical test selection, they struggle with subtle interpretative nuances compared to raw data reasoning.

## Open Questions & Future Work

- [[complex-time-series-benchmarks-for-llm-agents]]
- [[multimodal-time-series-reasoning-for-agents]]

## Archivist Review

I reviewed the proposed concepts and open questions. No concepts were approved as the paper focuses on evaluation paradigms (coding agents vs numerical input) rather than proposing a new, reusable mechanism or method. The two open questions were approved as they identify substantial bottlenecks in benchmarking agentic time series reasoning and the potential integration of multimodal capabilities, which remain significant and unresolved areas of study in the field.

### Approved Open Questions
- Complex time series benchmarks for LLM agents: Developing more complex, realistic benchmarks is essential for determining if LLM agents can genuinely perform autonomous time series analysis in professional, open-world settings rather than just answering constrained exam questions.
- Multimodal time series reasoning for agents: Visual analysis is a core competency of human data analysts; if LLMs can effectively combine visual and numerical reasoning, it could significantly improve the robustness and interpretability of automated time series analysis.

### Rejected Candidates
- [open_question] Developing complex time series benchmarks (`complex-time-series-benchmarks`) - duplicate_existing: Renamed for clarity and uniqueness within the existing vault.
- [open_question] Multimodal time series reasoning (`multimodal-time-series-reasoning`) - duplicate_existing: Renamed for clarity and uniqueness within the existing vault.

## Links

- [Abstract](https://arxiv.org/abs/2606.16545)
- [PDF](https://arxiv.org/pdf/2606.16545)

