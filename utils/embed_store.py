# utils/embed_store.py
import pickle
import numpy as np #type:ignore
import faiss #type:ignore
from sentence_transformers import SentenceTransformer #type:ignore

EMBED_MODEL = SentenceTransformer("all-MiniLM-L6-v2")
VECTOR_PATH = "vector.index"
DOCS_PATH = "docs.pkl"

def build_index(documents):
    embeddings = EMBED_MODEL.encode(documents, convert_to_numpy=True)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    faiss.write_index(index, VECTOR_PATH)

    with open(DOCS_PATH, "wb") as f:
        pickle.dump(documents, f)

def load_index():
    index = faiss.read_index(VECTOR_PATH)
    with open(DOCS_PATH, "rb") as f:
        docs = pickle.load(f)
    return index, docs

def search(query, k=3):
    index, docs = load_index()
    q_emb = EMBED_MODEL.encode([query], convert_to_numpy=True)
    distances, indices = index.search(q_emb, k)
    return [docs[i] for i in indices[0]]
