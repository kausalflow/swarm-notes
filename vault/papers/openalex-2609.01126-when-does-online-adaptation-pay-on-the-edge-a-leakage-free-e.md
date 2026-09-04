---
# CSL-compatible fields
title: "When Does Online Adaptation Pay on the Edge? A Leakage-Free Evaluation of Warmup, Learning-Rate Selection, and Resource Trade-offs for Time-Series Forecasting"
author:
  - literal: "Takumi Fujimoto"
  - literal: "Hiroaki Nishi"
issued:
  date-parts:
    - [2026, 9, 1]
url: "https://arxiv.org/abs/2609.01126"

# Custom fields
paper_id: "2609.01126"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
  - "evaluation"
  - "benchmark"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-04T09:10:38Z"
created_at: "2026-09-04T09:10:38Z"
---

# When Does Online Adaptation Pay on the Edge? A Leakage-Free Evaluation of Warmup, Learning-Rate Selection, and Resource Trade-offs for Time-Series Forecasting

**Authors**: Takumi Fujimoto, Hiroaki Nishi
**Date**: 2026-09-01
**Paper ID**: [openalex:2609.01126](https://arxiv.org/abs/2609.01126)

## Summary

This paper investigates the conditions under which online adaptation improves edge time-series forecasting under distribution drift, proposing a leakage-free streaming protocol and a validation-only commissioning procedure. The authors demonstrate that static baseline warmup budgets and shared default learning rates introduce substantial comparison bias, which distorts the measured benefits of online adaptation. Through extensive evaluation across six public multivariate streams using PatchTST backbones, they show that Adam consistently outperforms SGD+m when properly tuned, and that parameter-efficient adaptation variants achieve nondominated trade-offs on the adaptation-state-memory axis.

## Key Contributions

- Identifies that the static baseline's warmup budget has a two-sided effect, causing estimated adaptation benefits to shift by 3.0 to 18.8 percentage points across the 1,000-20,000-step range.
- Shows that comparing SGD with momentum and Adam at a shared default learning rate conflates optimizer quality with rate sensitivity, and proposes a validation-only commissioning procedure using a held-out pre-drift slice.
- Evaluates full, head-only, and calibration-based adaptation strategies on PatchTST frontiers, highlighting parameter-efficient variants as nondominated on the adaptation-state-memory axis.

## Limitations

Target-device latency and energy remain to be measured beyond A100-measured per-update latency.

## Open Questions & Future Work

- [[edge-hardware-validation-adaptation]]

## Archivist Review

The paper provides an insightful evaluation of online adaptation on the edge for time-series forecasting, highlighting warmup and learning-rate biases. While the evaluation insights are valuable, the proposed methodology terms are primarily paper-local evaluation protocols rather than reusable standalone architectural concepts. The open question regarding edge hardware validation is approved as it addresses a substantive practical limitation in deploying adaptation frameworks on constrained hardware.

### Approved Open Questions
- Edge Hardware Validation for Adaptation: Transitioning from simulated datacenter GPU metrics to real-world embedded hardware measurements is critical for validating the practical utility and resource feasibility of edge time-series adaptation frameworks.

### Rejected Candidates
- [concept] Leakage-Free Edge Adaptation Evaluation (`leakage-free-edge-adaptation-evaluation`) - paper_local: Evaluation protocol and bias identification details are too paper-specific and lack broader standalone conceptual reusability across diverse time-series forecasting frameworks.
- [concept] Validation-Only Commissioning Procedure (`validation-only-commissioning-procedure`) - not_novel: Tuning optimizers and warmup using a held-out pre-drift validation slice is a standard ML practice rather than a distinct standalone architectural concept.

## Links

- [Abstract](https://arxiv.org/abs/2609.01126)
- [PDF](https://arxiv.org/pdf/2609.01126)

