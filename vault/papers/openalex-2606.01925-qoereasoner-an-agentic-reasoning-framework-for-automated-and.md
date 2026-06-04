---
# CSL-compatible fields
title: "QoEReasoner: An Agentic Reasoning Framework for Automated and Explainable QoE Diagnosis in RANs"
author:
  - literal: "Qizhe Li"
  - literal: "Haolong Chen"
  - literal: "Shan Dai"
  - literal: "Zhuo Li"
  - literal: "Zhiwei Hu"
  - literal: "Xuan Li"
  - literal: "Guangxu Zhu"
  - literal: "Qingjiang Shi"
issued:
  date-parts:
    - [2026, 6, 1]
url: "https://arxiv.org/abs/2606.01925"

# Custom fields
paper_id: "2606.01925"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "agent"
  - "autonomous-agent"
  - "tool-use"
  - "explainability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "qoereasoner"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-04T08:46:36Z"
created_at: "2026-06-04T08:46:36Z"
---

# QoEReasoner: An Agentic Reasoning Framework for Automated and Explainable QoE Diagnosis in RANs

**Authors**: Qizhe Li, Haolong Chen, Shan Dai, Zhuo Li, Zhiwei Hu, Xuan Li, Guangxu Zhu, Qingjiang Shi
**Date**: 2026-06-01
**Paper ID**: [openalex:2606.01925](https://arxiv.org/abs/2606.01925)

## Summary

QoEReasoner addresses the limitations of Large Language Models in network troubleshooting, such as poor time-series analysis and causal hallucination, by grounding agentic reasoning in physical network realities. The framework utilizes a stateful central planner to orchestrate deterministic KPI analysis, domain-consistent fault propagation, and historical evidence retrieval. Evaluated on operational RAN datasets, the system demonstrates superior accuracy and significant efficiency gains, providing interpretable, expert-grade diagnostic reports.

## Key Contributions

- Introduced QoEReasoner, an agentic framework that integrates deterministic tools, domain-specific knowledge bases, and historical case banks to automate RAN QoE diagnosis.
- Achieved an 18%-40% accuracy improvement over existing diagnostic baselines on real-world RAN telemetry.
- Reduced expert diagnostic time from approximately 30 minutes to 3 minutes per session while maintaining robust interpretability.

## Open Questions & Future Work

- [[multi-chain-fault-diagnosis]]

## Key Concepts

- [[qoereasoner]]: An LLM-driven agentic system that uses deterministic tools and domain-specific knowledge to automate and explain QoE diagnosis in radio access networks.

## Archivist Review

I approved the QoEReasoner framework as a representative of domain-grounded agentic systems for time-series diagnostics and the open question regarding multi-chain fault diagnosis because it addresses a fundamental limitation in current automated root-cause analysis. I rejected no candidates because only one concept and one question were provided, both of which meet the criteria for permanence and reusability.

### Approved Concepts
- QoEReasoner: Central agentic framework proposed for automating network troubleshooting by grounding LLM reasoning in physical network constraints.

### Approved Open Questions
- Multi-chain Fault Causal Diagnosis: Moving beyond single-chain diagnosis is essential for increasing the diagnostic accuracy and comprehensiveness of AI agents in highly dynamic and complex 6G or O-RAN environments where multiple, interleaved root causes are common.

## Links

- [Abstract](https://arxiv.org/abs/2606.01925)
- [PDF](https://arxiv.org/pdf/2606.01925)

