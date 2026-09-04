---
created_at: '2026-09-04T09:11:08Z'
source_papers:
- '[[openalex-2609.01524-quantum-weighted-moving-average-for-predicting-limit-order-b]]'
title: Hardware-Friendly LCU Implementations for Financial ML
---

**Background:** Quantum machine learning models such as the quantum weighted moving average (QWMA) are evaluated for financial trend prediction using limit order book data, but current implementations rely on resource-intensive circuit subroutines.

**Question / Future Work:** Investigate and develop hardware-friendly implementations of linear combinations of unitaries (LCU), such as single-ancilla or ancilla-free methods, to reduce the reliance on costly multi-controlled quantum gates and multiple ancilla qubits required for quantum moving average models.

**Why It Matters:** Crucial for reducing the circuit overhead and qubit requirements of hybrid quantum-classical financial algorithms, making them more viable on near-term NISQ and early fault-tolerant hardware.

**Evidence:** As the LCU implementation employed in this work requires costly multi-controlled quantum gates and several ancilla qubits, one could also experiment with hardware friendly LCU implementations.