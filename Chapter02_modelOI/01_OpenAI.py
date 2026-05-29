import os
from openai import OpenAI
import dotenv

# 从环境变量读取API密钥（推荐安全存储）
dotenv.load_dotenv()

client = OpenAI(
    api_key=os.getenv("YZ_API_KEY"),
    base_url=os.getenv("YZ_BASE_URL")
)

"""非对话模型
# # 调用Completion接口
# response = client.completions.create(
#     model="gpt-3.5-turbo-instruct",  # 非对话模型
#     prompt="请将以下英文翻译成中文：\n'Artificial intelligence will reshape the future.'",
#     max_tokens=100,  # 生成文本最大长度
#     temperature=0.7,  # 控制随机性
# )
# # 提取结果
# print(response.choices[0].text.strip())
"""

#对话模型
completion = client.chat.completions.create(
model="gpt-3.5-turbo", # 对话模型
messages=[
{"role": "system", "content": "你是一个乐于助人的智能AI小助手"},
{"role": "user", "content": "你好，请你介绍一下你自己"}
],
max_tokens=150,
temperature=0.5
)
print(completion.choices[0].message)
