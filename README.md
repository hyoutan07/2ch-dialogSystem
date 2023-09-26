# 2ch-dialogSystem
https://github.com/1never/open2ch-dialogue-corpus
電通大の稲葉教授が公開している対話ログをrinnaでファインチューニングした対話システムです．
- フロント
  - Next.js
- バックエンド
  - fastAPI

## サーバー立ち上げ方
- docker-compose.ymlを作成
```yml
version: '3'
services:
  2ch_app_好きな名前:
    restart: always
    build:
      context: ./docker/app
      dockerfile: Dockerfile
    container_name: uec20_2ch_app_${USER_NAME}
    working_dir: '/root/'
    tty: true
    volumes:
      - ./src:/root/src
    # runtime: nvidia
    ports: 
     - "好きなポート番号1:8080"
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              capabilities: [ gpu ]

  2ch_app_web_好きな名前:
    restart: always
    build:
      context: ./docker/web
      dockerfile: Dockerfile
    container_name: front_${USER_NAME}
    working_dir: '/root/2ch_app'
    tty: true
    volumes:
      - ./2ch_app:/root/2ch_app
    # runtime: nvidia
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              capabilities: [ gpu ]
    ports: 
     - "好きなポート番号2:3000"
```
- イメージとコンテナを作成．
```bash
  $ docker-compose up -d --build
```
- フロントエンドサーバーを起動
```bash
  $ docker-comopose exec 2ch_app_web_好きな名前 bash
  $ npm i
  $ npm run dev
```
- バックエンドサーバーを起動
```bash
  $ docker-comopose exec 2ch_app_好きな名前 bash
  $ cd src
  $ uvicorn main:app --reload --host 0.0.0.0 --port 好きなポート番号2
```
- 設定したフロントエンドのサーバーにアクセス

### hagingfaceのtransformerを使う際の注意
1. tranformersをgithubからcloneする。
```bash 
git clone https://github.com/huggingface/transformers.git
```
2. transformers/examples/pytorch/language-modeling/run_clm.pyの58行目をコメントアウトする
```python
#check_min_version("4.29.0.dev0")
```

### backend立ち上げかた 
```
$ uvicorn main:app --reload --host 0.0.0.0 --port 8080
```