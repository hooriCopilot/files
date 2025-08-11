from sqlalchemy import Column, Integer, String, JSON
from core.database import Base

class Career(Base):
    __tablename__ = "careers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    required_skills = Column(JSON, nullable=False)  # List of skills
    description = Column(String(255), nullable=True)