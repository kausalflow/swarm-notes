---
# CSL-compatible fields
title: "ACEM: A Cost Estimation Model for Agentic Software Engineering"
author:
  - literal: "Mohammad El-Ramly"
issued:
  date-parts:
    - [2026, 8, 3]
url: "https://arxiv.org/abs/2608.02582"

# Custom fields
paper_id: "2608.02582"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "agent"
  - "autonomous-agent"
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
processed_at: "2026-08-06T07:32:49Z"
created_at: "2026-08-06T07:32:49Z"
---

# ACEM: A Cost Estimation Model for Agentic Software Engineering

**Authors**: Mohammad El-Ramly
**Date**: 2026-08-03
**Paper ID**: [openalex:2608.02582](https://arxiv.org/abs/2608.02582)

## Summary

The paper introduces ACEM (Agentic Cost Estimation Model), a framework designed to estimate software development costs in the era of autonomous AI agents. Traditional models like COCOMO II fail to capture agentic cost drivers such as nondeterministic token consumption, Human-in-the-Loop (HITL) oversight, and infrastructure orchestration. ACEM decomposes costs into LLM, HITL, and infrastructure dimensions, introducing novel constructs like the Revision Factor, Context Factor, and HITL Intensity Score while bridging traditional sizing metrics to token consumption.

## Key Contributions

- Proposes ACEM (Agentic Cost Estimation Model) to address the shift from human-centric to agentic software development cost structures.
- Decomposes total development cost into three additive dimensions: LLM token consumption, Human-in-the-Loop (HITL) oversight, and infrastructure orchestration costs.
- Introduces specialized constructs for agentic dynamics including the Revision Factor (RF), Context Factor (CF), and HITL Intensity Score (HIS).
- Bridges traditional sizing metrics (Use Case Points, Story Points, Function Points) with agentic token consumption estimation.

## Limitations

The model is presented as an early-stage proposal with constants left symbolic, requiring empirical grounding and calibration with real project data.

## Archivist Review

The paper proposes a cost estimation framework for agentic software engineering (ACEM). Although it introduces interesting metrics for LLM token consumption and human oversight, software cost estimation models fall outside the forecasting and core machine learning scope of this vault. Therefore, the concept is rejected.

### Rejected Candidates
- [concept] Agentic Cost Estimation Model (ACEM) (`agentic-cost-estimation-model-acem`) - low_impact: The paper focuses on software engineering cost estimation for AI agents rather than time-series forecasting or core machine learning architectures, making it outside the scope of the time-series and ML vault.

## Links

- [Abstract](https://arxiv.org/abs/2608.02582)
- [PDF](https://arxiv.org/pdf/2608.02582)

