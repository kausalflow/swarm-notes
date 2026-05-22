---
created_at: '2026-05-22T08:18:07Z'
source_papers:
- '[[openalex-2605.20085-spatially-prompted-visual-trajectory-prediction-for-egocentr]]'
title: Mitigating Compounding Stitched Drift
---

**Background:** Spatially prompted visual trajectory prediction (SP-VTP) relies on open-loop generation, where long-horizon motion plans are often formed by stitching individual short-term trajectory chunks.

**Question / Future Work:** Accumulated drift occurs during the stitching of independently predicted trajectory chunks over extended episodes, especially under significant camera or end-effector motion; investigating techniques to mitigate these compounding errors is necessary to move from open-loop prediction to robust closed-loop execution.

**Why It Matters:** This is a fundamental limitation of the proposed autoregressive or chunked-prediction paradigm, which currently prevents reliable long-term deployment in closed-loop systems.