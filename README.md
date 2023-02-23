# ChatGpt-LineBot
  - 圖片生成指令: /圖片:[prompt]
  - 程式生成指令: /產生程式:[language]/[prompt]
  - 文法校正指令: /英文校正:[prompt]
  - 蒐集資料: /收集:[數量]/[領域]
  - 內容總結: /總結:[數量]/[內容]
  - chat_gpt: 輸入 "/啟動" 後開始聊天，輸入 "/結束" 結束聊天


# Enviroment Install
```linux
udo apt update
sudo apt install python3 python3-dev python3-venv python3-pip screen

curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list && sudo apt update && sudo apt install ngrok
```

# LineBot Setting
- add webhook link
![add webhook link](https://github.com/Wunoodles/ChatGpt-LineBot/blob/main/image/1.png | width=50)
- close auto reply
![close auto reply](https://github.com/Wunoodles/ChatGpt-LineBot/blob/main/image/2.png | width=50)
# Command
```
python index.py
ngrok http 3000
```
