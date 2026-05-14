---
title: "RF Tokenizer"
slug: "rf-tokenizer"
type: concept
generated_stub: true
source_papers:
  - "[[openalex-2605.10825-large-spectrum-models-lsms-decoder-only-transformer-powered]]"
processed_at: "2026-05-14T07:38:26Z"
created_at: "2026-05-14T07:38:26Z"
---

# RF Tokenizer

> *Auto-generated stub. Edit this file to add more details.*

A method for converting raw IQ measurements into token sequences for transformer models by encoding power-spectral density, gain, frequency, FFT bin, and timestamp information.


## Why It Matters

It enables the application of LLM architectures to raw RF signal data, serving as the core bridge between physical radio frequency measurements and transformer-based sequence processing.

## Evidence

> A novel RF tokenizer is introduced to convert raw IQ measurements into token sequences by mapping each power-spectral density value to a fixed vocabulary along with embedding gain, frequency, FFT bin, and timestamp information.

## Related Papers

- [[openalex-2605.10825-large-spectrum-models-lsms-decoder-only-transformer-powered]]
