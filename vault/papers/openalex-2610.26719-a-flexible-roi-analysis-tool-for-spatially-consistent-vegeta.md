---
# CSL-compatible fields
title: "A Flexible ROI Analysis Tool for Spatially Consistent Vegetation Index Extraction from Turfgrass Imagery"
author:
  - literal: "Kibon Ku"
  - literal: "Thai Thanh Tuan"
  - literal: "Jinhyun Ahn"
issued:
  date-parts:
    - [2026, 10, 19]
url: "https://arxiv.org/abs/2610.26719"

# Custom fields
paper_id: "2610.26719"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "time-series"
  - "computer-vision"
  - "image-classification"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-22T09:45:20Z"
created_at: "2026-10-22T09:45:20Z"
---

# A Flexible ROI Analysis Tool for Spatially Consistent Vegetation Index Extraction from Turfgrass Imagery

**Authors**: Kibon Ku, Thai Thanh Tuan, Jinhyun Ahn
**Date**: 2026-10-19
**Paper ID**: [openalex:2610.26719](https://arxiv.org/abs/2610.26719)

## Summary

This paper presents an open-source software tool designed for spatially consistent vegetation index extraction from turfgrass imagery when camera positions vary across time-series acquisitions. The tool features an interactive GUI for placing orientation-adjustable regions of interest (ROIs) with N-way subdivision and a batch-processing script that exports coordinates and mean values in JSON format. Demonstrations on rail-mounted multispectral imagery show successful plot-level extraction of NDVI, NDRE, and SAVI without requiring GIS expertise or pre-georeferenced rasters.

## Key Contributions

- Developed an open-source tool with a GUI for interactive, orientation-adjustable ROI placement with N-way subdivision to handle varying camera positions in turfgrass imagery.
- Implemented a batch-processing script that computes plot-level mean VI values from single-band rasters and exports coordinates and measurements in reusable JSON format.
- Demonstrated reproducible spatial consistency across NDVI, NDRE, and SAVI extraction without requiring GIS expertise or georeferenced rasters.

## Limitations

Evaluated primarily on a specific rail-mounted multispectral turfgrass imagery dataset (18 images).

## Open Questions & Future Work

- [[automated-roi-estimation-registration]]

## Archivist Review

Applied strict selectivity standards, approving only one substantive open question about automated ROI registration while rejecting concepts and datasets that are overly application-specific or paper-local to turfgrass imagery software.

### Approved Open Questions
- Automated ROI Estimation and Registration: Manual ROI delineation is a major bottleneck in high-throughput plant phenotyping pipelines, limiting scalability when handling large temporal image collections.

### Rejected Candidates
- [open_question] Automated ROI Estimation and Registration (`automated-roi-estimation-registration`) - generic: Approved instead

## Links

- [Abstract](https://arxiv.org/abs/2610.26719)
- [PDF](https://arxiv.org/pdf/2610.26719)

