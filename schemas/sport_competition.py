from typing import List
from pydantic import BaseModel

class SportCompetitionBase(BaseModel):
    name: str
    max_score: int
    criteria_ids: List[int]

class SportCompetitionCreate(SportCompetitionBase):
    pass

class SportCompetition(SportCompetitionBase):
    id: int

    class Config:
        orm_mode = True