---
# CSL-compatible fields
title: "Evaluating Sequence Assembly Strategies for Differentially Private Synthetic Time-Series Forecasting"
author:
  - literal: "Guoxiong Long"
  - literal: "Huizhen Huang"
  - literal: "Qikun Cai"
  - literal: "Tao Huang"
  - literal: "Chen Hou"
issued:
  date-parts:
    - [2026, 10, 7]
url: "https://arxiv.org/abs/2610.10222"

# Custom fields
paper_id: "2610.10222"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "differential-privacy"
  - "synthetic-data"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-09T11:33:52Z"
created_at: "2026-10-09T11:33:52Z"
---

# Evaluating Sequence Assembly Strategies for Differentially Private Synthetic Time-Series Forecasting

**Authors**: Guoxiong Long, Huizhen Huang, Qikun Cai, Tao Huang, Chen Hou
**Date**: 2026-10-07
**Paper ID**: [openalex:2610.10222](https://arxiv.org/abs/2610.10222)

## Summary

Differentially private time-series generators typically produce fixed-length synthetic windows that must be assembled into continuous sequences for downstream forecasting. This paper systematically investigates post-generation sequence assembly strategies, including overlap rates and window-weighting schemes, across multiple public datasets and forecasting models under the Train-on-Synthetic-Test-on-Real (TSTR) paradigm. The findings reveal a forecaster-dependent assembly principle, showing that downstream utility is jointly determined by the forecaster and assembly configuration rather than purely by individual data fidelity diagnostics.

## Key Contributions

- Systematically evaluates post-generation sequence assembly strategies (overlap rates and window-weighting schemes) for differentially private synthetic time-series forecasting across four public datasets and five forecasting models.
- Establishes a forecaster-dependent assembly principle demonstrating that downstream TSTR forecasting utility is jointly shaped by the forecaster, overlap rate, and window-weighting scheme.
- Proves that boundary continuity and individual fidelity diagnostics alone are insufficient for predicting or selecting optimal synthetic sequence assembly configurations.

## Open Questions & Future Work

- [[adaptive-learned-sequence-assembly]]

## Archivist Review

Reviewed the submission according to the stringent vault criteria. No standalone concepts or datasets met the threshold for vault inclusion. One open question was initially considered but rejected due to low impact.

### Approved Open Questions
- Adaptive And Learned Sequence Assembly: Investigating adaptive or learned sequence assembly strategies could optimize downstream forecasting utility and mitigate the manual candidate-prioritization overhead currently required for different forecaster architectures.

### Rejected Candidates
- [open_question] Adaptive And Learned Sequence Assembly (`adaptive-learned-sequence-assembly`) - low_impact: The open question, while interesting, investigates a specific extension of post-generation window stitching rather than a broad, critical foundational bottleneck for the entire time-series forecasting literature.

## Links

- [Abstract](https://arxiv.org/abs/2610.10222)
- [PDF](https://arxiv.org/pdf/2610.10222)

