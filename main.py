from fastapi import FastAPI
from routes.quiz import router as quiz_router
from routes.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
from core.database import engine, Base 

app = FastAPI()
app.include_router(quiz_router, prefix="/api")
app.include_router(auth_router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set to ["https://yourfrontend.com"] in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)