---
created_at: '2026-09-10T09:16:10Z'
source_papers:
- '[[openalex-2609.09062-multi-task-learning-for-sparsely-labeled-time-series-a-case]]'
title: Robust Task Embedding Transfer Learning
---

**Background:** Task embedding models utilizing learned dense vectors provide strong performance in multi-task learning settings, but their adaptation to transfer learning via direct target embedding optimization often results in negative transfer.

**Question / Future Work:** Develop more robust optimization techniques or structural constraints for learning task embedding vectors during transfer learning so that new target tasks can effectively leverage source task spaces without suffering from optimization degradation.

**Why It Matters:** Understanding why target embedding optimization fails during transfer learning is crucial for enabling zero-shot or few-shot adaptation in sparse multi-task time series applications.

**Evidence:** However, transfer via the embedding model appears to significantly hurt performance compared to the MTL embedding models and even the STL model, indicating negative transfer.