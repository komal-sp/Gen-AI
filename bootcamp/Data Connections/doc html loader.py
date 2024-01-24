import os
from langchain.document_loaders import BSHTMLLoader

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = ""
loader = BSHTMLLoader("../moduleIO/some_data/some_website.html")
data = loader.load()
# print(data)
print(data[0].page_content)
