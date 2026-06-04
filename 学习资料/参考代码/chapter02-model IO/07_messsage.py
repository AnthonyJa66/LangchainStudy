from langchain_core.messages import SystemMessage, HumanMessage

system_message=SystemMessage(content="你是一名英语教学方向的专家")

human_message=HumanMessage(content="支出一句你觉得最好的英文诗句，并用中文翻译。")

message=[system_message,human_message]

print(message)
#打印内容
# [SystemMessage(content='你是一名英语教学方向的专家', additional_kwargs={}, response_metadata={}), HumanMessage(content='支出一句你觉得最好的英文诗句，并用中文翻译。',
# additional_kwargs={}, response_metadata={})]