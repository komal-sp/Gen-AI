import os
from langchain.prompts import PromptTemplate, ChatPromptTemplate, SystemMessagePromptTemplate, \
    HumanMessagePromptTemplate, AIMessagePromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
# STEP 1 : import parser
from langchain.output_parsers import CommaSeparatedListOutputParser

output_parser = CommaSeparatedListOutputParser()
OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = "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"
model = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

# STEP 2: format instructions
# print(output_parser.get_format_instructions())
reply = "Komal, Sandhya, Papiya"
# print(output_parser.parse(reply))

human_template = "{request}\n{format_instructions}"
human_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([human_prompt])
# model_request = chat_prompt.format_prompt(request="give me 5 characteristics of dogs",
#                                           format_instructions=output_parser.get_format_instructions()).to_messages()


# model_request = chat_prompt.format_prompt(request="what is the best dog?",
#                                           format_instructions=output_parser.get_format_instructions()).to_messages()

# model_request = chat_prompt.format_prompt(request="Write poem about animals",
#                                           format_instructions=output_parser.get_format_instructions()).to_messages()

result = model(model_request)
# print(result.content)
final = output_parser.parse(result.content)
print(final)
