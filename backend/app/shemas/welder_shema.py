from typing import Any, TypeAlias, TypeVar
from datetime import date
from re import fullmatch

from pydantic import BaseModel, ConfigDict, Field, field_validator

from .welder_certification_shema import WelderCertificationShema


Limit: TypeAlias = int
Offset: TypeAlias = int
Name: TypeAlias = str
Kleymo: TypeAlias = str
CertificationNumber: TypeAlias = str
Company: TypeAlias = str
SubCompany: TypeAlias = str
Project: TypeAlias = str
DateFrom: TypeAlias = str
DateBefore: TypeAlias = str
Count: TypeAlias = int
DomainModel = TypeVar("DomainModel")
Model = TypeVar("Model", bound=BaseModel)


class WelderShema(BaseModel):
    kleymo: str = Field(max_length=150)
    full_name: str | None  = Field(max_length=150, default=None)
    birthday: str | date | None  = Field(max_length=150, default=None)
    passport_id: str | None = Field(max_length=150, default=None)
    certifications: list["WelderCertificationShema"] | None = Field(max_length=150, default=None)

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True
    )


    @classmethod
    def model_validate_many(cls, objs: list[Any], *, strict: bool | None = None, from_attributes: bool | None = None, context: dict[str, Any] | None = None) -> list["WelderShema"]:
        return [cls.model_validate(obj, strict=strict, from_attributes=from_attributes, context=context) for obj in objs]


    @field_validator("kleymo")
    def validate_kleymo(cls, v: str):
        if fullmatch(r"[A-Z0-9]{4}", v.strip()):
            return v
        
        raise ValueError(f"Invalid kleymo: {v}")
