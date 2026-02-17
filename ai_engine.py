# ai_engine.py

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_ai_analysis(anime_data, deterministic_results):
    prompt = f"""
You are an advanced narrative systems analyst.

Analyze this fictional universe academically.
Title: {anime_data['title']}
Themes: {anime_data['themes']}
Power System: {anime_data['power_system']}
Political Structure: {anime_data['political_structure']}
Tone: {anime_data['tone']}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a computational narrative theorist."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
        )

        return response.choices[0].message.content

    except Exception as e:
        # Fallback mode
        return generate_local_analysis(anime_data, deterministic_results)


def generate_local_analysis(anime_data, deterministic_results):
    return (
        f"[LOCAL ANALYSIS MODE]\n\n"
        f"The universe of {anime_data['title']} operates under a "
        f"{anime_data['power_system']} structure, creating a power escalation index "
        f"of {deterministic_results['power_inflation']['value']}. "
        f"Ideological tensions centered around {', '.join(anime_data['themes'])} "
        f"generate systemic instability. "
        f"Projected sustainability score: "
        f"{deterministic_results['universe_stability']['value']}."
    )
