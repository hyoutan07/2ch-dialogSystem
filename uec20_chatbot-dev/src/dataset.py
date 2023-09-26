import csv

MAX_CEL = 100000
MAX_RESPONCE = 2

INPUT_FILE = 'datasets/livejupiter_replaced.tsv'
OUTPUT_FILE = 'datasets/dataset_num100000.txt'

with open(INPUT_FILE, 'r') as f_in, open(OUTPUT_FILE, 'w') as f_out:
  cnt = 0
  for line in f_in:
    line = line.strip().split('\t')  # 行をタブで区切る
    # <s>入力文[SEP]出力文</s>の形式に変更
    processed_line = f"<s>{line[0]}[SEP]{line[1]}</s>\n"
    f_out.write(processed_line)

    cnt += 1
    if cnt == MAX_CEL:
      break