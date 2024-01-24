import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = "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"
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

# TOPIC BLOG POST ---> [[ OUTLINE ---> CREATE BLOG POST FROM OUTLINE ]]--> BLOG POST TEXT

template = "Give me a simple bullet point outline for a blog post on {topic}"
first_prompt = ChatPromptTemplate.from_template(template)
chain_one = LLMChain(llm=llm, prompt=first_prompt)

template2 = "Write a blog post using this outline {outline}"
second_prompt = ChatPromptTemplate.from_template(template2)
chain_two = LLMChain(llm=llm, prompt=second_prompt)

full_chain = SimpleSequentialChain(chains=[chain_one, chain_two], verbose=True)

result = full_chain.run('Cheesecake')

print(result)
