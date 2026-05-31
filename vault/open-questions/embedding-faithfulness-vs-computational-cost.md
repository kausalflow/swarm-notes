---
created_at: '2026-05-31T08:11:04Z'
source_papers:
- '[[openalex-2605.30213-faithful-embeddings-of-irregular-and-asynchronous-data-for-o]]'
title: Faithfulness vs. Computational Cost
---

**Background:** Neural controlled differential equations model continuous-time hidden state evolution driven by a control path. The choice of how to embed discrete, irregular, and asynchronous observations into a continuous driving path is a significant design decision that can impact model robustness and computational efficiency.

**Question / Future Work:** An unresolved challenge is determining the optimal balance between injectivity and computational cost in embeddings, specifically regarding the inclusion of auxiliary channels. While these channels ensure a faithful embedding, they increase the driving path dimension and the resulting log-signature computation cost, creating a trade-off between mathematical theoretical faithfulness and practical efficiency for high-dimensional or high-depth applications.

**Why It Matters:** This trade-off between theoretical faithfulness (injectivity) and practical computational scalability is a fundamental bottleneck for deploying continuous-time models on complex real-world sequential data.