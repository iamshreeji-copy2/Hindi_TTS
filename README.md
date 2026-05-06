# Hindi TTS - GPT-SoVITS

This repository is focused on training and inference for Hindi Text-to-Speech (TTS) using the GPT-SoVITS framework.

## Project Overview
This project provides a complete setup for Hindi TTS, including:
- Integrated support for Hindi (`hi`) text processing and phonemization.
- Scripts for dataset preparation and conversion.
- Comprehensive training guides for Stage 1 (GPT) and Stage 2 (SoVITS).

## Getting Started

### 1. Training Guide
For detailed, step-by-step instructions on how to train your own Hindi TTS model, please refer to:
👉 **[hindi_tts_training_file.md](./hindi_tts_training_file.md)**

### 2. Installation
Follow the standard GPT-SoVITS installation:
```bash
conda create -n GPTSoVits python=3.10
conda activate GPTSoVits
bash install.sh
```

### 3. Quick Links
- [GPT-SoVITS Original README](./README_ORIGINAL.md)
- [Hindi Text Processing](./GPT_SoVITS/text/hindi.py)

---
*Based on the [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) framework.*
