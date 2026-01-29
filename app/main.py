from fastapi import FastAPI
from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Support API")

app.include_router(router)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://abhishek-shukla27.github.io/ai-chat-demo/",
                   "http://localhost:5500",
                   "http://127.0.0.1:5500",
                   ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Support Backend Running 🚀"}