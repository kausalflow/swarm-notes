---
# CSL-compatible fields
title: "On Subquadratic Architectures: From Applications to Principles"
author:
  - literal: "Anamaria-Roberta Hartl"
  - literal: "Levente Zólyomi"
  - literal: "David Stap"
  - literal: "Pieter-Jan Hoedt"
  - literal: "Niklas Schmidinger"
  - literal: "Lukas Hauzenberger"
  - literal: "Sebastian Böck"
  - literal: "Günter Klambauer"
  - literal: "Sepp Hochreiter"
issued:
  date-parts:
    - [2026, 6, 10]
url: "https://arxiv.org/abs/2606.12364"

# Custom fields
paper_id: "2606.12364"
paper_source: "openalex"
domain: "nlp"
tags:
  - "transformer"
  - "llm"
  - "language-model"
  - "time-series"
  - "mamba"
  - "code-generation"
architectures:
  - "mamba"
datasets:
  []
concept_slugs:
  - "xlstm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-13T08:16:57Z"
created_at: "2026-06-13T08:16:57Z"
---

# On Subquadratic Architectures: From Applications to Principles

**Authors**: Anamaria-Roberta Hartl, Levente Zólyomi, David Stap, Pieter-Jan Hoedt, Niklas Schmidinger, Lukas Hauzenberger, Sebastian Böck, Günter Klambauer, Sepp Hochreiter
**Date**: 2026-06-10
**Paper ID**: [openalex:2606.12364](https://arxiv.org/abs/2606.12364)

## Summary

This paper systematically evaluates the efficacy of leading subquadratic architectures—xLSTM, Mamba-2, and Gated DeltaNet—across code pre-training, distillation, and time-series foundation modeling. While all offer scaling advantages over standard Transformers, xLSTM demonstrates the strongest performance in capturing complex long-range dependencies. The authors attribute this advantage to xLSTM's unique gating mechanism, which enables more robust and flexible memory state updates. Controlled synthetic experiments confirm that these architectural gains are directly linked to superior state tracking and accumulation capabilities.

## Key Contributions

- Performs a systematic empirical comparison of xLSTM, Mamba-2, and Gated DeltaNet across code generation and time-series foundation modeling tasks.
- Identifies xLSTM as the superior architecture for complex dependency modeling due to its flexible gating and stable memory correction.
- Provides a unified theoretical formulation for xLSTM to isolate the impact of state tracking and memory dynamics on performance.

## Open Questions & Future Work

- [[scaling-subquadratic-architectures]]

## Key Concepts

- [[xlstm]]: An efficient, subquadratic sequence model architecture that leverages advanced gating and memory correction mechanisms.

## Archivist Review

The paper provides a rigorous empirical comparison of prominent subquadratic architectures. I approved the 'xLSTM' concept as it represents the central architectural innovation being evaluated. I also approved the open question regarding the scaling of subquadratic architectures to highlight the necessity of understanding these models beyond the specific study parameters. Other architectures mentioned were rejected to adhere to the scarcity policy.

### Approved Concepts
- xLSTM: xLSTM is identified as the best-performing architecture among leading subquadratic alternatives for complex sequence tasks.

### Approved Open Questions
- Scaling Subquadratic Architectures: Understanding the scaling behavior and robustness of these architectures across different environments is critical for their adoption as practical, general-purpose replacements for Transformers in foundation models.

### Rejected Candidates
- [concept] Mamba-2 (`mamba-2`) - not_novel: This is a specific model architecture variant that functions as an alternative to xLSTM rather than a fundamental, reusable conceptual contribution defined in this paper.
- [concept] Gated DeltaNet (`gated-deltanet`) - not_novel: This is a specific model architecture variant that functions as an alternative to xLSTM rather than a fundamental, reusable conceptual contribution defined in this paper.

## Links

- [Abstract](https://arxiv.org/abs/2606.12364)
- [PDF](https://arxiv.org/pdf/2606.12364)

