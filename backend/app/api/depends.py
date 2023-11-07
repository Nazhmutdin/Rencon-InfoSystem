from sqlalchemy.orm import Session

from db.engine import engine


def get_session() -> Session:
    return Session(bind=engine)