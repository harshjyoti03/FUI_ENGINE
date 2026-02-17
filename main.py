# main.py
analysis_cache = {}

from fastapi import FastAPI, HTTPException
from data import ANIME_DATABASE
from models import UniverseAnalysis
from engine import UniverseEngine

app = FastAPI(
    title="Fictional Universe Intelligence Engine",
    version="0.3"
)

from ai_engine import generate_ai_analysis

analysis_cache = {}

@app.get("/analyze", response_model=UniverseAnalysis)
def analyze_universe(anime: str):
    anime_key = anime.lower()

    if anime_key not in ANIME_DATABASE:
        raise HTTPException(status_code=404, detail="Anime not found")

    # If cached, return cached
    if anime_key in analysis_cache:
        return analysis_cache[anime_key]

    anime_data = ANIME_DATABASE[anime_key]

    engine = UniverseEngine(anime_data)
    deterministic_result = engine.analyze()

    ai_analysis = generate_ai_analysis(anime_data, deterministic_result)

    final_result = UniverseAnalysis(
        title=anime_data["title"],
        themes=anime_data["themes"],
        power_system=anime_data["power_system"],
        political_structure=anime_data["political_structure"],
        tone=anime_data["tone"],
        ai_deep_analysis=ai_analysis,
        **deterministic_result
    )

    analysis_cache[anime_key] = final_result

    return final_result
