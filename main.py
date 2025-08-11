from fastapi import FastAPI
from routes.quiz import router as quiz_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(quiz_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set to ["https://yourfrontend.com"] in production!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)