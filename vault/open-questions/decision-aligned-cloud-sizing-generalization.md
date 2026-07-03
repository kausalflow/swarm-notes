---
created_at: '2026-07-03T07:55:28Z'
source_papers:
- '[[openalex-2606.31470-cloudadv-decision-aligned-instance-sizing-with-zero-shot-fou]]'
title: Generalizing Decision-Aligned Cloud Sizing
---

**Background:** Cloud resource provisioning often relies on static, conservative estimates, and while foundation models offer zero-shot forecasting capabilities, their ability to guarantee safe, decision-aligned sizing under workload drift is not fully understood.

**Question / Future Work:** The performance of zero-shot time-series foundation models for cloud capacity optimization requires broader validation across diverse, heterogeneous workload profiles beyond limited production case studies. Further investigation is needed to quantify the contribution of the LLM layer versus the underlying rule-based sizing policy, and to integrate these systems with robust, continual adaptation mechanisms for environments where periodic re-evaluation is insufficient for non-stationary workloads.

**Why It Matters:** This is critical for bridging the gap between theoretical zero-shot forecasting performance and the reliability requirements of automated, safety-critical cloud infrastructure management.

**Evidence:** The evaluation covers seven production VMs, which constrains the assessment of generalizability to more diverse workload profiles and VM families. ... The pipeline also lacks a direct ablation against a fully rule-based system, which would more precisely quantify the contribution of the LLM layer beyond the sizing policy alone; we leave this comparison to future work. ... Future work will ... incorporate richer contextual signals to improve robustness under workload shift, and explore tighter integration with continual adaptation mechanisms for settings where periodic zero-shot re-evaluation is insufficient.