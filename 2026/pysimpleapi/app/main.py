from fastapi import FastAPI

from app.routers import patients

app = FastAPI(title="Patient API")

app.include_router(patients.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
