from sklearn.metrics.pairwise import cosine_similarity

from sentence_transformers import (
    SentenceTransformer
)

model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

def calculate_similarity(query, answer):

    embeddings = model.encode(
        [query, answer]
    )

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return similarity