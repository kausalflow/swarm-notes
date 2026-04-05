---
# CSL-compatible fields
title: "Application of parametric Shallow Recurrent Decoder Network to magnetohydrodynamic flows in liquid metal blankets of fusion reactors"
author:
  - literal: "M. Lo Verso"
  - literal: "C. Introini"
  - literal: "E. Cervi"
  - literal: "L. Savoldi"
  - literal: "J. Nathan Kutz"
  - literal: "A. Cammi"
issued:
  date-parts:
    - [2026, 4, 2]
url: "https://arxiv.org/abs/2604.02139"

# Custom fields
paper_id: "2604.02139"
paper_source: "openalex"
domain: "physics"
tags:
  - "time-series"
  - "recurrent-neural-network"
  - "rnn"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "shred-shallow-recurrent-decoder"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-05T06:09:21Z"
created_at: "2026-04-05T06:09:21Z"
---

# Application of parametric Shallow Recurrent Decoder Network to magnetohydrodynamic flows in liquid metal blankets of fusion reactors

**Authors**: M. Lo Verso, C. Introini, E. Cervi, L. Savoldi, J. Nathan Kutz, A. Cammi
**Date**: 2026-04-02
**Paper ID**: [openalex:2604.02139](https://arxiv.org/abs/2604.02139)

## Summary

This paper presents a data-driven approach for magnetohydrodynamic (MHD) state reconstruction in fusion reactor blankets using the SHallow REcurrent Decoder (SHRED) architecture. By integrating Singular Value Decomposition (SVD) for dimensionality reduction with recurrent neural networks, the model accurately recovers full spatio-temporal dynamics from sparse, local time-series observations. The framework demonstrates strong generalization to unseen magnetic field parameters and physical conditions, offering a computationally efficient alternative to traditional numerical solvers for real-time diagnostics.

## Key Contributions

- Demonstrates the application of the SHRED architecture for reconstructing complex magnetohydrodynamic (MHD) flows in fusion reactor blankets.
- Achieves robust state reconstruction under unseen parametric configurations, including varying magnetic field intensities, orientations, and time-dependent dynamics.
- Enables inference of hidden temporal magnetic field evolution using only temperature measurements, facilitating efficient real-time monitoring.

## Key Concepts

- [[shred-shallow-recurrent-decoder]]: A neural network architecture that combines SVD-based dimensionality reduction with recurrent decoders to reconstruct full spatio-temporal states from sparse time-series sensor data.

## Archivist Review

The SHRED architecture is approved as it provides a distinct, reusable methodology for spatio-temporal state reconstruction from sparse measurements, which is highly relevant to forecasting and physical system modeling. No new open questions were provided, and no specific datasets were identified as central to the paper's contribution beyond the application context itself.

### Approved Concepts
- SHallow REcurrent Decoder (SHRED): It serves as a computationally efficient, data-driven framework for state reconstruction in complex physical systems using sparse observations.

## Links

- [Abstract](https://arxiv.org/abs/2604.02139)
- [PDF](https://arxiv.org/pdf/2604.02139)

