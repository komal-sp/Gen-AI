import os
from langchain import OpenAI

os.environ['OPENAI_API_KEY'] = ""

llm = OpenAI(temperature=0.9)
prompt = "What would a good company name be for a company that makes colourful socks?"
# sprint(llm(prompt))

result = llm.generate([prompt]*5)
print(result)
# for company_name in result.generations:
#     print(company_name[0].text)


