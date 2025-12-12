# models.py (simple persistent profile model)
from sqlalchemy import Column, Integer, String, Date, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    current_title = Column(String)
    current_seniority = Column(String)
    skills = Column(JSON)  # store as JSON list
    years_experience = Column(Integer)