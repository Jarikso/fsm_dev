from fastapi import APIRouter, HTTPException
from schemas.sport_competition import SportCompetition, SportCompetitionCreate
from crud.sport_competition import (
    create_competition as crud_create,
    get_competitions as crud_get_all,
    get_competition as crud_get,
    update_competition as crud_update,
    delete_competition as crud_delete
)
from typing import List

router = APIRouter()

@router.post("/", response_model=SportCompetition)
async def create_competition(competition: SportCompetitionCreate):
    competition_id = await crud_create(competition)
    return {**competition.dict(), "id": competition_id}

@router.get("/", response_model=List[SportCompetition])
async def read_competitions(skip: int = 0, limit: int = 100):
    return await crud_get_all(skip, limit)

@router.get("/{competition_id}", response_model=SportCompetition)
async def read_competition(competition_id: int):
    competition = await crud_get(competition_id)
    if competition is None:
        raise HTTPException(status_code=404, detail="Competition not found")
    return competition

@router.put("/{competition_id}", response_model=SportCompetition)
async def update_competition(competition_id: int, competition: SportCompetitionCreate):
    await crud_update(competition_id, competition)
    return {**competition.dict(), "id": competition_id}

@router.delete("/{competition_id}")
async def delete_competition(competition_id: int):
    await crud_delete(competition_id)
    return {"message": "Competition deleted"}