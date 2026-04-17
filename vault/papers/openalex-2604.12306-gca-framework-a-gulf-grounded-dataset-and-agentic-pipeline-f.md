---
# CSL-compatible fields
title: "GCA Framework: A Gulf-Grounded Dataset and Agentic Pipeline for Climate Decision Support"
author:
  - literal: "Muhammad Umer Sheikh"
  - literal: "Khawar Shehzad"
  - literal: "Salman Khan"
  - literal: "Fahad Shahbaz Khan"
  - literal: "Muhammad Nauman Khan"
issued:
  date-parts:
    - [2026, 4, 14]
url: "https://arxiv.org/abs/2604.12306"

# Custom fields
paper_id: "2604.12306"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "llm"
  - "language-model"
  - "agent"
  - "autonomous-agent"
  - "tool-use"
  - "fine-tuning"
  - "dataset"
  - "evaluation"
architectures:
  []
datasets:
  - "GCA-DS"
concept_slugs:
  []
dataset_slugs:
  - "gca-ds"
skill: "TimeSeriesSkill"
processed_at: "2026-04-17T06:30:13Z"
created_at: "2026-04-17T06:30:13Z"
---

# GCA Framework: A Gulf-Grounded Dataset and Agentic Pipeline for Climate Decision Support

**Authors**: Muhammad Umer Sheikh, Khawar Shehzad, Salman Khan, Fahad Shahbaz Khan, Muhammad Nauman Khan
**Date**: 2026-04-14
**Paper ID**: [openalex:2604.12306](https://arxiv.org/abs/2604.12306)

## Summary

The GCA framework addresses the limitations of general-purpose LLMs in regional climate analysis by integrating specialized knowledge and tool-use capabilities. It provides GCA-DS, a 200k multimodal dataset linking governmental and scientific documents with remote-sensing data, alongside the Gulf Climate Agent (GCA) for automated climate analysis. The framework demonstrates that combining domain-specific datasets with modular, tool-augmented agent pipelines significantly enhances decision support accuracy in the Gulf context.

## Key Contributions

- Introduces GCA-DS, a specialized multimodal dataset of 200k QA pairs focused on Gulf climate policies, academic literature, and event-driven environmental reporting.
- Proposes the Gulf Climate Agent (GCA), an agentic pipeline that orchestrates geospatial processing tools and real-time climate signals for actionable decision support.
- Demonstrates that domain-specific fine-tuning and tool integration significantly improve the reliability of LLMs on region-specific climate reasoning tasks compared to general-purpose baselines.

## Open Questions & Future Work

- [[validating-automatically-generated-climate-datasets]]
- [[robustness-of-agentic-climate-pipelines]]

## Archivist Review

I approved the GCA-DS dataset as it represents a significant, structured multimodal resource for climate decision support, and I approved two open questions concerning the reliability and validation of automated climate informatics. I rejected the 'Gulf Climate Agent' concept as it refers to a specific, regionally constrained implementation rather than a generalizable architecture or method.

### Approved Open Questions
- Validating Automatically Generated Datasets: Ensuring the accuracy of datasets is critical for high-stakes climate decision-making where policy and geospatial evidence must be precise.
- Robustness of Agentic Climate Pipelines: Agentic tool reliability is a significant bottleneck for deploying automated assistants in real-world, high-stakes decision support environments.

### Rejected Candidates
- [concept] Gulf Climate Agent (GCA) (`gulf-climate-agent-gca`) - paper_local: The concept describes a specific, application-bound agentic implementation rather than a reusable architectural pattern or methodological breakthrough.

## Datasets

- [[gca-ds]]

## Links

- [Abstract](https://arxiv.org/abs/2604.12306)
- [PDF](https://arxiv.org/pdf/2604.12306)

