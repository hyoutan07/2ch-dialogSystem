import torch
from transformers import AutoTokenizer, T5Tokenizer, AutoModelForCausalLM
from nanj import NanJ



def main():
  tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-small", padding_side='left')
  model = AutoModelForCausalLM.from_pretrained("output_num50000/")
  device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

  nanj_min = NanJ(model, tokenizer, device) # NanJインスタンスを作成
  nanj_min.chat()   # チャットを開始
  

if __name__ == "__main__":
  main()
