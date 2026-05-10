---
# CSL-compatible fields
title: "A Scalable Digital Twin Framework for Energy Optimization in Data Centers"
author:
  - literal: "Raphael Hendrigo de Souza Gonçalves"
  - literal: "Wendel Marcos dos Santos"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.05581"

# Custom fields
paper_id: "2605.05581"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "lstm"
  - "iot"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:22:37Z"
created_at: "2026-05-10T07:22:37Z"
---

# A Scalable Digital Twin Framework for Energy Optimization in Data Centers

**Authors**: Raphael Hendrigo de Souza Gonçalves, Wendel Marcos dos Santos
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.05581](https://arxiv.org/abs/2605.05581)

## Summary

This paper presents a scalable Digital Twin framework designed for energy optimization in data center environments. By combining IoT-based monitoring with LSTM-driven forecasting, the system enables real-time tracking of power usage, temperature, and computational workload. Experimental results indicate that the approach effectively enhances Power Usage Effectiveness (PUE) and reduces overall energy consumption in a controlled testbed. The study highlights the framework's potential as a cost-effective, sustainable management solution for larger-scale data center operations.

## Key Contributions

- Introduces a scalable Digital Twin framework that integrates IoT data acquisition with machine learning for real-time energy management in data centers.
- Implements an LSTM-based forecasting module to predict energy demand, workload, and temperature, enabling proactive operational decision-making.
- Demonstrates empirical reductions in overall power consumption and improvements in Power Usage Effectiveness (PUE) within a controlled experimental environment.

## Open Questions & Future Work

- [[scalability-validation-digital-twins]]

## Archivist Review

The paper describes a standard application of LSTM-based forecasting for energy management in a small-scale data center. It provides no novel, reusable forecasting methodology or structural innovation that justifies a standalone concept note. I have approved the open question regarding the scalability of digital twins, as it addresses a persistent, high-level bottleneck in this research domain.

### Approved Open Questions
- Scalability of Digital Twin Frameworks: Ensuring that energy optimization frameworks are robust and scalable is essential for their industry adoption, as performance in constrained, small-scale models does not guarantee effectiveness in complex, high-traffic production environments.

### Rejected Candidates
- [concept] Digital Twin Energy Optimization Framework (`digital-twin-energy-optimization-framework`) - paper_local: The proposed framework lacks a distinct algorithmic innovation beyond standard IoT-LSTM integration, making it a paper-local system description rather than a reusable concept.

## Links

- [Abstract](https://arxiv.org/abs/2605.05581)
- [PDF](https://arxiv.org/pdf/2605.05581)

