import subprocess

script = """
#!/bin/bash
python ./transformers/examples/pytorch/language-modeling/run_clm.py \
    --model_name_or_path=rinna/japanese-gpt2-small \
    --train_file=dataset.txt \
    --validation_file=datasets/dataset_num100000.txt \
    --do_train \
    --do_eval \
    --num_train_epochs=10 \
    --save_steps=10000 \
    --save_total_limit=3 \
    --per_device_train_batch_size=1 \
    --per_device_eval_batch_size=1 \
    --output_dir=./output_num100000 \
    --use_fast_tokenizer=False
"""

subprocess.call(script, shell=True)