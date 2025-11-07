
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


from langchain_openai import OpenAIEmbeddings
import numpy as np

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

words = ["강아지", "고양이", "자동차", "트럭", "바이크", "컴퓨터", "노트북", "핸드폰", "태블릿", "음악", "영화", "책"]
word_embeddings = embeddings.embed_documents(words)

query = "돼지"
query_embedding = embeddings.embed_query(query)

print(len(query_embedding))

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))   

print(f"'{query}'에 대한 유사도")
for word, embedding in zip(words, word_embeddings):
    similarity = cosine_similarity(query_embedding, embedding)
    print(f"{word}: {similarity:.4f}")
