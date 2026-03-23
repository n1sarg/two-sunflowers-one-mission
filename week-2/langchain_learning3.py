from sentence_transformers import SentenceTransformer
from numpy import dot
from numpy.linalg import norm

#pip install sentence-transformers

model = SentenceTransformer("all-MiniLM-L6-v2")

vector = model.encode("Dragons love treasure")

query_vector = model.encode("fire-breathing creatures and gold")

similarity = dot(vector, query_vector) / (norm(vector) * norm(query_vector))
print(f"Similarity: {similarity}")  