# pip install -r requirements.txt

# api part is created, now we need some way to interact with the apis
# we are creating a web app with a front end that will interact with our api

import requests
import streamlit as st

def get_openai_response(input_text):
    #will use request obect to create a response and call the api
    response=requests.post("http://localhost:8000/essay/invoke", json={"input": {"topic": input_text}})
    # response = requests.post("http://localhost:8080/essay/invoke", json={"input": {"topic": input_text}}) #another port option
    return response.json()['output']['content']

def get_ollama_response(input_text):
    response=requests.post("http://localhost:8000/poem/invoke", json={"input": {"topic": input_text}})
    # response = requests.post("http://localhost:8080/poem/invoke", json={"input": {"topic": input_text}})  #another port option
    return response.json()['output']

##streamlit framework

st.title('Langchain Demo With LLAMA2 API')
input_text=st.text_input("Write an essay on")
input_text1=st.text_input("Write a poem on")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))

# RUN WITH
# streamlit run client.py

# btw you need to have app.py running in one terminal and client.py running in another terminal.
# they need to be running simultaneousy
# open ai api wont work because you dont have a api key for it. 