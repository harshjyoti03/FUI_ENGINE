# collapse_engine.py

import random
from data import ANIME_DATABASE
from engine import UniverseEngine
from ideology_engine import IdeologyEngine
from psychology_engine import PsychologyEngine


class CollapseEngine:

    def __init__(self):
        self.ideology_engine = IdeologyEngine()
        self.psychology_engine = PsychologyEngine()

    def simulate(self, anime_key: str, runs=500):
        if anime_key not in ANIME_DATABASE:
            return None

        anime_data = ANIME_DATABASE[anime_key]

        universe_engine = UniverseEngine(anime_data)
        metrics = universe_engine.analyze()

        ideology = self.ideology_engine.analyze_ideology(anime_key)
        psychology = self.psychology_engine.analyze_psychology(anime_key)

        power = metrics["power_inflation"]["value"]
        polarization = ideology["polarization_score"]
        extremism = psychology["extremism_potential"]
        trauma = psychology["trauma_index"]

        collapse_events = 0
        authoritarian_events = 0
        civil_war_events = 0

        for _ in range(runs):

            instability = (
                power * 0.25 +
                polarization * 0.25 +
                extremism * 0.25 +
                trauma * 0.25
            )

            # Add randomness (stochastic drift)
            instability += random.uniform(-10, 10)

            if instability > 70:
                collapse_events += 1

            if extremism + random.uniform(-10, 10) > 65:
                authoritarian_events += 1

            if polarization + trauma + random.uniform(-20, 20) > 100:
                civil_war_events += 1

        collapse_probability = round((collapse_events / runs) * 100, 2)
        authoritarian_risk = round((authoritarian_events / runs) * 100, 2)
        civil_war_risk = round((civil_war_events / runs) * 100, 2)

        # Estimate system half-life (rough heuristic)
        stability_score = metrics["universe_stability"]["value"]
        half_life = max(5, int(50 - stability_score * 0.4))

        return {
            "collapse_probability": collapse_probability,
            "authoritarian_takeover_risk": authoritarian_risk,
            "civil_war_risk": civil_war_risk,
            "system_half_life_years": half_life,
            "simulation_runs": runs
        }
