---
created_at: '2026-07-31T07:44:44Z'
source_papers:
- '[[openalex-2607.25576-matrix-free-photoacoustic-image-reconstruction-via-sensor-to]]'
title: 3D Sensor Attention Network Extension
---

**Background:** Photoacoustic tomography (PAT) relies on reconstructing initial pressure distributions from acoustic sensor measurements, typically requiring computationally expensive forward operators during inference.

**Question / Future Work:** Extend the Sensor Attention Network (SAN) architecture to three-dimensional PAT by replacing the two-dimensional spatial decoder with a volumetric decoder, and accommodate complex sensor configurations such as cylindrical or hemispherical geometries common in clinical scanners.

**Why It Matters:** Scaling direct Transformer-based reconstruction to 3D and non-planar geometries is critical for bridging the gap between simulated 2D setups and realistic clinical 3D tomographic scanners.

**Evidence:** Third, the SAN architecture should be extended to three-dimensional PAT by replacing the two-dimensional spatial decoder with a 3-D volumetric decoder, and by accommodating cylindrical or hemispherical sensor geometries common in clinical scanners