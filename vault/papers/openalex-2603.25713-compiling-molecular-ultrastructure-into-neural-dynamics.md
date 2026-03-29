---
# CSL-compatible fields
title: "Compiling molecular ultrastructure into neural dynamics"
author:
  - literal: "Konrad P. Körding"
  - literal: "Anton Arkhipov"
  - literal: "Davy Deng"
  - literal: "Sean Escola"
  - literal: "Seth G. N. Grant"
  - literal: "Gal Haspel"
  - literal: "Michał Januszewski"
  - literal: "Narayanan Kasthuri"
  - literal: "Nina Khera"
  - literal: "Richie E. Kohman"
  - literal: "Grace Lindsay"
  - literal: "Jeantine E. Lunshof"
  - literal: "Adam Marblestone"
  - literal: "David A. Markowitz"
  - literal: "Jordan Matelsky"
  - literal: "Brett D. Mensh"
  - literal: "Patrick Mineault"
  - literal: "Andrew Payne"
  - literal: "Joanne Peng"
  - literal: "Xaq Pitkow"
  - literal: "Philip Shiu"
  - literal: "Gregor F. P. Schuhknecht"
  - literal: "Sven Truckenbrodt"
  - literal: "Joshua T. Vogelstein"
  - literal: "Edward S. Boyden"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25713"

# Custom fields
paper_id: "2603.25713"
paper_source: "openalex"
domain: "biology"
tags:
  - "multimodal"
  - "tool-use"
  - "reasoning"
  - "agent"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "ultrastructure-to-dynamics-compiler"
  - "ul2d-paired-training-data"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-29T06:08:40Z"
created_at: "2026-03-29T06:08:40Z"
---

# Compiling molecular ultrastructure into neural dynamics

**Authors**: Konrad P. Körding, Anton Arkhipov, Davy Deng, Sean Escola, Seth G. N. Grant, Gal Haspel, Michał Januszewski, Narayanan Kasthuri, Nina Khera, Richie E. Kohman, Grace Lindsay, Jeantine E. Lunshof, Adam Marblestone, David A. Markowitz, Jordan Matelsky, Brett D. Mensh, Patrick Mineault, Andrew Payne, Joanne Peng, Xaq Pitkow, Philip Shiu, Gregor F. P. Schuhknecht, Sven Truckenbrodt, Joshua T. Vogelstein, Edward S. Boyden
**Date**: 2026-03-26
**Paper ID**: [openalex:2603.25713](https://arxiv.org/abs/2603.25713)

## Summary

This paper proposes a conceptual framework, the Ultrastructure-to-Dynamics Compiler, designed to translate high-resolution molecularly annotated neural ultrastructure data into simulator-ready, uncertainty-aware physiological parameters governing local neuronal dynamics. This is achieved by training a learned mapping using paired data consisting of simultaneously acquired structural imaging and physiological response measurements to perturbations. The successful implementation of this compiler would transform structure-to-function analysis from a descriptive process into a predictive one, directly informing biophysical simulations and the forecasting of intervention outcomes in neural circuits. The feasibility hinges on acquiring the necessary co-registered structural and dynamic experimental datasets.

## Key Contributions

- Proposed the concept of an ultrastructure-to-dynamics compiler: a learned mapping from molecularly annotated ultrastructure to simulator-ready, uncertainty-aware physiological parameters.
- Identified the critical requirement for paired training data: jointly acquired ultrastructure imaging and dynamical response experiments.
- Shifts the paradigm of structure-to-function analysis in neuroscience from descriptive simulation setup to predictive modeling of circuit dynamics.
- Enables the forecasting of intervention effects in neural circuits directly from structural maps.

## Limitations

The primary limitation is the current lack of the required paired training data, where ultrastructure and dynamics are simultaneously measured with sufficient fidelity.

## Key Concepts

- [[ultrastructure-to-dynamics-compiler]]: A machine learning model designed to translate high-resolution molecularly annotated brain ultrastructure maps directly into simulator-ready, uncertainty-aware physiological parameters for neural circuits.
- [[ul2d-paired-training-data]]: The necessary paired dataset consisting of molecularly annotated ultrastructure measurements and corresponding in-vivo or in-vitro physiological response data.

## Archivist Review

Two central concepts were approved: the 'Ultrastructure-to-Dynamics Compiler' as the core predictive mechanism, and the 'UL2D Paired Training Data' requirement, which is a crucial and reusable data constraint for bridging structural and functional domains. No datasets or open questions were deemed significant enough for separate vault entries in this highly conceptual proposal.

### Approved Concepts
- Ultrastructure-to-Dynamics Compiler: It is the central methodological proposal of the paper, aiming to bridge the gap between high-resolution molecular imaging data and functional neural dynamics models.
- UL2D (Ultrastructure-to-Dynamics) Data Pairing: This specific requirement for paired structural and dynamic experimental data is the critical bottleneck and enabling condition for training the compiler.

### Rejected Candidates
- [concept] Ultrastructure-to-Dynamics Compiler (`ultrastructure-to-dynamics-compiler`) - generic: This concept was approved.
- [concept] UL2D (Ultrastructure-to-Dynamics) Data Pairing (`ul2d-paired-training-data`) - generic: This concept was approved.

## Links

- [Abstract](https://arxiv.org/abs/2603.25713)
- [PDF](https://arxiv.org/pdf/2603.25713)

