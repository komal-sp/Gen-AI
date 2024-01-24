import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.chains import LLMChain

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = ""

human_template = "Make up a funny company name for a company that makes: {product}"
human_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([human_prompt])
chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

chain = LLMChain(llm=chat, prompt=chat_prompt)

result = chain.run(product='Computers')
print(result)

