---
created_at: '2026-05-31T08:08:38Z'
source_papers:
- '[[openalex-2605.29611-hierarchical-forecasting-the-role-of-information]]'
title: Role of diverse information sets
---

**Background:** Hierarchical forecasting reconciliation typically assumes that base forecasts are generated from a single, consistent information set, or that base forecast errors are conditionally unbiased. This assumption rarely holds in real-world scenarios where different components of a hierarchy are forecasted by different algorithms using disparate information sets.

**Question / Future Work:** Further research is needed to determine how existing and novel reconciliation methods perform when base forecasts are generated from fundamentally different information sets, particularly in cases where some forecasters possess forward-looking or auxiliary information not captured by univariate historical time series models. Investigating how reconciliation algorithms can systematically combine these diverse information sources without relying on the restrictive assumption of conditional unbiasedness remains a key open challenge.

**Why It Matters:** The authors explicitly state that because current evidence is derived from base forecasts using univariate information, it is difficult to identify whether improvements in reconciled forecasts are due to the imposition of constraints or the combination of information. They propose IComb as a step toward addressing this, but leave the deeper exploration of multi-source information integration as a primary future research direction.