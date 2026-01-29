BUSINESS_KNOWLEDGE = {}

def normalize_business_id(business_id:str)->str:
    return business_id.strip().lower()

def add_knowledge(business_id: str, content: str):
    BUSINESS_KNOWLEDGE[business_id] = content