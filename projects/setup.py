import os
from langchain.llms import HuggingFaceHub

HUGGINGFACEHUB_API_TOKEN = os.environ['HUGGINGFACEHUB_API_TOKEN'] = "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"
llm = HuggingFaceHub(huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN)


our_query = "What is currency of India?"
completion = llm(our_query)

print(completion)
