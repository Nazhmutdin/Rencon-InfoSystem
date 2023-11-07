from math import ceil

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api import depends
from repositories import WelderRepository
from shemas import WelderRequest


router = APIRouter()


@router.get("/get_welder")
def get_welder(ident: str, db: Session = Depends(depends.get_session)):
    repository = WelderRepository()

    return repository.get(ident, db)


@router.post("/get_welders")
def get_welder(request: WelderRequest, db: Session = Depends(depends.get_session), page: int = 1, page_size: int = 100):
    if page < 1:
        page = 1

    if page_size < 1:
        page_size = 100
    
    repository = WelderRepository()

    db_response = repository.get_many(request, db, limit=page_size, offset=page * page_size - page_size)

    return {
            "result": db_response.result,
            "num_pages": ceil(db_response.count / page_size),
            "current_page": page,
            "count": db_response.count
        }
