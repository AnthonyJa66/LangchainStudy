#from openai import OpenAI
# import dotenv
# import os
#
# dotenv.load_dotenv()

# client = OpenAI(
#     api_key=os.getenv("ZP_API_KEY"),
#     base_url=os.getenv("ZP_BASE_URL")
# )
#
# completion = client.chat.completions.create(
#     model="glm-4-air-250414",
#     messages=[
#         {"role": "system", "content": "你是一个聪明且富有创造力的小说作家"},
#         {"role": "user", "content": "请你作为童话故事大王，写一篇短篇童话故事，故事的主题是要永远保持一颗善良的心，要能够激发儿童的学习兴趣和想象力，同时也能够帮助儿童更好地理解和接受故事中所蕴含的道理和价值观。"}
#     ],
#     top_p=0.7,
#     temperature=0.9,
#     max_tokens=128,
# )
#
# print(completion.choices[0].message.content)

# from langchain_openai import ChatOpenAI
# from langchain.prompts import (
#     ChatPromptTemplate,
#     MessagesPlaceholder,
#     SystemMessagePromptTemplate,
#     HumanMessagePromptTemplate,
# )
# from langchain.chains import LLMChain
# from langchain.memory import ConversationBufferMemory
#
# llm = ChatOpenAI(
#     temperature=0.95,
#     model="glm-4-air-250414",
#     openai_api_key=os.getenv("ZP_API_KEY"),
#     openai_api_base=os.getenv("ZP_URL"),
# )
# prompt = ChatPromptTemplate(
#     messages=[
#         SystemMessagePromptTemplate.from_template(
#             "You are a nice chatbot having a conversation with a human."
#         ),
#         MessagesPlaceholder(variable_name="chat_history"),
#         HumanMessagePromptTemplate.from_template("{question}")
#     ]
# )
# memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
# conversation = LLMChain(
#     llm=llm,
#     prompt=prompt,
#     verbose=True,
#     memory=memory
# )
# conversation.invoke({"question": "给我讲个冷笑话"})

import dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

dotenv.load_dotenv()
# 创建 LLM 实例
llm = ChatOpenAI(
    temperature=0.7,
    model="glm-5.1",
    openai_api_key=os.getenv("ZP_API_KEY"),
    openai_api_base=os.getenv("ZP_BASE_URL")

)

# # 或者使用环境变量
# llm = ChatOpenAI(
#     temperature=0.6,
#     model="glm-5.1",
#     openai_api_key=os.getenv("ZAI_API_KEY"),
#     openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
# )

# 创建消息
messages = [
    SystemMessage(content="你是一个有用的 AI 助手"),
    HumanMessage(content="请介绍一下人工智能的发展历程")
]

# 调用模型
response = llm.invoke(messages)
print(response.content)