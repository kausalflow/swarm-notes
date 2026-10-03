---
# CSL-compatible fields
title: "Removing Timing Shortcuts Improves Non-Invasive Brain-to-Text"
author:
  - literal: "Dulhan Jayalath"
  - literal: "Ōiwi Parker Jones"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2609.40359"

# Custom fields
paper_id: "2609.40359"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "multimodal"
  - "benchmark"
  - "evaluation"
  - "robustness"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-03T10:09:30Z"
created_at: "2026-10-03T10:09:30Z"
---

# Removing Timing Shortcuts Improves Non-Invasive Brain-to-Text

**Authors**: Dulhan Jayalath, Ōiwi Parker Jones
**Date**: 2026-09-30
**Paper ID**: [openalex:2609.40359](https://arxiv.org/abs/2609.40359)

## Summary

The paper reveals that prominent non-invasive brain-to-text decoding methods rely on a timing shortcut caused by overlapping window segmentation that leaks word duration information. By replacing joint sentence-level window encoding with independent window processing, the proposed SimpleB2T approach forces models to rely on actual brain activity and allows pretrained LLM priors to effectively improve word error rates.

## Key Contributions

- Identified a critical timing shortcut in non-invasive brain-to-text decoding where overlapping time-window segmentation implicitly leaks word duration information, allowing neural networks to achieve 22.0% balanced accuracy on synthetic signals with no brain data.
- Proposed SimpleB2T by processing each time window independently rather than jointly encoding all sentence windows, effectively eliminating the timing shortcut.
- Demonstrated that removing timing shortcuts enables pretrained LLM linguistic priors and prediction aggregation to substantially improve decoding performance, achieving a 36.6% word error rate on a perceived speech benchmark.

## Limitations

Evaluated specifically on perceived speech benchmarks; generalizability to imagined speech or broader non-invasive brain-computer interface paradigms requires further study.

## Open Questions & Future Work

- [[extending-to-imagined-speech]]

## Archivist Review

Approved the open question on extending brain-to-text decoding shortcuts to imagined speech as it addresses a major generalizability limitation for non-invasive BCI paradigms. Rejected candidate concepts as they represent paper-local implementation details (SimpleB2T window processing).

### Approved Open Questions
- Extending to Imagined Speech: Moving from perceived speech to imagined speech is the ultimate goal for clinically viable non-invasive brain-computer interfaces, making the transferability of these decoding frameworks a critical open direction.

### Rejected Candidates
- [open_question] Optimizing Candidate Selection and Observation Efficiency (`optimizing-candidate-selection`) - low_impact: Focuses on specific beam search candidate selection and observation burden tuning rather than a fundamental theoretical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.40359)
- [PDF](https://arxiv.org/pdf/2609.40359)

