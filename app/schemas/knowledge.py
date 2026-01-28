from pydantic import BaseModel

class KnowledgeCreate(BaseModel):
    business_id: str
    content: str
