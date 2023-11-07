from typing import Sequence

from sqlalchemy import any_, or_
from sqlalchemy.orm import Session, subqueryload
from sqlalchemy.sql.elements import BinaryExpression

from repositories.welder_certification_repository import WelderCertificationRepository
from db import WelderModel, WelderCertificationModel
from shemas import (
    WelderShema,
    Result,
    WelderRequest,
    WelderCertificationRequest
)


class WelderRepository:
    certification_repository = WelderCertificationRepository()

    def get(self, ident: str, session: Session) -> WelderShema:
        welder = session.query(WelderModel).get(ident=ident)
        welder = WelderShema.model_validate(welder)

        certification_request = WelderCertificationRequest(
            kleymos = [ident]
        )

        welder.certifications = self.certification_repository.get_many(certification_request, session).result

        return welder


    def get_many(self, request: WelderRequest, session: Session, limit: int = 100, offset: int = 0) -> Result[WelderShema]:
        welders = session.query(WelderModel).filter(
                or_(*self._get_expressions(request))
            ).options(subqueryload(WelderModel.certifications))
        

        return Result(
            count=welders.count(),
            result=WelderShema.model_validate_many(welders.limit(limit).offset(offset).all())
        )


    def add(self, WelderShemas: Sequence[WelderShema]) -> Sequence[WelderShema]: ...

        
    def update(self, WelderShemas: Sequence[WelderShema]) -> None: ...


    def _add(self, WelderShema: WelderShema) -> None: ...


    def _update(self, WelderShema: WelderShema) -> None: ...


    def _get_expressions(self, request: WelderRequest) -> list[BinaryExpression]:
        expressions = []

        self._get_kleymo_expression(request.kleymos, expressions)
        self._get_name_expression(request.names, expressions)

        return expressions


    def _get_kleymo_expression(self, kleymos: list[str] | None, expressions: list[BinaryExpression]) -> None:
        if kleymos:
            expressions.append(WelderModel.kleymo.in_(kleymos))


    def _get_name_expression(self, names: list[str] | None, expressions: list[BinaryExpression]) -> None:
        if names:
            names = [f"%{name}%" for name in names]
            expressions.append(WelderModel.full_name.ilike(any_(names)))
