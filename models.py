from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from database import Base

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    lead_source = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
