from langchain_core.prompts import ChatPromptTemplate
from test import llm

# 需要注意的一点是，这里需要指明具体的role，在这里是system和用户
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是世界级的技术文档编写者"),
    ("user", "{input}")  # {input}为变量
])

# 我们可以把prompt和具体llm的调用和在一起。
chain = prompt | llm
message = chain.invoke({"input": "大模型中的LangChain是什么?"})

print(type(message))