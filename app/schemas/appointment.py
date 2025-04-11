from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class AppointmentStatus(str, Enum):
    scheduled = "scheduled"
    completed = "completed"
    canceled = "canceled"

class AppointmentCreate(BaseModel):
    patient_id: int
    doctor_id: int
    start_time: datetime
    end_time: datetime

class AppointmentOut(AppointmentCreate):
    id: int
    status: AppointmentStatus

    class Config:
        orm_mode = True
