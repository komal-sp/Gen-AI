from langchain.chat_models import ChatOpenAI
import os
from langchain.schema import AIMessage, HumanMessage, SystemMessage

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = "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"
chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

result = chat([SystemMessage(content="You are   very rude lazy teenager who only wants to party and not answer the questions"),
               HumanMessage(content='Tell me a fact about Pluto')])

# print(result.content)

result= chat.generate([
    [SystemMessage(content="You are   very rude lazy teenager who only wants to party and not answer the questions"),
     HumanMessage(content='Tell me a fact about Pluto')],
    [SystemMessage(content="You are   a friendly assistant"),
     HumanMessage(content='Tell me a fact about Pluto')]
             ])
print(result)
result.generations[0][0].text
