User can upload custom data for LLM to refer



User can chat with LLM with custom knowledge base




Overview

Users can upload their own documents and allow the LLM to use this custom knowledge when answering questions.
The system uses ChromaDB to store document embeddings and MD5 hashing to prevent duplicate uploads.

1. Upload Custom Data
   
Users upload documents that they want the LLM to refer to.
The system will:
-Generate an MD5 hash for the uploaded file.
-Check if the hash already exists in md5.txt.

Duplicated record exists
<img width="1915" height="691" alt="image" src="https://github.com/user-attachments/assets/97719e77-fba8-4d78-996e-51ba08511b2d" />

No duplicated record found
<img width="506" height="597" alt="image" src="https://github.com/user-attachments/assets/2a694339-b5f8-4104-a89e-2982a3f13475" />


2. Check Existing Data
-If MD5 hash exists, then the uploaded file has already been added before. Skip processing and do not save it again into ChromaDB.

Upload File
    ↓
Generate MD5
    ↓
Check md5.txt
    ↓
Hash Found
    ↓
Already Exists
    ↓
Skip

-If MD5 hash does not exist, the uploaded file is new. We will save MD5 hash into md5.txt, convert the document into embeddings and store the embeddings in ChromaDB

Upload File
    ↓
Generate MD5
    ↓
Check md5.txt
    ↓
Hash Not Found
    ↓
Save MD5
    ↓
Store Data in ChromaDB

3. Chat with LLM Using Custom Knowledge

Users can chat with the LLM based on their uploaded documents.

Process:

User Question
      ↓
Convert Question into Vector
      ↓
Search Similar Data in ChromaDB
      ↓
Retrieve Relevant Information
      ↓
LLM uses the retrieved information from the knowledge base to generates Answer

<img width="326" height="590" alt="image" src="https://github.com/user-attachments/assets/a98d69ee-1281-4c08-b839-90c8483627fd" />
<img width="1018" height="609" alt="image" src="https://github.com/user-attachments/assets/0bc90945-cc20-4f74-bdd9-73a451586c92" />

Main Components
LLM	- Generates answers
ChromaDB - Stores and searches document vectors
Embedding Model -	Converts text into vectors
MD5	- Detects duplicate uploads
md5.txt	- Stores uploaded file hashes

Features
Upload custom knowledge for LLM reference
Avoid duplicate uploads
Store and search documents using ChromaDB
Chat with LLM using custom knowledge
