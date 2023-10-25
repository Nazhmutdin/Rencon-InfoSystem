import os

from dotenv import load_dotenv


load_dotenv()


DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_NAME = os.getenv("DATABASE_NAME")
HOST = os.getenv("HOST")
USER = os.getenv("USER")
PORT = os.getenv("PORT")