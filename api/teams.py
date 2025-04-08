from fastapi import APIRouter, HTTPException
from schemas.team import Team, TeamCreate
from crud.team import (
    create_team as crud_create_team,
    get_teams as crud_get_teams,
    get_team as crud_get_team,
    update_team as crud_update_team,
    delete_team as crud_delete_team
)
from typing import List

router = APIRouter()

@router.post("/", response_model=Team)
async def create_team(team: TeamCreate):
    team_id = await crud_create_team(team)
    return {**team.dict(), "id": team_id}

@router.get("/", response_model=List[Team])
async def read_teams(skip: int = 0, limit: int = 100):
    return await crud_get_teams(skip, limit)

@router.get("/{team_id}", response_model=Team)
async def read_team(team_id: int):
    team = await crud_get_team(team_id)
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

@router.put("/{team_id}", response_model=Team)
async def update_team(team_id: int, team: TeamCreate):
    await crud_update_team(team_id, team)
    return {**team.dict(), "id": team_id}

@router.delete("/{team_id}")
async def delete_team(team_id: int):
    await crud_delete_team(team_id)
    return {"message": "Team deleted"}