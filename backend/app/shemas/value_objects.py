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


@dataclass
class WelderDBRequest:
    limit: Limit
    offset: Offset
    certification_numbers: list[CertificationNumber]
    kleymos: list[Kleymo]
    names: list[Name]


@dataclass
class NDTDBRequest:
    limit: Limit
    offset: Offset
    certification_numbers: list[CertificationNumber]
    kleymos: list[Kleymo]
    names: list[Name]


@dataclass
class DBResponse(Generic[Shema]):
    result: list[Shema]
    count: int


@dataclass
class WelderCertificationDBRequest:
    limit: Limit
    offset: Offset
    kleymos: list[str]