---
# CSL-compatible fields
title: "FLAIR-HUB: Large-scale multimodal dataset for land cover and crop mapping"
author:
  - literal: "Anatol Garioud"
  - literal: "Sébastien Giordano"
  - literal: "Nicolás David"
  - literal: "Nicolas Gonthier"
issued:
  date-parts:
    - [2026, 4, 27]
url: "https://arxiv.org/abs/2506.07080"

# Custom fields
paper_id: "2506.07080"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "dataset"
  - "benchmark"
  - "image-segmentation"
architectures:
  []
datasets:
  - "flair-hub"
concept_slugs:
  []
dataset_slugs:
  - "flair-hub"
skill: "TimeSeriesSkill"
processed_at: "2026-04-30T07:25:54Z"
created_at: "2026-04-30T07:25:54Z"
---

# FLAIR-HUB: Large-scale multimodal dataset for land cover and crop mapping

**Authors**: Anatol Garioud, Sébastien Giordano, Nicolás David, Nicolas Gonthier
**Date**: 2026-04-27
**Paper ID**: [openalex:2506.07080](https://arxiv.org/abs/2506.07080)

## Summary

FLAIR-HUB is a new large-scale multimodal dataset designed to advance land cover and crop type monitoring through the integration of six heterogeneous Earth observation data sources. By providing aligned aerial, satellite (SAR and optical), and topographic imagery with very-high-resolution annotations, it enables the evaluation of complex multimodal fusion architectures. The authors establish robust baselines using both convolutional neural networks and transformer-based models, highlighting the significant performance gains attainable through multi-modal integration in fine-grained semantic segmentation tasks. The dataset serves as a foundational resource for supervised, self-supervised, and transfer learning research in the remote sensing domain.

## Key Contributions

- Introduces FLAIR-HUB, a large-scale multimodal Earth observation dataset covering 2528 km² with 20cm resolution annotations.
- Integrates six aligned modalities including aerial, optical Sentinel-2, SAR Sentinel-1, SPOT satellite imagery, and topographic data.
- Provides a comprehensive benchmark for multimodal fusion and multi-task learning, demonstrating that combining all six modalities achieves 78.2% accuracy and 65.8% mIoU in land cover mapping.

## Open Questions & Future Work

- [[multimodal-fusion-architectures-bottleneck]]
- [[multitask-learning-synergy-gap]]

## Archivist Review

The FLAIR-HUB dataset provides a significant, high-resolution multi-modal benchmark for land cover mapping, which warrants a standalone entry. The identified open questions regarding multimodal fusion bottlenecks and multitask learning synergy in remote sensing are well-posed and address significant challenges in this domain. No specific methodological concepts were identified as novel or distinct from existing approaches.

### Approved Open Questions
- Multimodal Fusion Architecture Bottleneck: This is a fundamental bottleneck in remote sensing machine learning, as effective fusion is necessary to leverage the increasingly diverse EO data landscape.
- Multitask Learning Synergy Gap: Multitask learning is essential for efficient, large-scale deployment of geospatial AI models, and identifying why it fails in current remote sensing setups is critical for progress.

### Rejected Candidates
- [dataset] FLAIR-HUB (`flair-hub`) - other: While a large-scale dataset, the provided submission didn't specify it's a dataset deserving of permanent vault entry beyond standard benchmark status. (Re-reviewed to ensure consistency; actually, this represents a significant multi-source integration for Earth Observation and warrants entry.)

## Datasets

- [[flair-hub]]

## Links

- [Abstract](https://arxiv.org/abs/2506.07080)
- [PDF](https://arxiv.org/pdf/2506.07080)

