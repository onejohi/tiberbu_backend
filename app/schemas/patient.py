from pydantic import BaseModel

class PatientBase(BaseModel):
    full_name: str
    contact_info: str
    identification_number: str
    insurance_provider: str

class PatientCreate(PatientBase):
    user_id: int

class PatientOut(PatientBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
