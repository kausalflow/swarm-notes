---
created_at: '2026-06-28T08:17:11Z'
source_papers:
- '[[openalex-2606.27201-explaining-temporal-graph-neural-networks-via-feature-induce]]'
title: Automated Relevance Structure Construction
---

**Background:** Event-based Temporal Graph Neural Networks (ETGNNs) typically rely on complex recurrent architectures where events induce memory updates across nodes to capture long-range temporal dependencies. Existing explanation methods primarily focus on the final embedding and decoding stages, neglecting the information flow within the event processing (EP) module.

**Question / Future Work:** It is currently challenging to automate the construction of relevance structures for complex, modular neural architectures, such as ETGNNs, requiring manual definition of relevance at the module level. Future work is required to develop tools that facilitate the semi-automated construction of relevance structures, enabling a more direct transition from forward computation and LRP rules to actionable explanation insights.

**Why It Matters:** As neural network architectures become increasingly complex and modular, the manual derivation of layer-wise relevance propagation rules for every component becomes a significant bottleneck for deploying robust explainability tools. Automating this process is essential for scaling XAI methods to deeper and more heterogeneous graph-based models.