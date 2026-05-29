#导入 dotenv 库的 load_dotenv 函数，用于加载环境变量文件（.env）中的配置
import os
import dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


dotenv.load_dotenv() #加载当前目录下的 .env 文件

os.environ['OPENAI_API_KEY'] = os.getenv("YZ_API_KEY")
os.environ['OPENAI_BASE_URL'] = os.getenv("YZ_BASE_URL")
# 创建大模型实例

llm = ChatOpenAI(model="gpt-5.4-nano")
# 直接提供问题，并调用llm   gpt-5.4-nano
#deepseek-v4-flash
#mimo-v2.5-pro

response = llm.invoke("什么是大模型？")
print(response.content)

# # 需要注意的一点是，这里需要指明具体的role，在这里是system和用户
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "你是世界级的技术文档编写者"),
#     ("user", "{input}")  # {input}为变量
# ])
#
# # 我们可以把prompt和具体llm的调用和在一起。
# chain = prompt | llm
# message = chain.invoke({"input": "大模型中的Agent是什么?"})
#
# print(message)
# print(type(message))