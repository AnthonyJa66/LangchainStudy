# # 使用Openai的方式
# import os
# import dotenv
# from openai import OpenAI
#
# dotenv.load_dotenv()
# client = OpenAI(
#
#     api_key=os.getenv("DASHSCOPE_API_KEY"),
#     base_url=os.getenv("DASHSCOPE_BASE_URL")
# )
# completion = client.chat.completions.create(
#     model="qwen3.6-flash",  # 此处以 deepseek-r1 qwen3.6-flash qwen3-max glm-5.1 qwen3.7-max-preview
#     messages=[
#         {'role': 'user', 'content': '9.9和9.11谁大'}
#     ]
# )
# # 通过reasoning_content字段打印思考过程
# print("思考过程：")
# print(completion.choices[0].message.reasoning_content)
# # 通过content字段打印最终答案
# print("最终答案：")
# print(completion.choices[0].message.content)


# 使用dashscope SDK方式

# import os
# import dashscope
# import dotenv
#
# dotenv.load_dotenv()
#
# messages = [
#     {'role': 'system', 'content': 'You are a helpful assistant.'},
#     {'role': 'user', 'content': '你是谁？'}
# ]
# response = dashscope.Generation.call(
#     # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx"
#     api_key=os.getenv('DASHSCOPE_API_KEY'),
#     model="qwen-plus",  # 此处以qwen-plus为例，可按需更换模型名称。模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
#     messages=messages,
#     result_format='message'
# )
# print(response.output.choices[0].message.content)

import os
import dashscope
import dotenv

dotenv.load_dotenv()
messages = [
    {'role': 'user', 'content': '你是谁？'}
]
response = dashscope.Generation.call(
    # 若没有配置环境变量，请用阿里云百炼API Key将下行替换为：api_key="sk-xxx",
    api_key=os.getenv('DASHSCOPE_API_KEY'),
    model="deepseek-r1",  # 此处以 deepseek-r1 为例，可按需更换模型名称。
    messages=messages,
    # result_format参数不可以设置为"text"。
    result_format='message'
)
print("=" * 20 + "思考过程" + "=" * 20)
print(response.output.choices[0].message.reasoning_content)
print("=" * 20 + "最终答案" + "=" * 20)
print(response.output.choices[0].message.content)
