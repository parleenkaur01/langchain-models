from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2", dimensions=384)

text = "Delhi is the capital of India"

vector=embedding.embed_query(text)

print(str(vector ))