---
created_at: '2026-05-14T07:37:36Z'
source_papers:
- '[[openalex-2605.09870-intervention-based-time-series-causal-discovery-via-simulato]]'
title: Certifying Simulator Fidelity Bottlenecks
---

**Background:** Physical simulators allow for the generation of interventional data that can be used to identify causal structures that are otherwise non-identifiable from observational data alone. The fidelity of these simulators is a crucial but often unquantified factor that influences the accuracy and reliability of the discovered causal effects.

**Question / Future Work:** There is a need for a formal framework to certify simulator fidelity in causal discovery pipelines, specifically addressing how simulator bias impacts the validity of causal sign estimation. Developing certified bounds on simulator error is critical to preventing systematic causal reversal errors.

**Why It Matters:** This is a fundamental bottleneck because without a way to bound simulator fidelity, the causal conclusions drawn from these methods are inherently subject to unquantifiable systematic errors.

**Evidence:** None of these strategies provides a certified bound on δ𝒮; that would require access to the true interventional distribution.