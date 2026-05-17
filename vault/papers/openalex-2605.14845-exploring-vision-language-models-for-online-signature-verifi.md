---
# CSL-compatible fields
title: "Exploring Vision-Language Models for Online Signature Verification: A Zero-Shot Capability Study"
author:
  - literal: "Marta Robledo-Moreno"
  - literal: "Ruben Vera-Rodriguez"
  - literal: "Ruben Tolosana"
  - literal: "Javier Ortega-García"
issued:
  date-parts:
    - [2026, 5, 14]
url: "https://arxiv.org/abs/2605.14845"

# Custom fields
paper_id: "2605.14845"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "vision-language-model"
  - "zero-shot-learning"
  - "chain-of-thought"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "rationalization-trap"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-17T07:31:44Z"
created_at: "2026-05-17T07:31:44Z"
---

# Exploring Vision-Language Models for Online Signature Verification: A Zero-Shot Capability Study

**Authors**: Marta Robledo-Moreno, Ruben Vera-Rodriguez, Ruben Tolosana, Javier Ortega-García
**Date**: 2026-05-14
**Paper ID**: [openalex:2605.14845](https://arxiv.org/abs/2605.14845)

## Summary

This study investigates the zero-shot capabilities of advanced vision-language models (VLMs) for online signature verification by converting kinematic time-series data into static images. The authors introduce a scoring protocol based on latent token probabilities and evaluate performance on the Signature Verification Challenge (SVC) benchmark. Findings show exceptional performance in random forgery scenarios, but highlight a critical 'Rationalization Trap' in skilled forgery detection where Chain-of-Thought reasoning leads to performance degradation via kinematic hallucinations.

## Key Contributions

- Evaluates zero-shot performance of GPT-5.2 and Gemini 2.5 Pro on the SVC benchmark using a kinematic-to-image conversion method.
- Establishes a scoring protocol based on latent token probabilities for biometric verification tasks.
- Identifies the 'Rationalization Trap', where Chain-of-Thought reasoning creates kinematic hallucinations in skilled forgery detection.

## Open Questions & Future Work

- [[vlm-forensic-hallucination-mitigation]]

## Key Concepts

- [[rationalization-trap]]: A phenomenon where chain-of-thought reasoning in VLMs generates false justifications for biometric or structural artifacts, leading to performance degradation in high-precision tasks.

## Archivist Review

I approved the 'Rationalization Trap' as it identifies a critical, reusable failure mode in multimodal reasoning systems. The open question regarding forensic hallucinations was approved to track the research challenge of mitigating these structural errors in high-stakes settings. I rejected the SVC dataset as it is a specialized benchmark rather than a broadly foundational dataset.

### Approved Concepts
- Rationalization Trap: It identifies a novel failure mode in VLMs where internal reasoning mechanisms introduce errors during sensitive verification tasks.

### Approved Open Questions
- Mitigating VLM Forensic Hallucinations: The Rationalization Trap represents a significant barrier to using VLMs for reliable decision-making where internal reasoning transparency and factual accuracy are mandatory.

### Rejected Candidates
- [dataset] Signature Verification Challenge (SVC) (`Signature Verification Challenge (SVC)`) - low_impact: This is a benchmark dataset specific to the task of signature verification and does not qualify as a broad, critical dataset for the ML knowledge vault.

## Links

- [Abstract](https://arxiv.org/abs/2605.14845)
- [PDF](https://arxiv.org/pdf/2605.14845)

