import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import TransformChain, LLMChain, SimpleSequentialChain
from langchain.prompts import ChatPromptTemplate

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = ""
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

yelp_review = open('yelp_review.txt').read()


# print(yelp_review.split('REVIEW:')[-1].lower())
# INPUT --> CUSTOM PYTHON TRANSFORMATION --> LLMChain

# yelp review


def transformer_fun(inputs: dict) -> dict:
    text = inputs['text']
    only_review_text = text.split('REViEW:')[-1]
    lower_case_text = only_review_text.lower()
    return {'output': lower_case_text}


transform_chain = TransformChain(input_variables=['text'],
                                 output_variables=['output'],
                                 transform=transformer_fun)

template = "Create a one sentence summary of this review:\n{review}"

prompt = ChatPromptTemplate.from_template(template)
summary_chain = LLMChain(llm=llm,
                         prompt=prompt,
                         output_key="review_summary")

sequential_chain = SimpleSequentialChain(chains=[transform_chain, summary_chain],
                                         verbose=True)

result = sequential_chain(yelp_review)
print(result)
