from sqlalchemy.orm import Session
from models.prediction import Prediction
from models.skill_gap import SkillGap
from services.ml import predict_career, analyze_skill_gaps

def predict_careers(db: Session, user_id: int, quiz_response_id: int, quiz_data: dict):
    recommended_roles, confidence_scores, model_used = predict_career(quiz_data)
    prediction = Prediction(
        user_id=user_id,
        quiz_response_id=quiz_response_id,
        recommended_roles=recommended_roles,
        confidence_scores=confidence_scores,
        model_used=model_used
    )
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    return prediction

def create_skill_gaps(db: Session, user_id: int, recommended_roles: list, quiz_data: dict):
    skill_gaps = []
    for role in recommended_roles:
        missing_skills, suggested_resources = analyze_skill_gaps(quiz_data, role)
        gap = SkillGap(
            user_id=user_id,
            predicted_role=role,
            missing_skills=missing_skills,
            suggested_resources=suggested_resources
        )
        db.add(gap)
        skill_gaps.append(gap)
    db.commit()
    return skill_gaps