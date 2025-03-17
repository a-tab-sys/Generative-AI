# we are trying to create a chat bot in 2 ways
# 1. Using Paid LLM's {Open AI API or Cloudy API}
# 2. Open SOurce LLM

# calling API is very easy, the major thing is that since we have so many modules, we are going to use langchain which has many modules. We will use these modules to make different calls.

# Open AI API

# Install Libraries: After activating the virtual environment, you can install libraries anywhere within your project's folder, as long as your virtual environment is active.
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser #StrOutputParser is the default output parser when your LLM gives some response. we can also creae a custom output parser

import streamlit as st
import os
from dotenv import load_dotenv

# we are going to use 3 env variables: openai api key, langchain api key and langchain tracing version 2
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACKING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("OPENAI_API_KEY")

# Define prompt template
prompt=ChatPromptTemplate.from_messages()
