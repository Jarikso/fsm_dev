from sqlalchemy import select, insert, update, delete
from database import database
from models.penalty import Penalty as PenaltyModel
from schemas.penalty import PenaltyCreate

async def create_penalty(penalty: PenaltyCreate):
    query = insert(PenaltyModel).values(**penalty.model_dump())
    return await database.execute(query)

async def get_penalties(skip: int = 0, limit: int = 100):
    query = select(PenaltyModel).offset(skip).limit(limit)
    return await database.fetch_all(query)

async def get_penalty(penalty_id: int):
    query = select(PenaltyModel).where(PenaltyModel.id == penalty_id)
    return await database.fetch_one(query)

async def get_team_penalties(team_id: int):
    query = select(PenaltyModel).where(PenaltyModel.team_id == team_id)
    return await database.fetch_all(query)

async def update_penalty(penalty_id: int, penalty: PenaltyCreate):
    query = update(PenaltyModel).where(PenaltyModel.id == penalty_id).values(**penalty.model_dump())
    await database.execute(query)

async def delete_penalty(penalty_id: int):
    query = delete(PenaltyModel).where(PenaltyModel.id == penalty_id)
    await database.execute(query)