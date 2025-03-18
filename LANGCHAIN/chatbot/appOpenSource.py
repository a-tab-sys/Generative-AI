# We will use Olama.
# Olama is good because youll be able to run LLM locally
# automatically does compression????

# Install Libraries: After activating the virtual environment, you can install libraries anywhere within your project's folder, as long as your virtual environment is active.
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser #StrOutputParser is the default output parser when your LLM gives some response. we can also creae a custom output parser
from langchain_community.llms import Ollama #for 3rd party integrations
import streamlit as st

import os
from dotenv import load_dotenv

load_dotenv()

# we are going to use 3 env variables: openai api key, langchain api key and langchain tracing version 2
# langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true" 
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = "Project 1" #name it, this will show as the name when you look at tracing results. before results were showing up in the default project, now because of this they are being tracked in project 1 in langsmith

# Define prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        # system prompt and user prompt
        ("system", "You are a helpful assistant. Please respont to the user queries"),
        ("user", "Question:{questions}")
    ]
)

# defien streamlit framework
st.title('Langchain Demo with LLAMA2 API')
input_text=st.text_input("Search the topic you want")

# openAI llama2 LLM
llm=Ollama(model="llama2")
# before calling any models, we can check llama github to see what models/libraries are supported
# let say we want to use gamma model
# in order to do this, go to command prompt and write 
# ollama run gamma
# this will pull (download)the entire model
# you have to do this downloading step, if you want to use the model locally
output_parser=StrOutputParser() #gets the output
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'questions':input_text}))

# TO RUN THIS WRITE IN TERMINAL
# streamlit run appOpenSource.py


# if you wanted to ask alot of code related questions
# there is such thing as code llama which you can use directly