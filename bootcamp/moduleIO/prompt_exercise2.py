from langchain.prompts import ChatPromptTemplate, PromptTemplate, SystemMessagePromptTemplate, \
    AIMessagePromptTemplate, HumanMessagePromptTemplate
from datetime import datetime
from langchain.llms import OpenAI
from langchain.output_parsers import DatetimeOutputParser
from langchain.chat_models import ChatOpenAI
import os

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = ""


class HistoryQuiz():
    def create_history_question(self, topic):
        """
        This method should output a historical question about the topic that has a date as the correct answer
        For example: On what date did World War 2 end?
        """
        # SYSTEM PROMPT
        system_template = "You write single quiz question about {topic}. you only return the quiz question"
        system_prompt = SystemMessagePromptTemplate.from_template(system_template)

        # HUMAN REQUEST FOR QUESTION
        human_template = "{question_request}"
        human_prompt = HumanMessagePromptTemplate.from_template(human_template)

        # COMPILE THIS TO ChatPromptTemplate
        chat_prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])

        # INSERT THE TOPIC
        q = "Give me a quiz question where the correct answer is a specific date."
        request = chat_prompt.format_prompt(topic=topic, question_request=q).to_messages()

        # REQUEST
        chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
        result = chat(request)

        return result.content

    def get_AI_answer(self, question):
        """
        This method should get the answer to the historical question from the method above.
        Note: This answer must be in datetime format! Use DateTimeOutputParser to confirm!
        September 2, 1945 --> datetime.datetime(1945, 9, 2, 0, 0)
        """
        # Datetime Parser
        output_parser = DatetimeOutputParser()

        # SYSTEM Template
        system_template = "You answer a quiz question with just a date."
        system_prompt = SystemMessagePromptTemplate.from_template(system_template)

        # HUMAN Template --> format_instructions
        human_template = """Answer the user's question:
        {question}
        
        {format_instructions}"""
        human_prompt = HumanMessagePromptTemplate.from_template(human_template)

        # Compile ChatTemplate
        chat_prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])

        # Insert question and get_format_instructions
        format_instructions = output_parser.get_format_instructions()
        request = chat_prompt.format_prompt(question=question, format_instructions=format_instructions).to_messages()

        # Chat Bot Result --> format datetime
        chat = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
        result = chat(request)
        correct_datetime = output_parser.parse(result.content)

        return correct_datetime

    def get_user_answer(self, question):
        """
        This method should grab a user answer and convert it to datetime. It should collect a Year, Month, and Day.
       You can just use input() for this.
        """
        print(question)
        print('\n')
        # Get the year, month, and day from the user
        year = int(input("Enter the year: "))
        month = int(input("Enter the month(1-12): "))
        day = int(input("Enter the day(1-31): "))
        # Create a datetime object
        user_datetime = datetime(year, month, day)
        return user_datetime

    def check_user_answer(self, user_answer, ai_answer):
        # Should check the user answer against the AI answer and return the difference between them

        # Calculate the difference between the dates
        difference = user_answer - ai_answer

        # Format the difference into a string
        formatted_difference = str(difference)

        # Return the string reporting the difference
        print("The difference between the dates is:", formatted_difference)


quiz_boat = HistoryQuiz()
question = quiz_boat.create_history_question(topic='Neil Armstrong set foot moon date')
print(question)
ai_answer = quiz_boat.get_AI_answer(question)
print(ai_answer)
user_answer = quiz_boat.get_user_answer(question)
print(user_answer)
quiz_boat.check_user_answer(user_answer, ai_answer)



"""
History Quiz
Our main goal is to use LangChain and Python to create a very simple class with a few methods for:
    * Writing a historical question that has a date as the correct answer
    * Getting the correct answer from LLM
    * Getting a Human user's best guess at correct answer
    * Checking/reporting the difference between the correct answer and the user answer
"""
