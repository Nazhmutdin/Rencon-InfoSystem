from typing import Any, TypeAlias, TypeVar
from datetime import date, datetime
from re import fullmatch

from pydantic import BaseModel, ConfigDict, Field, field_validator


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


class WelderCertificationShema(BaseModel):
    kleymo: str | None = Field(default=None)
    certification_id: str = Field(default=None)
    job_title: str = Field(default=None)
    certification_number: str = Field(default=None)
    certification_date: date | str = Field(default=None)
    expiration_date: date | str = Field(default=None)
    renewal_date: date | str | None = Field(default=None)
    insert: str = Field(default=None)
    certification_type: str | None = Field(default=None)
    company: str | None = Field(default=None, alias="Место работы (организация, инн):")
    gtd: str | None = Field(default=None, alias="Группы технических устройств опасных производственных объектов:")
    method: str | None = Field(default=None, alias="Вид (способ) сварки (наплавки)")
    details_type: str | None = Field(default=None, alias="Вид деталей")
    joint_type: str | None = Field(default=None, alias="Типы швов")
    groups_materials_for_welding: str | None = Field(default=None, alias="Группа свариваемого материала")
    welding_materials: str | None = Field(default=None, alias="Сварочные материалы")
    details_thikness: str | None = Field(default=None, alias="Толщина деталей, мм")
    outer_diameter: str | None = Field(default=None, alias="аружный диаметр, мм")
    welding_position: str | None = Field(default=None, alias="оложение при сварке")
    connection_type: str | None = Field(default=None, alias="Вид соединения")
    rod_diameter: str | None = Field(default=None, alias="Диаметр стержня, мм")
    rod_axis_position: str | None = Field(default=None, alias="Положение осей стержней")
    weld_type: str | None = Field(default=None, alias="Тип сварного соединения")
    joint_layer: str | None = Field(default=None, alias="Слой шва")
    sdr: str | None = Field(default=None, alias="SDR")
    automation_level: str | None = Field( default=None, alias="Степень автоматизации")
    details_diameter: str | None = Field(default=None, alias="Диаметр деталей, мм")
    welding_equipment: str | None = Field(default=None, alias="Сварочное оборудование")

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True

    )


    @classmethod
    def model_validate_many(cls, objs: list[type[Any]], *, strict: bool | None = None, from_attributes: bool | None = None, context: dict[str, Any] | None = None) -> list["WelderCertificationShema"]:
        return [cls.model_validate(obj, strict=strict, from_attributes=from_attributes, context=context) for obj in objs]
        

    @field_validator("kleymo")
    def validate_kleymo(cls, v: str) -> str:
        if v == None:
            return None
        
        if fullmatch(r"[A-Z0-9]{4}", v.strip()):
            return v.strip()
        
        raise ValueError(f"Invalid kleymo ===> {v}")
    

    @field_validator("certification_date", "expiration_date")
    def validate_date(cls, v: date| str) -> str | None:
        if type(v) == date: 
            return v
        
        if fullmatch(r"([0-9]{4}[./-][0-9]{2}[./-][0-9]{2})|([0-9]{2}[./-][0-9]{2}[./-][0-9]{4})", v.strip()):
            return datetime.strptime(v.strip(), "%Y-%m-%d").date()
        
        raise ValueError("Invalid date")
