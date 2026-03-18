from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding =OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents =[
    "Virat Kolhi is the best batsman in the world",
    "Sachin Tendulkar is the best batsman in the world",
    "M S Dhoni is the best wicket keeper in the world",
    "Rohit Sharma is the best opening batsman in the world",

]
query = 'tell me about virat kolhi '

doc_embeddings = embedding.embed_documents(documents) #Convert everything to vectors
query_embedding = embedding.embed_query(query) #Convert everything to vectors
scores =cosine_similarity([query_embedding], doc_embeddings)[0] #returns similarity scores

index,score = sorted(list(enumerate(scores)),key =lambda x:x[1])[-1]  #list(enumerate(scores)) [(0, 0.65), (1, 0.30), (2, 0.29), (3, 0.39)]
#key=lambda x: x[1] #[(2, 0.29), (1, 0.30), (3, 0.39), (0, 0.65)]
 
print("query: ",query)
print(documents[index])
print("similarity score: ",score)   