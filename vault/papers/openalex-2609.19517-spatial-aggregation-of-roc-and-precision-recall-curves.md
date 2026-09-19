---
# CSL-compatible fields
title: "Spatial Aggregation of ROC and Precision-Recall Curves"
author:
  - literal: "Romain Pic"
  - literal: "Zhongwei Zhang"
  - literal: "Sebastian Engelke"
  - literal: "Johanna Ziegel"
issued:
  date-parts:
    - [2026, 9, 17]
url: "https://arxiv.org/abs/2609.19517"

# Custom fields
paper_id: "2609.19517"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
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
processed_at: "2026-09-19T09:04:38Z"
created_at: "2026-09-19T09:04:38Z"
---

# Spatial Aggregation of ROC and Precision-Recall Curves

**Authors**: Romain Pic, Zhongwei Zhang, Sebastian Engelke, Johanna Ziegel
**Date**: 2026-09-17
**Paper ID**: [openalex:2609.19517](https://arxiv.org/abs/2609.19517)

## Summary

Receiver Operating Characteristic (ROC) and Precision-Recall (PR) curves are heavily used to evaluate binary forecasts such as weather warnings, but spatial aggregation methods remain poorly understood and can lead to misleading interpretations. This paper investigates the theoretical conditions under which aggregation strategies preserve forecast dominance and curve concavity, proposing two novel strategies that satisfy these properties. The findings are demonstrated on AI-based global weather forecasts, showing that different aggregation techniques can alter model rankings.

## Key Contributions

- Investigates how different spatial aggregation strategies for Receiver Operating Characteristic (ROC) and Precision-Recall (PR) curves affect the performance assessment of binary event forecasts.
- Identifies theoretical conditions for aggregation strategies to satisfy desirable properties for fair comparison: preservation of dominance and preservation of concavity/achievability.
- Proposes two new aggregation strategies satisfying these sufficient conditions and compares them with existing literature baselines.
- Illustrates the framework using AI-based global weather forecasts, demonstrating how choice of aggregation strategy alters the ranking of competing forecasts.

## Limitations

Focuses primarily on spatial aggregation of binary event forecasts and their ROC/PR curve properties.

## Archivist Review

Applied strict selection filters, rejecting the paper-local open question as it focuses on specific spatial ROC/PR aggregation extensions. No concepts or datasets met the strict novelty and reusability standards.

### Rejected Candidates
- [open_question] Neighborhood-Based Contingency Table Aggregation (`neighborhood-contingency-tables-aggregation`) - low_impact: The question addresses a paper-specific extension regarding spatial ROC/PR curve aggregation and the double-penalty effect rather than a broad, foundational ML open problem.

## Links

- [Abstract](https://arxiv.org/abs/2609.19517)
- [PDF](https://arxiv.org/pdf/2609.19517)

