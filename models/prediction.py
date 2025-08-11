from sqlalchemy import Column, Integer, DateTime, JSON, ForeignKey, String
from sqlalchemy.sql import func
from core.database import Base

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    quiz_response_id = Column(Integer, ForeignKey("quiz_responses.id", ondelete="CASCADE"), nullable=False)
    recommended_roles = Column(JSON, nullable=False)
    confidence_scores = Column(JSON, nullable=False)
    model_used = Column(String(100))
    predicted_on = Column(DateTime, server_default=func.now())