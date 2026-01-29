from fastapi import FastAPI
from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware
from app.services.demo_data import load_demo_data
app = FastAPI(title="AI Support API")




app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://abhishek-shukla27.github.io",
                   "http://localhost:5500",
                   "http://127.0.0.1:5500",
                   ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.on_event("startup")
def startup_event():
    load_demo_data()

app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Support Backend Running 🚀"}