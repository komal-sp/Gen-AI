import os
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = "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"
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)
tools = load_tools(["llm-math"], llm=llm)
# print(type(tools))
# print(dir(AgentType))
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False)
agent.run("What is 134292 times 29388420?")
