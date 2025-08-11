from sqlalchemy.orm import Session
from models.quiz_response import QuizResponse

def create_quiz_response(db: Session, user_id: int, quiz_data: dict):
    quiz_response = QuizResponse(user_id=user_id, quiz_data=quiz_data)
    db.add(quiz_response)
    db.commit()
    db.refresh(quiz_response)
    return quiz_response