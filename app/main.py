from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI Support API")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Support Backend Running 🚀"}
