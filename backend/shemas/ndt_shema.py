from typing import Any, TypeAlias, Union, Sequence, TypeVar, Generic
from datetime import date, datetime
from re import fullmatch

from pydantic import BaseModel, ConfigDict, Field, field_validator


class NDTShema(BaseModel):
    full_name: str | None = Field(default=None)
    kleymo: str | int = Field(default=None)
    sicil_number: str | None = Field(default=None)
    birthday: date | None = Field(default=None)
    passport_number: str | int | None = Field(default=None)
    nation: str | None = Field(default=None)
    comp: str | None = Field(default=None)
    subcon: str | None = Field(default=None)
    project: str | None = Field(default=None)
    latest_welding_date: date = Field(default=None)
    total_weld_1: float | None = Field(default=None)
    total_ndt_1: float | None = Field(default=None)
    total_accepted_1: float | None = Field(default=None)
    total_repair_1: float | None = Field(default=None)
    repair_status_1: float | None = Field(default=None)
    total_weld_2: float | None = Field(default=None)
    total_ndt_2: float | None = Field(default=None)
    total_accepted_2: float | None = Field(default=None)
    total_repair_2: float | None = Field(default=None)
    repair_status_2: float | None = Field(default=None)
    total_weld_3: float | None = Field(default=None)
    total_ndt_3: float | None = Field(default=None)
    total_accepted_3: float | None = Field(default=None)
    total_repair_3: float | None = Field(default=None)
    repair_status_3: float | None = Field(default=None)
    ndt_id: str = Field(default=None)
    
    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True
    )


    @field_validator("latest_welding_date")
    def validate_latest_welding_date(cls, v):
        if type(v) != date or v == None:
            raise ValueError("latest_welding_date must be date type")
        
        return v


    @field_validator("kleymo")
    def validate_kleymo(cls, v) -> str:
        if not fullmatch(r"[A-Z0-9]{4}", str(v).strip()) or v == None:
            raise ValueError(f"Invalid kleymo ===> {v}")
        
        return str(v).strip()