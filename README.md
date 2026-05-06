# 🇮🇳 Hindi TTS - GPT-SoVITS 🚀

Welcome to the **Hindi TTS** project! This repository is a specialized version of the powerful [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) framework, optimized specifically for the **Hindi language**.

Whether you are a researcher, developer, or a hobbyist, this guide will help you set up and train your own Hindi voice model from scratch.

---

## 📋 Table of Contents
1. [Introduction](#introduction)
2. [Environmental Setup](#environmental-setup)
3. [Dataset Acquisition](#dataset-acquisition)
4. [Phonetics & Language Support](#phonetics--language-support)
5. [Training Workflow](#training-workflow)
6. [Inference](#inference)
7. [Fine-Tuning](#fine-tuning)

---

## 🌟 Introduction
This project provides:
- **Hindi (`hi`) Support**: Native phonemization and text normalization for Devanagari script.
- **Easy Preprocessing**: Scripts to convert LJSpeech-style datasets into GPT-SoVITS format.
- **High Quality**: Leverages the state-of-the-art GPT-SoVITS v2 architecture.

---

## 💻 Environmental Setup
Follow these steps to prepare your computer for training.

### 1. Install Anaconda/Miniconda
If you don't have it, download and install [Conda](https://docs.conda.io/en/latest/miniconda.html).

### 2. Create the Environment
```bash
# Create a new environment named GPTSoVits
conda create -n GPTSoVits python=3.10 -y

# Activate the environment
conda activate GPTSoVits
```

### 3. Install Dependencies
```bash
# Install the core project and its requirements
bash install.sh
```

---

## 📂 Dataset Acquisition
We use a high-quality Hindi dataset hosted on Hugging Face.

### 1. Download the Dataset
You can find the dataset at: [iamshreeji-copy1/Hindi_TTS_GPT_SoVITS](https://huggingface.co/datasets/iamshreeji-copy1/Hindi_TTS_GPT_SoVITS)

### 2. Prepare the Files
1. Download the `Hindi_Dataset.zip` file.
2. Extract it into a folder named `dataset/`.
3. The dataset should be in **LJSpeech format**:
   - `wavs/`: Contains your `.wav` audio files.
   - `metadata.csv`: Contains `audio_filename|text`.

### 3. Convert to Training List
Run this command to generate the `train.list` file required for training:
```bash
python create_train_list.py
```
*(Ensure you update the paths inside `create_train_list.py` to match your local dataset folder.)*

---

## 🗣️ Phonetics & Language Support
This project uses a refined **ARPA-based Phonetic Mapping** for Hindi. 

- **Transliteration**: We convert Devanagari (हिन्दी) to ITRANS (Latin) using the `indic-transliteration` library.
- **Phoneme Mapping**: Each ITRANS character is mapped to standard ARPA symbols (e.g., `नमस्ते` -> `N AH0 M AH0 S T EY1`).
- **Punctuation**: Full support for `. , ! ?` to handle speech prosody.

This ensures that the model understands the unique sounds of Hindi vowels and consonants accurately.

---

## 🛠️ Training Workflow
Training happens in two main stages.

### Pre-processing (Data Prep)
Run these in order to extract features:
```bash
# Step 1A: Text & BERT Features
export inp_text="train.list"; export exp_name="hindi_v1"; python GPT_SoVITS/prepare_datasets/1-get-text.py

# Step 1B: Audio Features (Hubert)
python GPT_SoVITS/prepare_datasets/2-get-hubert-wav32k.py

# Step 1C: Semantic Features
python GPT_SoVITS/prepare_datasets/3-get-semantic.py
```

### Stage 1: GPT Training (Text to Semantic)
This teaches the model "how to speak" the text.
```bash
python GPT_SoVITS/s1_train.py --config_file "GPT_SoVITS/configs/s1longer-v2.yaml"
```

### Stage 2: SoVITS Training (Semantic to Audio)
This teaches the model "the voice quality".
```bash
python GPT_SoVITS/s2_train.py --config "GPT_SoVITS/configs/s2.json"
```

---

## 🎯 Fine-Tuning
If you already have a pre-trained model and want to teach it a specific new voice:
1. Load the pre-trained weights in the WebUI.
2. Reduce the number of epochs (e.g., 10-20 for GPT, 50 for SoVITS).
3. Run the training scripts above using your new dataset.

---

## 🔊 Inference
To generate speech using your trained model:

### Using WebUI (Recommended for beginners)
```bash
python webui.py
```
1. Open the URL shown in your terminal (usually `http://localhost:9874`).
2. Go to the "Inference" tab.
3. Select your trained `.ckpt` (GPT) and `.pth` (SoVITS) files.
4. Type your Hindi text and click **Generate**.

---

## 🔗 Quick Links
- 📖 [Hindi Training Deep Dive](./hindi_tts_training_file.md)
- 🧪 [Original GPT-SoVITS README](./README_ORIGINAL.md)
- 🐍 [Hindi Phonemizer Logic](./GPT_SoVITS/text/hindi.py)

---
*Developed with ❤️ for the Hindi community. Based on the open-source [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) project.*
