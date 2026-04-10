---
# CSL-compatible fields
title: "Flowr -- Scaling Up Retail Supply Chain Operations Through Agentic AI in Large Scale Supermarket Chains"
author:
  - literal: "Eranga Bandara"
  - literal: "Ross Gore"
  - literal: "Sachin Shetty"
  - literal: "Piumi Siyambalapitiya"
  - literal: "Sachini Rajapakse"
  - literal: "Isurunima Kularathna"
  - literal: "Pramoda Karunarathna"
  - literal: "Ravi Mukkamala"
  - literal: "Peter Foytik"
  - literal: "Safdar Hussain Bouk"
  - literal: "Abdul Rahman"
  - literal: "Xueping Liang"
  - literal: "Amin Hass"
  - literal: "Tharaka Hewa"
  - literal: "Ng Wee Keong"
  - literal: "Kasun De Zoysa"
  - literal: "Aruna Withanage"
  - literal: "Nilaan Loganathan"
issued:
  date-parts:
    - [2026, 4, 7]
url: "https://arxiv.org/abs/2604.05987"

# Custom fields
paper_id: "2604.05987"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "agent"
  - "autonomous-agent"
  - "tool-use"
architectures:
  []
datasets:
  []
concept_slugs:
  - "flowr-agentic-ai-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-10T06:27:38Z"
created_at: "2026-04-10T06:27:38Z"
---

# Flowr -- Scaling Up Retail Supply Chain Operations Through Agentic AI in Large Scale Supermarket Chains

**Authors**: Eranga Bandara, Ross Gore, Sachin Shetty, Piumi Siyambalapitiya, Sachini Rajapakse, Isurunima Kularathna, Pramoda Karunarathna, Ravi Mukkamala, Peter Foytik, Safdar Hussain Bouk, Abdul Rahman, Xueping Liang, Amin Hass, Tharaka Hewa, Ng Wee Keong, Kasun De Zoysa, Aruna Withanage, Nilaan Loganathan
**Date**: 2026-04-07
**Paper ID**: [openalex:2604.05987](https://arxiv.org/abs/2604.05987)

## Summary

Flowr is an agentic AI framework designed to automate decision-intensive retail supply chain operations, such as procurement and inventory replenishment, which are traditionally managed manually. The system utilizes a hierarchy of domain-specialized LLMs coordinated by a central reasoning model, ensuring task accuracy while integrating human-in-the-loop oversight through a Model Context Protocol (MCP)-enabled interface. Evaluation on a large-scale supermarket chain demonstrates that Flowr effectively scales operations, reduces manual coordination, and improves proactive exception handling compared to fragmented, reactive legacy workflows.

## Key Contributions

- Introduces Flowr, an agentic AI framework that decomposes manual supply chain workflows into specialized, LLM-driven agents for end-to-end automation.
- Implements a central reasoning LLM orchestration model paired with Model Context Protocol (MCP) to facilitate human-in-the-loop supervision and maintain organizational accountability.
- Validates the framework within a large-scale supermarket chain, demonstrating a significant reduction in manual coordination overhead and enhanced proactive exception handling.

## Open Questions & Future Work

- [[long-term-impact-and-federated-agentic-supply-chain-workflows]]

## Key Concepts

- [[flowr-agentic-ai-framework]]: A framework that decomposes complex supply chain workflows into specialized, AI-coordinated agents for end-to-end automation.

## Archivist Review

I have approved the Flowr framework as a notable instance of agentic decomposition for enterprise workflows and identified the research need for federated agentic systems in supply chain contexts as a meaningful open problem. Other candidates were either redundant or covered by the primary contributions. Standard selectivity was applied to ensure the vault focuses on generalizable architectural patterns rather than paper-specific implementation details.

### Approved Concepts
- Flowr Agentic AI Framework: It provides a systematic methodology for decomposing complex, decision-intensive manual supply chain operations into specialized, coordinated agentic roles.

### Approved Open Questions
- Federated Agentic Supply Chain Workflows: Establishing longitudinal impact metrics and cross-organizational federated workflows is essential for moving agentic AI from proof-of-concept demonstrations to sustainable, scalable, and trustworthy enterprise-wide automation.

### Rejected Candidates
- [concept] Flowr Agentic AI Framework (`flowr-agentic-ai-framework`) - duplicate_existing: Already approved as a central framework.

## Links

- [Abstract](https://arxiv.org/abs/2604.05987)
- [PDF](https://arxiv.org/pdf/2604.05987)

