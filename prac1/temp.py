#llm = OpenAI(openai_api_key=OPENAI_API_KEY)
#Loader
#loader = PyPDFLoader("factfulness_1.pdf")
#pages = loader.load_and_split()

#로컬에서 돌리기, 도커에서 돌리기 등 방법은 다양 
#라마를 쓰고싶다면 바꿔주면 됨
#question = "이산화탄소 배출은 소득에 따라 몇배씩 증가하지?" 

#문서 갖고오기
#docs = retriever_from_llm.get_relevant_documents(query = question)

    # # To read file as bytes:
    # bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)

    # # To convert to a string based IO:
    # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    # # To read file as string:
    # string_data = stringio.read()
    # st.write(string_data)

    # # Can be used wherever a "file-like" object is accepted:
    # dataframe = pd.read_csv(uploaded_file)
    # st.write(dataframe)

# chat_model = ChatOpenAI()
# content = st.text_input("진단사항에 대해 말씀해주세요.")
# result = chat_model.predict(content+"의 종류 한가지만 말해줘.")
# st.write(result)