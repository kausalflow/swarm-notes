---
created_at: '2026-05-31T08:10:07Z'
source_papers:
- '[[openalex-2605.29467-composing-non-conjugate-factor-graphs-with-closed-form-varia]]'
title: Minimal Alphabet for Inference
---

**Background:** Probabilistic models composed of hierarchical building blocks often lack closed-form inference, forcing reliance on black-box variational inference or sampling methods. The potential to compose arbitrary probabilistic architectures while preserving closed-form updates is constrained by the limited availability of modular building blocks that satisfy conjugacy properties.

**Question / Future Work:** The search for an exhaustive set of probabilistic factors that support universal function approximation while maintaining closed-form inference remains an open challenge. It is currently unknown if the current primitives are minimal, or if there exist smaller or more efficient sets of factors that guarantee similar analytical tractability and expressiveness.

**Why It Matters:** Identifying a minimal or optimal alphabet is technically critical for reducing the complexity of factor graph construction, minimizing the memory footprint of inference algorithms, and broadening the library of available building blocks for expressive probabilistic programming.