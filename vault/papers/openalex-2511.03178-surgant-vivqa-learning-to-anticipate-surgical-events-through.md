---
# CSL-compatible fields
title: "SurgAnt-ViVQA: learning to anticipate surgical events through GRU-driven temporal cross-attention"
author:
  - literal: "Shreyas C. Dhake"
  - literal: "Jiayuan Huang"
  - literal: "Runlong He"
  - literal: "Danyal Z. Khan"
  - literal: "Evangelos B. Mazomenos"
  - literal: "Sophia Bano"
  - literal: "Hani J. Marcus"
  - literal: "Danail Stoyanov"
  - literal: "Matthew J. Clarkson"
  - literal: "Mobarak I. Hoque"
issued:
  date-parts:
    - [2026, 8, 26]
url: "https://arxiv.org/abs/2511.03178"

# Custom fields
paper_id: "2511.03178"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "vision-language-modelvlm"
  - "video-language-model"
  - "question-answering"
  - "parameter-efficient-fine-tuning"
  - "peft"
  - "gru"
  - "attention-mechanism"
  - "dataset"
  - "benchmark"
architectures:
  - "encoder-decoder"
datasets:
  - "pitvqa-anticipation"
concept_slugs:
  []
dataset_slugs:
  - "pitvqa-anticipation"
skill: "TimeSeriesSkill"
processed_at: "2026-08-29T11:24:08Z"
created_at: "2026-08-29T11:24:08Z"
---

# SurgAnt-ViVQA: learning to anticipate surgical events through GRU-driven temporal cross-attention

**Authors**: Shreyas C. Dhake, Jiayuan Huang, Runlong He, Danyal Z. Khan, Evangelos B. Mazomenos, Sophia Bano, Hani J. Marcus, Danail Stoyanov, Matthew J. Clarkson, Mobarak I. Hoque
**Date**: 2026-08-26
**Paper ID**: [openalex:2511.03178](https://arxiv.org/abs/2511.03178)

## Summary

SurgAnt-ViVQA is a video-language model designed to anticipate future surgical events (such as phases, steps, instruments, and remaining duration) in endonasal transsphenoidal pituitary surgery. It introduces the PitVQA-Anticipation dataset and combines a bidirectional GRU with an adaptive gate for token-level temporal cross-attention to inject visual dynamics into a parameter-efficiently fine-tuned language backbone. Experimental results show significant improvements over existing image and video-based VQA baselines on both PitVQA-Anticipation and the EndoVis18-VQA benchmark.

## Key Contributions

- Introduces PitVQA-Anticipation, a surgical VQA dataset comprising 33.5 hours of video and over 734k QA pairs for forward-looking reasoning across phase prediction, step forecasting, instrument anticipation, and duration estimation.
- Proposes SurgAnt-ViVQA, a video-language model featuring a bidirectional GRU and an adaptive gate for token-level temporal cross-attention to anticipate surgical events.
- Demonstrates superior performance over image and video baselines on PitVQA-Anticipation (achieving BLEU-4 72.38, ROUGE-L 84.94, METEOR 87.05) and successful zero-shot/transfer generalization to EndoVis18-VQA.

## Limitations

Prospective clinical utility requires further validation with surgeons and operating-room staff, and further controlled experiments are required to fully disentangle the independent contributions of recurrence and adaptive gating.

## Open Questions & Future Work

- [[generalizing-surgical-anticipatory-vqa]]

## Archivist Review

Applied high selectivity guidelines. Rejected the domain-specific VLGRU architecture concept as paper-local, but approved the primary surgical VQA dataset as a valuable benchmark and the open question regarding surgical anticipatory VQA generalization.

### Approved Open Questions
- Generalizing Surgical Anticipatory VQA: Important for generalizing anticipatory vision-language models beyond single-procedure datasets and verifying cross-specialty robustness in real-time medical assistance.

### Rejected Candidates
- [concept] SurgAnt-ViVQA (`surgant-vivqa`) - paper_local: Paper-internal model architecture and application-specific fusion mechanism rather than a broadly reusable forecasting principle.
- [dataset] PitVQA-Anticipation (`pitvqa-anticipation`) - duplicate_existing: Duplicate dataset candidate already covered under approved vault datasets or redundant naming.

## Datasets

- [[pitvqa-anticipation]]

## Links

- [Abstract](https://arxiv.org/abs/2511.03178)
- [PDF](https://arxiv.org/pdf/2511.03178)

