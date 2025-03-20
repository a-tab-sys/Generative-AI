from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

# creating an open ai api???

load_dotenv()  #helps me initialize my enviroment variables

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

##In order to create a fast api, we need to first create an app
##later we will keep adding routes to this app
app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

# one way to add route
add_routes(
    app,
    ChatOpenAI(),   # model we will use
    path="/openai"
)

# initialize 1 model
model=ChatOpenAI()

#call our other model ollama llama2
llm=Ollama(model="llama2")

# make 2 prompts templates
# prompt1 will interact with chat open api
# prompt2 will interact with out open source llm model

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me a poem about {topic} with 100 words")

add_routes(
   app,
   prompt1|model,
   path="/essay"
    #that means this path is responsible for interacting with the open ai api and this is denoted by /essay. the api url we will be getting will end in /essay
)

# can have many routes
add_routes(
   app,
   prompt2|llm,
   path="/poem"
)

if __name__=="__main__":
    # this application we can run in any server that we want. this is the first step towards building a production grade application
    uvicorn.run(app, host="localhost", port=8000)
    # uvicorn.run(app, host="localhost", port=8080)  # another port option



# RUN WITH
# python app.py

# whn you run this open the local host, youll get a detail not found inda message. if you want to see the entire api creted add /docs to the url. this will show  you the entire langchain server. this is called swagger ui.

# NOW WE HAVE CRATED THE API'S....WE NOW NEEED SOME WAY TO INTERACT WITH THESE APIS -> client.py