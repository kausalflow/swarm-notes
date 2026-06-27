---
created_at: '2026-06-27T07:43:35Z'
source_papers:
- '[[openalex-2507.01692-simulation-and-evaluation-of-local-daily-temperature-and-pre]]'
title: Improving climate-aware donor selection
---

**Background:** Statistical downscaling models that rely on the K-nearest donor locations often perform poorly in complex landscapes where geographic proximity does not guarantee climatic similarity.

**Question / Future Work:** Donor selection based solely on Euclidean distance in geographic space can be suboptimal when locations exist near climatological boundaries or in heterogeneous terrains. Future work should investigate more sophisticated donor selection methods, such as mapping stations into a 'climate space' or using clustering based on climatological regimes to ensure that the statistical relationships learned from donor locations are truly representative of the target location.

**Why It Matters:** Effective donor selection is critical to the accuracy of statistical downscaling in complex terrain, and current distance-based heuristics limit the model's reliability in varied climate regimes.