import chromadb
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer

# Set the model you want to use
model_name = "paraphrase-MiniLM-L12-v2"

# Load embedding function
embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)

# Start ChromaDB client (can use in-memory or persistent)
client = chromadb.PersistentClient(path="/db1/")  # Or chromadb.Client() for in-memory

# Create a new collection with this model
collection = client.get_or_create_collection(
    name="paraphrase_l12_collection",
    embedding_function=embedding_fn
)

# Add some test documents
collection.add(
    documents=["ChromaDB is great for semantic search!", "Sentence transformers provide useful embeddings."],
    ids=["doc1", "doc2"]
)

# Query the collection
results = collection.query(
    query_texts=["semantic search is useful"],
    n_results=1
)

print(results)
