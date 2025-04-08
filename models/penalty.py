from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Penalty(Base):
    __tablename__ = "penalties"

    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey("teams.id", ondelete="CASCADE"), nullable=False)
    points = Column(Integer, nullable=False)  # Отрицательное значение для штрафа
    description = Column(String(300), nullable=True)
    # Дополнительные поля при необходимости:
    # competition_id = Column(Integer, ForeignKey("sport_competitions.id"))
    # created_at = Column(DateTime, default=datetime.utcnow)