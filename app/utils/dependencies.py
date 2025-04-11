# dependencies.py
from fastapi import HTTPException, Depends
from app.models import User
from app.services.authorization import (
  get_current_user
)

def doctor_required(current_user: User = Depends(get_current_user)):
    if current_user.role.name.lower() != "doctor":
        raise HTTPException(status_code=403, detail="Doctor access required")
