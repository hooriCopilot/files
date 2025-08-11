from pydantic import BaseModel
from typing import List, Optional

class SkillGapRead(BaseModel):
    id: int
    user_id: int
    predicted_role: str
    missing_skills: List[str]
    suggested_resources: Optional[List[str]]

    class Config:
        orm_mode = True