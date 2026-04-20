---
# CSL-compatible fields
title: "Estimation of service value parameters for a queue with unobserved balking"
author:
  - literal: "Daniel Podorojnyi"
  - literal: "Liron Ravner"
issued:
  date-parts:
    - [2026, 4, 17]
url: "https://arxiv.org/abs/2409.04090"

# Custom fields
paper_id: "2409.04090"
paper_source: "openalex"
domain: "reinforcement-learning"
tags:
  - "reinforcement-learning"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "GeneralMLSkill"
processed_at: "2026-04-20T07:10:03Z"
created_at: "2026-04-20T07:10:03Z"
---

# Estimation of service value parameters for a queue with unobserved balking

**Authors**: Daniel Podorojnyi, Liron Ravner
**Date**: 2026-04-17
**Paper ID**: [openalex:2409.04090](https://arxiv.org/abs/2409.04090)

## Summary

This paper addresses the estimation of service value parameters in a queueing model with unobserved customer balking, building upon Naor's classic framework. By assuming a parametric distribution for customer service values, the authors construct a Maximum Likelihood Estimator using only observed queue length data. They prove the estimator's consistency and asymptotic normality and demonstrate its application in a dynamic pricing scheme designed to maximize revenue through iterative parameter updates. The methodology is validated through extensive simulation experiments.

## Key Contributions

- Construction of a Maximum Likelihood Estimator (MLE) for service value parameters in an M/M/1-type queue with unobserved balking.
- Provision of formal conditions ensuring the consistency and asymptotic normality of the proposed MLE.
- Development of an iterative dynamic pricing scheme that optimizes revenue based on parameter estimates obtained from observed queue lengths.

## Open Questions & Future Work

- [[unobserved-balking-heterogeneity-extensions]]

## Archivist Review

The paper provides a statistical estimation framework for a classic queueing theory problem. The methodology uses standard MLE techniques adapted for unobserved balking, which does not constitute a novel, reusable ML concept. The identified open question, however, highlights a relevant gap in extending such statistical inference to more complex, non-homogeneous, or non-parametric queueing environments.

### Approved Open Questions
- Extensions for Unobserved Balking Models: These directions are critical for moving beyond current restrictive model assumptions, allowing for more realistic and robust applications of statistical inference and revenue management in service systems.

### Rejected Candidates
- [concept] Maximum Likelihood Estimation for Queues with Unobserved Balking (`mle-for-unobserved-balking-queue`) - not_novel: This is a specific application of standard MLE to a classic queueing problem rather than a novel, reusable ML methodological paradigm.
- [concept] Iterative Dynamic Pricing via Parameter Estimation (`iterative-revenue-maximizing-dynamic-pricing`) - not_novel: This is a domain-specific application of parameter estimation, which is a common practice in control and operations research, rather than a general-purpose ML contribution.

## Links

- [Abstract](https://arxiv.org/abs/2409.04090)
- [PDF](https://arxiv.org/pdf/2409.04090)

