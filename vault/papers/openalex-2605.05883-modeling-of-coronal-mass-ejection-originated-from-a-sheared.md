---
# CSL-compatible fields
title: "Modeling of Coronal Mass Ejection Originated from a Sheared Arcade of Realistic Active-Region Scale and Its Propagation in the Heliosphere: Methodology"
author:
  - literal: "Chaowei Jiang"
  - literal: "Xueshang Feng"
  - literal: "Liping Yang"
  - literal: "Huichao Li"
  - literal: "Jinhan Guo"
  - literal: "Pingbing Zuo"
  - literal: "Yi Wang"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.05883"

# Custom fields
paper_id: "2605.05883"
paper_source: "openalex"
domain: "robotics"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:23:50Z"
created_at: "2026-05-10T07:23:50Z"
---

# Modeling of Coronal Mass Ejection Originated from a Sheared Arcade of Realistic Active-Region Scale and Its Propagation in the Heliosphere: Methodology

**Authors**: Chaowei Jiang, Xueshang Feng, Liping Yang, Huichao Li, Jinhan Guo, Pingbing Zuo, Yi Wang
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.05883](https://arxiv.org/abs/2605.05883)

## Summary

This paper presents a high-resolution, end-to-end magnetohydrodynamic (MHD) simulation methodology for modeling coronal mass ejections (CMEs) from solar active regions to the heliosphere. By employing block-structured adaptive mesh refinement and a novel semi-relativistic Boris correction, the model achieves critical resolution of active regions and handles high magnetic field strengths efficiently. The framework successfully reproduces CME initiation, structure, and 1 au arrival characteristics while maintaining sufficient computational speed for practical forecasting applications.

## Key Contributions

- Developed an end-to-end magnetohydrodynamic (MHD) modeling framework for Coronal Mass Ejections (CMEs) from solar active regions to 1.5 au.
- Implemented a block-structured adaptive mesh refinement (AMR) scheme achieving ~700 km resolution in the low corona with under 10^8 grid points.
- Introduced a semi-relativistic Boris correction and relativistic mass-density factor to enable stable simulation of 10^3 G magnetic field strengths without excessive time-step constraints.
- Demonstrated a computational efficiency of approximately one day on 600 processors for a full solar-to-Earth propagation simulation, enabling predictive lead times of two days.

## Open Questions & Future Work

- [[realistic-thermodynamics-in-cme-mhd-models]]
- [[data-driven-initialization-for-cme-simulations]]

## Archivist Review

The paper presents a specialized magnetohydrodynamic simulation framework for space weather forecasting. As the focus is on the physics of solar-to-Earth simulation, I have approved the two proposed open questions regarding thermodynamic modeling and observational data initialization, which are critical research bottlenecks for the field. No new concepts were approved as the core technical contributions are simulation-specific implementation choices rather than generally reusable ML forecasting concepts.

### Approved Open Questions
- Realistic Thermodynamics in CME Models: Refining the thermodynamic treatment is critical for accurately modeling the background solar wind environment through which CMEs propagate, as it directly impacts the density, temperature, and velocity structures that influence CME kinematics and shock formation.
- Data-Driven CME Simulation Initialization: The use of observed data is fundamental for moving from idealized physical experiments to operational forecasting tools that can accurately predict the behavior of specific, observed active regions.

## Links

- [Abstract](https://arxiv.org/abs/2605.05883)
- [PDF](https://arxiv.org/pdf/2605.05883)

