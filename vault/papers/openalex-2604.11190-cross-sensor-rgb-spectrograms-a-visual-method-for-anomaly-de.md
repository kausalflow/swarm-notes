---
# CSL-compatible fields
title: "Cross-Sensor RGB Spectrograms: A Visual Method for Anomaly Detection in Classical and Quantum Magnetometer Triads"
author:
  - literal: "Manas Pandey"
issued:
  date-parts:
    - [2026, 4, 13]
url: "https://arxiv.org/abs/2604.11190"

# Custom fields
paper_id: "2604.11190"
paper_source: "openalex"
domain: "speech"
tags:
  - "anomaly-detection"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "cross-sensor-rgb-spectrograms"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-16T06:29:29Z"
created_at: "2026-04-16T06:29:29Z"
---

# Cross-Sensor RGB Spectrograms: A Visual Method for Anomaly Detection in Classical and Quantum Magnetometer Triads

**Authors**: Manas Pandey
**Date**: 2026-04-13
**Paper ID**: [openalex:2604.11190](https://arxiv.org/abs/2604.11190)

## Summary

This paper presents a theoretical framework for 'cross-sensor RGB spectrograms', a visualization technique that maps STFT power spectra from three concurrent magnetometers into RGB color space. By mapping inter-sensor coherence to achromatic colors and unique spectral energy to saturated colors, the method allows for rapid identification of measurement health and anomalous magnetic activity. The construction is architecture-agnostic, applicable to both classical and quantum sensors, and includes a systematic taxonomy for interpreting spectral color patterns as distinct physical or technical phenomena.

## Key Contributions

- Introduces cross-sensor RGB spectrograms as a visual diagnostic tool for magnetometer triads.
- Formalizes the mapping of STFT power spectra into RGB channels, including explicit per-channel normalization strategies.
- Develops a color-anomaly taxonomy to classify coherent activity, sensor faults, pairwise asymmetries, and temporal drifts in magnetometer data.

## Open Questions & Future Work

- [[quantum-noise-aware-visualisation]]
- [[coherence-based-rgb-fusion]]

## Key Concepts

- [[cross-sensor-rgb-spectrograms]]: A visualization technique that maps three-channel magnetometer STFT power spectra into RGB image space to identify cross-sensor coherence and anomalies.

## Archivist Review

I have approved the core visualization technique as a reusable diagnostic concept for multi-sensor time-series monitoring. I also approved two research directions that address the limitations of the current power-spectrum-only approach by incorporating domain-specific (quantum) noise floors and inter-sensor coherence measures. These candidates provide actionable improvements for expanding the methodology's diagnostic utility in technical monitoring scenarios.

### Approved Concepts
- Cross-Sensor RGB Spectrograms: The core contribution of the paper, providing a novel visual diagnostic framework for multi-sensor magnetometer arrays.

### Approved Open Questions
- Quantum-noise-aware RGB normalization: Technically important for precise diagnostic characterization of quantum magnetometers, as it allows for an immediate visual separation of inherent quantum noise from extraneous technical faults.
- Coherence-based RGB spectrogram fusion: Enhances the diagnostic capability of the visualisation by capturing phase relationships and absolute amplitude disparities that are currently lost in the power-spectrum-only approach.

## Links

- [Abstract](https://arxiv.org/abs/2604.11190)
- [PDF](https://arxiv.org/pdf/2604.11190)

