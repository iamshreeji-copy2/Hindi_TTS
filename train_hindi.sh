#!/bin/bash
# Stage 1: GPT Training
echo "Starting GPT Training (Stage 1)..."
conda run --no-capture-output -n GPTSoVits python -u GPT_SoVITS/s1_train.py --config_file "logs/Hindi_Model_v1/s1.yaml" > /media/linux/Seagate/ravi_phd/gpt_sovits/GPT-SoVITS/training_infernece_logs_saved_here/gpt_training.txt 2>&1

# Stage 2: SoVITS Training
echo "Starting SoVITS Training (Stage 2)..."
conda run --no-capture-output -n GPTSoVits python -u GPT_SoVITS/s2_train.py --config "logs/Hindi_Model_v1/s2.json" > /media/linux/Seagate/ravi_phd/gpt_sovits/GPT-SoVITS/training_infernece_logs_saved_here/sovits_training.txt 2>&1
