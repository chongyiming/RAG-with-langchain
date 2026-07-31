md5_path="md5.txt"

collection_name="rag"
persist_directory="chroma_db"

chunk_size=1000
chunk_overlap=100
separators=["\n\n","\n",".","!","?",""," "]
max_split_char_number = 1000

similarity_threshold=1

embedding_model_name="qwen3-embedding:4b"
chat_model_name="qwen3.5:2b"
