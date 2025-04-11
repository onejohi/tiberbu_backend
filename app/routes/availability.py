from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.models.base import get_db
from app.models import Availability, Doctor
from app.schemas import AvailabilityCreate, AvailabilityOut
from app.services.authorization import get_current_user
from app.utils.dependencies import doctor_required

router = APIRouter(prefix="/availability", tags=["Availability"])

@router.post("/", response_model=AvailabilityOut)
def create_slot(
  slot: AvailabilityCreate,
  db: Session = Depends(get_db),
  current_user=Depends(get_current_user),
):
  doctor_required(current_user)

  doctor = db.query(Doctor).filter_by(user_id=current_user.id).first()
  if not doctor or doctor.id != slot.doctor_id:
    raise HTTPException(status_code=403, detail="Access denied")

  new_slot = Availability(**slot.dict())
  db.add(new_slot)
  db.commit()
  db.refresh(new_slot)
  return new_slot

@router.get("/doctor/{doctor_id}", response_model=List[AvailabilityOut])
def get_slots(doctor_id: int, db: Session = Depends(get_db)):
  return db.query(Availability).filter_by(doctor_id=doctor_id).all()
