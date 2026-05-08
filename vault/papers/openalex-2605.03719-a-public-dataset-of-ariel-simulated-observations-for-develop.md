---
# CSL-compatible fields
title: "A public dataset of Ariel simulated observations for developing exoplanetary atmosphere data reduction pipelines"
author:
  - literal: "Lorenzo V. Mugnai"
  - literal: "Kai Hou Yip"
  - literal: "Andrea Bocchieri"
  - literal: "Ανδρέας Παπαγεωργίου"
  - literal: "V. Batista"
  - literal: "Orphée Faucoz"
  - literal: "Angèle Syty"
  - literal: "Tara Tahseen"
  - literal: "Enzo Pascale"
  - literal: "Ingo Waldmann"
issued:
  date-parts:
    - [2026, 5, 5]
url: "https://arxiv.org/abs/2605.03719"

# Custom fields
paper_id: "2605.03719"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "dataset"
  - "multimodal"
  - "time-series"
architectures:
  []
datasets:
  - "ariel-simulated-observations-dataset"
concept_slugs:
  []
dataset_slugs:
  - "ariel-simulated-observations-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-05-08T06:28:02Z"
created_at: "2026-05-08T06:28:02Z"
---

# A public dataset of Ariel simulated observations for developing exoplanetary atmosphere data reduction pipelines

**Authors**: Lorenzo V. Mugnai, Kai Hou Yip, Andrea Bocchieri, Ανδρέας Παπαγεωργίου, V. Batista, Orphée Faucoz, Angèle Syty, Tara Tahseen, Enzo Pascale, Ingo Waldmann
**Date**: 2026-05-05
**Paper ID**: [openalex:2605.03719](https://arxiv.org/abs/2605.03719)

## Summary

This paper introduces a comprehensive public dataset of simulated observations for the ESA Ariel mission, specifically designed to support the development and validation of data-driven detrending algorithms for exoplanet transmission spectroscopy. By providing known ground truth data, the authors enable robust benchmarking of pipeline performance in the presence of instrumental and astrophysical noise. Additionally, the paper establishes a deep learning baseline for time-series reduction and identifies significant challenges regarding dataset shift, which poses a critical risk for the reliability of machine learning approaches in this domain.

## Key Contributions

- Release of a comprehensive simulated dataset for exoplanet transmission spectroscopy based on ESA Ariel mission payload design.
- Provision of a deep neural network baseline for time-series data reduction in exoplanetary atmospheric observations.
- Demonstration of dataset shift limitations in ML-based detrending methods when applied to exoplanetary spectral data.

## Open Questions & Future Work

- [[deep-learning-uncertainty-quantification-shift]]

## Archivist Review

The paper provides a valuable simulation dataset for exoplanetary science. I have approved the dataset for its utility in benchmarking data reduction pipelines. The open question regarding uncertainty quantification under dataset shift is a fundamental and reusable problem in scientific machine learning, deserving of a permanent tracking note. No other novel methodologies or concepts were identified as meeting the high threshold for standalone vault entry.

### Approved Open Questions
- Deep learning uncertainty quantification limits: Reliable uncertainty quantification is essential for scientific mission pipelines to distinguish between confident predictions and scenarios where the model is operating outside its training domain, which is critical for survey missions like Ariel.

### Rejected Candidates
- [dataset] Ariel Data Challenge 2024 (`ariel-data-challenge-2024`) - not_reusable: The Kaggle challenge is a ephemeral event; the dataset itself is the proper object to archive.

## Datasets

- [[ariel-simulated-observations-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2605.03719)
- [PDF](https://arxiv.org/pdf/2605.03719)

