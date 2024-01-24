import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import AIMessagePromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate, ChatPromptTemplate

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = "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"
chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

# AI BOT LEGAL --> Simple terms
system_template = "You are a helpful legal assistant that translates complex legal terms into plain understandable terms."
system_msg_prompt = SystemMessagePromptTemplate.from_template(system_template)

# FEW SHOT
# INPUT HUMAN
# OUTPUT AI
legal_text = "The provisions herein shall be severable, and if any provision or portion thereof is deemed invalid, illegal, or unenforceable by a court of competent jurisdiction, the remaining provisions or portions thereof shall remain in full force and effect to the maximum extent permitted by law. example_input_one = HumanMessagePromptTemplate.from_template(legal_text)"
example_input_one = HumanMessagePromptTemplate.from_template(legal_text)


plain_text = "The rule in this agreement can be separated"
example_output_one = AIMessagePromptTemplate.from_template(plain_text)

human_template = f"{legal_text}"
human_msg_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages(
    [system_msg_prompt, example_input_one, example_output_one, human_msg_prompt]
)

# print(chat_prompt.input_variables)

example_legal_text = "The grantor, being the fee simple owner of the real property herein described, conveys and warrants to the grantee, his heirs and assigns, all of the grantor's right, title, and interest in and to the said property, subject to all existing encumbrances, liens, and easements, as recorded in the official records of the county, and any applicable covenants, conditions, and restrictions affecting the property, in consideration of the sum of [purchase price] paid by the grantee."
request = chat_prompt.format_prompt(legal_text=example_legal_text).to_messages()
result = chat(request)
print(result.content)



