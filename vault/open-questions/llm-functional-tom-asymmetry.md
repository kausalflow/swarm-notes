---
created_at: '2026-04-25T06:15:27Z'
source_papers:
- '[[openalex-2604.20443-dialtom-a-theory-of-mind-benchmark-for-forecasting-state-dri]]'
title: Functional vs. Literal ToM Gap
---

**Background:** Theory of Mind (ToM) refers to the cognitive ability to infer and reason about the mental states of others. Benchmarks evaluating this capability often struggle to separate superficial pattern matching from genuine functional reasoning.

**Question / Future Work:** The observed reasoning asymmetry in LLMs, where proficiency in retrospective mental state identification does not translate to prospective dialogue trajectory forecasting, presents a significant bottleneck. It remains unclear whether this gap is an inherent limitation of current model architectures or a failure to ground state representations in causal dynamics, requiring further investigation into decoupling state reasoning from surface-level linguistic correlations.

**Why It Matters:** Understanding this gap is essential for determining if agents can reliably use internal state models to navigate social or complex sequential environments.

**Evidence:** Our results reveal a significant reasoning asymmetry: while LLMs excel at identifying mental states, most... fail to leverage this understanding to forecast social trajectories.