import json
import requests
import os
from llama_index.llms.solar import Solar
from llama_index.core.llms import ChatMessage
from openai import OpenAI
from dotenv import find_dotenv, load_dotenv
from langchain.llms import OpenAI
import key_param
load_dotenv(find_dotenv())
llm = OpenAI(openai_api_key=key_param.openai_api_key, temperature=0)
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def get_query_from_user(prompt): 
  template = """
  act as a ground control station operator for a drone. You are responsible for monitoring the drone's flight path and ensuring that it stays within the designated area. The drone is currently flying over a forested area, and you notice that it is veering off course. Write a message to the drone pilot instructing them to correct their course and return to the designated flight path.
          """
  prompt = PromptTemplate(template=template)
  llm_chain = LLMChain(prompt=prompt, llm=llm)
  response = llm_chain.run({"prompt": prompt})
  print(response)
  return response



