---
created_at: '2026-03-29T06:07:28Z'
source_papers:
- '[[openalex-2603.24936-tigflow-grpo-trajectory-forecasting-via-interaction-aware-fl]]'
title: Mitigating Long-Horizon Error Accumulation
---

**Background:** Trajectory forecasting models trained purely on observed data can develop accumulated rollout errors over longer prediction horizons, leading to physically implausible or unsafe predictions.

**Question / Future Work:** Future work should focus on developing novel mechanisms or reward structures that can specifically counteract the inherent error accumulation in continuous generative models over extended prediction horizons, thereby ensuring long-term stability beyond the gains observed from initial behavioral alignment.

**Why It Matters:** Improving long-horizon stability is a primary bottleneck for autonomous system planning, as decision-making relies on accurate predictions far into the future.

**Evidence:** Continuous generative forecasting models often become less reliable as the prediction horizon grows, partly because small rollout errors can accumulate over time. To assess this effect, Table 3 reports performance on ETH over extended horizons from 1.2s to 4.8s. [...] This gap suggests that the proposed post-training strategy helps maintain more stable long-horizon predictions.