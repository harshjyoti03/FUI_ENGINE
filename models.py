# models.py

from pydantic import BaseModel
from typing import List


class ScoreDetail(BaseModel):
    value: float
    explanation: str


class UniverseAnalysis(BaseModel):
    title: str
    themes: List[str]
    power_system: str
    political_structure: str
    tone: str

    power_inflation: ScoreDetail
    plot_armor: ScoreDetail
    ideology_conflict: ScoreDetail
    universe_stability: ScoreDetail

    overall_risk_index: float
    confidence_score: float
    executive_summary: str
    ai_deep_analysis: str
