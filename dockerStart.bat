@echo off
set model=bigscience/bloom-560m
set num_shard=1
set volume=%cd%\data

docker run --gpus all --shm-size 1g -p 8080:80 -v %volume%:/data ghcr.io/huggingface/text-generation-inference:latest --model-id %model% --num-shard %num_shard%
