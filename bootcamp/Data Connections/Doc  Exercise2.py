# Build a sample vectorDB
import os
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = ""


def us_constitution_helper(question):
    """Takes in a question about the US Constitution and returns the most relevant part of the constitution.
     Notice it may not directly answer the actual question!
     Follow the steps below to fill out this function: """
    # PART ONE:
    # LOAD \"some_data/US_Constitution in a Document object
    loder = TextLoader("some_data/US_Constitution.txt")
    documents = loder.load()

    # PART TWO:
    # Split the document into chunks (you choose how and what size)
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=500)
    docs = text_splitter.split_documents(documents)

    # PART THREE
    # EMBED THE Documents (now in chunks) to a persisted ChromaDB
    embedding_function = OpenAIEmbeddings()
    db = Chroma.from_documents(docs, embedding_function, persist_directory="./solution")
    db.persist()

    # PART FOUR
    # Use ChatOpenAI and ContextualCompressionRetriever to return the most part of the documents.
    llm = ChatOpenAI(temperature=0)
    compressor = LLMChainExtractor.from_llm(llm)
    compressor_retriever = ContextualCompressionRetriever(base_compressor=compressor,
                                                          base_retriever=db.as_retriever())
    compressor_docs = compressor_retriever.get_relevant_documents(question)

    print(compressor_docs[0].page_content)


us_constitution_helper("What is the 12th Amendment?")


"""
Ask a Legal Research Assistant Bot about the US Constitution
Let's revisit our first exercise and add offline capability using ChromaDB. Your function should do the following:
    * Read the US_Constitution.txt file inside the some_data folder
    * Split this into chunks (you choose the size)
    * Write this to a ChromaDB Vector Store
    * Use Context Compression to return the relevant portion of the document to the question
"""
