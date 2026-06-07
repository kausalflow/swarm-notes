---
# CSL-compatible fields
title: "Leveraging MTG-FCI fire observations for event-based fire behavior monitoring from near-real-time operation to seasonal analysis"
author:
  - literal: "Ronan Paugam"
  - literal: "Jean-Baptiste Filippi"
  - literal: "Akli Benali"
  - literal: "Jorge Gomes"
  - literal: "Weidong Xu"
  - literal: "Emanuel Dutra"
  - literal: "François André"
  - literal: "Damien Boulanger"
  - literal: "Vianney Retornard"
  - literal: "Andrea Meraner"
  - literal: "J M Harvie"
  - literal: "Victor Pénot"
  - literal: "Cyrielle Denjean"
issued:
  date-parts:
    - [2026, 6, 4]
url: "https://arxiv.org/abs/2606.06016"

# Custom fields
paper_id: "2606.06016"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  - "fire-event-tracker-fet"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-07T08:20:39Z"
created_at: "2026-06-07T08:20:39Z"
---

# Leveraging MTG-FCI fire observations for event-based fire behavior monitoring from near-real-time operation to seasonal analysis

**Authors**: Ronan Paugam, Jean-Baptiste Filippi, Akli Benali, Jorge Gomes, Weidong Xu, Emanuel Dutra, François André, Damien Boulanger, Vianney Retornard, Andrea Meraner, J M Harvie, Victor Pénot, Cyrielle Denjean
**Date**: 2026-06-04
**Paper ID**: [openalex:2606.06016](https://arxiv.org/abs/2606.06016)

## Summary

This paper presents the Fire Event Tracker (FET), an algorithm designed to process high-frequency (10-min) geostationary satellite hotspot detections from the Meteosat Third Generation (MTG) Flexible Combined Imager (FCI). By performing spatio-temporal clustering, FET transforms raw observations into coherent, persistent fire events with updated metrics such as geometry and fire radiative power. The approach is validated through retrospective analysis of the 2025 Mediterranean archive and operational deployments for wildfire monitoring and plume forecasting, demonstrating its efficacy for both tactical management and seasonal analysis.

## Key Contributions

- Introduces the Fire Event Tracker (FET) algorithm for spatio-temporal clustering of high-frequency geostationary satellite hotspot data.
- Enables consistent tracking of fire geometry, radiative power, and rate of spread at 10-minute intervals across near-real-time and retrospective applications.
- Demonstrates successful integration of FET outputs to initialize coupled fire-atmosphere simulations for operational plume forecasting.

## Key Concepts

- [[fire-event-tracker-fet]]: An algorithm for the spatio-temporal clustering of satellite hotspot detections to monitor fire evolution and behavior.

## Archivist Review

I approved the Fire Event Tracker (FET) as it defines a reusable spatio-temporal clustering mechanism for high-frequency geostationary data. I rejected the dataset because it is a specific, limited temporal archive that does not qualify as a foundational or broad-scale benchmark. No open questions were proposed, and none were identified that rise to the level of systemic research bottlenecks beyond this specific implementation.

### Approved Concepts
- Fire Event Tracker (FET): It serves as a novel, reusable methodology for spatio-temporal clustering of geostationary satellite data for fire event monitoring.

### Rejected Candidates
- [dataset] Mediterranean FCI hotspot archive 2025 (`mediterranean-fci-hotspot-archive-2025`) - low_impact: This is a domain-specific, time-bounded dataset rather than a foundational or widely applicable benchmark.

## Links

- [Abstract](https://arxiv.org/abs/2606.06016)
- [PDF](https://arxiv.org/pdf/2606.06016)

