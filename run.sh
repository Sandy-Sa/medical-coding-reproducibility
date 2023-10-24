#!/bin/bash

source /home/sandy/miniconda3/bin/activate coding

for chunk in 128 512; do
    python main.py experiment=mimiciv_icd10/plm_icd gpu=1 dataset.configs.chunk_size=$chunk
done
