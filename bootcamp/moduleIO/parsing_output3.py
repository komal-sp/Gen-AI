import os
from langchain.prompts import ChatPromptTemplate,HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI
# STEP 1 : import parser
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = ""
model = ChatOpenAI(openai_api_key=OPENAI_API_KEY)


class Scientist(BaseModel):
    name: str = Field(description="Name of a scientist")
    discoveries: list = Field(description="Python list of discoveries")


parser = PydanticOutputParser(pydantic_object=Scientist)
#print(parser.get_format_instructions())

human_template = "{request}\n{format_instructions}"
human_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([human_prompt])

request = chat_prompt.format_prompt(request="Tell me about famous scientist",
                                    format_instructions=parser.get_format_instructions()).to_messages()


result = model(request, temperature=0)
#print(result.content)
print(parser.parse(result.content))
# print(final)
