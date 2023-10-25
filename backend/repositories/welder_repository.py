from typing import Sequence


from db import WelderModel
from shemas import (
    WelderShema,
    DBResponse, 
    WelderDBRequest,
)

from repositories.welder_certification_repository import WelderCertificationRepository



class WelderRepository:
    __tablename__ = "WelderShema_table"
    __tablemodel__ = WelderModel
    certification_repository = WelderCertificationRepository()


    def get(self, request: WelderDBRequest) -> DBResponse: ...

    
    def add(self, WelderShemas: Sequence[WelderShema]) -> Sequence[WelderShema]: ...

        
    def update(self, WelderShemas: Sequence[WelderShema]) -> None: ...


    def _add(self, WelderShema: WelderShema) -> None: ...


    def _update(self, WelderShema: WelderShema) -> None: ...
