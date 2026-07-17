---
created_at: '2026-07-17T07:10:35Z'
source_papers:
- '[[openalex-2607.12500-adversarial-attacks-on-online-handwriting-using-salience-bas]]'
title: Defenses against temporal editing
---

**Background:** Online handwriting recognition systems process sequences of pen-tip coordinates, making them vulnerable to adversarial attacks that exploit the sequential structure of the input. While current methods for generating these attacks focus on additive spatial perturbations, such techniques often introduce unnatural high-frequency noise that violates the kinematic smoothness of handwritten trajectories.

**Question / Future Work:** The development of adversarial defense mechanisms specifically tailored to temporal editing attacks remains an open challenge. Although temporal editing successfully bypasses standard spatial perturbation-based defenses, effective countermeasures that maintain high recognition accuracy while robustly resisting these specific structural attacks have not yet been established.

**Why It Matters:** Since temporal editing attacks pose a distinct, more realistic threat to online handwriting than additive spatial noise, creating corresponding defenses is necessary for the security of deployed handwriting recognition systems.