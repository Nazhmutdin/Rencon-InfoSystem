from dataclasses import dataclass
from typing import (
    TypeAlias,
    TypeVar,
    Generic
)

from pydantic import BaseModel


Shema = TypeVar("Shema", bound=BaseModel)
Limit: TypeAlias = int
Offset: TypeAlias = int
Kleymo: TypeAlias = str
Name: TypeAlias = str
CertificationNumber: TypeAlias = str


class WelderRequest(BaseModel):
    limit: Limit = 100
    offset: Offset = 0
    names: list[str] | None = None
    kleymos: list[str] | None = None
    certification_numbers: list[str] | None = None


class WelderCertificationRequest(BaseModel):
    limit: Limit = 100
    offset: Offset = 0
    kleymos: list[str]


class NDTRequest(BaseModel):
    limit: Limit = 100
    offset: Offset = 0
    certification_numbers: list[CertificationNumber] | None = None
    kleymos: list[Kleymo] | None = None
    names: list[Name] | None = None


class Result(BaseModel, Generic[Shema]):
    result: list[Shema]
    count: int
