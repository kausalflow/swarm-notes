---
# CSL-compatible fields
title: "Multivariate quantum reservoir computing with discrete and continuous variable systems"
author:
  - literal: "Tobias Fellner"
  - literal: "Jonas Merklinger"
  - literal: "Christian Holm"
issued:
  date-parts:
    - [2026, 4, 9]
url: "https://arxiv.org/abs/2604.08427"

# Custom fields
paper_id: "2604.08427"
paper_source: "openalex"
domain: "time-series,"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "mixing-capacity"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-12T06:20:43Z"
created_at: "2026-04-12T06:20:43Z"
---

# Multivariate quantum reservoir computing with discrete and continuous variable systems

**Authors**: Tobias Fellner, Jonas Merklinger, Christian Holm
**Date**: 2026-04-09
**Paper ID**: [openalex:2604.08427](https://arxiv.org/abs/2604.08427)

## Summary

This paper addresses the limitation of quantum reservoir computing (QRC) to univariate time series by establishing a comprehensive framework for multivariate data processing. The authors introduce three distinct multivariate encoding schemes and propose 'mixing capacity' as a new metric to quantify the integration of multiple data streams within a reservoir. Through empirical assessment on the Lorenz-63 system, the study demonstrates that optimal encoding is highly task- and system-dependent, with peak performance often linked to non-classical quantum effects.

## Key Contributions

- Developed an extensive framework for multivariate time-series processing in quantum reservoir computing.
- Introduced 'mixing capacity' as a novel metric to quantify how effectively a reservoir integrates independent multivariate data streams.
- Systematically evaluated three multivariate encoding schemes using the Lorenz-63 chaotic system across both discrete and continuous-variable quantum reservoir architectures.

## Open Questions & Future Work

- [[theoretical-framework-quantum-resources-qrc-capacity]]

## Key Concepts

- [[mixing-capacity]]: A metric for evaluating the effectiveness of a reservoir in combining independent data streams in multivariate time-series processing.

## Archivist Review

I approved 'mixing capacity' as it is a well-defined and reusable metric for assessing information integration in reservoir systems, which is central to the paper's contribution. I also approved the theoretical framework question as a high-level, foundational research gap for quantum reservoir computing. Other candidates were rejected for being overly specialized or lacking the broader applicability required for the vault.

### Approved Concepts
- Mixing capacity: It provides a formal quantitative metric for assessing how well a reservoir architecture processes multiple input streams, which is a common challenge across various reservoir computing domains beyond just quantum systems.

### Approved Open Questions
- Theoretical framework for QRC capacity: Developing this framework is critical for the systematic design and optimization of QRC systems, allowing researchers to engineer specific quantum properties to achieve desired computational outcomes in high-dimensional temporal tasks.

### Rejected Candidates
- [open_question] Processing multivariate quantum data (`multivariate-quantum-data-processing`) - low_impact: The question is highly specialized and currently lacks the broader reach or technical maturity to serve as a high-value, long-lived open question for general time-series forecasting research.

## Links

- [Abstract](https://arxiv.org/abs/2604.08427)
- [PDF](https://arxiv.org/pdf/2604.08427)

