from pydantic import BaseModel

class CriterionBase(BaseModel):
    name: str
    description: str

class CriterionCreate(CriterionBase):
    pass

class Criterion(CriterionBase):
    id: int

    class Config:
        orm_mode = True