---
# CSL-compatible fields
title: "CausalMoE: A Billion-Scale Multimodal Foundation Model for Granger Causal Discovery with Pattern-Routed Heterogeneous Experts"
author:
  - literal: "Bo Liu"
  - literal: "Di Dai"
  - literal: "Jingwei Liu"
  - literal: "Jiarui Jin"
  - literal: "Xiaocheng Fang"
  - literal: "Guangkun Nie"
  - literal: "Hongyan Li"
  - literal: "Shenda Hong"
issued:
  date-parts:
    - [2026, 6, 11]
url: "https://arxiv.org/abs/2606.13024"

# Custom fields
paper_id: "2606.13024"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "multimodal"
  - "vision-language-model"
  - "time-series"
  - "mixture-of-experts"
  - "attention-mechanism"
architectures:
  []
datasets:
  []
concept_slugs:
  - "pattern-routed-mixture-of-heterogeneous-experts"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-14T08:39:18Z"
created_at: "2026-06-14T08:39:18Z"
---

# CausalMoE: A Billion-Scale Multimodal Foundation Model for Granger Causal Discovery with Pattern-Routed Heterogeneous Experts

**Authors**: Bo Liu, Di Dai, Jingwei Liu, Jiarui Jin, Xiaocheng Fang, Guangkun Nie, Hongyan Li, Shenda Hong
**Date**: 2026-06-11
**Paper ID**: [openalex:2606.13024](https://arxiv.org/abs/2606.13024)

## Summary

CausalMoE is a billion-scale multimodal foundation model designed to overcome the limitations of "one-size-fits-all" neural Granger causal discovery (GCD) methods. The model utilizes a novel pattern-routed mixture of heterogeneous experts to dynamically route temporal patches, effectively separating regime-specific mechanisms from general dynamics. By integrating multimodal priors from LLMs and VLMs and employing a causality-aware self-attention mechanism, CausalMoE achieves robust and interpretable sparse causal graph recovery, even under distribution shifts and few-shot scenarios.

## Key Contributions

- Introduces CausalMoE, a billion-scale multimodal foundation model for Granger causal discovery that uses patch-level routing to handle system heterogeneity.
- Implements a pattern-routed mixture-of-experts (MoE) architecture that dynamically decouples regime-specific causal mechanisms from shared system dynamics.
- Integrates LLM and VLM priors to regularize causal estimation and demonstrates state-of-the-art performance on supervised GCD benchmarks and few-shot generalization.

## Open Questions & Future Work

- [[gcd-to-interventional-causality-gap]]
- [[causal-foundation-model-auditability]]

## Key Concepts

- [[pattern-routed-mixture-of-heterogeneous-experts]]: A routing mechanism that dynamically assigns time-series patches to specialized experts to disentangle regime-specific mechanisms from shared dynamics.

## Archivist Review

I approved the core architectural concept of Pattern-Routed Mixture of Heterogeneous Experts as a reusable approach for handling non-stationary time series dynamics. I also approved two fundamental open questions regarding the theoretical limitations of Granger causal discovery frameworks compared to interventional modeling and the critical issue of benchmark leakage in large-scale causal foundation models. No datasets were approved as none were specifically central to the novelty beyond standard benchmark usage.

### Approved Concepts
- Pattern-Routed Mixture of Heterogeneous Experts: Core mechanism for addressing temporal distribution shifts and regime changes in Granger causal discovery by decoupling regime-specific mechanisms.

### Approved Open Questions
- Predictive vs. Interventional Causality: Moving from predictive dependency to interventional causality is critical for real-world decision-making and scientific discovery, as predictive methods often fail to guide effective interventions when confounders are present.
- Auditability and Benchmark Leakage: Benchmark leakage undermines the scientific validity of foundation models in causal discovery tasks, necessitating reliable probing and counterfactual testing methodologies.

## Links

- [Abstract](https://arxiv.org/abs/2606.13024)
- [PDF](https://arxiv.org/pdf/2606.13024)

