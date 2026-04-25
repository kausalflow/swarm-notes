---
# CSL-compatible fields
title: "OpenWaveLogger v2026 (OWL-v2026): an open source, low cost, easy to build, high performance logger for wave data measurements"
author:
  - literal: "Jean Rabault"
  - literal: "Joey Voermans"
  - literal: "Takuji Waseda"
  - literal: "Takehiko Nose"
  - literal: "Tsubasa Kodaira"
  - literal: "Koya Sato"
  - literal: "ALEXANDER BABANIN"
  - literal: "Gaute Hope"
  - literal: "Malte Müller"
  - literal: "Lars Willas Dreyer"
  - literal: "Øystein Lande"
  - literal: "Atle Jensen"
  - literal: "Øyvind Breivik"
issued:
  date-parts:
    - [2026, 4, 22]
url: "https://arxiv.org/abs/2604.20502"

# Custom fields
paper_id: "2604.20502"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-25T06:16:01Z"
created_at: "2026-04-25T06:16:01Z"
---

# OpenWaveLogger v2026 (OWL-v2026): an open source, low cost, easy to build, high performance logger for wave data measurements

**Authors**: Jean Rabault, Joey Voermans, Takuji Waseda, Takehiko Nose, Tsubasa Kodaira, Koya Sato, ALEXANDER BABANIN, Gaute Hope, Malte Müller, Lars Willas Dreyer, Øystein Lande, Atle Jensen, Øyvind Breivik
**Date**: 2026-04-22
**Paper ID**: [openalex:2604.20502](https://arxiv.org/abs/2604.20502)

## Summary

The paper introduces the OpenWaveLogger (OWL-v2026), a cost-effective, open-source data logging solution designed to capture high-frequency in-situ ocean wave data that telemetry-based systems often struggle to transmit. Constructed from accessible off-the-shelf components, the system enables precise six-axis IMU logging combined with GNSS positioning and velocity tracking. By utilizing PPS synchronization and optimized power management, the device provides reliable, long-term performance suitable for advanced wave physics research. This hardware contribution aims to lower the barrier for collecting high-resolution wave time series, significantly expanding data availability for climate and weather model validation.

## Key Contributions

- Presents OpenWaveLogger (OWL-v2026), an open-source, low-cost (approx. 220 USD) data logger for high-frequency in-situ wave measurements.
- Achieves high-frequency, low-jitter six-axis IMU logging at up to 416Hz and GNSS logging at 10Hz using off-the-shelf components.
- Demonstrates 20-day battery autonomy and absolute UTC timestamping accuracy typically better than 10ms via Pulse Per Second (PPS) synchronization.

## Open Questions & Future Work

- [[high-frequency-sd-logging-limits]]

## Archivist Review

The paper presents a valuable hardware contribution for high-frequency time-series data collection but does not introduce new machine learning concepts or algorithms. The open question regarding SD logging limitations was approved as it captures a generic, persistent challenge in scientific data acquisition using low-cost instrumentation.

### Approved Open Questions
- High-frequency SD logging limitations: This represents a fundamental bottleneck for democratizing high-frequency scientific data collection, which is necessary for observing phenomena like micro-scale wave dynamics or turbulence.

### Rejected Candidates
- [concept] OpenWaveLogger v2026 (`owl-v2026`) - paper_local: This is a specific piece of hardware/instrumentation rather than a general-purpose ML concept or reusable algorithmic technique.

## Links

- [Abstract](https://arxiv.org/abs/2604.20502)
- [PDF](https://arxiv.org/pdf/2604.20502)

