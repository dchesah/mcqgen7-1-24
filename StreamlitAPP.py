import os
import json
import pandas as pd
import traceback
#from langchain.llms import OpenAI
from langchain_community.llms import openai
from langchain_openai import ChatOpenAI
from langchain_core.chains import LLMChain
#from langchain.prompts import PromptTemplate
from langchain_community.prompts import PromptTemplate
#from langchain.chains import LLMChain
from langchain.chains import SequentialChain
#from langchain.callbacks import get_openai_callback
from langchain_community.callbacks import get_openai_callback

#from lanchain_core.chains import LLMChain
import PyPDF2
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
import streamlit as st
from src.mcqgenerator.logger import logging
from src.mcqgenerator.MCQGENERATOR import generate_evaluate_chain
import altair



