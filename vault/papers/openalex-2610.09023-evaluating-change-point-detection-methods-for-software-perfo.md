---
# CSL-compatible fields
title: "Evaluating Change Point Detection Methods for Software Performance Regression Analysis"
author:
  - literal: "Diego Elias Costa"
  - literal: "Michele Tucci"
  - literal: "Luca Traini"
  - literal: "Daniele Di Pompeo"
  - literal: "Thomas Bach"
  - literal: "François Farquet"
  - literal: "David Daly"
  - literal: "Simon Eismann"
  - literal: "Petr Tůma"
  - literal: "Vittorio Cortellessa"
  - literal: "André van Hoorn"
issued:
  date-parts:
    - [2026, 10, 6]
url: "https://arxiv.org/abs/2610.09023"

# Custom fields
paper_id: "2610.09023"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
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
processed_at: "2026-10-09T11:36:18Z"
created_at: "2026-10-09T11:36:18Z"
---

# Evaluating Change Point Detection Methods for Software Performance Regression Analysis

**Authors**: Diego Elias Costa, Michele Tucci, Luca Traini, Daniele Di Pompeo, Thomas Bach, François Farquet, David Daly, Simon Eismann, Petr Tůma, Vittorio Cortellessa, André van Hoorn
**Date**: 2026-10-06
**Paper ID**: [openalex:2610.09023](https://arxiv.org/abs/2610.09023)

## Summary

This paper presents a comprehensive empirical evaluation of twelve Change Point Detection (CPD) methods applied to software performance regression analysis. By collecting performance measurement data from three large software systems and analyzing human annotators' consistency, the study characterizes the unique properties of performance time series and assesses the effectiveness of different CPD techniques. The findings offer practical insights into automating the detection of software performance regressions.

## Key Contributions

- Evaluated twelve distinct Change Point Detection (CPD) methods on real-world software performance measurement datasets collected from three large software systems.
- Characterized the unique properties of software performance time series data and assessed the consistency of human annotators in identifying performance changes.
- Provided comprehensive insights into the applicability, accuracy, and effectiveness of various CPD techniques for software performance regression analysis.

## Open Questions & Future Work

- [[cost-sensitive-change-point-evaluation]]

## Archivist Review

Evaluated the paper according to strict archival standards. No concepts or datasets met the reusability thresholds. The sole candidate open question was reviewed and rejected as paper-local to software performance regression evaluation metrics.

### Approved Open Questions
- Cost-Sensitive Change Point Evaluation: Evaluating change point detection under symmetric scores does not align with industrial realities where missing regressions and false positives have vastly different economic impacts.

### Rejected Candidates
- [open_question] Cost-Sensitive Change Point Evaluation (`cost-sensitive-change-point-evaluation`) - paper_local: The open question focuses specifically on software performance regression analysis evaluation metrics rather than a general open problem in time-series methodology.

## Links

- [Abstract](https://arxiv.org/abs/2610.09023)
- [PDF](https://arxiv.org/pdf/2610.09023)

