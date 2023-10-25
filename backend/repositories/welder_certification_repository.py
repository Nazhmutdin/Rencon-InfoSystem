from typing import Sequence

from db import WelderCertificationModel
from shemas import (
    WelderCertificationShema,
    DBResponse, 
    WelderCertificationDBRequest
)


class WelderCertificationRepository:
    __tablename__ = "welder_certification_table"
    __tablemodel__ = WelderCertificationModel


    def get(self, request: WelderCertificationDBRequest) -> DBResponse: ...

    
    def add(self, certifications: Sequence[WelderCertificationShema]) -> Sequence[WelderCertificationShema]: ...
    

    def update(self, certifications: Sequence[WelderCertificationShema]) -> None: ...


    def _add(self, certification: WelderCertificationShema) -> None: ...


    def _update(self, certification: WelderCertificationShema) -> None: ...
