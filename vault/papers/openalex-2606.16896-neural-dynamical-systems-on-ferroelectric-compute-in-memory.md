---
# CSL-compatible fields
title: "Neural dynamical systems on ferroelectric compute-in-memory for real-time forecasting"
author:
  - literal: "Keshava Katti"
  - literal: "Adithya Selvakumar"
  - literal: "Pratik Chaudhari"
  - literal: "Deep Jariwala"
issued:
  date-parts:
    - [2026, 6, 15]
url: "https://arxiv.org/abs/2606.16896"

# Custom fields
paper_id: "2606.16896"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "model-compression"
architectures:
  []
datasets:
  []
concept_slugs:
  - "ferronds"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-17T09:26:17Z"
created_at: "2026-06-17T09:26:17Z"
---

# Neural dynamical systems on ferroelectric compute-in-memory for real-time forecasting

**Authors**: Keshava Katti, Adithya Selvakumar, Pratik Chaudhari, Deep Jariwala
**Date**: 2026-06-15
**Paper ID**: [openalex:2606.16896](https://arxiv.org/abs/2606.16896)

## Summary

This paper presents FerroNDS, a novel neuromorphic architecture that maps continuous-time neural dynamical systems onto ferroelectric compute-in-memory hardware. By utilizing analog integrator and oscillator primitives, the system efficiently computes time-frequency representations and performs real-time forecasting. Evaluations show significant improvements in energy efficiency, area footprint, and latency compared to traditional digital hardware for complex signal prediction.

## Key Contributions

- Introduced FerroNDS, a neuromorphic system mapping continuous-time neural dynamical models onto ferrodiode-based compute-in-memory.
- Demonstrated 25-40x area reduction and sub-watt energy efficiency (0.29-1.64 μJ/inference) compared to digital SRAM-based systems for signal forecasting.
- Achieved real-time forecasting of periodic, quasi-periodic, and chaotic signals over a 500-ms horizon with microsecond-to-millisecond latency.

## Open Questions & Future Work

- [[low-voltage-ferroelectric-cim-operation]]

## Key Concepts

- [[ferronds]]: A neuromorphic system leveraging ferroelectric compute-in-memory for real-time continuous-time forecasting.

## Archivist Review

The paper is approved for the FerroNDS architecture and the associated open question regarding ferroelectric voltage scaling, as these represent a novel intersection of continuous-time dynamical systems and analog hardware substrates. I have applied a strict filter to ensure only the central architectural proposal and the critical hardware-bottleneck question are retained. Other potential candidates were deemed either too specific to this implementation or covered by broader existing concepts in neuromorphic/CIM hardware.

### Approved Concepts
- FerroNDS: It is the first end-to-end integration of ferrodiode-based compute-in-memory hardware for neural dynamical systems.

### Approved Open Questions
- Lower-Voltage Ferroelectric CIM Operation: Voltage reduction is identified as a critical bottleneck for reaching the energy-efficiency levels required to outperform current state-of-the-art spike-based neuromorphic processors.

## Links

- [Abstract](https://arxiv.org/abs/2606.16896)
- [PDF](https://arxiv.org/pdf/2606.16896)

