import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.chains import LLMChain, SequentialChain

OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = ""

# Reading in our example Email Text File:
spanish_email = open('spanish_customer_email.txt').read()


# print(spanish_email)

# Function to fill out:
def translate_and_summarize(email):
    """
        Translates an email written in a detected language to English and generates a summary.

        Args:
            email (str): The email to be processed and translated.\n",

        Returns:
            dict: A dictionary containing the following keys:
                - 'language': The language the email was written in.
                - 'translated_email': The translated version of the email in English.
                - 'summary': A short summary of the translated email.

        Raises:
            Exception: If any error occurs during the LLM chain execution.

        Example:
            email = "Hola, ¿cómo estás? Espero que todo vaya bien."
            result = translate_and_summarize(email)
            print(result)
            Output:
             {
                 'language': 'Spanish'
                 'translated_email': 'Hello, how are you? I hope everything is going well.
                 'summary': 'A friendly greeting and a wish for well-being.
               }
    """

    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)

    # DETECT LANGUAGE
    template1 = "Return the language this email is written in : \n{email}\nONLY return the language is was written"
    prompt1 = ChatPromptTemplate.from_template(template1)
    chain1 = LLMChain(llm=llm, prompt=prompt1, output_key="language")

    # TRANSLATE
    template2 = "Translate this email from {language} to English:\n" + email
    prompt2 = ChatPromptTemplate.from_template(template2)
    chain2 = LLMChain(llm=llm, prompt=prompt2, output_key="translated_email")

    # SUMMARY
    template3 = "Create a short summary of this email:\n{translated_email}"
    prompt3 = ChatPromptTemplate.from_template(template3)
    chain3 = LLMChain(llm=llm, prompt=prompt3, output_key="summary")

    seq_chain = SequentialChain(chains=[chain1, chain2, chain3],
                                input_variables=["email"],
                                output_variables=["language", "translated_email", "summary"],
                                verbose=True)

    return seq_chain(email)


result = translate_and_summarize(spanish_email)
print(result)
result.keys()
result['language']
result['translated_email']
result['summary']

"""
Chains Exercise
TASK:
Fill out the function below that takes in a string input Customer Support email that could be written in any language.
The function will then detect the language, translate the email, and provide a summary

Fill out the function below using a Sequential Chain, the function should do the following:

1. Detect the language the email is written in
2. Translate the email from detected language to English
3. Return a summary of the translated email

Note: The Function should return a dictionary that contains all three of these outputs!
"""
