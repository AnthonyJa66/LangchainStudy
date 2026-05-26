from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from test import llm

# 初始化模型
llm = ChatOpenAI(model="mimo-v2.5-pro")
#deepseek-v4-flash
#mimo-v2.5-pro

# 创建提示模板
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是世界级的技术文档编写者。"),
    ("user", "{input}")
])

# 使用输出解析器
# output_parser = StrOutputParser()
output_parser = JsonOutputParser()

# 将其添加到上一个链中
# chain = prompt | llm
chain = prompt | llm | output_parser

# 调用它并提出同样的问题。答案是一个字符串，而不是ChatMessage
# chain.invoke({"input": "LangChain是什么?"})
chain.invoke({"input": "LangChain是什么? 用JSON格式回复，问题用question，回答用answer"})