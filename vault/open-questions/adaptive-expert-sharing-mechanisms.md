---
created_at: '2026-08-08T05:34:12Z'
source_papers:
- '[[openalex-2608.04695-personalized-federated-sparse-adaptation-of-time-series-foun]]'
title: Adaptive Expert-Sharing Mechanisms
---

**Background:** Time-series foundation models exhibit diverse behaviors when adapted across distributed non-IID clients using personalized mixture-of-experts frameworks, leaving the optimal degree of personalization and expert sharing an open question.

**Question / Future Work:** Investigate adaptive expert-sharing mechanisms that dynamically determine which experts should be globally shared and which should remain client-specific, potentially combined with meta-learned adapters for rapid client adaptation.

**Why It Matters:** Understanding how to optimally partition and dynamically share expert modules across heterogeneous clients is critical for maximizing both cross-client transfer and local personalization in foundation model federated learning.

**Evidence:** The backbone-dependent behavior observed across MOMENT, Chronos-2, and Moirai suggests that there is no universally optimal personalization strategy for federated TSFM adaptation. Instead, the degree of personalization may itself need to be learned. Future work could develop adaptive expert-sharing mechanisms that dynamically determine which experts should be shared globally and which should remain client-specific, potentially combined with meta-learned adapters that enable rapid adaptation to new clients.