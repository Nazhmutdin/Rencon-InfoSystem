from typing import Sequence

from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import BinaryExpression

from db import WelderCertificationModel
from shemas import (
    WelderCertificationShema,
    DBResponse, 
    WelderCertificationDBRequest
)


class WelderCertificationRepository:

    def get(self, ident: str, session: Session) -> WelderCertificationShema:
        certification_obj = session.query(WelderCertificationModel).get(ident)

        return WelderCertificationShema(
            **certification_obj
        )


    def get_many(self, request: WelderCertificationDBRequest, session: Session) -> DBResponse[WelderCertificationShema]:
        result = session.query(WelderCertificationModel).filter(
            self._get_kleymo_expression(request.kleymos)
        ).all()
        
        return DBResponse(
            count=len(result),
            result=WelderCertificationShema.model_validate_many(result[request.offset: request.offset + request.limit])
        )

    
    def add(self, certifications: Sequence[WelderCertificationShema]) -> Sequence[WelderCertificationShema]: ...
    

    def update(self, certifications: Sequence[WelderCertificationShema]) -> None: ...


    def _add(self, certification: WelderCertificationShema) -> None: ...


    def _update(self, certification: WelderCertificationShema) -> None: ...


    def _get_kleymo_expression(self, kleymos: list[str]) -> BinaryExpression:
        return WelderCertificationModel.kleymo.in_(kleymos)
