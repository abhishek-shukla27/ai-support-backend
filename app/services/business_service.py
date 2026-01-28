from sqlalchemy.orm import Session
from app.models.business import Business
from app.schemas.business import BusinessCreate

def create_business(db: Session, business: BusinessCreate):
    new_business = Business(
        name=business.name,
        email=business.email,
        industry=business.industry
    )
    db.add(new_business)
    db.commit()
    db.refresh(new_business)
    return new_business
