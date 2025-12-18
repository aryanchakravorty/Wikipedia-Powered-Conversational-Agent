# REPLACE THIS WITH YOUR CODE
import llama_index
from llama_index.core.tools.query_engine import QueryEngineTool
from llama_index.core.tools.types import ToolMetadata
from llama_index.core.agent.react.base import ReActAgent
from llama_index.core.chat_engine.types import AgentChatResponse
from llama_index.llms.openai import OpenAI
import chainlit as cl
from chainlit.input_widget import Select
from chainlit.input_widget import TextInput
import openai 
from index_wikipages import create_index
from utils import get_apikey



index = None
agent = None

@cl.on_chat_start
async def on_chat_start():
    global index
    global agent
    # Settings
    settings = await cl.ChatSettings(
        [
            Select(
                id="MODEL", # REPLACE THIS WITH YOUR CODE
                label= "OpenAI-Model",# REPLACE THIS WITH YOUR CODE
                values=["gpt-3.5-turbo"],# REPLACE THIS WITH YOUR CODE
                initial_index=0,
            ),
            
            # REPLACE THIS WITH YOUR CODE,
            TextInput(id="WIKIPAGE_REQUEST", label="Request Wikipage", initial="AI")
        ]
    ).send()


def wikisearch_engine(index):
    query_engine =index.as_query_engine(response_mode="compact",verbose=True,similarity_top_k=10) # REPLACE THIS WITH YOUR CODE
    return query_engine


def create_react_agent(MODEL):
    query_engine_tools = [
        QueryEngineTool(
            # REPLACE THIS WITH YOUR CODE
            query_engine=wikisearch_engine(index),
            metadata=ToolMetadata(name="Wikipedia",description="Useful for performing searches on the Wikipedia knowledgebase")
        )
    ]

    openai.api_key = get_apikey()# REPLACE THIS WITH YOUR CODE
    llm =OpenAI(model=MODEL) # REPLACE THIS WITH YOUR CODE
    agent =ReActAgent.from_tools(tools=query_engine_tools, llm=llm,verbose=True) # REPLACE THIS WITH YOUR CODE
    return agent


@cl.on_settings_update
async def setup_agent(settings):
    global agent
    global index
    query = settings["WIKIPAGE_REQUEST"] # REPLACE THIS WITH YOUR CODE
    if not isinstance(query, str):
        query = str(query)
    index =create_index(query) # REPLACE THIS WITH YOUR CODE
    print("Index created for query:", query)

    print("on_settings_update", settings)
    MODEL =settings["MODEL"] # REPLACE THIS WITH YOUR CODE
    if not isinstance(MODEL, str):
        MODEL = str(MODEL)
    agent = create_react_agent(MODEL)# REPLACE THIS WITH YOUR CODE
    await cl.Message(
        author="Agent", content=f"""Wikipage(s) "{query}" successfully indexed"""
    ).send()


@cl.on_message
async def main(message: cl.Message):
    global agent
    if agent:
        print("Agent is available, processing message.")

    print("Received message:", message)
    # if not isinstance(message, str):
    #     message = str(message)
    if agent:
        print("Agent is available, processing message.")
        response = await cl.make_async(agent.chat)(message.content)# REPLACE THIS WITH YOUR CODE
        await cl.Message(author="Agent", content=response).send()
    else:
        print("Agent is not available.")