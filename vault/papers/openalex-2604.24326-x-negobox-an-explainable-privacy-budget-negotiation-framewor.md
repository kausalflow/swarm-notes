---
# CSL-compatible fields
title: "X-NegoBox: An Explainable Privacy-Budget Negotiation Framework for Secure Peer-to-Peer Energy Data Exchange"
author:
  - literal: "Poushali Sengupta"
  - literal: "Sabita Maharjan"
  - literal: "Frank Eliassen"
  - literal: "Yan ZHANG"
issued:
  date-parts:
    - [2026, 4, 27]
url: "https://arxiv.org/abs/2604.24326"

# Custom fields
paper_id: "2604.24326"
paper_source: "openalex"
domain: "nlp"
tags:
  - "differential-privacy"
  - "agent"
  - "autonomous-agent"
  - "interpretability"
  - "explainability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "autonomous-privacy-budget-negotiation-protocol-apbnp"
  - "explainable-agreement-layer-x-contract"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-30T07:25:17Z"
created_at: "2026-04-30T07:25:17Z"
---

# X-NegoBox: An Explainable Privacy-Budget Negotiation Framework for Secure Peer-to-Peer Energy Data Exchange

**Authors**: Poushali Sengupta, Sabita Maharjan, Frank Eliassen, Yan ZHANG
**Date**: 2026-04-27
**Paper ID**: [openalex:2604.24326](https://arxiv.org/abs/2604.24326)

## Summary

X-NegoBox is an explainable framework for secure P2P energy data exchange that replaces fixed privacy policies with adaptive budget negotiation. It utilizes an Autonomous Privacy Budget Negotiation Protocol (APBNP) to calculate privacy budgets based on contextual factors like data sensitivity and historical behavior. To ensure transparency, an Explainable Agreement Layer (X-Contract) provides justifications for decisions, and data remains private within local DataBoxes while only sanitized results are shared after sandbox execution.

## Key Contributions

- Introduces X-NegoBox, a framework enabling adaptive privacy-budget negotiation for P2P energy data exchange.
- Develops the Autonomous Privacy Budget Negotiation Protocol (APBNP) to determine budget allocations based on dynamic trust, sensitivity, and risk metrics.
- Implements an Explainable Agreement Layer (X-Contract) that provides transparent, human-readable justifications for negotiation outcomes.

## Open Questions & Future Work

- [[negotiation-aware-threshold-secret-sharing]]

## Key Concepts

- [[autonomous-privacy-budget-negotiation-protocol-apbnp]]: A protocol that dynamically determines privacy budgets for data requests based on context-aware factors like trust and sensitivity.
- [[explainable-agreement-layer-x-contract]]: A module that provides human- and machine-readable justifications for automated privacy-preserving data exchange decisions.

## Archivist Review

I approved the negotiation protocol and explainable contract layer as these represent a novel, reusable paradigm for privacy-preserving, decentralized data exchange. I also included the proposed open question regarding the integration of negotiation constraints directly into threshold cryptographic schemes, as this identifies a high-level technical bottleneck for secure, policy-aware decentralized systems. No datasets were approved as none were specifically named or central to the paper's claims.

### Approved Concepts
- Autonomous Privacy Budget Negotiation Protocol (APBNP): It is the core negotiation logic proposed to replace static privacy policies in peer-to-peer data exchange.
- Explainable Agreement Layer (X-Contract): Provides the critical transparency mechanism required for user trust in automated privacy negotiation.

### Approved Open Questions
- Negotiation-Aware Threshold Secret Sharing: Integrating policy-aware logic into the cryptographic primitive itself would eliminate the need for a separate, loosely coupled authorization step, potentially enhancing security by ensuring that reconstruction is cryptographically bound to the negotiation outcome.

## Links

- [Abstract](https://arxiv.org/abs/2604.24326)
- [PDF](https://arxiv.org/pdf/2604.24326)

