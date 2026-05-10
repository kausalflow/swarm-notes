---
created_at: '2026-05-10T07:21:01Z'
source_papers:
- '[[openalex-2605.05736-sdflow-similarity-driven-flow-matching-for-time-series-gener]]'
title: Universal Time-Series Tokenizer
---

**Background:** Time series generation models often rely on dataset-specific VQ tokenizers and fixed codebooks, which limits cross-domain applicability.

**Question / Future Work:** Developing a universal time-series tokenizer with a shared codebook would enable generative frameworks to operate in a unified latent space across multiple domains, facilitating transfer learning and multi-domain generation.

**Why It Matters:** Developing a universal tokenizer is a key bottleneck toward multi-domain generative modeling and improving the generalizability of latent-space generation frameworks.

**Evidence:** Currently, SDFlow uses a dataset-specific VQ tokenizer and codebook. A natural next step is to develop a universal time-series tokenizer with a shared codebook.