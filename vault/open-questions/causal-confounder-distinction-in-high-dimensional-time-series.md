---
created_at: '2026-06-26T08:26:03Z'
source_papers:
- '[[openalex-2606.24283-investigating-causality-between-principal-components-in-prot]]'
title: Causal confounder distinction
---

**Background:** Causal inference for time series aims to determine directed dynamical influences between variables, but identifying whether inferred links are direct or mediated by hidden confounders remains a fundamental challenge in complex systems.

**Question / Future Work:** Distinguishing between direct causal interactions and those mediated by unobserved intermediate variables when analyzing directed dependency networks derived from high-dimensional time series data remains an open research challenge. Addressing this is necessary for building robust structural causal models beyond identifying simple putative asymmetries.

**Why It Matters:** This is a fundamental challenge for the validity of causal inference in any complex dynamical system where confounding is present, which is common in molecular and physical simulations.

**Evidence:** The presence of an asymmetric dynamical coupling between two variables is a necessary condition of the presence of a causal link between the two variables. However, this condition is not sufficient, since the two variables could be simultaneously caused by a third unobserved variable.