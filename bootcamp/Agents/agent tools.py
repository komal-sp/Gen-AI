import os
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = ""
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)
