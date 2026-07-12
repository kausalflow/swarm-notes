---
created_at: '2026-07-12T07:28:07Z'
source_papers:
- '[[openalex-2607.08641-steering-neural-network-training-through-interpretable-const]]'
title: Local vs global interpretability constraints
---

**Background:** Current explanation-guided learning often relies on global interpretability measures like partial dependence, which may obscure complex, heterogeneous effects. Exploring alternative, localized interpretability constraints could enable finer-grained steering of model training.

**Question / Future Work:** There is a need to evaluate the efficacy of constraining neural network training with alternative, localized interpretation methods such as individual conditional expectation (ICE) and compare them with global measures in terms of predictive performance and explanation faithfulness.

**Why It Matters:** Extending the scope of guided learning beyond global measures is critical for addressing complex datasets where local feature interactions are paramount.