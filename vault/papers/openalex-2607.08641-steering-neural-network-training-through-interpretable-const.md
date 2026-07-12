---
# CSL-compatible fields
title: "Steering Neural Network Training through Interpretable Constraints Based on Partial Dependence"
author:
  - literal: "Yann Claes"
  - literal: "Pierre Geurts"
  - literal: "Vân Anh Huynh‐Thu"
issued:
  date-parts:
    - [2026, 7, 9]
url: "https://arxiv.org/abs/2607.08641"

# Custom fields
paper_id: "2607.08641"
paper_source: "openalex"
domain: "nlp"
tags:
  - "interpretability"
  - "explainability"
  - "regression"
  - "training-constraint"
architectures:
  []
datasets:
  []
concept_slugs:
  - "explanation-guided-learning"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-12T07:28:07Z"
created_at: "2026-07-12T07:28:07Z"
---

# Steering Neural Network Training through Interpretable Constraints Based on Partial Dependence

**Authors**: Yann Claes, Pierre Geurts, Vân Anh Huynh‐Thu
**Date**: 2026-07-09
**Paper ID**: [openalex:2607.08641](https://arxiv.org/abs/2607.08641)

## Summary

This paper presents a novel method for steering neural networks by imposing constraints based on partial dependence, ensuring that model predictions align with functional domain knowledge. By integrating these interpretability constraints during training, the authors improve model performance and data efficiency in regression tasks, such as dynamical systems forecasting. Furthermore, the approach produces explanations that are more faithful to user-provided knowledge compared to standard, unconstrained training.

## Key Contributions

- Introduces an approach to steer neural network training using partial dependence constraints to align average feature responses with functional domain knowledge.
- Demonstrates that constrained models outperform unconstrained ones on regression tasks, including dynamical systems forecasting, while improving data efficiency.
- Shows that the proposed training method ensures model interpretations are faithful to user-provided knowledge, whereas unconstrained models produce misleading explanations.

## Open Questions & Future Work

- [[automated-prior-knowledge-acquisition-for-guided-learning]]
- [[local-vs-global-interpretability-constraints-for-training]]

## Key Concepts

- [[explanation-guided-learning]]: A training paradigm that incorporates interpretable constraints to ensure model explanations adhere to prior knowledge.

## Archivist Review

The paper introduces a structured approach to steering neural networks using partial dependence as a constraint, which is a significant and reusable advancement in interpretability-aware training. I have approved 'Explanation-Guided Learning' as a concept and two open questions that address the challenges of acquiring priors and extending the interpretability measures used for constraints. Datasets were rejected as none were provided or identified as central to the paper's claim.

### Approved Concepts
- Explanation-Guided Learning: Central to the paper's focus on aligning neural network explanations with domain-specific functional knowledge.

### Approved Open Questions
- Automated prior knowledge acquisition: Developing automated ways to establish priors is essential for the scalability and practical utility of explanation-guided training methods.
- Local vs global interpretability constraints: Extending the scope of guided learning beyond global measures is critical for addressing complex datasets where local feature interactions are paramount.

### Rejected Candidates
- [open_question] Learning priors without explicit knowledge (`learning-prior-without-explicit-knowledge`) - other: Renamed for clarity and conciseness to better match vault standards.
- [open_question] Constraining with alternative interpretations (`constraining-beyond-partial-dependence`) - other: Renamed for clarity and conciseness to better match vault standards.

## Links

- [Abstract](https://arxiv.org/abs/2607.08641)
- [PDF](https://arxiv.org/pdf/2607.08641)

