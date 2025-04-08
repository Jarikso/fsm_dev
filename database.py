import databases
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://postgres:0000@localhost/fsm_data"

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
Base = declarative_base()

engine = sqlalchemy.create_engine(DATABASE_URL)