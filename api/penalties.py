from fastapi import APIRouter, HTTPException, Depends
from typing import List
from schemas.penalty import Penalty, PenaltyCreate
from crud.penalty import (
    create_penalty as crud_create_penalty,
    get_penalties as crud_get_penalties,
    get_penalty as crud_get_penalty,
    get_team_penalties as crud_get_team_penalties,
    update_penalty as crud_update_penalty,
    delete_penalty as crud_delete_penalty
)

router = APIRouter(prefix="/penalties", tags=["penalties"])

@router.post("/", response_model=Penalty, status_code=201)
async def create_penalty(penalty: PenaltyCreate):
    penalty_id = await crud_create_penalty(penalty)
    return {**penalty.model_dump(), "id": penalty_id}

@router.get("/", response_model=List[Penalty])
async def read_penalties(skip: int = 0, limit: int = 100):
    return await crud_get_penalties(skip, limit)

@router.get("/team/{team_id}", response_model=List[Penalty])
async def read_team_penalties(team_id: int):
    return await crud_get_team_penalties(team_id)

@router.get("/{penalty_id}", response_model=Penalty)
async def read_penalty(penalty_id: int):
    penalty = await crud_get_penalty(penalty_id)
    if not penalty:
        raise HTTPException(status_code=404, detail="Penalty not found")
    return penalty

@router.put("/{penalty_id}", response_model=Penalty)
async def update_penalty(penalty_id: int, penalty: PenaltyCreate):
    await crud_update_penalty(penalty_id, penalty)
    return {**penalty.model_dump(), "id": penalty_id}

@router.delete("/{penalty_id}", status_code=204)
async def delete_penalty(penalty_id: int):
    await crud_delete_penalty(penalty_id)