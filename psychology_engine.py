# psychology_engine.py

from data import ANIME_DATABASE
from engine import UniverseEngine
from ideology_engine import IdeologyEngine


class PsychologyEngine:

    def __init__(self):
        self.ideology_engine = IdeologyEngine()

    def analyze_psychology(self, anime_key: str):
        if anime_key not in ANIME_DATABASE:
            return None

        anime_data = ANIME_DATABASE[anime_key]

        # Use existing engines
        universe_engine = UniverseEngine(anime_data)
        universe_metrics = universe_engine.analyze()

        ideology_metrics = self.ideology_engine.analyze_ideology(anime_key)

        themes = anime_data["themes"]
        tone = anime_data["tone"]

        power_index = universe_metrics["power_inflation"]["value"]
        ideology_score = universe_metrics["ideology_conflict"]["value"]
        polarization = ideology_metrics["polarization_score"]

        # ---------------------------
        # Trauma Index
        # ---------------------------
        trauma_keywords = ["War", "Oppression", "Betrayal", "Cycle of Hatred", "Depression"]
        trauma_score = sum(15 for theme in themes if theme in trauma_keywords)
        trauma_score += polarization * 0.4
        trauma_score = min(round(trauma_score, 2), 100)

        # ---------------------------
        # Moral Rigidity
        # ---------------------------
        rigidity_keywords = ["Justice", "Control", "Fate", "God Complex"]
        rigidity_score = sum(20 for theme in themes if theme in rigidity_keywords)
        rigidity_score += ideology_score * 0.3
        rigidity_score = min(round(rigidity_score, 2), 100)

        # ---------------------------
        # Extremism Potential
        # ---------------------------
        extremism_score = round((rigidity_score * 0.6 + polarization * 0.4), 2)
        extremism_score = min(extremism_score, 100)

        # ---------------------------
        # Cognitive Flexibility
        # ---------------------------
        flexibility_score = round(100 - rigidity_score * 0.8, 2)
        flexibility_score = max(flexibility_score, 0)

        # ---------------------------
        # Archetype Classification
        # ---------------------------
        if extremism_score > 75:
            archetype = "Ideological Extremist"
        elif trauma_score > 60:
            archetype = "Trauma-Driven Hero"
        elif rigidity_score > 60:
            archetype = "Moral Absolutist"
        else:
            archetype = "Adaptive Protagonist"

        summary = (
            f"This universe produces a protagonist archetype classified as '{archetype}'. "
            f"Psychological modeling indicates trauma index of {trauma_score}, "
            f"moral rigidity of {rigidity_score}, and extremism potential of {extremism_score}. "
            f"Cognitive flexibility estimated at {flexibility_score}."
        )

        return {
            "trauma_index": trauma_score,
            "moral_rigidity": rigidity_score,
            "extremism_potential": extremism_score,
            "cognitive_flexibility": flexibility_score,
            "hero_archetype": archetype,
            "psychological_profile_summary": summary
        }
