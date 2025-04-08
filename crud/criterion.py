from sqlalchemy import select, insert, update, delete
from database import database
from models.criterion import Criterion as CriterionModel
from schemas.criterion import CriterionCreate

async def create_criterion(criterion: CriterionCreate):
    query = insert(CriterionModel).values(**criterion.dict())
    return await database.execute(query)

async def get_criteria(skip: int = 0, limit: int = 100):
    query = select(CriterionModel).offset(skip).limit(limit)
    return await database.fetch_all(query)

async def get_criterion(criterion_id: int):
    query = select(CriterionModel).where(CriterionModel.id == criterion_id)
    return await database.fetch_one(query)

async def update_criterion(criterion_id: int, criterion: CriterionCreate):
    query = update(CriterionModel).where(CriterionModel.id == criterion_id).values(**criterion.dict())
    await database.execute(query)
    return {**criterion.dict(), "id": criterion_id}

async def delete_criterion(criterion_id: int):
    query = delete(CriterionModel).where(CriterionModel.id == criterion_id)
    await database.execute(query)
    return {"message": "Criterion deleted"}