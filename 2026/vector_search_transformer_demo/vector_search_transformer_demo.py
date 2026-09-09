"""Demo: vector search over 10 sentences using transformer embeddings + cosine similarity."""

import numpy as np
from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"

SENTENCES = [
    "The cat sat quietly on the warm windowsill.",
    "Dogs love to play fetch in the park.",
    "Python is a popular programming language for data science.",
    "The stock market fell sharply after the interest rate hike.",
    "She brewed a fresh pot of coffee this morning.",
    "Machine learning models can find patterns in large datasets.",
    "The mountain trail offered a stunning view of the valley.",
    "He fixed the leaking faucet in the kitchen sink.",
    "Vector databases enable fast similarity search over embeddings.",
    "The chef added basil and garlic to the tomato sauce.",
]


def build_index(sentences: list[str]) -> tuple[SentenceTransformer, np.ndarray]:
    model = SentenceTransformer(MODEL_NAME)
    vectors = model.encode(sentences, normalize_embeddings=True)
    return model, vectors


def search(query: str, model: SentenceTransformer, vectors: np.ndarray, top_k: int = 3):
    query_vec = model.encode([query], normalize_embeddings=True)
    # Vectors are normalized, so the dot product equals cosine similarity.
    scores = query_vec @ vectors.T
    scores = scores[0]
    ranked = np.argsort(scores)[::-1][:top_k]
    return [(SENTENCES[i], scores[i]) for i in ranked]


def main() -> None:
    model, vectors = build_index(SENTENCES)

    queries = [
        "What programming language is good for AI?",
        "Tell me about hiking in nature.",
        "How does searching by embeddings work?",
    ]

    for query in queries:
        print(f"\nQuery: {query}")
        for sentence, score in search(query, model, vectors):
            print(f"  {score:.3f}  {sentence}")


if __name__ == "__main__":
    main()
