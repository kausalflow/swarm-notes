---
created_at: '2026-07-17T07:09:05Z'
source_papers:
- '[[openalex-2407.06312-adversarial-dynamical-systems-characterize-when-data-driven]]'
title: Limits of Koopman Spectral Computation
---

**Background:** Koopman operator theory provides a framework for representing nonlinear dynamical systems as linear systems by acting on an infinite-dimensional space of observables. However, identifying conditions that guarantee the reliable computation of spectral properties, such as the spectrum and spectral type, from finite data remains a significant open challenge.

**Question / Future Work:** Determining the specific conditions, such as the modulus of continuity of the dynamics or system-specific geometric properties, that reduce the number of successive data limits required to compute spectral properties of Koopman operators (i.e., the Solvability Complexity Index) remains a critical question for establishing robust convergence guarantees.

**Why It Matters:** This question is essential for establishing a rigorous complexity theory for data-driven modeling, as it directly informs the development of provably robust algorithms and identifies the fundamental trade-offs between system structure, data availability, and algorithm complexity.

**Evidence:** While methods provide SCI upper bounds, a key challenge is determining whether these bounds are optimal. This raises fundamental questions: Can convergence be achieved with fewer limits? If not, what assumptions make it easier?