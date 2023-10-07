# from dotenv import load_dotenv
# load_dotenv()

# from langchain.llms import OpenAI
# llm = OpenAI()
# result = llm.predict("what you gonna do?")
# print(result)


from langchain.chat_models import ChatOpenAI
import streamlit as st
chat_model = ChatOpenAI()


st.title('AI시인 방랑 키삿갓')

content = st.text_input('짓고 싶은 시의 주제를 정하세요')


if st.button('시 작성 요청하기'):
    with st.spinner('AI가 시를 만드는 중입니다..'):
        result =chat_model.predict(content+"에 대한 시를 써줘, 운율을 ")
        st.write(result)



