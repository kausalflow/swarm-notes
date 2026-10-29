---
# CSL-compatible fields
title: "Revealing Imaging Characteristics of Thermal Wakes from Underwater Vehicles Without Cooling-Water Discharge"
author:
  - literal: "Guoyi Zhang"
  - literal: "Yanjin Du"
  - literal: "Guangsheng Xu"
  - literal: "Zhengyao Zhao"
  - literal: "Siyang Chen"
  - literal: "Jingjing Gao"
  - literal: "Yuezheng Zhou"
  - literal: "Yiyang Wu"
  - literal: "Bin Wu"
  - literal: "T Zhang"
  - literal: "Lejia Ye"
  - literal: "Donghe Wang"
  - literal: "Jie Wang"
  - literal: "Kaiye Hu"
  - literal: "Zhipeng Ren"
  - literal: "Han Wang"
  - literal: "Boo Cheong Khoo"
  - literal: "Xiangpeng Xu"
  - literal: "Xiaohu Zhang"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2610.35038"

# Custom fields
paper_id: "2610.35038"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "benchmark"
  - "dataset"
  - "robustness"
architectures:
  []
datasets:
  - "avp-ir-wake"
concept_slugs:
  []
dataset_slugs:
  - "avp-ir-wake"
skill: "TimeSeriesSkill"
processed_at: "2026-10-29T11:12:03Z"
created_at: "2026-10-29T11:12:03Z"
---

# Revealing Imaging Characteristics of Thermal Wakes from Underwater Vehicles Without Cooling-Water Discharge

**Authors**: Guoyi Zhang, Yanjin Du, Guangsheng Xu, Zhengyao Zhao, Siyang Chen, Jingjing Gao, Yuezheng Zhou, Yiyang Wu, Bin Wu, T Zhang, Lejia Ye, Donghe Wang, Jie Wang, Kaiye Hu, Zhipeng Ren, Han Wang, Boo Cheong Khoo, Xiangpeng Xu, Xiaohu Zhang
**Date**: 2026-10-26
**Paper ID**: [openalex:2610.35038](https://arxiv.org/abs/2610.35038)

## Summary

This paper investigates the infrared thermal wake characteristics of uncrewed underwater vehicles without cooling-water discharge, introducing the AVP-IR-Wake benchmark of over 161,485 real-world frames. The authors reveal that while individual wake vortices are locally indistinguishable from background clutter, they exhibit global morphological separability governed by vehicle trajectories. This insight demonstrates that reliable wake detection must abandon conventional compact target assumptions in favor of global trajectory-constrained physical modeling.

## Key Contributions

- Established AVP-IR-Wake, the first large-scale, real-world, physically diverse infrared thermal wake benchmark comprising 161,485 frames collected over three years.
- Demonstrated local indistinguishability where individual wake vortices are statistically identical to wind-induced background vortices across temporal, frequency, and sparse domains.
- Established global morphological separability, showing that reliable thermal wake detection requires shifting from local feature extraction to global trajectory-constrained physical modeling.

## Limitations

Forecasting wake observability remains challenging due to global and seasonal variations in the ocean cold-skin layer, necessitating deeper integration of physical oceanography and atmospheric science.

## Open Questions & Future Work

- [[broad-oceanic-regime-observability]]

## Archivist Review

In accordance with the stringent vault guidelines, we maintain high selectivity by approving only the primary benchmark dataset (AVP-IR-Wake) and one non-redundant open question concerning broad oceanic regime observability. Other candidates were either domain-specific or overlapped with existing physics-constrained modeling entries.

### Approved Open Questions
- Broad Oceanic Regime Observability: Crucial for transitioning thermal wake surveillance from localized port environments to general oceanic deployment under varying climatic and meteorological regimes.

### Rejected Candidates
- [open_question] Physics-Constrained Global Detection Models (`physics-constrained-global-detection`) - duplicate_existing: Redundant with existing open questions on physics-guided and trajectory-constrained state estimation in the vault.

## Datasets

- [[avp-ir-wake]]

## Links

- [Abstract](https://arxiv.org/abs/2610.35038)
- [PDF](https://arxiv.org/pdf/2610.35038)

