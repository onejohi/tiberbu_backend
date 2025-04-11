from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.models.base import Base

class Doctor(Base):
    __tablename__ = "doctors"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    specialty = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    is_active = Column(Boolean, default=True)

    doctor_availability = relationship("DoctorAvailability", back_populates="doctor")
    appointments = relationship("Appointment", back_populates="doctor")
    user = relationship("User", back_populates="doctor_profile")
