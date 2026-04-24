---
# CSL-compatible fields
title: "A Long-Form Single-Speaker Real-Time MRI Speech Dataset and Benchmark"
author:
  - literal: "Sean Foley"
  - literal: "Jihwan Lee"
  - literal: "Kevin Huang"
  - literal: "Xuan Shi"
  - literal: "Yoonjeong Lee"
  - literal: "Louis Goldstein"
  - literal: "Shrikanth Narayanan"
issued:
  date-parts:
    - [2026, 4, 21]
url: "https://arxiv.org/abs/2509.14479"

# Custom fields
paper_id: "2509.14479"
paper_source: "openalex"
domain: "speech"
tags:
  - "speech-recognition"
  - "dataset"
  - "benchmark"
  - "multimodal"
architectures:
  []
datasets:
  - "usc-long-single-speaker-dataset"
concept_slugs:
  []
dataset_slugs:
  - "usc-long-single-speaker-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-04-24T07:00:35Z"
created_at: "2026-04-24T07:00:35Z"
---

# A Long-Form Single-Speaker Real-Time MRI Speech Dataset and Benchmark

**Authors**: Sean Foley, Jihwan Lee, Kevin Huang, Xuan Shi, Yoonjeong Lee, Louis Goldstein, Shrikanth Narayanan
**Date**: 2026-04-21
**Paper ID**: [openalex:2509.14479](https://arxiv.org/abs/2509.14479)

## Summary

The paper introduces the USC Long Single-Speaker (LSS) dataset, which contains approximately one hour of synchronized real-time MRI video of vocal tract dynamics and audio for speech production research. This high-quality, single-speaker dataset addresses the scarcity of long-duration MRI speech data available to the community. Alongside the raw recordings, the authors provide processed data representations and baseline models for articulatory synthesis and phoneme recognition. The release aims to foster advancements in modeling the relationship between vocal tract movement and acoustic output.

## Key Contributions

- Introduces the USC Long Single-Speaker (LSS) dataset, providing approximately one hour of synchronized real-time vocal tract MRI video and audio from a single speaker.
- Provides pre-processed data representations including vocal tract crops, denoised audio, and regions-of-interest timeseries suitable for speech analysis.
- Establishes baseline performance benchmarks for articulatory synthesis and phoneme recognition tasks on the LSS dataset.

## Open Questions & Future Work

- [[multimodal-fusion-strategies-for-speech-articulatory-dynamics]]

## Archivist Review

Approved the USC Long Single-Speaker (LSS) dataset as a significant community resource for speech research. The open question regarding multimodal fusion was kept but renamed to better reflect its scope and technical nuance regarding articulatory-acoustic dynamics. No new concepts were approved as the primary contribution is the dataset and the task, not a novel modeling paradigm.

### Approved Open Questions
- Multimodal Speech Fusion Strategies: This is critical because multimodal fusion is a fundamental challenge in speech processing. Identifying successful fusion strategies could lead to significantly more robust ASR systems that leverage articulatory data to resolve acoustic ambiguities.

### Rejected Candidates
- [open_question] Multimodal Integration for Speech Recognition (`multimodal-integration-strategies-speech-recognition`) - duplicate_existing: Renamed for clarity and consistency with existing vault conventions.

## Datasets

- [[usc-long-single-speaker-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2509.14479)
- [PDF](https://arxiv.org/pdf/2509.14479)

