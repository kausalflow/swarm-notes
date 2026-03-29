---
# CSL-compatible fields
title: "Does Explanation Correctness Matter? Linking Computational XAI Evaluation to Human Understanding"
author:
  - literal: "Gregor Baer"
  - literal: "chao zhang"
  - literal: "Isel Grau"
  - literal: "Pieter Van Gorp"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25251"

# Custom fields
paper_id: "2603.25251"
paper_source: "openalex"
domain: "nlp"
tags:
  - "explanation"
  - "explainable-ai"
  - "evaluation"
  - "human-understanding"
  - "time-series"
  - "reasoning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "forward-simulation-xai-evaluation"
  - "explanation-correctness-thresholds"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-29T06:09:00Z"
created_at: "2026-03-29T06:09:00Z"
---

# Does Explanation Correctness Matter? Linking Computational XAI Evaluation to Human Understanding

**Authors**: Gregor Baer, chao zhang, Isel Grau, Pieter Van Gorp
**Date**: 2026-03-26
**Paper ID**: [openalex:2603.25251](https://arxiv.org/abs/2603.25251)

## Summary

This paper investigates the empirical link between the computational fidelity (correctness) of AI explanations and resulting human understanding, using a controlled user study on time series classification. Researchers manipulated explanation correctness at four levels (100%, 85%, 70%, 55%) where participants performed forward simulation by predicting model decisions based only on the explanations. The key finding is that performance drops only below 70% correctness, suggesting that small functional inaccuracies do not always translate to reduced human comprehension or learning of the model's reasoning. The study underscores that validation of functional XAI metrics against actual human outcomes is necessary, as high correctness does not guarantee understanding.

## Key Contributions

- Demonstrated experimentally that functional explanation correctness does not linearly translate to human understanding in a time series classification task.
- Identified a critical threshold (70%) in explanation correctness below which further degradation yields no additional loss in human performance.
- Showed that high functional correctness (100%) does not guarantee human understanding, as a subset of users still failed to learn the decision pattern.
- Established a user study paradigm (forward simulation) where human performance is directly linked to manipulating explanation correctness levels.

## Limitations

The study was limited to a time series classification task, and participants were explicitly prevented from using domain knowledge or visual intuition, which may limit generalizability to other tasks or settings.

## Open Questions & Future Work

- [[unresolved-correctness-impact-85-vs-100-percent]]
- [[conditions-for-informative-self-reports]]
- [[factors-beyond-correctness-for-learning]]

## Key Concepts

- [[forward-simulation-xai-evaluation]]: A user study methodology where participants are tasked with predicting the AI's output based solely on its provided explanation for a given input.
- [[explanation-correctness-thresholds]]: Empirically determined thresholds in explanation correctness (e.g., 70%) below which further degradation does not significantly impact human performance or learning of the model's decision patterns.

## Archivist Review

Archivist review kept only candidates judged central to the paper and reusable across future work. Approved 2 concept(s), 3 open question(s), and 0 dataset(s), with 2 rejected candidate note(s).

### Approved Concepts
- Forward Simulation in XAI User Studies: This is a specific experimental setup used to measure human understanding of model reasoning via explanations, which is a core methodological contribution.
- Explanation Correctness Thresholds: The finding that functional correctness degradation beyond a certain (70%) threshold does not cause further human understanding loss is a critical insight for metric design.

### Approved Open Questions
- Finer Correctness Range Analysis: Resolving the inconclusive finding between 85% and 100% correctness is crucial because this small performance gap is common between state-of-the-art XAI methods, and understanding if this difference is meaningful to users is vital for guiding practical XAI development.
- Investigate Informative Self-Reports: Understanding when subjective self-reports align with objective performance is a major unresolved issue in human-centered XAI evaluation, as current findings suggest they are only reliable under specific, favorable conditions.
- Factors Supporting Explanation Learning: Correctness is a necessary but not sufficient condition for understanding; identifying the other crucial factors (e.g., presentation style, required cognitive effort) is required to move XAI evaluation beyond simply measuring faithfulness.

### Rejected Candidates
- [open_question] Equivalence of Correctness Metrics (`equivalence-of-correctness-metrics`) - paper_local: This open question relates to the equivalence between functional metrics, which is a specialized question about the computational validation of XAI, rather than a broad, reusable unresolved mechanism bottleneck.
- [dataset] ETTh1 (`ETTh1`) - low_impact: ETTh1 is a generic, routine benchmark dataset for time series forecasting and does not warrant a dedicated vault entry in an XAI evaluation paper context.

## Links

- [Abstract](https://arxiv.org/abs/2603.25251)
- [PDF](https://arxiv.org/pdf/2603.25251)

