from fastapi import FastAPI
from app.routes import auth

app = FastAPI()

app.include_router(auth.router)

@app.get('/')
def read_root():
  return {"message": "Tiberbu API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)