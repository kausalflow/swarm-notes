---
# CSL-compatible fields
title: "Implementation of a Near-Realtime Recording and Reporting System of Solar Radio Bursts"
author:
  - literal: "Peijin Zhang"
  - literal: "Anastasia Kuske"
  - literal: "Bin Chen"
  - literal: "Mengjia Xu"
  - literal: "Gelu M. Nita"
  - literal: "Marin M. Anderson"
  - literal: "Judd D. Bowman"
  - literal: "Ruby Byrne"
  - literal: "Morgan Catha"
  - literal: "Xingyao Chen"
  - literal: "Sherry Chhabra"
  - literal: "Larry D'Addario"
  - literal: "Ivey Davis"
  - literal: "Jayce Dowell"
  - literal: "Katherine Elder"
  - literal: "Dale Gary"
  - literal: "Gregg Hallinan"
  - literal: "Charlie Harnach"
  - literal: "Greg Hellbourg"
  - literal: "Jack Hickish"
  - literal: "Rick Hobbs"
  - literal: "David Hodge"
  - literal: "Mark Hodges"
  - literal: "Yuping Huang"
  - literal: "Andrea Isella"
  - literal: "Daniel C. Jacobs"
  - literal: "Ghislain Kemby"
  - literal: "John T. Klinefelter"
  - literal: "Matthew Kolopanis"
  - literal: "Nikita Kosogorov"
  - literal: "James Lamb"
  - literal: "Casey Law"
  - literal: "Nivedita Mahesh"
  - literal: "Surajit Mondal"
  - literal: "Brian O'Donnell"
  - literal: "Kathryn Plant"
  - literal: "Corey Posner"
  - literal: "Travis Powell"
  - literal: "Vinand Prayag"
  - literal: "Andres Rizo"
  - literal: "Andrew Frederic Romero-Wolf"
  - literal: "Jun Shi"
  - literal: "Greg Taylor"
  - literal: "Jordan Trim"
  - literal: "Mike Virgin"
  - literal: "Akshatha Vydula"
  - literal: "Sandy Weinreb"
  - literal: "Scott White"
  - literal: "D. P. Woody"
  - literal: "Sijie Yu"
  - literal: "Thomas Zentmeyer"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25446"

# Custom fields
paper_id: "2603.25446"
paper_source: "openalex"
domain: "speech"
tags:
  - "object-detection"
  - "audio-language-model"
  - "realtime"
  - "tool-use"
architectures:
  - "cnn"
datasets:
  []
concept_slugs:
  - "yolo-solar-burst-identification"
  - "physics-based-synthetic-burst-training"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-29T06:09:07Z"
created_at: "2026-03-29T06:09:07Z"
---

# Implementation of a Near-Realtime Recording and Reporting System of Solar Radio Bursts

**Authors**: Peijin Zhang, Anastasia Kuske, Bin Chen, Mengjia Xu, Gelu M. Nita, Marin M. Anderson, Judd D. Bowman, Ruby Byrne, Morgan Catha, Xingyao Chen, Sherry Chhabra, Larry D'Addario, Ivey Davis, Jayce Dowell, Katherine Elder, Dale Gary, Gregg Hallinan, Charlie Harnach, Greg Hellbourg, Jack Hickish, Rick Hobbs, David Hodge, Mark Hodges, Yuping Huang, Andrea Isella, Daniel C. Jacobs, Ghislain Kemby, John T. Klinefelter, Matthew Kolopanis, Nikita Kosogorov, James Lamb, Casey Law, Nivedita Mahesh, Surajit Mondal, Brian O'Donnell, Kathryn Plant, Corey Posner, Travis Powell, Vinand Prayag, Andres Rizo, Andrew Frederic Romero-Wolf, Jun Shi, Greg Taylor, Jordan Trim, Mike Virgin, Akshatha Vydula, Sandy Weinreb, Scott White, D. P. Woody, Sijie Yu, Thomas Zentmeyer
**Date**: 2026-03-26
**Paper ID**: [openalex:2603.25446](https://arxiv.org/abs/2603.25446)

## Summary

This work details the development of a near-realtime system for recording and reporting solar radio bursts, crucial for space weather monitoring, using the Owens Valley Radio Observatory Long Wavelength Array (OVRO LWA). The system directly streams live radio dynamic spectrograms from a real-time buffer and employs a deep-learning module for identifying type III radio bursts. This identifier is specifically based on the YOLO architecture and is trained using synthetic bursts generated via a physics-based model to ensure detection accuracy and robustness. The entire pipeline successfully enables the automatic reporting of events within approximately 10 seconds of their occurrence, significantly reducing latency for critical space weather diagnostics.

## Key Contributions

- Development and implementation of a near-realtime radio burst recording and reporting system using the Owens Valley Radio Observatory Long Wavelength Array (OVRO LWA).
- Creation of a live radio dynamic spectrogram stream directly clipped from a real-time data buffer.
- Implementation of a deep-learning-based module, based on YOLO, for automatic identification of type III radio bursts.
- Achieving continuous realtime radio spectrum streaming and automatic reporting of type III radio bursts within approximately 10 seconds of occurrence.

## Limitations

The system's latency and sensitivity are constrained by the real-time buffer clipping and processing capabilities of the OVRO LWA.

## Open Questions & Future Work

- [[solar-radio-burst-detector-multi-type-retraining]]

## Key Concepts

- [[yolo-solar-burst-identification]]: A deep-learning-based module using the YOLO architecture for the automatic detection and classification of type III solar radio bursts.
- [[physics-based-synthetic-burst-training]]: The technique of generating synthetic type III radio burst data using a physics-based model to train a deep learning detector.

## Archivist Review

Two core methodological concepts were approved: the specific application of YOLO for burst detection in spectrograms and the use of physics-based synthetic data for training. One significant open question was approved concerning the necessary next step of expanding the detection model to cover multiple, critical solar radio burst types, which is crucial for operational space weather utility. Other candidates were rejected as they described system implementation details or the hardware used, rather than reusable ML contributions.

### Approved Concepts
- YOLO-based Solar Burst Identification: This specific application of YOLO to identify type III solar radio bursts in dynamic spectrograms is a novel system component for space weather monitoring.
- Physics-Based Synthetic Burst Training: Using a physics-based model to generate synthetic training data for a deep learning model in radio astronomy is a critical methodological step for robustness.

### Approved Open Questions
- Expand ML detector to new burst types: Expanding the event catalog beyond Type III/IIIb bursts to include Type II bursts (signatures of CME-driven shocks) is necessary to make the system operationally useful for comprehensive space-weather monitoring, which relies on multiple burst types.

### Rejected Candidates
- [open_question] expanding-solar-radio-burst-classification (`expanding-solar-radio-burst-classification`) - duplicate_existing: This open question is identical to the approved candidate 'solar-radio-burst-detector-multi-type-retraining'.
- [concept] Realtime Radio Dynamic Spectrogram Streaming (`realtime-radio-dynamic-spectrogram-streaming`) - paper_local: This is a specific system implementation detail (clipping data from a realtime buffer) rather than a general, reusable ML concept for forecasting or representation learning.
- [concept] Near-Realtime Radio Burst Reporting System (`near-realtime-radio-burst-reporting-system`) - paper_local: This is a description of the end-to-end system implementation for a specific scientific task, not a reusable, generalizable ML method or artifact.
- [dataset] Owens Valley Radio Observatory Long Wavelength Array (`owens-valley-radio-observatory-long-wavelength-array`) - low_impact: This is a facility/instrument, not a named dataset used for benchmarking or training in the ML context.

## Links

- [Abstract](https://arxiv.org/abs/2603.25446)
- [PDF](https://arxiv.org/pdf/2603.25446)

