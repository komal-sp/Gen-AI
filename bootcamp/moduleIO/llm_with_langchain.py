from langchain.llms import OpenAI
import os

os.environ['OPENAI_API_KEY'] = "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"
# print(os.environ.get('OPENAI_API_KEY'))

llm = OpenAI(temperature=0.9)
# print(llm("Here is fun fact about pluto:"))

response = llm.generate(['Here is fun fact about pluto:', 'Here is fun fact about Mars:'])
# print(response)
print(response.generations[1][0].text)
# print(response.schema())
# print(response.llm_output)

