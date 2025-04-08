from typing import List
from pydantic import BaseModel

class CreativeCompetitionBase(BaseModel):
    name: str
    max_score: int
    criteria_ids: List[int]

class CreativeCompetitionCreate(CreativeCompetitionBase):
    pass

class CreativeCompetition(CreativeCompetitionBase):
    id: int

    class Config:
        orm_mode = True