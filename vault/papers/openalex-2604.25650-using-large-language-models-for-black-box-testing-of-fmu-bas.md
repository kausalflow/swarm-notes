---
# CSL-compatible fields
title: "Using Large Language Models for Black-Box Testing of FMU-Based Simulations"
author:
  - literal: "Abdullah Mughees"
  - literal: "Gaadha Sudheerbabu"
  - literal: "Tanwir Ahmad"
  - literal: "Dragoş Truşcan"
  - literal: "Mikael Månngård"
  - literal: "Kristian Klemets"
issued:
  date-parts:
    - [2026, 4, 28]
url: "https://arxiv.org/abs/2604.25650"

# Custom fields
paper_id: "2604.25650"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "testing"
  - "simulation"
  - "automated-testing"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-01T07:22:49Z"
created_at: "2026-05-01T07:22:49Z"
---

# Using Large Language Models for Black-Box Testing of FMU-Based Simulations

**Authors**: Abdullah Mughees, Gaadha Sudheerbabu, Tanwir Ahmad, Dragoş Truşcan, Mikael Månngård, Kristian Klemets
**Date**: 2026-04-28
**Paper ID**: [openalex:2604.25650](https://arxiv.org/abs/2604.25650)

## Summary

This paper presents a framework that leverages LLMs to automate the testing of Functional Mock-up Units (FMUs) by generating structured test scenarios from system specifications. The approach converts requirements into Given-When-Then formatted goals, maps them to concrete input time series, and applies assertion oracles to validate simulation outputs. By automating scenario design and providing human-readable feedback, the method significantly reduces manual effort in the verification of dynamic simulation models. Performance was validated on a Lube Oil Cooling system, showing the utility of the approach in practical simulation-based testing workflows.

## Key Contributions

- Introduces a human-in-the-loop framework utilizing LLMs to automate black-box test scenario generation for FMU-based simulation models.
- Implements a structured generation pipeline that transforms functional specifications into testable Given-When-Then scenarios, complete with input time series and assertion oracles.
- Demonstrates the effectiveness of LLM-assisted verification on a Lube Oil Cooling system, providing human-readable logs and diagnostic plots for simulation outcomes.

## Open Questions & Future Work

- [[adaptive-oracle-calibration-simulation-testing]]

## Archivist Review

I approved the open question regarding adaptive oracle calibration because it addresses a fundamental, recurring bottleneck in automated verification of dynamical systems that extends beyond this specific LLM-based approach. The paper's primary framework was rejected as a concept because it represents a specific application of agentic workflows to simulation testing, which does not constitute a distinct, reusable architectural primitive for the time-series forecasting domain.

### Approved Open Questions
- Adaptive Calibration of Simulation Oracles: This is a fundamental challenge in automated test generation for dynamic systems, where relying solely on fixed, expert-defined thresholds limits scalability and reduces the reliability of test verdicts.

### Rejected Candidates
- [concept] LLM-assisted FMU Testing Framework (`llm-assisted-fmu-testing-framework`) - not_novel: This is a specific application of LLM-based prompting for automated testing rather than a reusable core mechanism or architectural pattern in time series forecasting or simulation.

## Links

- [Abstract](https://arxiv.org/abs/2604.25650)
- [PDF](https://arxiv.org/pdf/2604.25650)

