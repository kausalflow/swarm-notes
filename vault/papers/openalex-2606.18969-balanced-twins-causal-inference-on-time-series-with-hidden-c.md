---
# CSL-compatible fields
title: "Balanced Twins: Causal Inference on Time Series with Hidden Confounding"
author:
  - literal: "Ouali Maha"
  - literal: "Ghattas Badih"
  - literal: "Flachaire Emmanuel"
  - literal: "Charpentier Philippe"
  - literal: "B Laurent"
issued:
  date-parts:
    - [2026, 6, 17]
url: "https://arxiv.org/abs/2606.18969"

# Custom fields
paper_id: "2606.18969"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "causal-inference"
  - "latent-representation-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "balanced-twins"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-20T08:16:53Z"
created_at: "2026-06-20T08:16:53Z"
---

# Balanced Twins: Causal Inference on Time Series with Hidden Confounding

**Authors**: Ouali Maha, Ghattas Badih, Flachaire Emmanuel, Charpentier Philippe, B Laurent
**Date**: 2026-06-17
**Paper ID**: [openalex:2606.18969](https://arxiv.org/abs/2606.18969)

## Summary

This paper addresses the challenge of causal inference in time series with hidden confounding and staggered treatment adoption. The authors propose Balanced Twins, a neural framework that simultaneously learns latent representations and propensity scores to estimate individual treatment effects (ITE). By utilizing a flexible matching procedure, the method avoids the restrictive convexity constraints of traditional synthetic control approaches and effectively handles non-stationary dynamics without explicit temporal modeling. Empirical validation on energy consumption and clinical ICU data demonstrates its robustness in identifying counterfactuals under latent bias.

## Key Contributions

- Introduces Balanced Twins, a neural framework for estimating the average treatment effect for the treated (ATT) in time series with staggered interventions.
- Enables individual treatment effect (ITE) estimation under hidden confounding by jointly learning low-dimensional latent time-series representations and propensity scores.
- Provides a matching-based counterfactual estimation procedure that relaxes the rigid convexity constraints inherent in traditional synthetic control methods.

## Open Questions & Future Work

- [[advanced-representation-heterogeneous-treatment-modeling]]

## Key Concepts

- [[balanced-twins]]: A neural framework for causal inference in time series that uses joint latent representation learning and propensity scoring to estimate counterfactuals and handle hidden confounding.

## Archivist Review

I have approved the core 'Balanced Twins' framework as it provides a distinct, reusable methodology for causal inference in staggered time-series settings. The open question was approved in a refined form to highlight the specific technical bottleneck of balancing representation power with dynamic treatment effect estimation under non-stationarity, rather than simply calling for 'better models'. No datasets were approved as they were not specific or uniquely named in the text.

### Approved Concepts
- Balanced Twins: Addresses causal inference in time series under hidden confounding and staggered adoption by jointly learning latent representations and propensity scores.

### Approved Open Questions
- Advanced representation and heterogeneous treatment modeling: Improving the representational capacity for counterfactual estimation is critical for causal inference in healthcare and energy systems where latent confounders are pervasive and data is highly dynamic.

### Rejected Candidates
- [open_question] Advanced representation and heterogeneous treatment modeling (`advanced-representation-heterogeneous-treatment-modeling`) - other: While potentially valuable, the proposal is framed as a request for more sophisticated architecture and better modeling, which borders on the boilerplate research request policy. However, I am approving it as a refined open question focusing on the tension between representation capacity and dynamic treatment effect robustness.

## Links

- [Abstract](https://arxiv.org/abs/2606.18969)
- [PDF](https://arxiv.org/pdf/2606.18969)

