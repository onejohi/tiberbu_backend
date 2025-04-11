from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from app.models.base import get_db
from app.models.user import UserCreate, UserOut, Token, User, Role
from app.services.authorization import (
  create_access_token,
  get_password_hash,
  authenticate_user,
  get_current_user
)
import pprint

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
  existing_user = db.query(User).filter(User.username == user.username).first()
  if existing_user:
    raise HTTPException(status_code=400, detail="Username already exists")
  password_hash = get_password_hash(user.password)
  role_obj = db.query(Role).filter(Role.name == user.role).first()
  if not role_obj:
    raise HTTPException(status_code=400, detail="Invalid role")
  new_user = User(
    username=user.username,
    email=user.email,
    hashed_password = password_hash,
    role_id=role_obj.id
  )
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

@router.post("/login", response_model=Token)
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
  user = authenticate_user(form_data.username, form_data.password, db)
  if not user:
    raise HTTPException(status_code=401, detail="Invalid credentials")
  access_token = create_access_token(data={"sub": user.username})
  return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserOut)
def get_profile(current_user: UserOut = Depends(get_current_user)):
  return current_user

@router.post("/logout")
def logout():
  return {"msg": "Logout successful"}
