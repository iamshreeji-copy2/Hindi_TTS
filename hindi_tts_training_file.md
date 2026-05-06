# Hindi TTS Training Guide for GPT-SoVITS

This guide provides step-by-step instructions to train a Hindi Text-to-Speech (TTS) model using the GPT-SoVITS framework. This is intended for users with access to a large GPU.

## 1. Environment Setup

### Prerequisites
- Python 3.9+
- CUDA-enabled GPU (16GB+ VRAM recommended)
- FFmpeg installed

### Installation
```bash
# Clone the repository (if not already done)
git clone https://github.com/RVC-Boss/GPT-SoVITS.git
cd GPT-SoVITS

# Create and activate environment
conda create -n gptsovits python=3.9 -y
conda activate gptsovits

# Install dependencies
pip install -r requirements.txt
```

### Download Pretrained Models
Download the following from [HuggingFace](https://huggingface.co/lj1995/GPT-SoVITS/tree/main):
- `chinese-hubert-base` -> Put in `GPT_SoVITS/pretrained_models/chinese-hubert-base`
- `chinese-roberta-wwm-ext-large` -> Put in `GPT_SoVITS/pretrained_models/chinese-roberta-wwm-ext-large`
- `gsv-v2final-pretrained` (v2 models) -> Put in `GPT_SoVITS/pretrained_models/gsv-v2final-pretrained`

## 2. Dataset Preparation

### Data Format
Your dataset should consist of:
1.  **Audio Files**: `.wav` files (mono, 32kHz or higher).
2.  **Metadata**: A `.list` file containing the mapping.

### Generate `train.list`
The training list must follow this format:
`absolute_path_to_wav|speaker_name|language|text`

Example line:
`/home/user/data/hindi_001.wav|Hindi_Female|hi|नमस्ते, आप कैसे हैं?`

You can use a script like `create_train_list.py` (if provided) to generate this file from your raw data.

## 3. Data Preprocessing

Run the following scripts in order. Replace `<exp_name>` with your project name (e.g., `hindi_v1`).

### Step 1A: Text & BERT Feature Extraction
```bash
export inp_text="train.list"
export exp_name="hindi_v1"
export opt_dir="logs/$exp_name"
export bert_pretrained_dir="GPT_SoVITS/pretrained_models/chinese-roberta-wwm-ext-large"
export is_half="True"
export i_part="0"
export all_parts="1"
export version="v2"

python GPT_SoVITS/prepare_datasets/1-get-text.py
```

### Step 1B: Hubert & Wav32k Extraction
```bash
export cnhubert_base_dir="GPT_SoVITS/pretrained_models/chinese-hubert-base"
export inp_wav_dir="path/to/your/wavs" # Optional if absolute paths used in train.list

python GPT_SoVITS/prepare_datasets/2-get-hubert-wav32k.py
```

### Step 1C: Semantic Feature Extraction
```bash
export pretrained_s2G="GPT_SoVITS/pretrained_models/gsv-v2final-pretrained/s2G233k.pth"
export s2config_path="GPT_SoVITS/configs/s2.json"

python GPT_SoVITS/prepare_datasets/3-get-semantic.py
```

## 4. Training

### Stage 1: GPT Training
1.  Prepare the config: Copy `GPT_SoVITS/configs/s1longer-v2.yaml` to `logs/hindi_v1/s1.yaml`.
2.  Update paths in `s1.yaml` if necessary (usually handled by environment variables in scripts).

Run training:
```bash
python GPT_SoVITS/s1_train.py --config_file "logs/hindi_v1/s1.yaml"
```

### Stage 2: SoVITS Training
1.  Prepare the config: Copy `GPT_SoVITS/configs/s2.json` to `logs/hindi_v1/s2.json`.
2.  Run training:
```bash
python GPT_SoVITS/s2_train.py --config "logs/hindi_v1/s2.json"
```

## 5. Tips for Large GPUs

If you have a very powerful GPU (e.g., A100, H100, or 4090 with 24GB+), you can speed up training by:

1.  **Increase Batch Size**:
    - In `s1.yaml`, increase `batch_size` from 8 to 16 or 32.
    - In `s2.json`, increase `batch_size` from 32 to 64 or 128.
2.  **Use Multiple GPUs**:
    - For preprocessing (Step 1A-1C), you can set `all_parts` to the number of GPUs and run multiple processes with different `i_part`.
    - For training, use `CUDA_VISIBLE_DEVICES` to specify which GPUs to use.
3.  **Precision**:
    - Ensure `is_half="True"` or `precision: 16-mixed` is set to utilize Tensor Cores.

## 6. Inference & Export

Once training is complete, the weights will be saved in:
- GPT weights: `GPT_weights_v2/`
- SoVITS weights: `SoVITS_weights_v2/`

You can use `webui.py` or `api.py` to test your model by selecting these new weights.

### Testing via CLI (Optional)
```bash
python GPT_SoVITS/inference_cli.py \
    --gpt_path "GPT_weights_v2/hindi_v1-e20.ckpt" \
    --sovits_path "SoVITS_weights_v2/hindi_v1_e100.pth" \
    --ref_audio "ref.wav" \
    --ref_text "Reference text here" \
    --target_text "नमस्ते, यह एक परीक्षण है।" \
    --language "Hindi"
```
