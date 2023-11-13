from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.chains import RetrievalQA

load_dotenv()
#Loader
loader = PyPDFLoader("factfulness_1.pdf")
pages = loader.load_and_split()

#Split
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 300,
    chunk_overlap  = 20,
    length_function = len,
    is_separator_regex = False,
)
texts = text_splitter.split_documents(pages)

#Embedding
embeddings_model = OpenAIEmbeddings()

# load it into Chroma
db = Chroma.from_documents(texts, embeddings_model)

#Question
question = "인류가 농사를 발명한 기원전 8000년전에는 세계의 총 인구가 몇이야?"
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm,retriever=db.as_retriever())
result = qa_chain({"query": question})
print(result)