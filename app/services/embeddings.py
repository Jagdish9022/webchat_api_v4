from sentence_transformers import SentenceTransformer
import logging

# Initialize the embedding model
try:
    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
    logging.info("Embedding model loaded successfully")
except Exception as e:
    logging.error(f"Failed to load embedding model: {e}")
    raise

def get_embeddings(texts: list[str]) -> list[list[float]]:
    """Generate embeddings for a list of texts."""
    try:
        if not texts:
            return []
        embeddings = embedding_model.encode(texts, show_progress_bar=True)
        return embeddings.tolist()
    except Exception as e:
        logging.error(f"Failed to generate embeddings: {e}")
        raise

def get_question_embedding(question: str) -> list[float]:
    """Generate embedding for a single question."""
    try:
        embedding = embedding_model.encode([question])
        return embedding[0].tolist()
    except Exception as e:
        logging.error(f"Failed to generate question embedding: {e}")
        raise