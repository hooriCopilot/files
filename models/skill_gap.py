from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from core.database import Base

class SkillGap(Base):
    __tablename__ = "skill_gaps"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    predicted_role = Column(String(255), nullable=False)
    missing_skills = Column(JSON, nullable=False)
    suggested_resources = Column(JSON, nullable=True)