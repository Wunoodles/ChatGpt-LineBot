from prompt import Prompt

import os
import openai
from const import *

openai.api_key = OPENAI_API_KEY

class ChatGPT:
    def __init__(self):
        self.prompt = Prompt()
        self.model = os.getenv("OPENAI_MODEL", default = "text-davinci-003")
        #self.model = os.getenv("OPENAI_MODEL", default = "chatbot")
        self.temperature = float(os.getenv("OPENAI_TEMPERATURE", default = 0))
        self.frequency_penalty = float(os.getenv("OPENAI_FREQUENCY_PENALTY", default = 0))
        self.presence_penalty = float(os.getenv("OPENAI_PRESENCE_PENALTY", default = 0.6))
        self.max_tokens = int(os.getenv("OPENAI_MAX_TOKENS", default = 2000))

    def get_response(self):
        response = openai.Completion.create(
            model=self.model,
            prompt=self.prompt.generate_prompt(),
            temperature=self.temperature,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            max_tokens=self.max_tokens
        )
        return response['choices'][0]['text'].strip()

    def get_image(self, prompt):
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )

        return response['data'][0]['url']


    def get_grammer_check(self, prompt):
        start_prompt = 'Can you check the spelling and grammar in the following text? '
        response = openai.Completion.create(
            model=self.model,
            prompt=start_prompt+prompt,
            temperature=self.temperature,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            max_tokens=self.max_tokens
        )
        return response['choices'][0]['text'].strip()

    
    def get_code(self, language, prompt):
        prompt_ = f'你現在是一個 {language} 專家，請幫我用 {language} 寫一個函式，它需要做到 {prompt} 某個功能'
        response = openai.Completion.create(
            model=self.model,
            prompt=prompt_,
            temperature=self.temperature,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            max_tokens=self.max_tokens
        )
        return response['choices'][0]['text'].strip()

    
    def get_collect_domain_paper(self, count, prompt):
        prompt_ = f'給我 {count} 篇，有關 {prompt} 的文章'
        response = openai.Completion.create(
            model=self.model,
            prompt=prompt_,
            temperature=self.temperature,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            max_tokens=self.max_tokens
        )
        return response['choices'][0]['text'].strip()


    def get_coutent_summary(self, count, prompt):
        prompt_ = f'用列點的方式總結出這篇文章的 {count} 個重點：{prompt}'
        response = openai.Completion.create(
            model=self.model,
            prompt=prompt_,
            temperature=self.temperature,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            max_tokens=self.max_tokens
        )
        return response['choices'][0]['text'].strip()


    def add_msg(self, text):
        self.prompt.add_msg(text)
