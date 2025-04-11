from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.base import get_db
from app.models.patient import Patient
from app.models.doctor import Doctor
from app.schemas import PatientCreate, PatientOut
from typing import List, Optional
from fastapi import Query

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.post("/", response_model=PatientOut)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    existing = db.query(Patient).filter_by(user_id=patient.user_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Patient profile already exists.")
    new_patient = Patient(**patient.dict())
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient

@router.get("/{patient_id}", response_model=PatientOut)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
  patient = db.query(Patient).filter_by(id=patient_id).first()
  if not patient:
      raise HTTPException(status_code=404, detail="Patient not found.")
  return patient

@router.get("/", response_model=List[PatientOut])
def get_patients(
  insurance_provider: Optional[str] = Query(None),
  is_active: Optional[bool] = Query(None),
  db: Session = Depends(get_db)
):
  query = db.query(Patient)

  if insurance_provider:
    query = query.filter(Patient.insurance_provider.ilike(f"%{insurance_provider}%"))

  if is_active is not None:
    query = query.filter(Patient.is_active == is_active)

  return query.all()
