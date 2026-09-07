"""Demo: vector search over 10 sentences using TF-IDF embeddings + cosine similarity."""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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


def build_index(sentences: list[str]) -> tuple[TfidfVectorizer, np.ndarray]:
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(sentences).toarray()
    return vectorizer, vectors


def search(query: str, vectorizer: TfidfVectorizer, vectors: np.ndarray, top_k: int = 3):
    query_vec = vectorizer.transform([query]).toarray()
    scores = cosine_similarity(query_vec, vectors)[0]
    ranked = np.argsort(scores)[::-1][:top_k]
    return [(SENTENCES[i], scores[i]) for i in ranked]


def main() -> None:
    vectorizer, vectors = build_index(SENTENCES)

    queries = [
        "What programming language is good for AI?",
        "Tell me about hiking in nature.",
        "How does searching by embeddings work?",
    ]

    for query in queries:
        print(f"\nQuery: {query}")
        for sentence, score in search(query, vectorizer, vectors):
            print(f"  {score:.3f}  {sentence}")


if __name__ == "__main__":
    main()
