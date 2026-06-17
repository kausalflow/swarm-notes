---
# CSL-compatible fields
title: "Artificial Intelligence for Power-Converter-Rich Electrical Systems: A Review"
author:
  - literal: "Pengfeng Lin"
  - literal: "Yuan Gao"
  - literal: "Yuxi Tang"
  - literal: "Muhammad Waqas Qaisar"
  - literal: "Peifeng Hui"
  - literal: "Chuanlin Zhang"
  - literal: "Miao Zhu"
  - literal: "Peng Wang"
issued:
  date-parts:
    - [2026, 6, 14]
url: "https://arxiv.org/abs/2606.15948"

# Custom fields
paper_id: "2606.15948"
paper_source: "openalex"
domain: "nlp"
tags:
  - "reinforcement-learning"
  - "robotics"
  - "forecasting"
  - "robustness"
  - "interpretability"
  - "safety"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-17T09:27:57Z"
created_at: "2026-06-17T09:27:57Z"
---

# Artificial Intelligence for Power-Converter-Rich Electrical Systems: A Review

**Authors**: Pengfeng Lin, Yuan Gao, Yuxi Tang, Muhammad Waqas Qaisar, Peifeng Hui, Chuanlin Zhang, Miao Zhu, Peng Wang
**Date**: 2026-06-14
**Paper ID**: [openalex:2606.15948](https://arxiv.org/abs/2606.15948)

## Summary

This paper reviews the integration of artificial intelligence into power-converter-rich electrical systems, addressing the limitations of traditional physics-based modeling under complex, nonlinear dynamics. It categorizes AI applications across the full system life-cycle, including converter design, real-time control, and system-level operations. By evaluating deployment-readiness and technical gaps such as safety certification and sim-to-real transfer, the authors offer a structured guide for transitioning AI tools into safety-critical infrastructure.

## Key Contributions

- Provides a systematic review of AI applications across the life-cycle of power-converter-rich electrical systems, covering design, real-time control, system operation, and compliance governance.
- Establishes a taxonomy of AI-based methods tailored for the unique challenges of inverter-based resources, such as nonlinear dynamics, multi-physics tradeoffs, and sub-millisecond control requirements.
- Identifies deployment-critical barriers for AI, including safety certification, sim-to-real transfer, and cybersecurity, providing a roadmap for translating engineering research into reliable power infrastructure.

## Open Questions & Future Work

- [[sim-to-real-transfer-power-electronics]]
- [[ai-extrapolation-uncertainty-power-systems]]

## Archivist Review

This paper is a review article and does not introduce novel technical concepts but provides a comprehensive taxonomy of AI in power systems. I have approved two open questions that capture the fundamental deployment-critical bottlenecks identified by the review: sim-to-real transfer and extrapolation robustness, which are essential for any AI adoption in safety-critical infrastructure.

### Approved Open Questions
- Bridging sim-to-real gaps: Without bridging this gap, learning-based control for power converters cannot be trusted for critical infrastructure where performance must be guaranteed despite model inaccuracies and hardware limitations.
- Robustness and extrapolation limitations: Extrapolation failure in power systems can lead to catastrophic hardware damage or grid instability; defining the operational boundary of an AI model is essential for safety certification.

## Links

- [Abstract](https://arxiv.org/abs/2606.15948)
- [PDF](https://arxiv.org/pdf/2606.15948)

