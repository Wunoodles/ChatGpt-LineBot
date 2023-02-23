# ChatGpt-LineBot
  - 圖片生成指令: /圖片:[prompt]
  - 程式生成指令: /產生程式:[language]/[prompt]
  - 文法校正指令: /英文校正:[prompt]
  - 蒐集資料: /收集:[數量]/[領域]
  - 內容總結: /總結:[數量]/[內容]
  - chat_gpt: 輸入 "/啟動" 後開始聊天，輸入 "/結束" 結束聊天


# Ngrok Install
```linux
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok
```


# command
```
python index.py
ngrok http 3000
```
