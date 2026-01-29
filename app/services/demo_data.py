from app.services.knowledge_service import BUSINESS_KNOWLEDGE,normalize_business_id

def load_demo_data():
    key=normalize_business_id("Sync IO")
    BUSINESS_KNOWLEDGE["Sync IO"] = """
Company Name: Sync IO

Project 1: Shree Heights Phase 1
Location: Sector 62, Gurugram
Configuration: 2 BHK, 3 BHK
2 BHK Price: Starting from ₹65 Lakhs
3 BHK Price: Starting from ₹85 Lakhs
Amenities: Swimming pool, gym, clubhouse, children play area
Possession: December 2026

Project 2: Shree Heights Phase 2
Location: Sector 75, Gurugram
Configuration: 3 BHK, 4 BHK
3 BHK Price: Starting from ₹1.1 Crore
4 BHK Price: Starting from ₹1.5 Crore
Amenities: Park, jogging track, security, parking
Possession: June 2027

Office Timings: Monday to Saturday, 10 AM to 7 PM
Site Visit: Available on prior appointment
"""
