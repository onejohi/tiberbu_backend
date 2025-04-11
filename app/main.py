from fastapi import FastAPI
from app.routes import auth
from app.routes import doctor
from app.routes import patient
from app.routes import appointment
from app.routes import medical_records
from app.routes import availability

app = FastAPI()

app.include_router(auth.router)
app.include_router(doctor.router)
app.include_router(patient.router)
app.include_router(appointment.router)
app.include_router(medical_records.router)
app.include_router(availability.router)

@app.get('/')
def read_root():
  return {"message": "Tiberbu API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)