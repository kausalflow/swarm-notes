---
title: "Triangularized SVAR Parameterization"
slug: "triangularized-svar-parameterization"
type: concept
generated_stub: true
source_papers:
  - "[[openalex-2606.03227-learning-temporal-causal-structure-via-smooth-differentiable]]"
processed_at: "2026-06-05T08:39:13Z"
created_at: "2026-06-05T08:39:13Z"
---

# Triangularized SVAR Parameterization

> *Auto-generated stub. Edit this file to add more details.*

A parameterization method that enforces acyclicity in SVAR models by learning a differentiable variable permutation for triangular matrix decomposition.


## Why It Matters

It eliminates the need for complex, computationally expensive acyclicity constraints by parameterizing the instantaneous structure to be naturally acyclic via a learned triangular form.

## Evidence

> we learn a differentiable permutation of variables using the Gumbel--Sinkhorn operator and triangularize the instantaneous coefficient matrix of a Structural Vector Autoregressive (SVAR) model in the learned order

## Related Papers

- [[openalex-2606.03227-learning-temporal-causal-structure-via-smooth-differentiable]]
