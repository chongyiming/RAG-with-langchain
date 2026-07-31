from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.document_loaders import CSVLoader
import streamlit as st
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from knowledge_base import KnowledgeBaseService
import time
from rag import RagService
import config_data as config
st.title("AI support")
st.divider()


if "message" not in st.session_state:
    st.session_state["message"]=[{"role":"assistant","content":"How can I help?"}]

if "rag" not in st.session_state:
    st.session_state["rag"]=RagService()

for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])

prompt=st.chat_input()

if prompt:
    st.chat_message("user").write(prompt)

    st.session_state["message"].append({"role":"user","content":prompt})
    with st.spinner():
        res=st.session_state["rag"].chain.invoke(prompt)
        st.chat_message("assistant").write(res)
        st.session_state["message"].append({"role":"assistant","content":res})

      
