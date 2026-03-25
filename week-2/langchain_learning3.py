""""
I am feeling sad - [0.2, -0.8, 0.1, 0.5, ...]
I was feeling really down - [0.2, -0.7, 0.1, 0.4, ...]
I love pizza - [0.9, 0.3, 0.7, -0.2, ...]

Text that mean similar things get similar numbers.
Text that mean different things get different numbers.

GPS Corrdinates for meaning : 

Cardiff castle : [51.48, 3.18]
Bute park : [51.48, 3.18]
Tokyo Tower : [35.65, 139.75]


In embeddings space :

HAppy and joyful are right next to each other.
HAppy and Sad are far away from each other.
Dog and pupppy are right next to each other.
Dog and Quantom Physics are far away from each other.


Documents : 
Dragond love treasuer -> [0.3, 0.7, -0.1, 0.4] -> Storing the vectors into the vector database.
Knights ride horses -> [0.5, 0.2, 0.6, 0.3] -> Storing the vectors into the vector database.

search query: fire breating creatures and gold -> [0.3, 0.6, -0.1, 0.4, ...]

Similarity search :

1) Cosine similarity :
it meansure the angle between the two vectors / two arrow.

same direction - cosine similarity is 1 (similar)
right angle - cosine similarity is 0 (unrelated)
opposite direction - cosine similarity is -1 (opposite)

2) Euclidean distance :
measure the straight line distance between the two vectors / two points on the map.

same point - euclidean distance is 0 (similar)
far apart - euclidean distance is large (unrelated)


3) Dot product :
a math shortcut that measure both directions and magnitude of the topic.


cosine - close to 1 (similar) - most of the search tasl
euclidean - close to 0 (similar) - clustering or grouping
dot prodcut - large number (similar) - ranking or sorting


1 -load documents
2- split documents into chunks
3- create embeddings for the chunks
4 - store the embeddings in the vector database
5 - user ask a question
6 - embedding of the user question
7 - find the most similar chunk based on the cosine similarity of the question and all chunks.
8 - send  the found chunks + question to the LLM
9 - AI answer the question based on the found chunks.
"""



# pip install sentence-transformers langchain-text-splitters pypdf langchain_huggingface chromadb

# from sentence_transformers import SentenceTransformer
# from numpy import dot
# from numpy.linalg import norm

# model = SentenceTransformer("all-MiniLM-L6-v2")

# vector = model.encode("Cats are pretty good at running fast for long distances.")
# print(vector)
# query_vector = model.encode("Cats are pretty good at catching mice.")
# print(query_vector)

# cosine_similarity = dot(vector, query_vector) / (norm(vector) * norm(query_vector))
# print(f"Cosine Similarity: {cosine_similarity}")  

# euclidean_distance = norm(vector - query_vector)
# print(f"Euclidean Distance: {euclidean_distance}")

# dot_product = dot(vector, query_vector)
# print(f"Dot Product: {dot_product}")



#for the first step copy and paste this in the terminal: 
# pip install sentence-transformers langchain-text-splitters pypdf langchain_huggingface chromadb
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os
load_dotenv()

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
# Load the document

path = r"/Users/nisruch/Downloads/working-at-the-welsh-government-your-welcome-pack.pdf" # change the path to the document you want to use
loader = PyPDFLoader(path)
docs = loader.load()   



# Split the document into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap =50, separators=["\n\n", "\n", " ", ""])
chunks = text_splitter.split_documents(docs)
print(len(chunks))

#create the embedding model
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

#create the vector store
vector_store = Chroma.from_documents(documents=chunks, embedding=embedding_model)

#create the retriever
user_question = "What is the purpose of the document?"
number_of_result = 10
similary_results = vector_store.similarity_search_with_score(query = user_question, k = number_of_result)


context_part = []
for i, (chunk, score) in enumerate(similary_results):
    context_part.append(f"Chunk {i+1} : {chunk.page_content} \n\n")

context_part = "\n".join(context_part)

prompt = f"""

Answer the user question based only on the following context, if the context does not contain the answer, say "I don't know".

context : {context_part}

User question: {user_question}


"""

llm = ChatAnthropic(model="claude-opus-4-6", temperature=0.0)
response = llm.invoke(prompt)
print(response.content)