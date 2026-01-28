import faiss
import numpy as np

# Dimension for MiniLM
DIMENSION = 384

index = faiss.IndexFlatL2(DIMENSION)
documents = []

def add_text(embedding, text):
    vector = np.array([embedding]).astype("float32")
    index.add(vector)
    documents.append(text)

def search(query_embedding, top_k=3):
    if index.ntotal == 0:
        return []

    vector = np.array([query_embedding]).astype("float32")
    distances, indices = index.search(vector, top_k)

    results = []
    for i in indices[0]:
        if i == -1:
            continue
        if i < len(documents):
            results.append(documents[i])

    return results

