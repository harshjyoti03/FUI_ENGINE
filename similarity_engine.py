# similarity_engine.py

import faiss
import numpy as np
from embedding_engine import embed_text
from data import ANIME_DATABASE


class SimilarityEngine:
    def __init__(self):
        self.keys = []
        self.index = None
        self.dimension = None
        self._build_index()

    def _build_index(self):
        embeddings = []

        for key, data in ANIME_DATABASE.items():
            text_blob = (
                f"{data['title']} "
                f"{' '.join(data['themes'])} "
                f"{data['power_system']} "
                f"{data['political_structure']} "
                f"{data['tone']}"
            )

            vector = embed_text(text_blob)
            embeddings.append(vector)
            self.keys.append(key)

        embeddings = np.array(embeddings).astype("float32")

        self.dimension = embeddings.shape[1]

        # Create FAISS index
        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(embeddings)

    def find_similar(self, anime_key: str, top_k=3):
        if anime_key not in self.keys:
            return []

        target_index = self.keys.index(anime_key)

        # Get target vector
        target_vector = self.index.reconstruct(target_index).reshape(1, -1)

        # Search
        distances, indices = self.index.search(target_vector, top_k + 1)

        results = []

        for idx, dist in zip(indices[0], distances[0]):
            key = self.keys[int(idx)]

            if key == anime_key:
                continue

            # IMPORTANT: Convert to native float
            similarity_score = float(100.0 - float(dist))

            # Clamp to avoid weird negatives
            similarity_score = round(max(similarity_score, 0.0), 2)

            results.append((key, similarity_score))

        return results[:top_k]
