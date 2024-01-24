import os
from langchain.document_loaders import PyPDFLoader

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = ""
loader = PyPDFLoader("../moduleIO/some_data/SomeReport.pdf")
data = loader.load()
# print(data)
# print(data[0].page_content)
print(data[0].page_content.replace('\n', ' '))
