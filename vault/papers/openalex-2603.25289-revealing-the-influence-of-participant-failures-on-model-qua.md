---
# CSL-compatible fields
title: "Revealing the influence of participant failures on model quality in cross-silo Federated Learning"
author:
  - literal: "Fabian Stricker"
  - literal: "David Bermbach"
  - literal: "Christian Zirpins"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25289"

# Custom fields
paper_id: "2603.25289"
paper_source: "openalex"
domain: "federated"
tags:
  - "federated"
  - "robustness"
  - "evaluation"
  - "distributed-training"
architectures:
  []
datasets:
  []
concept_slugs:
  - "fl-participant-failure-impact-analysis"
  - "fl-global-model-utility-for-dropped-out-clients"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-29T06:08:36Z"
created_at: "2026-03-29T06:08:36Z"
---

# Revealing the influence of participant failures on model quality in cross-silo Federated Learning

**Authors**: Fabian Stricker, David Bermbach, Christian Zirpins
**Date**: 2026-03-26
**Paper ID**: [openalex:2603.25289](https://arxiv.org/abs/2603.25289)

## Summary

This paper addresses the reliability gap in Federated Learning (FL) by systematically investigating the impact of participant failures, specifically client dropouts, on the quality and stability of the global model. The authors conduct extensive experiments using image, tabular, and time-series data, analyzing how factors like data skewness and availability patterns mediate these effects. A key finding is that data skewness profoundly affects outcomes, often inflating model evaluations beyond true performance. Furthermore, the study examines the utility of the resulting global model specifically for the participants who were absent during the training process.

## Key Contributions

- Systematic investigation into the impact of missing participants on model performance in FL across image, tabular, and time-series data.
- Demonstration that data skewness significantly influences FL model performance and can lead to overly optimistic evaluation results.
- Analysis of how different participant availability patterns and model architectures mediate the effect of failures.
- Examination of the utility of the final global model specifically for the participants who were missing during training.

## Limitations

The study is focused primarily on crash/absence failures; other fault scenarios like Byzantine attacks or slow/stale participation are not explicitly covered in the abstract's scope.

## Open Questions & Future Work

- [[multi-participant-failure-impact-analysis]]
- [[generalizability-of-failure-impact-modifiers]]

## Key Concepts

- [[fl-participant-failure-impact-analysis]]: A systematic methodology for assessing how the absence or failure of individual participants impacts the performance and utility of the global model in Federated Learning systems.
- [[fl-global-model-utility-for-dropped-out-clients]]: The evaluation metric quantifying the performance or utility of the final global model specifically on the private data held by participants who failed to complete the training process.

## Archivist Review

Two concepts detailing the systematic impact analysis framework and the utility metric for dropped-out clients were approved as they represent novel, reusable contributions to FL reliability research. Two of the three open questions were approved, focusing on multi-participant failure aggregation and the generalizability of failure modifiers, as these represent substantial unresolved system-level challenges in FL robustness. The third open question, concerning server-side data requirements for Shapley Values, was rejected as too local to the specific contribution methodology used.

### Approved Concepts
- Participant Failure Impact Analysis in FL: This forms the central, systematic contribution of the paper: quantifying how client dropouts affect FL model quality and evaluation.
- Model Utility for Missing Participants: This addresses a critical practical concern in FL: whether the final model is still useful to the clients that dropped out during training.

### Approved Open Questions
- Simultaneous participant crash impact: Understanding multi-participant failure scenarios is vital for deploying robust fault-tolerance mechanisms that account for correlated failures in distributed systems.
- Generalizability of failure impact modifiers: Establishing the generalizability of FIM interactions is necessary to create broadly applicable fault-tolerance guidelines for cross-silo FL.

### Rejected Candidates
- [open_question] Data-free participant impact prediction (`server-side-data-free-fl-contribution-metrics`) - paper_local: The described open question discusses the necessity of server-side data for calculating Shapley Values, which is a limitation of the *method* used, not a fundamental open question about FL reliability itself that requires a new, permanent vault note.

## Links

- [Abstract](https://arxiv.org/abs/2603.25289)
- [PDF](https://arxiv.org/pdf/2603.25289)

