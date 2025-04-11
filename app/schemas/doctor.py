from pydantic import BaseModel

class DoctorBase(BaseModel):
    full_name: str
    specialization: str
    contact_info: str
    is_active: bool = True

class DoctorCreate(DoctorBase):
    user_id: int

class DoctorUpdate(BaseModel):
    full_name: str | None = None
    specialization: str | None = None
    contact_info: str | None = None
    is_active: bool | None = None

class DoctorOut(DoctorBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
