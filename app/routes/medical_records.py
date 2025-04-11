from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.models import MedicalRecord, Appointment, Doctor
from app.schemas import MedicalRecordCreate, MedicalRecordOut
from app.models.base import get_db
from app.services.authorization import get_current_user
from app.utils.dependencies import doctor_required

router = APIRouter(prefix="/medical-records", tags=["Medical Records"])

@router.post("/", response_model=MedicalRecordOut)
def create_record(
    record: MedicalRecordCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    doctor_required(current_user)
    doctor = db.query(Doctor).filter_by(user_id=current_user.id).first()
    appointment = db.query(Appointment).filter_by(id=record.appointment_id).first()

    if appointment.doctor_id != doctor.id:
        raise HTTPException(status_code=403, detail="Not allowed to add record to this appointment")

    new_record = MedicalRecord(**record.dict())
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

@router.get("/patient/{patient_id}", response_model=List[MedicalRecordOut])
def get_patient_records(
    patient_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    doctor_required(current_user)
    doctor = db.query(Doctor).filter_by(user_id=current_user.id).first()

    records = (
        db.query(MedicalRecord)
        .join(Appointment, MedicalRecord.appointment_id == Appointment.id)
        .filter(
            MedicalRecord.patient_id == patient_id,
            Appointment.doctor_id == doctor.id
        ).all()
    )
    return records
