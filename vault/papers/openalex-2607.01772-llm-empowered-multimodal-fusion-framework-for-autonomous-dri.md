---
# CSL-compatible fields
title: "LLM-Empowered Multimodal Fusion Framework for Autonomous Driving: Semantic Enhancement and Channel-Adaptive Design"
author:
  - literal: "Wen Wang"
  - literal: "Yaping Sun"
  - literal: "Yejun He"
  - literal: "Hao Chen"
  - literal: "Zhiyong Chen"
  - literal: "X X Xu"
  - literal: "Nan Ma"
  - literal: "Shuguang Cui"
issued:
  date-parts:
    - [2026, 7, 2]
url: "https://arxiv.org/abs/2607.01772"

# Custom fields
paper_id: "2607.01772"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "llm"
  - "multimodal"
  - "vision-language-model"
  - "lora"
  - "mixture-of-experts"
  - "trajectory-prediction"
  - "autonomous-agent"
architectures:
  []
datasets:
  - "nuScenes"
  - "VIRAT"
concept_slugs:
  - "lm-scip-framework"
dataset_slugs:
  - "nuscenes"
  - "virat"
skill: "TimeSeriesSkill"
processed_at: "2026-07-05T07:53:33Z"
created_at: "2026-07-05T07:53:33Z"
---

# LLM-Empowered Multimodal Fusion Framework for Autonomous Driving: Semantic Enhancement and Channel-Adaptive Design

**Authors**: Wen Wang, Yaping Sun, Yejun He, Hao Chen, Zhiyong Chen, X X Xu, Nan Ma, Shuguang Cui
**Date**: 2026-07-02
**Paper ID**: [openalex:2607.01772](https://arxiv.org/abs/2607.01772)

## Summary

The LM-SCIP framework addresses the challenge of dynamically varying fusion quality in autonomous driving by using an LLM as a central reasoning core for multimodal fusion. The architecture integrates a hierarchical encoder with a Channel-Adaptive Semantic Module (CASM) that uses channel prompts to gate radar features based on current input quality. A LoRA-tuned LLM combined with a heterogeneous Mixture-of-Experts (H-MoE) then arbitrates between local visual cues and external radar context to improve localization and trajectory forecasting accuracy. Experimental results on the nuScenes and VIRAT datasets demonstrate robust performance across varying Signal-to-Noise Ratio (SNR) conditions.

## Key Contributions

- Introduces LM-SCIP, a Large Language Model-centric framework for robust multimodal perception in autonomous driving.
- Proposes the Channel-Adaptive Semantic Module (CASM) to map link quality indicators into prompts that dynamically gate radar features.
- Achieves a 40.0% reduction in localization RMSE on the nuScenes dataset compared to a vision-only baseline by enabling robust vision-dominant fallbacks at low SNR.

## Open Questions & Future Work

- [[multi-agent-prompt-sharing]]

## Key Concepts

- [[lm-scip-framework]]: An LLM-centric framework for autonomous driving that uses channel-adaptive semantic reasoning to dynamically arbitrate between multimodal perception streams based on signal quality.

## Archivist Review

The paper proposes a relevant framework for LLM-mediated multimodal fusion in autonomous driving. I approved the framework and a core research question regarding communication constraints in multi-agent settings. Sub-components were rejected as they are best captured within the framework's overarching definition.

### Approved Concepts
- LM-SCIP Framework: It introduces an LLM-centric reasoning core for dynamically fusing multi-modal (vision and radar) streams by leveraging channel quality information as prompts, a strategy likely to recur in robust perception.

### Approved Open Questions
- Multi-Agent Prompt-Level Sharing: Scaling collaborative intelligence while accounting for realistic communication bottlenecks is a critical challenge for urban-scale autonomous deployment.

### Rejected Candidates
- [concept] Channel-Adaptive Semantic Module (CASM) (`casm-module`) - subcomponent_of_broader_mechanism: This is a sub-component of the LM-SCIP architecture and is adequately covered by the broader framework note.

## Datasets

- [[nuscenes]]
- [[virat]]

## Links

- [Abstract](https://arxiv.org/abs/2607.01772)
- [PDF](https://arxiv.org/pdf/2607.01772)

