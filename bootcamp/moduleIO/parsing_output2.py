import os
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate,HumanMessagePromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
# STEP 1 : import parser
from langchain.output_parsers import DatetimeOutputParser
from langchain.output_parsers import OutputFixingParser

output_parser = DatetimeOutputParser()
OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = ""
model = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

# STEP 2: format instructions
# print(output_parser.get_format_instructions())


human_template = "{request}\n{format_instructions}"
human_prompt = HumanMessagePromptTemplate.from_template(human_template)

system_template = "You always reply to questions only in datetime patterns."
system_prompt = SystemMessagePromptTemplate.from_template(system_template)

chat_prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])
# sometimes it will not work

#chat_prompt = ChatPromptTemplate.from_messages([human_prompt])
model_request = chat_prompt.format_prompt(request="When was the 13th Amendment ratified in the US?",
                                          format_instructions=output_parser.get_format_instructions()).to_messages()
result = model(model_request, temperature=0)
# print(result.content)
# final = output_parser.parse(result.content)
# print(final)

miss_formatted = result.content
new_parser = OutputFixingParser.from_llm(parser=output_parser, llm=model)
print(miss_formatted)
#print(new_parser.parser(miss_formatted))


