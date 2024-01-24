import os
import streamlit as st
from streamlit_chat import message
from langchain_community.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import (ConversationBufferMemory,
                                                  ConversationSummaryMemory,
                                                  ConversationBufferWindowMemory

                                                  )

# OPENAI_API_KEY = os.environ['OPENAI_API_KEY'] = "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"
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = None
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
if 'API_Key' not in st.session_state:
    st.session_state['API_Key'] = ""

# Setting page title and header
st.set_page_config(page_title="Chat GPT Clone", page_icon=":robot_face:")
st.markdown("<h1 style='text-align: center;'>How can I assist you? </h1>", unsafe_allow_html=True)

st.sidebar.title("😎")
st.session_state['API_Key'] = st.sidebar.text_input("What's your API key?", type="password")
summarise_button = st.sidebar.button("Summarise the conversation", key="summarise")
if summarise_button:
    # summarise_placeholder = st.sidebar.write("Nice chatting with you my friend ❤️:\n\n" + "Hello Friend!")
    summarise_placeholder = st.sidebar.write(
        "Nice chatting with you my friend ❤️:\n\n" + st.session_state['conversation'].memory.buffer)
    # summarise_placeholder.write("Nice chatting with you my friend ❤️:\n\n"+st.session_state['conversation'].memory.buffer)


def get_response(userinput, apikey):
    if st.session_state['conversation'] is None:
        llm = OpenAI(
            temperature=0,
            openai_api_key=apikey,
            model_name='gpt-3.5-turbo-instruct'
            # 'text-davinci-003' model is depreciated now, so we are using the openai's recommended model
        )
        # conversation=
        st.session_state['conversation'] = ConversationChain(
            llm=llm,
            verbose=True,
            # memory=ConversationBufferMemory()
            memory=ConversationSummaryMemory(llm=llm)
        )

    # conversation("Good Morning A!")
    # conversation("My name is Komal!")
    # print(conversation.memory.buffer)
    # response = conversation.predict(input="What is my name?")
    response = st.session_state['conversation'].predict(input=userinput)
    print(st.session_state['conversation'].memory.buffer)
    return response


response_container = st.container()
# Here we will have a container for user input text box
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_area("Your question goes here:", key='input', height=100)
        submit_button = st.form_submit_button(label='Send')
        if submit_button:
            st.session_state['messages'].append(user_input)
            # answer = get_response(user_input)
            model_response = get_response(user_input, st.session_state['API_Key'])
            st.session_state['messages'].append(model_response)
            # st.write(st.session_state['messages'])
            # with response_container:
            #     # st.write(answer)
            #     st.write(model_response)

            with response_container:
                for i in range(len(st.session_state['messages'])):
                    if (i % 2) == 0:
                        message(st.session_state['messages'][i], is_user=True, key=str(i) + '_user')
                    else:
                        message(st.session_state['messages'][i], key=str(i) + '_AI')
