# ideology_engine.py

import networkx as nx
from data import ANIME_DATABASE


IDEOLOGY_GROUPS = {
    "Freedom": "liberation",
    "Oppression": "authoritarian",
    "Control": "authoritarian",
    "Justice": "moral_order",
    "Corruption": "moral_decay",
    "War": "conflict",
    "Peace": "stability",
    "Fate": "determinism",
    "Free Will": "agency",
    "Revolution": "liberation",
    "Cycle of Hatred": "conflict",
}


class IdeologyEngine:

    def analyze_ideology(self, anime_key: str):
        if anime_key not in ANIME_DATABASE:
            return None

        themes = ANIME_DATABASE[anime_key]["themes"]

        G = nx.Graph()

        # Add nodes
        for theme in themes:
            G.add_node(theme)

        # Add edges based on ideological group difference
        for i in range(len(themes)):
            for j in range(i + 1, len(themes)):
                t1 = themes[i]
                t2 = themes[j]

                group1 = IDEOLOGY_GROUPS.get(t1, "neutral")
                group2 = IDEOLOGY_GROUPS.get(t2, "neutral")

                if group1 != group2:
                    G.add_edge(t1, t2, weight=1.0)

        centrality = nx.degree_centrality(G)

        dominant = max(centrality, key=centrality.get) if centrality else None

        polarization = round(len(G.edges()) * 10.0, 2)
        polarization = min(polarization, 100.0)

        return {
            "themes": themes,
            "dominant_ideology": dominant,
            "polarization_score": polarization,
            "centrality_scores": {
                theme: round(score, 3)
                for theme, score in centrality.items()
            }
        }
