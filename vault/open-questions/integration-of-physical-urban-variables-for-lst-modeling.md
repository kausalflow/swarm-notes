---
created_at: '2026-05-16T07:10:08Z'
source_papers:
- '[[openalex-2605.13566-spatiotemporal-downscaling-and-nowcasting-of-urban-land-surf]]'
title: Integrating physical urban variables
---

**Background:** Land Surface Temperature (LST) patterns are significantly influenced by urban characteristics such as land cover, vegetation, and geometry, which regulate the surface energy balance. While current models rely on geostationary and polar-orbiting satellite thermal data, they often exclude these physical urban variables, relying instead on implicit encoding of these factors within the temperature signal.

**Question / Future Work:** It remains unresolved how explicitly incorporating physical urban variables—such as land cover composition, vegetation indices, sky view factors, and anthropogenic heat sources—into deep learning models would impact their predictive accuracy, generalization capabilities, and physical interpretability. Research is needed to determine whether these variables can be effectively integrated as auxiliary features without introducing unwanted city-specific biases or complicating model training.

**Why It Matters:** The current data-minimal approach may be reaching an accuracy ceiling in complex urban environments; assessing the feasibility of adding exogenous physical constraints is critical for advancing towards physically-informed, more robust forecasting models.