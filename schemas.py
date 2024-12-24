from pydantic import BaseModel

class LeadCreate(BaseModel):
    name: str
    email: str
    lead_source: str

class LeadResponse(LeadCreate):
    id: int
    created_at: str

    class Config:
        orm_mode = True
