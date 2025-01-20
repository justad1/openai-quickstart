
from openai import OpenAI

client = OpenAI(api_key="sk-a6207c8a16a1489b9f13c75a14184d8e", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "帮我写一个端口扫描的脚本工具"},
    ],
    stream=False
)

print(response.choices[0].message.content)
