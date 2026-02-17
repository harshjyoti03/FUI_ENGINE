# engine.py

class UniverseEngine:
    def __init__(self, anime_data: dict):
        self.data = anime_data

    def analyze(self):
        power = self.calculate_power_inflation()
        plot = self.calculate_plot_armor()
        ideology = self.calculate_ideology_conflict()
        stability = self.calculate_stability(power["value"], ideology["value"])
        risk = round((power["value"] + ideology["value"]) / 2, 2)

        summary = self.generate_summary(power, ideology, stability)

        return {
            "power_inflation": power,
            "plot_armor": plot,
            "ideology_conflict": ideology,
            "universe_stability": stability,
            "overall_risk_index": risk,
            "confidence_score": 0.82,
            "executive_summary": summary
        }

    def calculate_power_inflation(self):
        power_system = self.data["power_system"]

        if power_system in ["Ki Energy", "Titan Shifting"]:
            value = 90.0
            explanation = "Extreme escalation mechanics allow exponential growth."
        elif power_system in ["Chakra-based ninjutsu", "Nen", "Alchemy"]:
            value = 70.0
            explanation = "Structured but scalable power hierarchy."
        elif power_system == "None (Realistic Combat)":
            value = 30.0
            explanation = "Minimal supernatural escalation."
        else:
            value = 55.0
            explanation = "Moderate supernatural influence."

        return {"value": value, "explanation": explanation}

    def calculate_plot_armor(self):
        tone = self.data["tone"]

        if "Dark" in tone or "Psychological" in tone:
            value = 45.0
            explanation = "Higher narrative consequences reduce survival bias."
        elif "High Power" in tone or "Epic" in tone:
            value = 85.0
            explanation = "Protagonist protection likely due to heroic scaling."
        else:
            value = 60.0
            explanation = "Moderate narrative bias present."

        return {"value": value, "explanation": explanation}

    def calculate_ideology_conflict(self):
        themes = self.data["themes"]

        conflict_triggers = ["War", "Freedom", "Oppression", "Justice", "Fate", "Control"]

        score = sum(15 for theme in themes if theme in conflict_triggers)
        score = min(score, 100.0)

        explanation = "Universe driven by strong ideological polarity." if score > 50 else "Ideological tension exists but not dominant."

        return {"value": score, "explanation": explanation}

    def calculate_stability(self, power, ideology):
        stability = 100 - ((power * 0.6) + (ideology * 0.4))
        stability = round(max(stability, 10.0), 2)

        explanation = (
            "High risk of systemic collapse due to imbalance."
            if stability < 40
            else "Relatively stable with manageable tensions."
        )

        return {"value": stability, "explanation": explanation}

    def generate_summary(self, power, ideology, stability):
        return (
            f"This universe exhibits a power escalation index of {power['value']} "
            f"and ideological conflict intensity of {ideology['value']}. "
            f"Stability analysis suggests a sustainability score of {stability['value']}. "
            f"Primary systemic risk arises from concentrated power hierarchies."
        )
