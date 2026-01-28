from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal, engine
from app.db.database import Base
from app.schemas.business import BusinessCreate, BusinessResponse
from app.services.business_service import create_business
from app.schemas.knowledge import KnowledgeCreate
from app.services.knowledge_service import add_knowledge
from app.schemas.chat import ChatRequest
from app.services.chat_service import answer_question


router = APIRouter()

# Create tables
Base.metadata.create_all(bind=engine)

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/hello")
def hello():
    return {"message": "FastAPI folder structure works 🚀"}

@router.post("/business", response_model=BusinessResponse)
def register_business(
    business: BusinessCreate,
    db: Session = Depends(get_db)
):
    return create_business(db, business)

@router.post("/knowledge")
def upload_knowledge(data: KnowledgeCreate):
    add_knowledge(data.business_id,data.content)
    return {"message": "Knowledge added successfully"}

@router.post("/chat")
def chat(data: ChatRequest):
    answer = answer_question(business_id=data.business_id,
                             question=data.question)
    return {"answer": answer}
