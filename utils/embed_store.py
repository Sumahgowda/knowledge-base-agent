import pickle
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

EMBED_MODEL = SentenceTransformer("all-MiniLM-L6-v2")
VECTOR_PATH = "vector.index"
DOCS_PATH = "docs.pkl"
EMB_PATH = "embeddings.npy"

def build_index(documents):
    embeddings = EMBED_MODEL.encode(documents, convert_to_numpy=True)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    faiss.write_index(index, VECTOR_PATH)
    np.save(EMB_PATH, embeddings)

    with open(DOCS_PATH, "wb") as f:
        pickle.dump(documents, f)

def load_index():
    index = faiss.read_index(VECTOR_PATH)
    embeddings = np.load(EMB_PATH)
    with open(DOCS_PATH, "rb") as f:
        docs = pickle.load(f)
    return index, embeddings, docs

def search(query, k=3):
    index, embeddings, docs = load_index()
    q_emb = EMBED_MODEL.encode([query], convert_to_numpy=True)
    distances, indices = index.search(q_emb, k)
    return [docs[i] for i in indices[0]]
