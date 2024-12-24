from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas, fake_hubspot
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/leads/", response_model=schemas.LeadResponse)
def create_lead(lead: schemas.LeadCreate, db: Session = Depends(get_db)):
    db_lead = models.Lead(**lead.dict())
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead

@app.get("/fetch-and-save-lead/")
def fetch_and_save_lead(db: Session = Depends(get_db)):
    # Obtener un lead simulado
    simulated_lead = fake_hubspot.fetch_leads()
    # Validar y guardar el lead
    lead_schema = schemas.LeadCreate(**simulated_lead)
    return create_lead(lead=lead_schema, db=db)
