from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Appointment, Availability
from app.schemas import AppointmentCreate, AppointmentOut
from app.models.base import get_db
from typing import List
from app.utils.dependencies import doctor_required
from app.services.authorization import get_current_user
from app.models.doctor import Doctor

router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.post("/", response_model=AppointmentOut)
def book_appointment(appt: AppointmentCreate, db: Session = Depends(get_db)):
  availability = db.query(Availability).filter(
    Availability.doctor_id == appt.doctor_id,
    Availability.start_time <= appt.start_time,
    Availability.end_time >= appt.end_time
  ).first()

  if not availability:
    raise HTTPException(status_code=400, detail="Time slot not available")

  overlapping = db.query(Appointment).filter(
      Appointment.doctor_id == appt.doctor_id,
      Appointment.start_time < appt.end_time,
      Appointment.end_time > appt.start_time
  ).first()

  if overlapping:
      raise HTTPException(status_code=400, detail="Doctor already has an appointment at that time")

  new_appt = Appointment(**appt.dict())
  db.add(new_appt)
  db.commit()
  db.refresh(new_appt)
  return new_appt

@router.get("/", response_model=List[AppointmentOut])
def get_all_appointments(db: Session = Depends(get_db)):
  return db.query(Appointment).all()

@router.get("/me", response_model=List[AppointmentOut])
def get_my_appointments(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    doctor_required(current_user)
    doctor = db.query(Doctor).filter_by(user_id=current_user.id).first()
    return db.query(Appointment).filter_by(doctor_id=doctor.id).all()
