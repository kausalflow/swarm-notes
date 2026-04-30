---
created_at: '2026-04-30T07:25:17Z'
source_papers:
- '[[openalex-2604.24326-x-negobox-an-explainable-privacy-budget-negotiation-framewor]]'
title: Negotiation-Aware Threshold Secret Sharing
---

**Background:** Threshold Secret Sharing (TSS) is used to distribute execution authorization for privacy-preserving data exchanges, ensuring that no single entity can unilaterally authorize the release of data.

**Question / Future Work:** Current deployments utilize standard, general-purpose TSS constructions to authorize the release of differentially private outputs. A critical open problem remains the design of a next-generation, negotiation-aware TSS scheme that can directly embed fine-grained policy constraints—such as those derived from local privacy-budget optimization—into the secret reconstruction process itself.

**Why It Matters:** Integrating policy-aware logic into the cryptographic primitive itself would eliminate the need for a separate, loosely coupled authorization step, potentially enhancing security by ensuring that reconstruction is cryptographically bound to the negotiation outcome.

**Evidence:** Designing a next-generation, negotiation-aware TSS that embeds policy constraints directly into the reconstruction process is left for future work.