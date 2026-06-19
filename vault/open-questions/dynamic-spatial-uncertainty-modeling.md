---
created_at: '2026-06-19T09:25:33Z'
source_papers:
- '[[openalex-2606.18044-model-based-clustering-of-compositional-trajectories-for-the]]'
title: Dynamic Spatial Uncertainty Modeling
---

**Background:** The compositional representation of mobility trajectories currently utilizes a fixed radius for the circular neighborhood around estimated user positions to calculate road-type proportions. This approach does not account for the varying spatial uncertainty associated with different telephonic cell coverage areas.

**Question / Future Work:** There is a need to develop a dynamic, position-specific approach for defining the neighborhood around estimated user locations in compositional trajectory modeling, incorporating confidence bounds that adapt to the specific size of telephonic cell coverage areas and account for signal-bouncing phenomena.

**Why It Matters:** Ensuring the compositional representation accurately reflects the underlying spatial uncertainty is fundamental to the reliability of mobility pattern extraction.

**Evidence:** However, further research in this direction would be helpful to provide a confidence bound around the estimated positions based on the dimension of the coverage areas and the strength of the phenomenon of bouncing of the telephonic signal.