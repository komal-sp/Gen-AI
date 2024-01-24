# install Libraries
# pip install openai
# pip install langchain
# pip install unstructured
# pip install tiktoken
# pip install pinecone-client
# pip install pypdf
# pip install sentence-transformers

# Import Dependencies
import openai
import os
import pinecone
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone
from langchain_community.llms import OpenAI
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = ""
HUGGINGFACEHUB_API = os.environ['HUGGINGFACEHUB_API_TOKEN'] = ""


# Load Documents :loads pdf files available in directory with pypdf
# Function to read documents


def load_docs(directory):
    loader = PyPDFDirectoryLoader(directory)
    documents = loader.load()
    return documents


# passing the directory to the load_docs function
input_directory = "Docs/"
output_docs = load_docs(input_directory)


# print(len(output_docs))
# print(output_docs)

# Transformer Documents: split documents into smaller chunks
# this function will split the documents into chunks

def split_docs(documents, chunk_size=1000, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs =
