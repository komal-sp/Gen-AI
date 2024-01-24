import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.document_loaders import CSVLoader

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = ""
embeddings = OpenAIEmbeddings()

text = "This is some normal string that I want to embed as a vector"
embedded_text = embeddings.embed_query(text)

# embedded text
loader = CSVLoader("some_data/penguins.csv")
data = loader.load()

# [text.page_docs gor text in data]
embedded_doc = embeddings.embed_documents([text.page_content for text in data])





