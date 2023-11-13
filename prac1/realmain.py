from langchain.document_loaders import PyPDFLoader
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.chains import RetrievalQA
import os
import streamlit as st
import pandas as pd
from io import StringIO
import tempfile
#from streamlit_extras.buy_me_a_coffee import button
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

#button(username="AID.co.kr", floating=True, width=221)

#제목
st.title("K-health")
st.write("---")

#OPENAI_API_KEY = "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"
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

st.title('클리블랜드 심장질환 진단 - chatPDF')
st.write("---") #마크다운(제목과 구분선)

#파일 업로드
uploaded_file = st.file_uploader("file을 업로드해주세요.", type=["pdf"])
st.write("---")

def pdf_to_document(uploaded_file):
    temp_dir = tempfile.TemporaryDirectory()
    temp_filepath = os.path.join(temp_dir.name, uploaded_file.name) #no attribute 'getValue'
    with open(temp_filepath, "wb") as f:
        f.write(uploaded_file.read())
    loader = PyPDFLoader(temp_filepath)
    pages = loader.load_and_split()
    return pages


#업로드 되면 동작하는 코드
if uploaded_file is not None:
    pages = pdf_to_document(uploaded_file)
    #Split
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 300,
        chunk_overlap  = 20,
        length_function = len,
        is_separator_regex = False,
    )
    texts = text_splitter.split_documents(pages)

    #Embedding
    embedding_model = OpenAIEmbeddings() #성능 중요 - 정보를 가져오는 것 =>context를 생성하게 됨 -> 정보를 생성하는 건 LLM의 영역
    
    #Load it into Chroma
    db = Chroma.from_documents(texts, embedding_model) #persist_directory="/chroma" 옵션
    
    #Question
    st.header("Aidbot에게 질문해보세요.")
    
    #input
    question = st.text_input("질문을 입력하세요.")
    #질문하기 버튼
    if st.button("질문하기"):
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0) #옵션 설정 가능 -temperature를 높인 경우 있는 자료에서 뽑게 됨
        qa_chain=RetrievalQA.from_chain_type(llm, retriever=db.as_retriever())
        result = qa_chain({"query":question})
        st.write(result)

