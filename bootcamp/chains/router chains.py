import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.chains.router.multi_prompt import MULTI_PROMPT_ROUTER_TEMPLATE
from langchain.prompts import PromptTemplate
from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser
from langchain.chains.router import MultiPromptChain
OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = "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"
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

# Student ask Physics
# "how does a magnet work?
# "explain Feynman diagram?
# INPUT --> ROUTER --> LLM decides Chain --> OUTPUT

beginner_template = """You are a physics teacher who is really focused on beginner and explaining complex concepts in 
                    simple to understand terms. You assume no prior knowledge. Here is your question:\n{input}"""

expert_template = """You are a physics professor who explains physics topics to advanced audience members. You can 
                assume anyone you answer has a PhD in physics. Here is your question:\n{input} """

# ROUTE PROMPT INFORMATION
# [] NAME, DESCRIPTION, TEMPLATE

prompt_infos = [
                {
                    'name':'beginner physics',
                    'description':'Answers basic physics question',
                    'template':beginner_template,
                },

                {
                    'name':'advance physics',
                    'description': 'Answers advanced physics questions',
                    'template': expert_template,
                }
]

destination_chains = {}
for p_info in prompt_infos:
    name = p_info['name']
    prompt_template = p_info['template']
    prompt = ChatPromptTemplate.from_template(template=prompt_template)
    chain = LLMChain(llm=llm, prompt=prompt)
    destination_chains[name] = chain

# LLMCHAIN --> Template

default_prompt = ChatPromptTemplate.from_template('{input}')
default_chain = LLMChain(llm=llm, prompt=default_prompt)

destinations = [f"{p['name']}: {p['description']}" for p in prompt_infos]

destination_str = "\n".join(destinations)

router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(destinations=destination_str)
router_prompt = PromptTemplate.from_template(template=router_template,
                                             inpit_variables=['input'],
                                             output_parser=RouterOutputParser())
router_chain = LLMRouterChain.from_llm(llm, router_prompt)
chain = MultiPromptChain(router_chain=router_chain,
                         destination_chains=destination_chains,
                         default_chain=default_chain,
                         verbose=True)

print(chain.run("How do magnet work?"))



