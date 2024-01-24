import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate
# Prompts and Models Exercise
# TASK: Create a Python function that uses Prompts and Chat internally to give travel ideas related to two variables:
# 1.An Interest or Hobby 2. A Budget
# Remember that you should also decide on a system prompt. The end function will just be a nice wrapper on top of all
# the previous LangChain components we've discussed earlier.

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = ""


def travel_idea(interest, budget):
    """ INPUTS:
            interest: A str interest or hobby (e.g. fishing)
            budget: A str budget (e.g. $10,000)
    """
    # Define system interest, budget template -->PromptTemplate
    system_template = "You are a travel agent that helps people plan trips about {interest} on a budget of {budget}"
    system_msg_prompt = SystemMessagePromptTemplate.from_template(system_template)

    # Human Template --> PromptTemplate
    human_template = "Please give me an example itinerary"
    human_msg_prompt = HumanMessagePromptTemplate.from_template(human_template)

    # compile --> ChatPromptTemplate
    chat_prompt = ChatPromptTemplate.from_messages([system_msg_prompt, human_msg_prompt])

    # insert variables --> ChatPromptTemplate
    request = chat_prompt.format_prompt(interest=interest, budget=budget).to_messages()

    # chat request
    chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
    result = chat(request)
    return result.content


print(travel_idea('hiking', '1000₹'))



