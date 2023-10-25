from typing import Sequence

from db import NDTModel
from shemas import (
    NDTShema,
    DBResponse,
    NDTDBRequest
)


class NDTRepository:
    __tablename__ = "NDTShema_summary_table"
    __tablemodel__ = NDTModel


    def get(self, request: NDTDBRequest) -> DBResponse[NDTShema]: ...


    def add(self, NDTShemas: Sequence[NDTShema]) -> NDTShema: ...

    
    def update(self, NDTShemas: Sequence[NDTShema]) -> None: ...


    def _update(self, NDTShema: NDTShema) -> None: ...


    def _add(self, NDTShema: NDTShema) -> None: ...
