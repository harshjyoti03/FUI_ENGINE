# similarity_engine.py

from embedding_engine import embed_text, cosine_similarity
from data import ANIME_DATABASE

class SimilarityEngine:

    def __init__(self):
        self.embeddings = {}
        self._precompute_embeddings()

    def _precompute_embeddings(self):
        for key, data in ANIME_DATABASE.items():
            text_blob = (
                f"{data['title']} "
                f"{' '.join(data['themes'])} "
                f"{data['power_system']} "
                f"{data['political_structure']} "
                f"{data['tone']}"
            )
            self.embeddings[key] = embed_text(text_blob)

    def find_similar(self, anime_key: str, top_k=3):
        if anime_key not in self.embeddings:
            return []

        target_embedding = self.embeddings[anime_key]

        similarities = []

        for key, embedding in self.embeddings.items():
            if key == anime_key:
                continue

            score = cosine_similarity(target_embedding, embedding)
            similarities.append((key, round(score * 100, 2)))

        similarities.sort(key=lambda x: x[1], reverse=True)

        return similarities[:top_k]