from fastapi import APIRouter, HTTPException
from schemas.criterion import Criterion, CriterionCreate
from crud.criterion import (
    create_criterion as crud_create,
    get_criteria as crud_get_all,
    get_criterion as crud_get,
    update_criterion as crud_update,
    delete_criterion as crud_delete
)
from typing import List

router = APIRouter()

@router.post("/", response_model=Criterion)
async def create_criterion(criterion: CriterionCreate):
    criterion_id = await crud_create(criterion)
    return {**criterion.dict(), "id": criterion_id}

@router.get("/", response_model=List[Criterion])
async def read_criteria(skip: int = 0, limit: int = 100):
    return await crud_get_all(skip, limit)

@router.get("/{criterion_id}", response_model=Criterion)
async def read_criterion(criterion_id: int):
    criterion = await crud_get(criterion_id)
    if criterion is None:
        raise HTTPException(status_code=404, detail="Criterion not found")
    return criterion

@router.put("/{criterion_id}", response_model=Criterion)
async def update_criterion(criterion_id: int, criterion: CriterionCreate):
    await crud_update(criterion_id, criterion)
    return {**criterion.dict(), "id": criterion_id}

@router.delete("/{criterion_id}")
async def delete_criterion(criterion_id: int):
    await crud_delete(criterion_id)
    return {"message": "Criterion deleted"}