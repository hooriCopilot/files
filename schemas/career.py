from pydantic import BaseModel
from typing import List, Optional

class CareerRead(BaseModel):
    id: int
    name: str
    required_skills: List[str]
    description: Optional[str]

    class Config:
        orm_mode = True