from pydantic import BaseModel
from typing import Dict, List, Any

class PredictionRead(BaseModel):
    id: int
    user_id: int
    quiz_response_id: int
    recommended_roles: List[str]
    confidence_scores: Dict[str, float]
    model_used: str

    class Config:
        orm_mode = True