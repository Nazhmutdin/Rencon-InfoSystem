from typing import Sequence

from sqlalchemy.orm import Session
from sqlalchemy.sql.elements import BinaryExpression

from repositories.welder_certification_repository import WelderCertificationRepository
from db import WelderModel
from shemas import (
    WelderShema,
    DBResponse,
    WelderDBRequest,
    WelderCertificationDBRequest
)


class WelderRepository:
    certification_repository = WelderCertificationRepository()

    def get(self, ident: str, session: Session) -> WelderShema:
        welder = session.query(WelderModel).get(ident=ident)
        welder = WelderShema(**welder)

        certification_request = WelderCertificationDBRequest(
            kleymos = [ident]
        )

        welder.certifications = self.certification_repository.get_many(certification_request, session)

        return welder


    def get_many(self, request: WelderDBRequest, session: Session) -> DBResponse[WelderShema]:
        result = []
        welders = WelderShema.model_validate_many(
            session.query(WelderModel).filter(
                self._get_kleymo_expression(request.kleymos)
            ).all()
        )
    
        for welder in welders:
            cert_request = WelderCertificationDBRequest(
                kleymos=[welder.kleymo]
            )
            welder.certifications = self.certification_repository.get_many(cert_request, session).result

            result.append(welder)

        return DBResponse(
            count=len(welders),
            result=result[request.offset: request.offset + request.limit]
        )


    def add(self, WelderShemas: Sequence[WelderShema]) -> Sequence[WelderShema]: ...

        
    def update(self, WelderShemas: Sequence[WelderShema]) -> None: ...


    def _add(self, WelderShema: WelderShema) -> None: ...


    def _update(self, WelderShema: WelderShema) -> None: ...


    def _get_kleymo_expression(self, kleymos: list[str]) -> BinaryExpression:
        return WelderModel.kleymo.in_(kleymos)
