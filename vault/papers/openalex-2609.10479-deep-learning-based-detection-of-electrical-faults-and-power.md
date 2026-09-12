---
# CSL-compatible fields
title: "Deep Learning-Based Detection of Electrical Faults and Power Quality Disturbances in Aerospace Power Systems"
author:
  - literal: "Ian C. Guzmán"
  - literal: "Radu Babiceanu"
  - literal: "Berker Peköz"
issued:
  date-parts:
    - [2026, 9, 9]
url: "https://arxiv.org/abs/2609.10479"

# Custom fields
paper_id: "2609.10479"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "convolutional-neural-network"
  - "lstm"
  - "quantization"
  - "edge-ai"
  - "hardware-aware-ai"
  - "fault-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-12T08:55:40Z"
created_at: "2026-09-12T08:55:40Z"
---

# Deep Learning-Based Detection of Electrical Faults and Power Quality Disturbances in Aerospace Power Systems

**Authors**: Ian C. Guzmán, Radu Babiceanu, Berker Peköz
**Date**: 2026-09-09
**Paper ID**: [openalex:2609.10479](https://arxiv.org/abs/2609.10479)

## Summary

This paper presents a hardware-aware deep learning framework for detecting electrical faults and power quality disturbances in 400 Hz aerospace power systems, inspired by the Boeing 787 architecture. Using simulated voltage and current waveforms across 21 conditions, the authors evaluate various 1D and 2D models, finding that a compact ResNet achieves an optimal accuracy-complexity tradeoff. Following 8-bit quantization, deployment on a Xilinx Zynq UltraScale Plus MPSoC ZCU102 achieves 95.87% accuracy with a 6.90 ms latency per input record.

## Key Contributions

- Proposes a hardware-aware deep learning framework for multiclass detection of electrical faults and power quality disturbances in a 400 Hz aerospace power system.
- Generates high-fidelity simulation datasets covering 21 normal, disturbance, switching, open-circuit, and short-circuit conditions using a Boeing 787-inspired architecture.
- Evaluates multiple architectures (CNNs, LSTMs, CNN-LSTMs, ResNet, MobileNet, VGG) and identifies a compact ResNet achieving 96.94% software test accuracy.
- Demonstrates edge hardware feasibility on a Xilinx Zynq UltraScale Plus MPSoC ZCU102 after 8-bit quantization, achieving 95.87% accuracy and 6.90 ms latency.

## Limitations

Focuses on simulation-based evaluation; leaves open end-to-end data acquisition and experimental hardware validation.

## Archivist Review

No concepts or datasets met the strict novelty and reusability criteria for permanent vault entries.

## Links

- [Abstract](https://arxiv.org/abs/2609.10479)
- [PDF](https://arxiv.org/pdf/2609.10479)

