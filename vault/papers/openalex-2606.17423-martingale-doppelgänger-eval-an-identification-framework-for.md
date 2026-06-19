---
# CSL-compatible fields
title: "Martingale Doppelgänger-Eval: An Identification Framework for Auditing Candlestick Understanding in Vision-Language Models"
author:
  - literal: "Ziyao Wang"
issued:
  date-parts:
    - [2026, 6, 16]
url: "https://arxiv.org/abs/2606.17423"

# Custom fields
paper_id: "2606.17423"
paper_source: "openalex"
domain: "finance"
tags:
  - "multimodal"
  - "vision-language-model"
  - "time-series"
  - "benchmark"
  - "evaluation"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "martingale-doppelganger-eval"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-19T09:26:17Z"
created_at: "2026-06-19T09:26:17Z"
---

# Martingale Doppelgänger-Eval: An Identification Framework for Auditing Candlestick Understanding in Vision-Language Models

**Authors**: Ziyao Wang
**Date**: 2026-06-16
**Paper ID**: [openalex:2606.17423](https://arxiv.org/abs/2606.17423)

## Summary

This paper presents Martingale Doppelgänger-Eval, a benchmark designed to audit whether vision-language models (VLMs) actually process candlestick chart evidence or merely rely on trend-following shortcuts. By employing formal intervention methods—such as martingale-null markets and counterfactual trend swaps—the authors prove that observational evaluation fails to differentiate between grounded and shortcut-based reasoning. Experimental results on frozen commercial and open-source models reveal a critical failure mode: these models often ignore specific visual evidence in favor of past trend patterns. The framework provides a reusable template for evaluating visual grounding in complex time-series imagery.

## Key Contributions

- Introduces the Martingale Doppelgänger-Eval benchmark, which utilizes controlled interventions (martingale-null, injected-alpha, trend-label swaps) to isolate visual grounding in financial chart analysis.
- Proves formally that observational benchmarks fail to distinguish between grounded reasoning and trend-shortcut heuristics in financial time-series imagery.
- Demonstrates that current frozen VLMs exhibit significant bias toward past trend extrapolation while failing to rely on candlestick evidence.

## Open Questions & Future Work

- [[causal-audit-generalization-and-robustness]]

## Key Concepts

- [[martingale-doppelganger-eval]]: A shadow-market benchmark and auditing framework for evaluating visual grounding of candlestick patterns in vision-language models.

## Archivist Review

The approved concept and open question establish a rigorous framework for auditing vision-language models on time-series imagery by replacing observational evaluation with interventional causal identification. This methodology addresses the fundamental ambiguity between visual grounding and trend extrapolation, which is a major, reusable challenge in multimodal time-series analysis. No datasets were approved as the benchmark itself is a methodology rather than a static data collection, and it avoids duplicative entries.

### Approved Concepts
- Martingale Doppelgänger-Eval: Provides a novel, intervention-based audit framework for testing visual grounding in financial chart analysis, addressing limitations of traditional observational benchmarks.

### Approved Open Questions
- Generalizing Causal Audit Frameworks: The current benchmark is limited by potential reliance on synthetic artifacts; developing more robust methods for removing or accounting for these artifacts is essential for reliable evaluation. Additionally, extending this framework to other time-series domains is critical for broadening the impact of causal identification in multimodal auditing.

## Links

- [Abstract](https://arxiv.org/abs/2606.17423)
- [PDF](https://arxiv.org/pdf/2606.17423)

