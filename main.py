from fastapi import FastAPI
from starlette.responses import RedirectResponse

from database import database, metadata, engine
from api import (
    teams,
    creative_competitions,
    sport_competitions,
    criteria,
    penalties
)

# app = FastAPI(docs_url="/hidden-docs", redoc_url="/hidden-redoc")
app = FastAPI()
app.include_router(teams.router, prefix="/teams", tags=["teams"])
app.include_router(creative_competitions.router, prefix="/creative-competitions", tags=["creative competitions"])
app.include_router(sport_competitions.router, prefix="/sport-competitions", tags=["sport competitions"])
app.include_router(criteria.router, prefix="/criteria", tags=["criteria"])
app.include_router(penalties.router, prefix="/penalties", tags=["penalties"])

@app.on_event("startup")
async def startup():
    await database.connect()
    # Создаем таблицы (в продакшене используйте миграции)
    metadata.create_all(engine)

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
def home_page():
    return {"message": "My first API"}