---
created_at: '2026-06-14T08:38:07Z'
source_papers:
- '[[openalex-2606.12990-exposure-bias-as-epistemic-underidentification-in-recursive]]'
title: Richer Provenance Representations
---

**Background:** Recursive forecasting models are typically trained using teacher forcing on observed data but deployed autoregressively on self-generated states, a mismatch often cited as the cause of exposure bias. Theoretical analysis suggests this deployment process functions as an epistemic underidentification problem when the state representation is insufficient to uniquely determine the corrective target.

**Question / Future Work:** Research is needed to develop and evaluate richer, more effective induced-state summaries, such as deep rollout traces, uncertainty estimates, or structured latent-state representations that better capture the information required to align training targets with deployment needs beyond simple binary provenance indicators.

**Why It Matters:** This question identifies a critical bottleneck in leveraging provenance for improving recursive forecasting, moving beyond the current limitations of simplistic binary flags toward more robust, information-rich state representations.

**Evidence:** Richer induced-state summaries may be more effective, including rollout depth, uncertainty estimates, latent-state summaries, or structured traces of state construction.