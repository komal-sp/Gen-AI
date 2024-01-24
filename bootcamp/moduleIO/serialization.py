import os
from langchain.prompts import PromptTemplate, load_prompt
from langchain.chat_models import ChatOpenAI


OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = ""
model = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

template = "Tell me a fact about {planet}"
prompt = PromptTemplate(template=template, input_variables=["planet"])
prompt.save("myprompt.json")

loaded_prompt = load_prompt("myprompt.json")
print(loaded_prompt)
