---
# CSL-compatible fields
title: "Cluster gravitational redshifts: uncertainties and survey requirements"
author:
  - literal: "Eleni Tsaprazi"
  - literal: "Giorgio F. Lesci"
  - literal: "Federico Marulli"
  - literal: "Alan F. Heavens"
  - literal: "Enrico Maraboli"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25339"

# Custom fields
paper_id: "2603.25339"
paper_source: "openalex"
domain: "physics"
tags:
  - "forecasting"
  - "model,gravitational-redshift,modified-gravity,survey-design"
architectures:
  []
datasets:
  []
concept_slugs:
  - "cluster-gravitational-redshifts-modified-gravity-probe"
  - "halo-occupation-distribution-population-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-29T06:09:24Z"
created_at: "2026-03-29T06:09:24Z"
---

# Cluster gravitational redshifts: uncertainties and survey requirements

**Authors**: Eleni Tsaprazi, Giorgio F. Lesci, Federico Marulli, Alan F. Heavens, Enrico Maraboli
**Date**: 2026-03-26
**Paper ID**: [openalex:2603.25339](https://arxiv.org/abs/2603.25339)

## Summary

This paper presents an end-to-end forecasting pipeline to quantify the achievable precision of cluster gravitational redshifts as a probe for modified gravity, parametrized by a linear rescaling $\alpha_{\mathrm{MG}}$. The methodology involves generating synthetic galaxy catalogues using a Halo Occupation Distribution (HOD) model, applying survey-like selections, and systematically varying observational uncertainties. The authors find that velocity dispersion imposes a hard limit on redshift precision gains and that spectroscopic surveys are preferable to photometric ones for this cosmological constraint. A critical finding is that accurate cluster centering is essential in upcoming high signal-to-noise surveys to avoid systematic biases mimicking new physics.

## Key Contributions

- Established an end-to-end forecasting pipeline, combining generative modeling, HOD, and survey simulations, to assess the precision of cluster gravitational redshifts ($\alpha_{\mathrm{MG}}$) as a modified gravity probe.
- Determined that intracluster velocity dispersion sets an effective floor, with no precision improvement for $\alpha_{\mathrm{MG}}$ beyond redshift precision of $\sigma_z\sim 10^{-4}(1+z)$.
- Concluded that shallow, narrower spectroscopic surveys are more advantageous than deep, wide photometric surveys for obtaining precise constraints on modified gravity parameters.
- Identified accurate determination of cluster centres as an essential requirement for upcoming high Signal-to-Noise surveys to prevent misinterpreting systematic centering errors as new physics.

## Limitations

The study focuses on forecasting pipeline sensitivity, implicitly assuming the underlying theoretical parameterization ($\alpha_{\mathrm{MG}}$) is sufficient to capture all relevant modifications to GR.</em>',open_questions:[],published:

## Open Questions & Future Work

- [[exploring-post-GW170817-modified-gravity-models]]
- [[accurate-cluster-center-determination-strategies]]
- [[self-consistent-modified-gravity-simulations]]

## Key Concepts

- [[cluster-gravitational-redshifts-modified-gravity-probe]]: Using the gravitational redshift of galaxies within galaxy clusters to constrain deviations from General Relativity (GR) via a parameter $\\alpha_{\\mathrm{MG}}$.
- [[halo-occupation-distribution-population-model]]: A five-parameter statistical model used to populate dark matter haloes with observable galaxies based on halo mass and other properties.

## Archivist Review

Approved two core concepts: the central observable (Gravitational Redshifts as a Probe) and a key simulation component (HOD Model). For open questions, three candidates were rejected as they primarily describe general follow-up or required infrastructure development. Three remain: one on exploring viable modified gravity models post-GW170817, one on solving the critical center-determination systematic, and one on the necessity of self-consistent modified-gravity simulations, all of which represent substantial methodological or physical bottlenecks for this research program.

### Approved Concepts
- Cluster Gravitational Redshifts as a Modified Gravity Probe: The entire paper focuses on establishing and quantifying the precision of this specific cosmological probe.
- Halo Occupation Distribution (HOD) Population Model: The HOD is a critical, explicit modeling component used to generate the synthetic member galaxy catalog necessary for the forecasting pipeline.

### Approved Open Questions
- Investigate viable modified gravity models: The current analysis focuses on parameterizations compatible with standard modified gravity models; exploring new, viable models is necessary for a comprehensive test of modified gravity.
- Develop accurate cluster center proxies: Accurate center determination is critical because mis-centering can introduce systematic shifts that mimic deviations from GR at the level required by high-precision Stage-IV/V surveys.
- Develop self-consistent modified gravity simulations: Ignoring self-consistent structure formation in modified gravity may introduce model biases that become significant as statistical errors decrease.

### Rejected Candidates
- [open_question] Exploit future spectroscopic facilities (`future-survey-exploitation-gravitational-redshifts`) - low_impact: This open question is essentially boilerplate future work emphasizing the use of named surveys, rather than pointing to a specific unsolved technical mechanism.
- [open_question] Explore richer gravity parameterizations (`explore-comprehensive-modified-gravity-parameterizations`) - low_impact: While this is a reasonable research direction, the paper suggests it as a natural follow-up rather than identifying a specific, deep, unresolved technical bottleneck in the methodology itself.
- [open_question] Propagate mass uncertainties and match survey specifics (`propagate-mass-uncertainties-match-surveys`) - low_impact: This summarizes general next steps in applying the pipeline (propagating calibration errors and matching survey specs) but does not isolate a unique, deep, unresolved technical challenge.

## Links

- [Abstract](https://arxiv.org/abs/2603.25339)
- [PDF](https://arxiv.org/pdf/2603.25339)

