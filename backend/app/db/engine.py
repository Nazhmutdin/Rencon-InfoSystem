import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv


load_dotenv()

DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_NAME = os.getenv("DATABASE_NAME")
HOST = os.getenv("HOST")
USER = os.getenv("USER")
PORT = os.getenv("PORT")


Base = declarative_base()
engine = create_engine("postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".format(USER, DATABASE_PASSWORD, HOST, PORT, DATABASE_NAME))

Base.metadata.create_all(engine)
