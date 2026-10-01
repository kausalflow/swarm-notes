---
created_at: '2026-10-01T11:15:39Z'
source_papers:
- '[[openalex-2609.34783-tqts-bench-a-multi-syntax-benchmark-for-text-to-query-over-t]]'
title: Generalizable Text-to-Query over TSDBs
---

**Background:** Large language models perform well on relational database text-to-query tasks but their capabilities over time-series databases remain limited due to heterogeneous syntaxes, diverse application domains, and time-specific query intents.

**Question / Future Work:** Investigate and develop generalized text-to-query methods that can seamlessly adapt to non-unified query syntaxes, heterogeneous schema structures (such as metrics, labels, and tags), and large-scale schemas across diverse time-series database management systems without suffering from domain-specific performance degradation.

**Why It Matters:** Existing text-to-query methods are either tightly coupled to specific SQL/RDB structures or single-system TSDB variants like PromQL, exhibiting poor generalizability across the 23+ different syntaxes found in modern time-series databases.

**Evidence:** These findings highlight new opportunities to narrow the gap between current LLM capabilities and the requirements of TSDB queries in real-world applications.