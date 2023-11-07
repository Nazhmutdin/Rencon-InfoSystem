
from math import ceil

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api import depends
from repositories import NDTRepository
from shemas import NDTRequest, NDTShema


router = APIRouter()


@router.get("/get_ndt", response_model=NDTShema)
def get_ndt(ident: str, db: Session = Depends(depends.get_session)):
    repository = NDTRepository()

    return repository.get(ident, db)


@router.post("/get_ndts")
def get_ndts(request: NDTRequest, db: Session = Depends(depends.get_session), page: int = 1, page_size: int = 100):
    if page < 1:
        page = 1

    if page_size < 1:
        page_size = 100
    
    repository = NDTRepository()

    db_response = repository.get_many(request, db, limit=page_size, offset=page * page_size - page_size)

    return {
            "result": db_response.result,
            "num_pages": ceil(db_response.count / page_size),
            "current_page": page,
            "count": db_response.count
        }
