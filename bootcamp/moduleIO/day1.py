import os
import openai

os.environ['OPENAI_API_KEY'] = ""
# print(os.environ.get('OPENAI_API_KEY'))

template = 'Give me two reasons to learn OpenAI API with python?'

response = openai.ChatCompletion.create(model='text-davinci-003',
                                        prompt=template,
                                        max_tokens=300)
print(response)
