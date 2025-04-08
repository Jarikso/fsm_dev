from pydantic import BaseModel

class TeamBase(BaseModel):
    name: str

class TeamCreate(TeamBase):
    pass

class Team(TeamBase):
    id: int

    class Config:
        orm_mode = True