from openai import OpenAI

client = OpenAI(
    api_key="sk-g6G1xSRxxx5LPN7WUCSwtdxG465GVvqSt",
    base_url="https://youziapi.com/v1"
)

response = client.responses.create(
    model="gpt-4.1-mini:floor",
    input=[{"role": "user", "content": "你好，请做个自我介绍"}],
    stream=True,
)

print(response)
# for event in response:
#     print(event.delta)

# for event in response:
#     if event.type == "response.output_text.delta":
#         print(event.delta, end="", flush=True)
