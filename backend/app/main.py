from fastapi import FastAPI
from app.api.routes import router
from app.config import APP_NAME
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "API is running"}
