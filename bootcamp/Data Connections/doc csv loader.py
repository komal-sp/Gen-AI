import os
from langchain.document_loaders import CSVLoader

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = ""
loader = CSVLoader("../moduleIO/some_data/penguins.csv")
data = loader.load()
# print(type(data))
# print(data[0])
print(data[2].page_content)


