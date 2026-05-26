import vector
from langchain_core.prompts import PromptTemplate

retriever = vector.as_retriever()
retriever.search_kwargs = {"k": 3}
docs = retriever.invoke("建设用地使用权是什么？")

# for i,doc in enumerate(docs):
#     print(f"⭐第{i+1}条规定：")
#     print(doc)

# 6.定义提示词模版
prompt_template = """
你是一个问答机器人。
你的任务是根据下述给定的已知信息回答用户问题。
确保你的回复完全依据下述已知信息。不要编造答案。
如果下述已知信息不足以回答用户的问题，请直接回复"我无法回答您的问题"。

已知信息:
{info}

用户问：
{question}

请用中文回答用户问题。
"""
# 7.得到提示词模版对象
template = PromptTemplate.from_template(prompt_template)

# 8.得到提示词对象
prompt = template.format(info=docs, question='建设用地使用权是什么？')

## 9. 调用LLM
response = llm.invoke(prompt)
print(response.content)