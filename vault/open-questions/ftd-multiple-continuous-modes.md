---
created_at: '2026-03-29T06:08:18Z'
source_papers:
- '[[openalex-2603.25530-adaptive-subspace-modeling-with-functional-tucker-decomposit]]'
title: Expand FTD to multiple continuous modes
---

**Background:** The Functional Tucker Decomposition (FTD) framework is currently restricted to models with only one continuous tensor mode due to computational considerations in solving for the core tensor.

**Question / Future Work:** The current formulation of the Functional Tucker Decomposition (FTD) is limited to a single continuous mode, which constrains its applicability in complex scenarios such as analyzing multi-channel medical data like electrocardiogram (ECG) or electroencephalogram (EEG) signals where multiple modes may require functional modeling. Investigating the expansion of FTD to support multiple continuous modes is necessary for broader application in these domains.

**Why It Matters:** Expanding to multiple continuous modes is crucial for complex, multi-channel medical time-series analysis, significantly increasing the method's utility beyond its current single-mode limitation.

**Evidence:** For instance, the current formulation is restricted to one continuous mode because of computational considerations regarding the solution for the core tensor. Even though this setup already covers many real-world applications, an expansion to an FTD with multiple continuous modes could be interesting for medical challenges such as the analysis of electrocardiogram (ECG) or electroencephalogram (EEG) data with multiple channels.