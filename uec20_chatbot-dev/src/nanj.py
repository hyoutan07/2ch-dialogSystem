class NanJ:
  def __init__(self, model, tokenizer, device):
    self.model = model
    self.tokenizer = tokenizer
    self.device = device


  # generate_replyメソッド：入力を受け取って，GPT2によって返答を生成し，プリントする
  def generate_reply(self, inp, num_gen=1, min_length=10, max_length=64):
    model = self.model
    tokenizer = self.tokenizer
    device = self.device

    input_text = "<s>" + str(inp) + "[SEP]"
    input_ids = tokenizer.encode(input_text, return_tensors='pt').to(device)
    model.to(device)  # モデルにもデバイスを渡す必要あり https://stackoverflow.com/questions/71050697/transformers-how-to-use-cuda-for-inferencing
    out = model.generate(input_ids,
                        pad_token_id=tokenizer.eos_token_id, # 対策：The attention mask and the pad token id were not set.
                        do_sample=True, 
                        min_length=min_length,
                        max_length=max_length, 
                        num_return_sequences=num_gen, 
                        top_p=0.95, 
                        top_k=20, 
                        bad_words_ids=[[1], [5]], 
                        no_repeat_ngram_size=3)

    print(">", "なんJ民")
    for sent in tokenizer.batch_decode(out):
      sent = sent.split('[SEP]</s>')[1]
      sent = sent.replace('</s>', '')
      sent = sent.replace('<br>', '\n')
      print(sent)


  # replyメソッド：入力を受け取って，GPT2によって返答を生成し，返答を return 
  # generate_replyとの違いは，returnするかしないか．APIはこれつかうといいとおもう
  def reply(self, inp, num_gen=1, min_length=10, max_length=64):
    model = self.model
    tokenizer = self.tokenizer
    device = self.device

    input_text = "<s>" + str(inp) + "[SEP]"
    input_ids = tokenizer.encode(input_text, return_tensors='pt').to(device)
    model.to(device)  # モデルにもデバイスを渡す必要あり https://stackoverflow.com/questions/71050697/transformers-how-to-use-cuda-for-inferencing
    out = model.generate(input_ids,
                        pad_token_id=tokenizer.eos_token_id, # 対策：The attention mask and the pad token id were not set.
                        do_sample=True, 
                        min_length=min_length,
                        max_length=max_length, 
                        num_return_sequences=num_gen, 
                        top_p=0.95, 
                        top_k=20, 
                        bad_words_ids=[[1], [5]], 
                        no_repeat_ngram_size=3)

    for sent in tokenizer.batch_decode(out):
      sent = sent.split('[SEP]</s>')[1]
      sent = sent.replace('</s>', '')
      sent = sent.replace('<br>', '\n')
      return sent
      print(sent)
  

  # chatメソッド：なんJ民とチャットします
  def chat(self):
    while True:
      try:
        inp = input("> イッチ\n", )
        self.generate_reply(inp)
      except KeyboardInterrupt:
        print("( ・ω・)おつかれーした")
        break