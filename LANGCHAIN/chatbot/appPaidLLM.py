# we are trying to create a chat bot in 2 ways
# 1. Using Paid LLM's {Open AI API or Cloudy API}
# 2. Open Source LLM

# calling API is very easy, the major thing is that since we have so many modules, we are going to use langchain which has many modules. We will use these modules to make different calls.

###Open AI API

# Install Libraries: After activating the virtual environment, you can install libraries anywhere within your project's folder, as long as your virtual environment is active.
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser #StrOutputParser is the default output parser when your LLM gives some response. we can also creae a custom output parser

import streamlit as st
import os
from dotenv import load_dotenv

# we are going to use 3 env variables: openai api key, langchain api key and langchain tracing version 2
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
# langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true" 
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# Define prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        # system prompt and user prompt
        ("system", "You are a helpful assistant. Please respont to the user queries"),
        ("user", "Question:{questions}")
    ]
)

# define streamlit framework
st.title('Langchain Demo with OPENAI API')
input_text=st.text_input("Search the topic you want")

# openAI LLM
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser() #gets the output
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))

# SO YOU MADE A REQUIREMENTS TEXT FILE - this will install all your requirements
# pip install -r requirements.txt in terminal

# TO RUN THIS WRITE IN TERMINAL
# streamlit run appPaidLLM.py