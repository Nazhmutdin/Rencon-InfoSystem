from typing import Sequence

from sqlalchemy.sql.elements import BinaryExpression
from sqlalchemy.orm import Session

from db import NDTModel, WelderModel
from shemas import (
    NDTShema,
    Result,
    NDTRequest
)


class NDTRepository:

    def get(self, ident: str, session: Session) -> NDTShema:
        ndt = session.query(WelderModel, NDTModel).join(WelderModel, WelderModel.kleymo == NDTModel.kleymo).get(ident)

        return NDTShema.model_validate(ndt)


    def get_many(self, request: NDTRequest, session: Session, limit: int, offset: int) -> Result[NDTShema]:
        ndts = NDTShema.model_validate_many(
            session.query(NDTModel).filter(
                self._get_kleymo_expression(request.kleymos)
            ).all()
        )

        return Result(
            count=len(ndts),
            result=ndts[offset: offset + limit]
        )


    def add(self, NDTShemas: Sequence[NDTShema]) -> NDTShema: ...

    
    def update(self, NDTShemas: Sequence[NDTShema]) -> NDTShema: ...


    def _update(self, NDTShema: NDTShema) -> None: ...


    def _add(self, NDTShema: NDTShema) -> None: ...


    def _get_kleymo_expression(self, kleymos: list[str]) -> BinaryExpression:
        return NDTModel.kleymo.in_(kleymos)
