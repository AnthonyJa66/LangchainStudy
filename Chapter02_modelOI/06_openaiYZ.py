from langchain_openai import ChatOpenAI
import os
import dotenv

# 前提：加载配置文件
dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")

# 1、获取对话模型
chat_model = ChatOpenAI(
    # api_key=,
    # base_url=,
    model_name="gpt-4o-mini",
    max_tokens=128,
)

# 2、调用对话模型
response = chat_model.invoke("帮我解释一下什么是langchain?")

# 3、处理响应数据
# print(response)
print(response.content)
print(type(response))  #<class 'langchain_core.messages.ai.AIMessage'>