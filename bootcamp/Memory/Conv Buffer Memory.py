import os
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import pickle

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = "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"
llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory, verbose=True)
conversation.predict(input="Hello nice to meet you")
conversation.predict(input="Tell me about an interesting physics fact")
# print(memory.buffer)
# print(memory.load_memory_variables({}))
# conversation.memory
pickled_str = pickle.dumps(conversation.memory)
with open('convo_memory.pkl','wb') as f:
    f.write(pickled_str)

new_memory = open('convo_memory.pkl', 'rb').read()
llm1 = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
reload_conversation = ConversationChain(llm=llm1, memory=pickle.loads(new_memory))

print(reload_conversation.memory.buffer)


