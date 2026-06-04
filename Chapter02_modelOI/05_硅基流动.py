import dotenv
import os
from openai import OpenAI

dotenv.load_dotenv()

client = OpenAI(
    api_key=os.getenv("SILICON_API_KEY"),
    base_url=os.getenv("SILICON_BASE_URL"))

response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3.2",#Pro/deepseek-ai/DeepSeek-R1
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "推理模型会给市场带来哪些新的机会"}
    ],
    temperature=0.7,
    max_tokens=256,
    stream=True
)


# 逐步接收并处理响应
for chunk in response:
    if not chunk.choices:
        continue
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
    if hasattr(chunk.choices[0].delta, 'reasoning_content') and chunk.choices[0].delta.reasoning_content:
        print(chunk.choices[0].delta.reasoning_content, end="", flush=True)
