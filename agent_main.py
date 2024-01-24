# Agents
import pprint
# from langchain.agents import get_all_tool_names
from langchain.agents import load_tools, initialize_agent
from langchain import OpenAI

llm = OpenAI(temperature=0)
prompt = "When was the 3rd president of the United States born? What is that year raised to the power of 3?"

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(get_all_tool_names())

tools = load_tools(["wikipedia", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

agent.run(prompt)
