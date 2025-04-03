from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship
from app.models.base import Base

class Patient(Base):
    __tablename__ = "patients"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    date_of_birth = Column(Date)
    phone_number = Column(String, unique=True)
    email = Column(String, unique=True)
    insurance_number = Column(String, unique=True)
    is_active = Column(Boolean, default=True)

    appointments = relationship("Appointment", back_populates="patient")
