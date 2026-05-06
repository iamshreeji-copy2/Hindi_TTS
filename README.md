# 🇮🇳 Hindi TTS - GPT-SoVITS (In-Depth Guide) 🚀

This repository is a specialized, feature-rich version of the **GPT-SoVITS** framework, tailor-made for high-quality **Hindi Text-to-Speech (TTS)**. Whether you have zero coding experience or are a seasoned pro, this guide will take you from installation to generating your first Hindi voice clone.

---

## 📖 Project Overview
GPT-SoVITS is a powerful "few-shot" voice cloning tool. This version adds:
- **Full Hindi Support**: Native processing for Devanagari script.
- **Phonetic Accuracy**: Uses a custom ARPA-based system for natural Hindi pronunciation.
- **Dataset Ready**: Pre-configured to work with common Hindi datasets on Hugging Face.

---

## 🛠️ 1. Environmental Setup (Step-by-Step)
Follow these commands exactly to set up your training environment.

### A. Install Conda
If you don't have it, download [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

### B. Create & Activate Environment
```bash
# Create the environment
conda create -n GPTSoVits python=3.10 -y

# Activate it
conda activate GPTSoVits
```

### C. Install the Software
```bash
# This installs all necessary libraries (PyTorch, Transformers, etc.)
bash install.sh
```

---

## 📂 2. Dataset Acquisition (Hugging Face)
We use a standardized Hindi dataset for the best results.

1.  **Download from Hugging Face**: [iamshreeji-copy1/Hindi_TTS_GPT_SoVITS](https://huggingface.co/iamshreeji-copy1/Hindi_TTS_GPT_SoVITS/tree/main)
2.  **Format**: The dataset is in **LJSpeech format** (a zip file containing a `wavs` folder and a `metadata.csv` file).
3.  **Extraction**:
    - Extract the zip file into the `dataset/` folder.
    - Path should look like: `dataset/wavs/*.wav` and `dataset/metadata.csv`.

### 📝 Convert Dataset for Training
Run the helper script to create the `train.list` file which the model needs:
```bash
python create_train_list.py
```
*Note: Open `create_train_list.py` and make sure the `dataset_root` path points to your extracted folder.*

---

## 🗣️ 3. Phonetics: How it Works
This project uses a **Refined ARPA Mapping** for Hindi.

- **What are Phonetics?**: It's how we tell the computer exactly how a word sounds. 
- **The Process**: 
  1.  **Devanagari** (हिन्दी) is transliterated to **ITRANS** (Latin script).
  2.  **ITRANS** is then mapped to **ARPA symbols** (standard phonetic labels used in speech research).
  3.  Example: `नमस्ते` -> `N AH0 M AH0 S T EY1`.
- **Why this matters**: It allows the model to capture the subtle nuances of Hindi vowels (like 'अ' vs 'आ') and consonants accurately.

---

## 🏗️ 4. Training (The A-to-Z Workflow)
Training is done in two "Stages". Think of Stage 1 as the model learning the *language*, and Stage 2 as it learning the *voice*.

### Step A: Feature Extraction (Preparing the Data)
Run these commands one by one:
```bash
# 1. Extract Text & BERT features
export inp_text="train.list"; export exp_name="Hindi_Model_v1"; python GPT_SoVITS/prepare_datasets/1-get-text.py

# 2. Extract Audio features (Hubert)
python GPT_SoVITS/prepare_datasets/2-get-hubert-wav32k.py

# 3. Extract Semantic features
python GPT_SoVITS/prepare_datasets/3-get-semantic.py
```

### Step B: Stage 1 Training (GPT)
```bash
python GPT_SoVITS/s1_train.py --config_file "GPT_SoVITS/configs/s1longer-v2.yaml"
```

### Step C: Stage 2 Training (SoVITS)
```bash
python GPT_SoVITS/s2_train.py --config "GPT_SoVITS/configs/s2.json"
```

---

## 🚀 5. Inference (Generating Speech)
Once trained, you can use the **WebUI** to generate speech.

1.  **Start the UI**:
    ```bash
    python webui.py
    ```
2.  **In the Browser**:
    - Go to the **Inference** tab.
    - Load your GPT model (`.ckpt`) and SoVITS model (`.pth`).
    - Input a **Reference Audio** (the voice you want to copy).
    - Type your **Target Hindi Text**.
    - Click **Generate**.

---

## 🔄 6. Fine-Tuning
If you want to train on a **small amount of data** (e.g., only 1 minute of a specific person's voice):
1. Use the pre-trained weights located in `GPT_SoVITS/pretrained_models/`.
2. Follow the training steps above but for fewer **Epochs** (e.g., 10-15 for GPT).
3. This "fine-tunes" the existing knowledge to a new voice quickly.

---

## 🔗 Quick Links
- 📖 [Step-by-Step Training Deep Dive](./hindi_tts_training_file.md)
- 🧪 [Original GPT-SoVITS Docs](./README_ORIGINAL.md)
- 🐍 [Hindi Phonemizer Source](./GPT_SoVITS/text/hindi.py)

---
*Created for the Hindi AI Community. Based on the open-source [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) project.*
