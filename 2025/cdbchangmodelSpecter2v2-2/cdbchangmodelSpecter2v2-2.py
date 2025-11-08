import chromadb
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np

# Set the model you want to use
# SPECTER2 needs to be loaded differently - use transformers directly
model_name = "allenai/specter2_base"
#model_name = "paraphrase-MiniLM-L12-v2"

# Create a custom embedding function for SPECTER2
class Specter2EmbeddingFunction:
    def __init__(self, model_name):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)
    
    def name(self):
        return self.model_name
    
    def _embed(self, input):
        """Helper method to generate embeddings"""
        # Tokenize the input
        inputs = self.tokenizer(input, padding=True, truncation=True, 
                               return_tensors="pt", max_length=512)
        
        # Get embeddings
        with torch.no_grad():
            outputs = self.model(**inputs)
            # Use CLS token embedding
            embeddings = outputs.last_hidden_state[:, 0, :].cpu().numpy()
        
        return embeddings.tolist()
    
    def __call__(self, input):
        """Embed documents"""
        return self._embed(input)
    
    def embed_query(self, input):
        """Embed query texts - can be a single string or list of strings"""
        # Handle if input is a string or list
        if isinstance(input, str):
            # Single query string
            return self._embed([input])
        else:
            # Multiple query strings
            return self._embed(input)

# Load embedding function
embedding_fn = Specter2EmbeddingFunction(model_name=model_name)

# Start ChromaDB client (can use in-memory or persistent)
client = chromadb.PersistentClient(path="/home/user1/vectordb/dbspecter/")  # Or chromadb.Client() for in-memory

# Create a new collection with this model
collection = client.get_or_create_collection(
    name="paraphrase_l12_collection",
    embedding_function=embedding_fn
)

# Add some test documents
collection.add(
    documents=["ChromaDB is quite great for semantic search!", "Sentence transformers provide quite useful embeddings."],
    ids=["doc1", "doc2"]
)

# Query the collection
results = collection.query(
    query_texts=["semantic search is useful"],
    n_results=1
)

print(results)
