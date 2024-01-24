from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
import os

os.environ['OPENAI_API_KEY'] = ""

template = "You are naming consultant for new companies. What is good name for a {company} that makes {product}?"

prompt = PromptTemplate.from_template(template)
# print(prompt.format(product="colorful socks"))
llm = OpenAI(temperature=0.9)

chain = LLMChain(llm=llm, prompt=prompt)

print(chain.run({"company": "Komal.ltd", "product": "colorful socks"}))
