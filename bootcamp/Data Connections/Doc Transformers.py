import os
from langchain.text_splitter import CharacterTextSplitter

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = "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"

with open('some_data/FDR_State_of_Union_1944.txt') as file:
    speech_text = file.read()

text_splitter = CharacterTextSplitter(separator="\n\n", chunk_size=1000)

texts = text_splitter.create_documents([speech_text])
# print(texts[0].page_content)

# speech text
# based on token count
# pip install tiktoken
texts = text_splitter.split_text(speech_text)
print(texts)



