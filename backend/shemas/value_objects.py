from dataclasses import dataclass
from typing import (
    TypeAlias,
    TypeVar,
    Generic
)


Model = TypeVar("Model")
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
class DBResponse(Generic[Model]):
    result: list[Model]
    count: int


@dataclass
class WelderCertificationDBRequest:
    ...