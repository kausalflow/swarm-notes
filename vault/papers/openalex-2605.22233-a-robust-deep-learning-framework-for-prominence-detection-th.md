---
# CSL-compatible fields
title: "A Robust Deep Learning Framework for Prominence Detection through Composite Feature Representations"
author:
  - literal: "Harry Birch"
  - literal: "Stéphane Régnier"
  - literal: "Richard Morton"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.22233"

# Custom fields
paper_id: "2605.22233"
paper_source: "openalex"
domain: "computer-vision, space-weather"
tags:
  - "object-detection"
  - "robustness"
  - "benchmark"
architectures:
  []
datasets:
  - "sdo-aia-dataset"
concept_slugs:
  - "composite-feature-representation-bias-mitigation"
dataset_slugs:
  - "sdo-aia-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:48:14Z"
created_at: "2026-05-24T07:48:14Z"
---

# A Robust Deep Learning Framework for Prominence Detection through Composite Feature Representations

**Authors**: Harry Birch, Stéphane Régnier, Richard Morton
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.22233](https://arxiv.org/abs/2605.22233)

## Summary

This paper addresses the performance limitations of existing deep learning models for detecting solar prominences, which often struggle with coronal emission contamination and color-map bias. The authors introduce a novel dataset preprocessing pipeline that creates composite three-channel images—incorporating full-disk, enhanced corona, and disk-removed representations—to better isolate physically meaningful prominence features. Evaluated on SDO/AIA data, the proposed composite framework achieves superior detection metrics and demonstrates effective cross-instrument generalization to SUVI observations. By mitigating instrument-induced biases, the approach provides a more robust and reliable tool for automated space weather monitoring.

## Key Contributions

- Develops an original preprocessing pipeline to construct composite three-channel solar images that mitigate bias from extreme ultraviolet (EUV) emissions.
- Achieves a mAP@50 of 0.749 and 78% recall for solar prominence detection, outperforming existing baseline models.
- Demonstrates improved model robustness and cross-instrument generalization by validating the model on SUVI image data.
- Identifies and quantifies specific dataset biases in existing prominence detection models stemming from color-map dependency.

## Open Questions & Future Work

- [[automated-relabeling-of-scientific-datasets]]

## Key Concepts

- [[composite-feature-representation-bias-mitigation]]: A preprocessing strategy that constructs multi-channel inputs from derived physical image representations to decouple model performance from instrument-specific colormaps and sensor artifacts.

## Archivist Review

The review focused on extracting the reusable methodology for mitigating sensor-dependent bias in scientific imaging and the broader research challenge of ground-truth quality in scientific datasets. I renamed the concept and question to reflect their potential for generalization beyond the specific domain of solar prominence detection. I approved only SDO/AIA as it is the foundational dataset used for the novel pipeline construction.

### Approved Concepts
- Composite Feature Representation for Bias Mitigation: The paper demonstrates that simple object detectors are prone to spurious correlations with raw sensor colormaps; constructing composite channels (full-disk, enhanced, disk-removed) forces the model to learn physically grounded geometric features rather than imaging artifacts.

### Approved Open Questions
- Automated Relabeling of Scientific Datasets: The quality of ground truth labels limits the upper bound of model performance; without objective re-labeling, performance metrics remain confounded by the absence of labels for objects that are visibly present in optimized data.

### Rejected Candidates
- [concept] Composite Feature Representations for Prominence Detection (`composite-feature-representations-solar-prominence`) - other: Renamed to a more general and reusable concept slug.
- [dataset] SUVI (`SUVI`) - low_impact: The paper uses SUVI for testing/validation, not as a primary dataset for the foundational training work. SDO/AIA is more central.
- [open_question] Relabeling Prominence Datasets (`relabeling-prominence-datasets-wow`) - other: Renamed to a more general research question relevant to the broader field of scientific ML.

## Datasets

- [[sdo-aia-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2605.22233)
- [PDF](https://arxiv.org/pdf/2605.22233)

