---
# CSL-compatible fields
title: "Structured Frequency-Domain Evidence for LLM-Based Time-Series Anomaly Detection"
author:
  - literal: "Jungwook Seo"
  - literal: "Sangwon Son"
  - literal: "Minjeong Kim"
  - literal: "Seungmin Han"
  - literal: "Seojin Yoo"
  - literal: "Sungyong Baik"
issued:
  date-parts:
    - [2026, 8, 25]
url: "https://arxiv.org/abs/2608.24113"

# Custom fields
paper_id: "2608.24113"
paper_source: "openalex"
domain: "time-series"
tags:
  - "llm"
  - "time-series"
  - "anomaly-detection"
  - "zero-shot-learning"
  - "multimodal"
  - "benchmark"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "structured-frequency-domain-evidence"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-28T16:59:27Z"
created_at: "2026-08-28T16:59:27Z"
---

# Structured Frequency-Domain Evidence for LLM-Based Time-Series Anomaly Detection

**Authors**: Jungwook Seo, Sangwon Son, Minjeong Kim, Seungmin Han, Seojin Yoo, Sungyong Baik
**Date**: 2026-08-25
**Paper ID**: [openalex:2608.24113](https://arxiv.org/abs/2608.24113)

## Summary

This paper proposes an evidence-augmented zero-shot time-series anomaly detection framework that incorporates multi-resolution frequency-domain evidence computed via the Fast Fourier Transform to complement traditional time-domain inputs. By constructing global and local spectral evidence, the method captures both sequence-level periodic context and time-localized spectral departures. Evaluations across multiple advanced LLMs on AnomLLM and TSB-AD-U benchmarks demonstrate that explicit frequency-domain evidence improves zero-shot TSAD performance.

## Key Contributions

- Proposes an evidence-augmented zero-shot time-series anomaly detection (TSAD) framework that integrates structured frequency-domain evidence computed via FFT alongside time-domain inputs.
- Constructs evidence at two resolutions: global frequency-domain evidence summarizing sequence-level periodic context and local frequency-domain evidence capturing time-localized spectral departures.
- Evaluates across multiple leading LLMs (InternVL2-LLaMA3-76B, Qwen2.5-VL-72B-Instruct, Gemini-2.5-Flash, and GPT-4o) on the AnomLLM and TSB-AD-U benchmarks, demonstrating performance improvements over existing LLM-based TSAD baselines.

## Open Questions & Future Work

- [[interpreting-multimodal-evidence-llm-tsad]]

## Key Concepts

- [[structured-frequency-domain-evidence]]: A multi-resolution frequency-domain evidence augmentation method computed via Fast Fourier Transform to assist LLM-based time-series anomaly detection.

## Archivist Review

Approved the core conceptual contribution regarding structured multi-resolution frequency-domain evidence augmentation for LLM-based time-series tasks, along with an open question addressing multimodal evidence interpretation. Standard benchmarks such as TSB-AD-U were excluded per vault guidelines.

### Approved Concepts
- Structured Frequency-Domain Evidence: Introduces a novel multi-resolution frequency-domain evidence construction (global and local spectral context) to aid LLM-based time-series anomaly detection.

### Approved Open Questions
- Interpreting Multimodal Evidence in LLMs: Important for understanding the causal mechanisms and faithfulness of multimodal and evidence-augmented reasoning in time-series anomaly detection.

### Rejected Candidates
- [dataset] TSB-AD-U (`tsb-ad-u`) - not_reusable: Standard benchmark subset without a standalone permanent conceptual note required.

## Links

- [Abstract](https://arxiv.org/abs/2608.24113)
- [PDF](https://arxiv.org/pdf/2608.24113)

