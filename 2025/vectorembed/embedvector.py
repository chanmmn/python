from sentence_transformers import SentenceTransformer
import numpy as np

# Initialize the model
model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_word_to_vector(word):
    # Generate embedding for the word
    embedding = model.encode(word)
    return embedding

def save_vector_to_file(word, vector, file_path):
    # Save the word and its vector to a file in a simple format
    with open(file_path, 'w') as f:
        f.write(f"Word: {word}\n")
        f.write("Vector: " + ", ".join(map(str, vector)) + "\n")

if __name__ == "__main__":
    word = "dog"
    vector = embed_word_to_vector(word)
    save_vector_to_file(word, vector, "word_vector.txt")
    print(f"Vector for '{word}' saved to 'word_vector.txt'")