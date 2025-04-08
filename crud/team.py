from sqlalchemy import select, insert, update, delete
from database import database
from models.team import Team as TeamModel
from schemas.team import TeamCreate

async def create_team(team: TeamCreate):
    query = insert(TeamModel).values(**team.dict())
    return await database.execute(query)

async def get_teams(skip: int = 0, limit: int = 100):
    query = select(TeamModel).offset(skip).limit(limit)
    return await database.fetch_all(query)

async def get_team(team_id: int):
    query = select(TeamModel).where(TeamModel.id == team_id)
    return await database.fetch_one(query)

async def update_team(team_id: int, team: TeamCreate):
    query = update(TeamModel).where(TeamModel.id == team_id).values(**team.dict())
    await database.execute(query)
    return {**team.dict(), "id": team_id}

async def delete_team(team_id: int):
    query = delete(TeamModel).where(TeamModel.id == team_id)
    await database.execute(query)
    return {"message": "Team deleted"}