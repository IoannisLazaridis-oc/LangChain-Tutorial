import os
from langchain_openai import ChatOpenAI

# Retrieving OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initializing LangChain with OpenAI
openai_llm = ChatOpenAI(api_key=openai_api_key)

# Creating and executing a prompt
prompt = "Hi!"
response = openai_llm.invoke(prompt)

print(response.content)
