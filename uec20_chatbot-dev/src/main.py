from fastapi import FastAPI
import torch
from transformers import AutoTokenizer, T5Tokenizer, AutoModelForCausalLM
from nanj import NanJ
from models import Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS設定
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
  return {"greeting": "Hello World!"}


@app.post("/api/v1/nanj")
async def create_reply(query: Query):
  tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-small", padding_side='left')
  model = AutoModelForCausalLM.from_pretrained("output_num50000/")
  device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
  
  nanj_min = NanJ(model, tokenizer, device)
  reply = nanj_min.reply(query)
  response = {
    "reply": reply
  }
  return response
