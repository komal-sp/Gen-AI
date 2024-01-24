import os
from langchain.memory import ChatMessageHistory

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = ""

history = ChatMessageHistory()
history.add_user_message("Hello nice to meet you")
history.add_ai_message("Nice to meet you!")

print(history)
