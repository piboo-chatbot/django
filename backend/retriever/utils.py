from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.retrievers.ensemble import EnsembleRetriever

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.retrievers.ensemble import EnsembleRetriever
import numpy as np

class NormalizedHFEmbeddings(HuggingFaceEmbeddings):
    def embed_documents(self, texts):
        embeddings = super().embed_documents(texts)
        return [emb / np.linalg.norm(emb) for emb in embeddings]  # L2 정규화

    def embed_query(self, text):
        embedding = super().embed_query(text)
        return embedding / np.linalg.norm(embedding)  # 쿼리도 정규화
    
def set_embedding_model():
    return NormalizedHFEmbeddings( 
        model_name="snunlp/KR-SBERT-V40K-klueNLI-augSTS"
    )

def load_chromadbs(embedding_model):
    chroma1 = Chroma(
        persist_directory="./vectordb/cosmetic_chromadb",
        embedding_function=embedding_model,
        collection_metadata={"hnsw:space": "cosine"}  # 코사인 유사도 사용
    )
    chroma2 = Chroma(
        persist_directory="./vectordb/ingredient_chromadb",
        embedding_function=embedding_model,
        collection_metadata={"hnsw:space": "cosine"}  # 코사인 유사도 사용
    )

    print("cosmetic_chromadb 문서 수:", chroma1._collection.count())
    print("ingredient_chromadb 문서 수:", chroma2._collection.count())

    return chroma1, chroma2

def create_ensemble_retriever(chroma1, chroma2):
    retriever1 = chroma1.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )
    retriever2 = chroma2.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )
    ensemble_retriever = EnsembleRetriever(retrievers=[retriever1, retriever2])
    return ensemble_retriever

def search_documents(ensemble_retriever, query: str, k: int = 3):
    docs = ensemble_retriever.invoke(query)
    print("검색 결과 개수:", len(docs))
    for i, doc in enumerate(docs):
        print(f"문서 {i}:", doc)
    return [doc.page_content for doc in docs[:k]] 