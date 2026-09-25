---
# CSL-compatible fields
title: "TimeInteract: Towards Real-Time Interactive Intelligence for Streaming Time Series"
author:
  - literal: "Sheng Pan"
  - literal: "Yongli Gu"
  - literal: "Yiqing Guo"
  - literal: "Warren Jin"
  - literal: "Bo Du"
  - literal: "Shirui Pan"
  - literal: "Ming Jin"
issued:
  date-parts:
    - [2026, 9, 22]
url: "https://arxiv.org/abs/2609.26389"

# Custom fields
paper_id: "2609.26389"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "language-model"
  - "llm"
  - "multimodal"
  - "streaming"
  - "dataset"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "timeinteract"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-25T09:54:13Z"
created_at: "2026-09-25T09:54:13Z"
---

# TimeInteract: Towards Real-Time Interactive Intelligence for Streaming Time Series

**Authors**: Sheng Pan, Yongli Gu, Yiqing Guo, Warren Jin, Bo Du, Shirui Pan, Ming Jin
**Date**: 2026-09-22
**Paper ID**: [openalex:2609.26389](https://arxiv.org/abs/2609.26389)

## Summary

Existing time-series language models are static and struggle with continuous streaming input during interaction. This paper introduces Time-Series Interaction, a regime where models continuously perceive streaming time-series data and autonomously decide when to speak. To achieve this, the authors propose TimeInteract, combining a dual-view streaming encoder, an adaptive response control mechanism, and a decoupled streaming inference pipeline. Evaluated on the newly constructed StreamTSI-34K dataset, TimeInteract outperforms existing LLMs, VLMs, and TSLMs while delivering up to a 2.15x inference speedup.

## Key Contributions

- Introduces Time-Series Interaction, a new regime enabling models to continuously perceive incoming time-series and user intent while autonomously deciding when to respond.
- Develops TimeInteract featuring a dual-view streaming time-series encoder, a response control mechanism, and a decoupled streaming inference mechanism.
- Constructs StreamTSI-34K, a large-scale streaming time-series interaction dataset comprising 34,588 episodes and 77,505 responses.
- Achieves up to 2.15x inference speedup and near-zero stream stall while improving response triggering across four interaction levels.

## Open Questions & Future Work

- [[real-world-interaction-data-collection]]

## Key Concepts

- [[timeinteract]]: A real-time interactive time-series model featuring dual-view streaming encoding, response control, and decoupled inference.

## Archivist Review

Approved the core TimeInteract framework as a reusable concept for streaming time-series interaction and retained the important open question on expanding to natural real-world interaction traces. Rejected the dataset as paper-specific.

### Approved Concepts
- TimeInteract: Introduces a novel framework for real-time interactive intelligence in streaming time series.

### Approved Open Questions
- Real-World Time-Series Interaction Data: Transitioning from synthetic scenarios to fully natural real-world interaction traces is essential to ensure generalizability, handle long-tail edge cases, and validate interactive time-series intelligence in safety-critical deployment domains.

### Rejected Candidates
- [dataset] StreamTSI-34K (`streamtsi-34k`) - low_impact: Dataset is specific to this paper and does not meet the high threshold for standalone vault notes.

## Links

- [Abstract](https://arxiv.org/abs/2609.26389)
- [PDF](https://arxiv.org/pdf/2609.26389)

