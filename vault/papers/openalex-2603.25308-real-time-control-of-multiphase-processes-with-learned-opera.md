---
# CSL-compatible fields
title: "Real-time control of multiphase processes with learned operators"
author:
  - literal: "Paolo Guida"
  - literal: "Didier Barradas-Bautista"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25308"

# Custom fields
paper_id: "2603.25308"
paper_source: "openalex"
domain: "robotics"
tags:
  - "reinforcement-learning"
  - "planning"
  - "agent"
  - "tool-use"
  - "fourier-neural-operator"
architectures:
  []
datasets:
  []
concept_slugs:
  - "fourier-neural-operator-for-forecasting"
  - "surrogate-assisted-mpc-for-multiphase-processes"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-29T06:08:23Z"
created_at: "2026-03-29T06:08:23Z"
---

# Real-time control of multiphase processes with learned operators

**Authors**: Paolo Guida, Didier Barradas-Bautista
**Date**: 2026-03-26
**Paper ID**: [openalex:2603.25308](https://arxiv.org/abs/2603.25308)

## Summary

This paper addresses the computational bottleneck of using high-fidelity numerical models for real-time control of complex multiphase processes by proposing a surrogate-assisted Model Predictive Control (MPC) framework. The authors train a Fourier Neural Operator (FNO) to act as a fast surrogate, capable of forecasting the spatiotemporal evolution of a phase-indicator field (volume fraction) based on recent states and candidate actuation signals. This learned operator is then iteratively called within the MPC optimization loop to identify the optimal control input in real-time. The approach is successfully demonstrated on an optimal control problem involving tracking liquid level setpoints in a two-phase Eulerian bubble column by manipulating the gas flow rate. The results confirm that FNO-based field-level forecasting is computationally efficient enough to support closed-loop optimization for fast unit operations.

## Key Contributions

- Proposing a surrogate-assisted Model Predictive Control (MPC) framework that utilizes learned operators to enable real-time control of multiphase processes.
- Training a Fourier Neural Operator (FNO) to rapidly forecast the spatiotemporal evolution of a phase-indicator field (volume fraction) over a finite horizon.
- Demonstrating the framework's applicability by solving an Optimal Control Problem (OCP) for tracking liquid level setpoints in a two-phase Eulerian bubble column by adjusting gas flow rate.
- Showing that field-level forecasting with FNOs offers a low evaluation cost suitable for closed-loop optimization in fast multiphase unit operations.

## Limitations

The demonstration is currently limited to a specific two-phase system (Eulerian bubble column) and does not fully address partial observability, which is left for future work.

## Key Concepts

- [[fourier-neural-operator-for-forecasting]]: Using a Fourier Neural Operator to learn the spatiotemporal evolution of system states for fast forecasting in a control loop.
- [[surrogate-assisted-mpc-for-multiphase-processes]]: A control framework where a learned neural operator acts as a fast, differentiable surrogate model inside an iterative Model Predictive Control optimization loop.

## Archivist Review

Two core concepts were approved. The first establishes the use of the Fourier Neural Operator (FNO) as a computational surrogate for spatiotemporal forecasting within a control context. The second approves the overall framework of 'Surrogate-Assisted MPC', which details the reusable pattern of embedding a fast learned model inside an iterative real-time controller for computationally expensive systems. No datasets or open questions were deemed necessary for vault inclusion.

### Approved Concepts
- Fourier Neural Operator (FNO) for Forecasting: The FNO is the core learned operator used as a fast, differentiable surrogate for the complex multiphase dynamics within the Model Predictive Control (MPC) framework.
- Surrogate-Assisted Model Predictive Control for Multiphase Processes: This framework explicitly integrates a learned, fast surrogate (the FNO) into a standard MPC loop to overcome the computational bottleneck of using high-fidelity numerical simulators for real-time control.

### Rejected Candidates
- [concept] Fourier Neural Operator (FNO) for Forecasting (`fourier-neural-operator-for-forecasting`) - other: The concept 'Fourier Neural Operator (FNO) for Forecasting' is approved, but the provided slug `fourier-neural-operator-for-forecasting` is nearly identical to the existing 'fourier-neural-operator' in the vault, suggesting it should be treated as a direct synonym or a specific application of the existing one. However, since the paper heavily features the FNO as the core surrogate, and no existing concept perfectly captures this specific role in MPC for fluid dynamics, I will approve it as a new, more specific concept for clarity in this context, despite the close name. (Correction: Upon final review, the closest existing concept is 'fourier-neural-operator', which is *not* in the vault list provided. The provided list does not contain 'fourier-neural-operator'. Therefore, both approved concepts are distinct and new/necessary.)
- [concept] Surrogate-Assisted Model Predictive Control for Multiphase Processes (`surrogate-assisted-mpc-for-multiphase-processes`) - other: This concept explicitly combines the method (surrogate-assisted MPC) with the application domain (multiphase processes), which is central to the paper's novelty and a reusable pattern in physical control systems.

## Links

- [Abstract](https://arxiv.org/abs/2603.25308)
- [PDF](https://arxiv.org/pdf/2603.25308)

