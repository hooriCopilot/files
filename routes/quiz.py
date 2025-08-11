from fastapi import APIRouter
from services.ml import predict_careers

router = APIRouter(prefix="/quiz", tags=["quiz"])

@router.post("/submit")
def submit_quiz(quiz_data: dict):
    results = predict_careers(quiz_data)
    return results