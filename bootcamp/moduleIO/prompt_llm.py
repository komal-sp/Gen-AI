import os
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate
from langchain.prompts import ChatPromptTemplate, PromptTemplate, SystemMessagePromptTemplate, AIMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.schema import AIMessage, HumanMessage, SystemMessage

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = ""

# ---------------------------------------------------------------------------------------------------------------------#

llm = OpenAI(openai_api_key=OPENAI_API_KEY)
chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

planet = "Venus"
result = llm(f"Here is a fact about {planet}")

no_input_prompt = PromptTemplate(input_variables=[], template="Tell me a fact")

# print(llm(no_input_prompt.format()))

no_input_prompt = PromptTemplate(input_variables=["topic"], template="Tell me a fact about {topic}")
# print(llm(no_input_prompt.format(topic="human")))

multi_input_prompt = PromptTemplate(input_variables=["topic", "level"],
                                    template="Tell me a fact about {topic} and {level}")
# print(llm(multi_input_prompt.format(topic="human", level="blood")))

# ---------------------------------------------------------------------------------------------------------------------#

system_template = "You are an AI assistant that specializes in {dietary_preference} dishes that can be prepared in {time}"
system_msg_prompt = SystemMessagePromptTemplate.from_template(system_template)

human_template = "{recipe_request}"


# ---------------------------------------------------------------------------------------------------------------------#
