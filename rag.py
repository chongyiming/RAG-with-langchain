from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from vector_stores import VectorStoreService
from langchain_ollama import OllamaLLM, OllamaEmbeddings,ChatOllama
import config_data as config
from langchain_core.prompts import ChatPromptTemplate
class RagService(object):
    def __init__(self):
        self.vector_service=VectorStoreService(OllamaEmbeddings(model="qwen3-embedding:4b"))
        self.prompt_template=ChatPromptTemplate.from_messages(
            [
                ("system","Based on material given,""answer user question. Material:{context}"),
                ("user","please answer user input:{input}")
            ]
        )
        self.chat_model=ChatOllama(model=config.chat_model_name)
        self.chain=self.__get_chain()

    def __get_chain(self):
        retriever=self.vector_service.get_retriever()

        
        def format_func(docs:list[Document]):
            if not docs:
                return "no material"
            formatted_str="["
            for doc in docs:
                formatted_str+=f"page_content:{doc.page_content},metadatas:{doc.metadata}"
            formatted_str+="]"
            return formatted_str
        def print_prompt(prompt):
            print("="*20)
            print(prompt.to_string())
            return prompt
        chain=(
            {
                "input":RunnablePassthrough(),"context": retriever | format_func
            } | self.prompt_template | self.chat_model | StrOutputParser()
        )
   

        return chain
