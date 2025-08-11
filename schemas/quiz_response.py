from pydantic import BaseModel
from typing import Dict, Any

class QuizResponseCreate(BaseModel):
    quiz_data: Dict[str, Any]

class QuizResponseRead(QuizResponseCreate):
    id: int
    user_id: int

    class Config:
        orm_mode = True