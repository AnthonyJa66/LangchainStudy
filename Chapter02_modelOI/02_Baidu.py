import os
import dotenv
from openai import OpenAI

dotenv.load_dotenv()

client = OpenAI(
    api_key=os.getenv("BD_API_KEY"),
    base_url=os.getenv("BD_BASE_URL"),
    default_headers={"appid": "app-vTrdZxbY"},
)

completion = client.chat.completions.create(
    model="ernie-4.0-turbo-8k",  # 预置服务请查看模型列表，定制服务请填入API地址
    messages=[{'role': 'system', 'content': '你好，我是你的AI助手。'},
              {'role': 'user', 'content': '你会什么？'}]
)

print(completion.choices[0].message.content)
