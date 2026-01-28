from pydantic import BaseModel

class BusinessCreate(BaseModel):
    name: str
    email: str
    industry: str

class BusinessResponse(BusinessCreate):
    id: str
