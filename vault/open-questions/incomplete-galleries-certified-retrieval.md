---
created_at: '2026-11-01T11:33:17Z'
source_papers:
- '[[openalex-2610.40579-when-imputation-changes-the-nearest-neighbor-exact-certifica]]'
title: Certified Retrieval with Incomplete Galleries
---

**Background:** Time series similarity search often encounters missing values, requiring imputation methods that can alter the retrieved nearest neighbors depending on how gaps are filled.

**Question / Future Work:** Investigate the extension of certified similarity retrieval frameworks to handle incomplete reference galleries rather than relying exclusively on complete historical data.

**Why It Matters:** Real-world databases routinely feature missing values in both queries and historical galleries, making single-sided completeness a major bottleneck for scalable deployment.

**Evidence:** Future work includes incomplete galleries, window minima on trees or graphs, and retrieval by worst-case regret.