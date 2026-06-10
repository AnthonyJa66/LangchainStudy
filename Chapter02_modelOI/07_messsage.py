from langchain_openai import ChatOpenAI
import os
import dotenv
from langchain_core.messages import SystemMessage, HumanMessage

# 前提：加载配置文件
dotenv.load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_BASE_URL"] = os.getenv("OPENAI_BASE_URL")


system_message=SystemMessage(content="你是一名英语教学方向的专家")

human_message=HumanMessage(content="支出一句你觉得最好的英文诗句，并用中文翻译。")

message=[system_message,human_message]

#print(message)
#打印内容
# [SystemMessage(content='你是一名英语教学方向的专家', additional_kwargs={}, response_metadata={}), HumanMessage(content='支出一句你觉得最好的英文诗句，并用中文翻译。',
# additional_kwargs={}, response_metadata={})]

# 1、获取对话模型
chat_model = ChatOpenAI(
    # api_key=,
    # base_url=,
    model_name="gpt-4o-mini",
    max_tokens=64,
)

response = chat_model.invoke(message)
# print(response)
# print(type(response))#<class 'langchain_core.messages.ai.AIMessage'>
# print(response.content)
print(type(response.content))#<class 'str'>
