# main.py

from fastapi import FastAPI, HTTPException
from data import ANIME_DATABASE
from models import UniverseAnalysis
from engine import UniverseEngine
from similarity_engine import SimilarityEngine

app = FastAPI(
    title="Fictional Universe Intelligence Engine",
    description="Computational Narrative Intelligence System (Local AI Mode)",
    version="0.4"
)

# ----------------------------
# Global Engines (Loaded Once)
# ----------------------------

similarity_engine = SimilarityEngine()

# Simple in-memory cache
analysis_cache = {}

# ----------------------------
# ANALYZE ENDPOINT
# ----------------------------

@app.get("/analyze", response_model=UniverseAnalysis)
def analyze_universe(anime: str):
    anime_key = anime.lower()

    if anime_key not in ANIME_DATABASE:
        raise HTTPException(status_code=404, detail="Anime not found")

    # Return cached result if exists
    if anime_key in analysis_cache:
        return analysis_cache[anime_key]

    anime_data = ANIME_DATABASE[anime_key]

    # Run deterministic + semantic engine
    engine = UniverseEngine(anime_data)
    result = engine.analyze()

    final_result = UniverseAnalysis(
        title=anime_data["title"],
        themes=anime_data["themes"],
        power_system=anime_data["power_system"],
        political_structure=anime_data["political_structure"],
        tone=anime_data["tone"],
        **result
    )

    # Cache it
    analysis_cache[anime_key] = final_result

    return final_result


# ----------------------------
# SIMILARITY ENDPOINT
# ----------------------------

@app.get("/similar")
def get_similar_universes(anime: str):
    anime_key = anime.lower()

    if anime_key not in ANIME_DATABASE:
        raise HTTPException(status_code=404, detail="Anime not found")

    similar = similarity_engine.find_similar(anime_key)

    response = []

    for key, score in similar:
        response.append({
            "title": ANIME_DATABASE[key]["title"],
            "similarity_score": score
        })

    return {
        "selected_universe": ANIME_DATABASE[anime_key]["title"],
        "most_similar_universes": response
    }


# ----------------------------
# ROOT CHECK ENDPOINT
# ----------------------------

@app.get("/")
def root():
    return {
        "message": "Fictional Universe Intelligence Engine is running.",
        "version": "0.4",
        "mode": "Local AI / Free Mode"
    }