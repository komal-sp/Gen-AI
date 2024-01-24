import os
from langchain.document_loaders import HNLoader
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.chat_models import  ChatOpenAI


OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = "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"
loader = HNLoader("https://news.ycombinator.com/item?id=38544729")

data = loader.load()
# print(data)
# print(data[0].page_content)

human_template = "Please give me a short of the following HackerNews comment: \n{comment}"
human_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([human_prompt])

model = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

result = model(chat_prompt.format_prompt(comment=data[0].page_content).to_messages())
print(result.content)
