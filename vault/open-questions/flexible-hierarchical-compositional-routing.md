---
created_at: '2026-08-28T17:01:02Z'
source_papers:
- '[[openalex-2608.24763-mote-mixture-of-task-experts-for-multi-task-video-understand]]'
title: Flexible and Compositional Task Routing
---

**Background:** Large multimodal and video-language models often face stability-plasticity trade-offs and ambiguity when handling multi-task user requests, where soft, hierarchical, or compositional routing strategies are not yet fully supported by discrete task-structured routers.

**Question / Future Work:** Investigate more flexible routing mechanisms, such as soft routing, hierarchical expert structures, or compositional task experts, to effectively handle ambiguous, overlapping, or multi-intent user prompts that fall outside strict discrete task boundaries.

**Why It Matters:** Crucial for extending modular mixtures of task experts from clean, isolated academic benchmarks to real-world, open-ended conversational scenarios involving complex, multi-intent user instructions.

**Evidence:** The prompt-conditioned selector is evaluated on generated variants of five predefined COIN intents, but this controlled result does not cover ambiguous, overlapping, or compositional requests; softer routing, hierarchical experts, or expert composition may be needed in such cases.