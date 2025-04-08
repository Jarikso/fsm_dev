from sqlalchemy import select, insert, update, delete
from database import database
from models.creative_competition import CreativeCompetition as CompetitionModel
from schemas.creative_competition import CreativeCompetitionCreate

async def create_competition(competition: CreativeCompetitionCreate):
    query = insert(CompetitionModel).values(**competition.dict())
    return await database.execute(query)

async def get_competitions(skip: int = 0, limit: int = 100):
    query = select(CompetitionModel).offset(skip).limit(limit)
    return await database.fetch_all(query)

async def get_competition(competition_id: int):
    query = select(CompetitionModel).where(CompetitionModel.id == competition_id)
    return await database.fetch_one(query)

async def update_competition(competition_id: int, competition: CreativeCompetitionCreate):
    query = update(CompetitionModel).where(CompetitionModel.id == competition_id).values(**competition.dict())
    await database.execute(query)
    return {**competition.dict(), "id": competition_id}

async def delete_competition(competition_id: int):
    query = delete(CompetitionModel).where(CompetitionModel.id == competition_id)
    await database.execute(query)
    return {"message": "Competition deleted"}