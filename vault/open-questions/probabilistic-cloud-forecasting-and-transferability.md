---
created_at: '2026-09-06T09:01:08Z'
source_papers:
- '[[openalex-2609.03763-from-nowcasting-to-forecasting-adapting-a-reanalysis-trained]]'
title: Probabilistic Cloud Forecasting and Transferability
---

**Background:** Cloud-cover forecasting models often combine observation-based initial conditions with numerical weather prediction (NWP) dynamics, but extending these models into probabilistic frameworks and verifying them across diverse geographic domains remains underexplored.

**Question / Future Work:** Extend the conditional flow matching (CFM) framework into fully probabilistic or ensemble cloud-cover forecasts to quantify uncertainty, evaluate model transferability across additional years and geographic domains, adapt the direct-prediction setup for sub-hourly forecasts, and optimize the atmospheric forcing variable set.

**Why It Matters:** Crucial for advancing generative and observation-guided weather prediction models toward robust operational uncertainty quantification and multi-region generalization.

**Evidence:** Future work should extend both the forecasting framework and the evaluation. Because the CFM formulation is stochastic, it could be developed into probabilistic or ensemble forecasts that quantify uncertainty in cloud evolution. Evaluation over additional years and geographic domains is also needed to assess the model’s robustness and transferability. The direct-prediction setup could also support sub-hourly forecasts, provided that suitable forcing fields are available at the target times. Finally, the atmospheric forcing set was not extensively optimized in this study; a broader or more carefully selected set of predictors may further improve forecast quality.