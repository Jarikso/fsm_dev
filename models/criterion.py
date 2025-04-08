from sqlalchemy import Column, Integer, String, Text
from database import Base

class Criterion(Base):
    __tablename__ = "criteria"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
    description = Column(Text)