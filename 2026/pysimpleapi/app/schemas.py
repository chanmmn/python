from datetime import date, datetime

from pydantic import BaseModel, ConfigDict


class PatientBase(BaseModel):
    registered_by: str
    mrn: str
    full_name: str
    dob: date
    ic_num: str
    barcode: str


class PatientCreate(PatientBase):
    pass


class PatientUpdate(BaseModel):
    registered_by: str | None = None
    mrn: str | None = None
    full_name: str | None = None
    dob: date | None = None
    ic_num: str | None = None
    barcode: str | None = None


class PatientOut(PatientBase):
    model_config = ConfigDict(from_attributes=True)

    patient_id: int
    registered_time: datetime
    last_updated: datetime
