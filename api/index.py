# -*- coding: utf-8 -*-
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage 
from api.chatgpt import ChatGPT

import os, re
from const import *

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
line_handler = WebhookHandler(LINE_CHANNEL_SECRET)
working_status = os.getenv("DEFALUT_TALKING", default = "true").lower() == "true"

app = Flask(__name__)
chatgpt = ChatGPT()

# domain root
@app.route('/')
def home():
    return 'Hello, World!'

@app.route("/webhook", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        line_handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


@line_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global working_status
    
    if event.message.type != "text":
        return


    if event.message.text == '--help':
        text = """圖片生成指令: /圖片:[prompt]
程式生成指令: /產生程式:[language]/[prompt]
文法校正指令: /英文校正:[prompt]
蒐集資料: /收集:[數量]/[領域]
內容總結: /總結:[數量]/[內容]
chat_gpt: 輸入 "/啟動" 後開始聊天，輸入 "/結束" 結束聊天"""
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=text))


    if event.message.text.startswith('/圖片:'):
        prompt = event.message.text.replace('/圖片:')
        image_url = chatgpt.get_image(prompt)
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(original_content_url=image_url,
                             preview_image_url=image_url))
    

    if event.message.text.startswith('/英文校正:'):
        prompt = event.message.text.replace('/英文校正:')
        reply_msg = chatgpt.get_grammer_check(prompt)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_msg))
        
    
    if event.message.text.startswith('/產生程式:'):
        lan, prompt = event.message.text.replace('/產生程式:').split('/')
        reply_msg = chatgpt.get_code(lan, prompt)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_msg))


    if event.message.text.startswith('/收集:'):
        count, prompt = event.message.text.replace('/收集:').split('/')
        reply_msg = chatgpt.get_collect_domain_paper(count, prompt)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_msg))


    if event.message.text.startswith('/總結:'):
        count, prompt = event.message.text.replace('/總結:').split('/')
        reply_msg = chatgpt.get_coutent_summary(count, prompt)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_msg))

    if event.message.text == "/啟動":
        working_status = True
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="開始聊天~"))
        return

    if event.message.text == "/結束":
        working_status = False
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="下次再見~"))
        return
    
    if working_status:
        chatgpt.add_msg("Human:{}?\n".format(event.message.text))
        reply_msg = chatgpt.get_response().replace("AI:", "", 1)
        chatgpt.add_msg("AI:{}\n".format(reply_msg))
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_msg))


if __name__ == "__main__":
    app.run(port=3000)
