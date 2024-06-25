from langchain_cohere import ChatCohere
from langchain.schema.messages import HumanMessage, SystemMessage
import os

chat = ChatCohere(cohere_api_key=os.environ.get("COHERE_API_KEY"))
messages = [
    SystemMessage(content="You are michael scott from the office"),
    HumanMessage(content="Tell me the funniest joke you know")
]

response = chat.invoke(messages)
print(response.content)