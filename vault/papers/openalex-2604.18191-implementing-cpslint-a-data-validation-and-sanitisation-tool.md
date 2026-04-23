---
# CSL-compatible fields
title: "Implementing CPSLint: A Data Validation and Sanitisation Tool for Industrial Cyber-Physical Systems"
author:
  - literal: "Uraz Odyurt"
  - literal: "Ömer Sayilir"
  - literal: "Mariëlle Stoelinga"
  - literal: "Vadim Zaytsev"
issued:
  date-parts:
    - [2026, 4, 20]
url: "https://arxiv.org/abs/2604.18191"

# Custom fields
paper_id: "2604.18191"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "information-extraction"
architectures:
  []
datasets:
  []
concept_slugs:
  - "cpslint-dsl"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-23T06:56:18Z"
created_at: "2026-04-23T06:56:18Z"
---

# Implementing CPSLint: A Data Validation and Sanitisation Tool for Industrial Cyber-Physical Systems

**Authors**: Uraz Odyurt, Ömer Sayilir, Mariëlle Stoelinga, Vadim Zaytsev
**Date**: 2026-04-20
**Paper ID**: [openalex:2604.18191](https://arxiv.org/abs/2604.18191)

## Summary

Raw time-series data from industrial Cyber-Physical Systems (CPS) often requires tedious, case-specific manual processing. This paper introduces CPSLint, a Domain-Specific Language (DSL) designed to standardize and automate the data validation and sanitization process. By raising the level of abstraction, CPSLint allows both data scientists and domain experts to efficiently prepare data-centric workflows without relying on repetitive, ad-hoc scripting.

## Key Contributions

- Introduces CPSLint, a Domain-Specific Language (DSL) that replaces ad-hoc Python scripts for CPS data preparation.
- Enables both data scientists and domain experts to perform time-series sanitization via an abstracted, declarative interface.
- Provides a publicly available tool that reduces repetitive data preparation tasks in industrial time-series workflows.

## Open Questions & Future Work

- [[automated-content-based-data-segmentation]]

## Key Concepts

- [[cpslint-dsl]]: A Domain-Specific Language (DSL) designed for declarative data validation and sanitization in industrial Cyber-Physical Systems time-series workflows.

## Archivist Review

I approved the core DSL concept and the open question regarding content-based segmentation, as these address significant bottlenecks in data pipeline modularity and signal processing respectively. I rejected the open question on native units as it is essentially a domain-specific software engineering task rather than a foundational research challenge for the ML community.

### Approved Concepts
- CPSLint: It addresses the recurring problem of fragmented, ad-hoc data preparation in industrial time-series workflows by abstracting common cleaning and sanitization tasks into a declarative interface.

### Approved Open Questions
- Automated Content-Based Segmentation: Automated, content-based segmentation is critical for robust time-series analysis in scenarios where sensor data logging is inconsistent or unavailable.

### Rejected Candidates
- [open_question] Native Domain-Specific Units (`native-domain-specific-units-in-dsls`) - low_impact: This is a software engineering feature request rather than a fundamental research bottleneck in machine learning or time-series analysis.

## Links

- [Abstract](https://arxiv.org/abs/2604.18191)
- [PDF](https://arxiv.org/pdf/2604.18191)

