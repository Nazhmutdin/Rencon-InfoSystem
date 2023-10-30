from typing import Sequence

from sqlalchemy.sql.elements import BinaryExpression
from sqlalchemy.orm import Session

from db import NDTModel
from shemas import (
    NDTShema,
    DBResponse,
    NDTDBRequest
)


class NDTRepository:

    def get(self, ident: str, session: Session) -> DBResponse[NDTShema]:
        ndt = session.query(NDTModel).get(ident)

        return NDTShema.model_validate(ndt)


    def get_many(self, request: NDTDBRequest, session: Session) -> DBResponse[NDTShema]:
        ndts = NDTShema.model_validate_many(
            session.query(NDTModel).filter(
                self._get_kleymo_expression(request.kleymos)
            ).all()
        )

        return DBResponse(
            count=len(ndts),
            result=ndts[request.offset: request.offset + request.limit]
        )


    def add(self, NDTShemas: Sequence[NDTShema]) -> NDTShema: ...

    
    def update(self, NDTShemas: Sequence[NDTShema]) -> NDTShema: ...


    def _update(self, NDTShema: NDTShema) -> None: ...


    def _add(self, NDTShema: NDTShema) -> None: ...


    def _get_kleymo_expression(self, kleymos: list[str]) -> BinaryExpression:
        return NDTModel.kleymo.in_(kleymos)
