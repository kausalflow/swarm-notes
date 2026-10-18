---
created_at: '2026-10-18T09:13:20Z'
source_papers:
- '[[openalex-2610.21223-learning-and-forecasting-multiscale-spatiotemporal-epidemic]]'
title: Identifiability and Adaptation in Epidemic Neural ODEs
---

**Background:** Epidemic forecasting models often combine heterogeneous data streams within shared representations, leaving the correspondence between information sources and physical processes implicit.

**Question / Future Work:** Investigate how to improve the identifiability of latent epidemic states and learned process fluxes from sparse, delayed, or changing surveillance data, as well as enhancing adaptation to abrupt behavioral shifts and mobility interventions not fully captured by frozen auxiliary networks.

**Why It Matters:** Improving identifiability and adaptability under nonstationary interventions is critical for deploying continuous-time neural epidemic models in real-world public health crises where reporting noise and sudden policy shifts are ubiquitous.

**Evidence:** First, latent epidemic states and learned process fluxes may be only partially identifiable from reported incidence, particularly when observations are sparse, delayed or affected by changes in reporting. Additional epidemiological and behavioral measurements could provide stronger constraints on the hidden dynamics. Second, the auxiliary mobility network is pretrained on historical OD observations and frozen during epidemic-model training. Although its outputs remain dependent on epidemic state and time, its fixed parameters may limit adaptation to abrupt mobility changes caused by interventions or behavioral shifts.