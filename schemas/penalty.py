from pydantic import BaseModel
from typing import Optional

class PenaltyBase(BaseModel):
    team_id: int
    points: int
    description: Optional[str] = None

class PenaltyCreate(PenaltyBase):
    pass

class Penalty(PenaltyBase):
    id: int

    class Config:
        from_attributes = True