---
# CSL-compatible fields
title: "Label-Efficient Learning for Ground-Based Sky-Image Classification: A Benchmark of Transfer Learning, Active Learning, and Pseudo-Labeling on GCD"
author:
  - literal: "Esther Bou Dagher"
  - literal: "Viktoriya Bu-Dager"
  - literal: "Boguslaw Zegarlinski"
issued:
  date-parts:
    - [2026, 9, 22]
url: "https://arxiv.org/abs/2609.26631"

# Custom fields
paper_id: "2609.26631"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "benchmark"
  - "dataset"
  - "evaluation"
  - "image-classification"
  - "transfer-learning"
  - "active-learning"
  - "semi-supervised-learning"
architectures:
  []
datasets:
  - "Ground-based Cloud Dataset"
concept_slugs:
  []
dataset_slugs:
  - "ground-based-cloud-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-09-25T09:58:08Z"
created_at: "2026-09-25T09:58:08Z"
---

# Label-Efficient Learning for Ground-Based Sky-Image Classification: A Benchmark of Transfer Learning, Active Learning, and Pseudo-Labeling on GCD

**Authors**: Esther Bou Dagher, Viktoriya Bu-Dager, Boguslaw Zegarlinski
**Date**: 2026-09-22
**Paper ID**: [openalex:2609.26631](https://arxiv.org/abs/2609.26631)

## Summary

This paper benchmarks label-efficient learning strategies—specifically supervised transfer learning, uncertainty-based active learning, and high-confidence pseudo-labeling—for ground-based cloud classification on the Ground-based Cloud Dataset (GCD). Using a frozen ImageNet-pretrained ResNet50 backbone across label budgets from 1% to 100%, the study shows that supervised transfer learning alone is highly efficient, approaching full-label accuracy with only 40% of labels. Diagnostic analyses indicate that while active learning targets difficult classes and pseudo-labeling produces high-accuracy subsets, neither strategy delivers substantial aggregate improvements over the supervised baseline.

## Key Contributions

- Provided a comprehensive benchmark evaluating supervised transfer learning, uncertainty-based active learning, and high-confidence pseudo-labeling for ground-based sky-image classification across label budgets from 1% to 100%.
- Demonstrated that supervised transfer learning using an ImageNet-pretrained ResNet50 is highly label-efficient on GCD, achieving 0.730 test accuracy with only 40% of the training labels compared to 0.735 with full labels.
- Revealed through diagnostic analyses that active learning focuses on visually challenging cloud categories (Mixed, Stratocumulus, and Cumulonimbus) while pseudo-labeling remains reliable yet biased toward easy high-confidence groups, resulting in modest overall performance gains.

## Limitations

Active learning and pseudo-labeling strategies fail to provide large or consistent aggregate gains over a strong supervised transfer learning baseline under limited annotation budgets.

## Archivist Review

The paper provides an empirical benchmark of label-efficient learning strategies (transfer learning, active learning, and pseudo-labeling) on a cloud dataset (GCD). It proposes no novel architectures or permanent conceptual primitives suitable for the knowledge vault, but includes a recognized dataset name.

### Rejected Candidates
- [open_question] Generalization Across Sky Image Datasets (`generalize-label-efficient-sky-classification-datasets`) - low_impact: Too general and asks for standard dataset transfer validation.

## Datasets

- [[ground-based-cloud-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2609.26631)
- [PDF](https://arxiv.org/pdf/2609.26631)

