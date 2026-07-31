from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.document_loaders import CSVLoader
import streamlit as st
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from knowledge_base import KnowledgeBaseService
st.title("Test")
uploader_file=st.file_uploader("Upload txt file",type=['txt'], accept_multiple_files=False)

if "service" not in st.session_state:
    st.session_state["service"]=KnowledgeBaseService()

if uploader_file is not None:
    file_name=uploader_file.name
    file_type=uploader_file.type
    file_size=uploader_file.size/1024

    text=uploader_file.getvalue().decode("utf-8")
    result=st.session_state["service"].upload_by_str(text,file_name)
    st.write(result)
