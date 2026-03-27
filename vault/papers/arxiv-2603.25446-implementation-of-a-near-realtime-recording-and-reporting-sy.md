---
# CSL-compatible fields
title: "Implementation of a Near-Realtime Recording and Reporting System of Solar Radio Bursts"
author:
  - literal: "Peijin Zhang"
  - literal: "Anastasia Kuske"
  - literal: "Bin Chen"
  - literal: "Mengjia Xu"
  - literal: "Gelu Nita"
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
  - literal: "Kathryn A. Plant"
  - literal: "Corey Posner"
  - literal: "Travis Powell"
  - literal: "Vinand Prayag"
  - literal: "Andres Rizo"
  - literal: "Andrew Romero-Wolf"
  - literal: "Jun Shi"
  - literal: "Greg Taylor"
  - literal: "Jordan Trim"
  - literal: "Mike Virgin"
  - literal: "Akshatha Vydula"
  - literal: "Sandy Weinreb"
  - literal: "Scott White"
  - literal: "David Woody"
  - literal: "Sijie Yu"
  - literal: "Thomas Zentmeyer"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25446"

# Custom fields
paper_id: "2603.25446"
paper_source: "arxiv"
domain: "speech"
tags:
  - "object-detection"
  - "tool-use"
  - "agent"
  - "speech"
  - "benchmark"
architectures:
  - "object-detection"
datasets:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T09:10:24Z"
created_at: "2026-03-27T09:10:24Z"
---

# Implementation of a Near-Realtime Recording and Reporting System of Solar Radio Bursts

**Authors**: Peijin Zhang, Anastasia Kuske, Bin Chen, Mengjia Xu, Gelu Nita, Marin M. Anderson, Judd D. Bowman, Ruby Byrne, Morgan Catha, Xingyao Chen, Sherry Chhabra, Larry D'Addario, Ivey Davis, Jayce Dowell, Katherine Elder, Dale Gary, Gregg Hallinan, Charlie Harnach, Greg Hellbourg, Jack Hickish, Rick Hobbs, David Hodge, Mark Hodges, Yuping Huang, Andrea Isella, Daniel C. Jacobs, Ghislain Kemby, John T. Klinefelter, Matthew Kolopanis, Nikita Kosogorov, James Lamb, Casey Law, Nivedita Mahesh, Surajit Mondal, Brian O'Donnell, Kathryn A. Plant, Corey Posner, Travis Powell, Vinand Prayag, Andres Rizo, Andrew Romero-Wolf, Jun Shi, Greg Taylor, Jordan Trim, Mike Virgin, Akshatha Vydula, Sandy Weinreb, Scott White, David Woody, Sijie Yu, Thomas Zentmeyer
**Date**: 2026-03-26
**Paper ID**: [arxiv:2603.25446](https://arxiv.org/abs/2603.25446)

## Summary

This work details the creation of a near-realtime system utilizing the Owens Valley Radio Observatory Long Wavelength Array data stream for recording and reporting solar radio bursts, critical for space weather applications. The core innovation involves a deep-learning module based on the YOLO architecture, trained on synthetic bursts generated via a physics-based model, to identify Type III radio bursts directly from a live radio dynamic spectrogram buffer. The system successfully processes data and automatically reports burst events within about 10 seconds of occurrence, offering a significant reduction in latency compared to previous capabilities. This continuous, automated monitoring capability addresses the long-standing limitation of low-latency, high-sensitivity radio burst detection in solar physics.

## Key Contributions

- Developed a near-realtime radio burst recording and reporting system for the Owens Valley Radio Observatory Long Wavelength Array, achieving reporting within approximately 10 seconds of occurrence.
- Implemented a deep-learning-based burst identification module based on the YOLO architecture to automatically detect Type III radio bursts from live radio dynamic spectrograms.
- Trained the YOLO burst identifier using synthetic Type III radio bursts generated from a physics-based model to ensure accurate and robust detection performance.
- Enabled continuous, low-latency monitoring of solar radio emissions, significantly improving capabilities for space weather monitoring and forecasting applications.

## Limitations

The system's performance is contingent on the accuracy of the underlying physics-based model used to generate synthetic training data for the YOLO identifier.

## Open Questions & Future Work

- [[expanding-solar-radio-burst-classification]]

## Key Concepts

- [Type III Radio Burst Identification](../concepts/type-iii-radio-burst-identification.md): A deep learning system utilizing a YOLO architecture for the near-realtime detection and reporting of Type III solar radio bursts from observational data streams.

## Limitations

The system's performance is contingent on the accuracy of the underlying physics-based model used to generate synthetic training data for the YOLO identifier.

## Links

- [ArXiv Abstract](https://arxiv.org/abs/2603.25446)
- [PDF](https://arxiv.org/pdf/2603.25446)

