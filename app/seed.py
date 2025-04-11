from sqlalchemy.orm import Session
from app.models.user import Role
from app.models.base import SessionLocal

def seed_roles():
    db: Session = SessionLocal()
    roles = ["admin", "doctor", "patient"]
    for role in roles:
        exists = db.query(Role).filter_by(name=role).first()
        if not exists:
            db.add(Role(name=role))
    db.commit()
    db.close()

if __name__ == "__main__":
    seed_roles()
