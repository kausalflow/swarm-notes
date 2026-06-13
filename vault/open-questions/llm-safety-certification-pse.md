---
created_at: '2026-06-13T08:16:30Z'
source_papers:
- '[[openalex-2606.11589-large-language-models-in-process-systems-engineering-opportu]]'
title: Safety Certification for LLM-PSE
---

**Background:** Large Language Models (LLMs) operate on probabilistic next-token prediction, which fundamentally lacks formal verification and safety guarantees necessary for critical industrial process control. Conventional control systems are designed for high-frequency, safety-critical execution, while LLMs operate with higher latency and opacity, necessitating a clear definition of their safe, reliable role in industrial environments.

**Question / Future Work:** It remains an open research question how to establish rigorous validation and safety certification frameworks for LLM-based systems deployed in industrial process control. Currently, no established pathway exists to certify an LLM as part of a safety function, requiring further development of formal verification of neural networks and uncertainty quantification methods to enable their use in higher-stakes settings.

**Why It Matters:** Addressing this is critical for moving beyond advisory roles to potential autonomous or safety-critical industrial applications, as current methods fail to meet the rigorous functional safety standards required in process industries.