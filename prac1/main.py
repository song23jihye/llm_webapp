from langchain.document_loaders import PyPDFLoader
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.chains import RetrievalQA
import os
import pandas as pd
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import streamlit as st
from PIL import Image

image = Image.open('aidlogo.png')
st.image(image)#, caption='Sunrise by the mountains')
#button(username="AID.co.kr", floating=True, width=221)

#제목
st.title("K-health")
st.write("---")

#OPENAI_API_KEY = "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"
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

st.title('클리블랜드 심장질환 진단 - chatPDF')
st.write("---") #마크다운(제목과 구분선)

import pandas as pd
# streamlit_app.py

import supabase
from supabase import create_client, Client

# Initialize connection.
# Uses st.cache_resource to only run once.


sburl = st.secrets["https://ycajnrbygrguymswihba.supabase.co"]
sbkey = st.secrets["eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InljYWpucmJ5Z3JndXltc3dpaGJhIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTk4NTEwMjQsImV4cCI6MjAxNTQyNzAyNH0.jNCvUGRqW6BvcjFgJIYfT8jKBGpaJLSxx_ag9v6FKHs"]
supabase_client = supabase.create_client(sburl, sbkey)

@st.cache_resource
def init_connection():
    return create_client(sburl, sbkey)

supabase = init_connection()

# Supabase에서 데이터 가져오기
def fetch_data():
    query = "SELECT * FROM your_table"
    response = supabase_client.query(query)
    data = response.get('data', [])
    return data

data = fetch_data()

@st.cache_data(ttl=600)
def run_query():
    return supabase.table("aidHealthDB").select("*").execute()

st.write("supabase DB")
st.write(data)