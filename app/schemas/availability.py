from pydantic import BaseModel
from datetime import datetime

class AvailabilityBase(BaseModel):
    start_time: datetime
    end_time: datetime

class AvailabilityCreate(AvailabilityBase):
    doctor_id: int

class AvailabilityOut(AvailabilityBase):
    id: int
    doctor_id: int

    class Config:
        orm_mode = True
