import os
from langchain.prompts import ChatPromptTemplate,  HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import WikipediaLoader

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = "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"


def answer_question_about(person_name, question):
    #   Use the Wikipedia Document Loader to help answer questions about someone, insert it as additional helpful context.
    # LOAD DOCUMENT
    loder = WikipediaLoader(query=person_name, load_max_docs=1)
    context_text = loder.load()[0].page_content

    # CONNECT OPENAI MODEL
    model = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

    # PROMPT - FORMAT QUESTION
    template = "Answer this question:\n{question}\n, Here is some extra context:\n{document}"
    human_prompt = HumanMessagePromptTemplate.from_template(template)

    # CHAT PROMPT- GET RESULT CONTENT
    chat_prompt = ChatPromptTemplate.from_messages([human_prompt])
    result = model(chat_prompt.format_prompt(question=question,
                                             document=context_text).to_messages())

    print(result.content)


answer_question_about("Claude Shannon", "When was he born?")
"""
Document Loading Exercise
Answering a Single Question
Using the Wikipedia Document Loader Integration,can you make a function that accepts a famous historical figure name and
a question about them, and then uses a ChatModel to answer questions with the additional context? Notice how in our 
example, the query doesn't mention the famous person. Keep in mind there are many potential ways to solve this problem!



"""
