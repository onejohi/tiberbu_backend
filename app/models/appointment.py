from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.models.base import Base
from enum import Enum as PyEnum

class AppointmentStatus(PyEnum):
    scheduled = "scheduled"
    completed = "completed"
    canceled = "canceled"

class Appointment(Base):
    __tablename__ = "appointments"
    
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    scheduled_at = Column(DateTime, default=func.now())
    status = Column(Enum(AppointmentStatus, name="appointment_status_enum"), default=AppointmentStatus.scheduled)

    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")
