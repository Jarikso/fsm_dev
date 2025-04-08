from sqlalchemy import Column, Integer, String, JSON
from database import Base

class CreativeCompetition(Base):
    __tablename__ = "creative_competitions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    max_score = Column(Integer)
    criteria_ids = Column(JSON)  # Список ID критериев